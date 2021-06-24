from antlr4 import *
from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from grammar.GrammarVisitor import GrammarVisitor

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.errors = []
        self.memory = []

    def visitSimple_select_command(self, ctx:GrammarParser.Simple_select_commandContext):
        nErrors = len(self.errors)

        # extract table data
        table = {'name': ctx.select_base().select_base_table().table.text}
        if ctx.select_base().select_base_table().alias:
            table['alias'] = ctx.select_base().select_base_table().alias.text

        if ctx.select_base().STAR() is not None:
            self.memory.append('db.%s.find()' % table['name'])
        else:
            # extract field data
            fields = []
            for field in ctx.select_base().select_base_field():
                aux = {}
                if field.table:
                    aux['table'] = field.table.text
                aux['name'] = field.field.text
                if field.alias:
                    aux['alias'] = field.alias.text
                fields.append(aux)


            # check if the table exists for table assigned fields
            for field in fields:
                table_id = table['name'] if not table.get('alias') else table['alias']
                if field.get('table') and field['table'] not in [table_id]:
                    self.errors.append('Error on field: \'%s.%s\' there is no table \'%s\' in the sentence\'' % (field['table'], field['name'], field['table']))

            # check if there are duplicatated fields
            for i, ifield in enumerate(fields[:-1]):
                for jfield in fields[i+1:]:
                    if ifield.get('table') == jfield.get('table') and ifield['name'] == jfield['name']:
                        if ifield.get('table'):
                            self.errors.append('Duplicated column name: \'%s.%s\'' % (ifield['table'], ifield['name']))
                        else:
                            self.errors.append('Duplicated column name: \'%s\'' % ifield['name'])
                        break

            if len(self.errors) == nErrors:
                projection = '_id: 0'
                for field in fields:
                    if field.get('alias'):
                        projection += ', %s: \"$%s\"' % (field['alias'], field['name'])
                    else:
                        projection += ', %s: 1' % field['name']
                self.memory.append('db.%s.find({}, {%s})' % (table['name'], projection))

        return self.visitChildren(ctx)

    def visitSelect_with_join_command(self, ctx:GrammarParser.Select_with_join_commandContext):
        nErrors = len(self.errors)

        # extract original table data
        original_table = {'name': ctx.select_base().select_base_table().table.text}
        if ctx.select_base().select_base_table().alias:
            original_table['alias'] = ctx.select_base().select_base_table().alias.text

        # extract fields data
        fields = []
        for field in ctx.select_base().select_base_field():
            aux = {}
            if field.table:
                aux['table'] = field.table.text
            aux['name'] = field.field.text
            if field.alias:
                aux['alias'] = field.alias.text
            fields.append(aux)

        # extract join table data
        join_table = {'name': ctx.join_base().select_base_table().table.text}
        if ctx.join_base().select_base_table().alias:
            join_table['alias'] = ctx.join_base().select_base_table().alias.text

        # check table names
        original_table_id = original_table['name'] if not original_table.get('alias') else original_table['alias']
        join_table_id = join_table['name'] if not join_table.get('alias') else join_table['alias']

        ## in the fields
        for field in fields:
            if not field.get('table'):
                self.errors.append('Join sentences require fields assigned to tables, field \'%s\' is not assigned' % field['name'])
            else:
                if field['table'] not in [original_table_id, join_table_id]:
                    self.errors.append('Field \'%s\' assigned to table \'%s\', but there is no table \'%s\' in the sentence' % (field['name'], field['table'], field['table']))

        ## in the on
        if ctx.join_base().left_table.text not in [original_table_id, join_table_id]:
            self.errors.append('Field \'%s\' assigned to table \'%s\', but there is no table \'%s\' in the sentence' % (
                ctx.join_base().left_field.text,
                ctx.join_base().left_table.text,
                ctx.join_base().left_table.text
            ))
        if ctx.join_base().right_table.text not in [original_table_id, join_table_id]:
            self.errors.append('Field \'%s\' assigned to table \'%s\', but there is no table \'%s\' in the sentence' % (
                ctx.join_base().right_field.text,
                ctx.join_base().right_table.text,
                ctx.join_base().right_table.text
            ))

        if len(self.errors) == nErrors:
            # assign the on fields to the tables
            original_table_on_field = ctx.join_base().left_field.text if ctx.join_base().left_table.text == original_table_id else ctx.join_base().right_field.text
            join_table_on_field = ctx.join_base().right_field.text if original_table_on_field == ctx.join_base().left_field.text else ctx.join_base().left_field.text


            # invert things when right join
            if ctx.join_base().join_type().getText() == 'left join':
                # make projection
                projection = '_id: 0'
                for field in fields:
                    if field['table'] == original_table_id:
                        if field.get('alias'):
                            projection += ', %s: \"$%s\"' % (field['alias'], field['name'])
                        else:
                            projection += ', %s: 1' % field['name']
                    else:
                        if field.get('alias'):
                            projection += ', %s: \"$%s.%s\"' % (field['alias'], join_table_id, field['name'])
                        else:
                            projection += ', %s: 1' % (join_table_id, field['name'])

                comm  = "db.%s.aggregate([\n" % original_table['name']
                comm += "   {\n"
                comm += "     $lookup:\n"
                comm += "       {\n"
                comm += "         from: \"%s\",\n" % join_table['name']
                comm += "         localField: \"%s\",\n" % original_table_on_field
                comm += "         foreignField: \"%s\",\n" % join_table_on_field
                comm += "         as: \"%s\",\n" % join_table_id
                comm += "       }\n"
                comm += "  },\n"
                comm += "  {\n"
                comm += "    $project: {%s}\n" % projection
                comm += "  }\n"
                comm += "])"
                self.memory.append(comm)
            else:
                # make projection
                projection = '_id: 0'
                for field in fields:
                    if field['table'] == join_table_id:
                        if field.get('alias'):
                            projection += ', %s: \"$%s\"' % (field['alias'], field['name'])
                        else:
                            projection += ', %s: 1' % field['name']
                    else:
                        if field.get('alias'):
                            projection += ', %s: \"$%s.%s\"' % (field['alias'], original_table_id, field['name'])
                        else:
                            projection += ', %s.%s: 1' % (original_table_id, field['name'])

                comm  = "db.%s.aggregate([\n" % join_table['name']
                comm += "   {\n"
                comm += "     $lookup:\n"
                comm += "       {\n"
                comm += "         from: \"%s\",\n" % original_table['name']
                comm += "         localField: \"%s\",\n" % join_table_on_field
                comm += "         foreignField: \"%s\",\n" % original_table_on_field
                comm += "         as: \"%s\",\n" % original_table_id
                comm += "       }\n"
                comm += "  },\n"
                comm += "  {\n"
                comm += "    $project: {%s}\n" % projection
                comm += "  }\n"
                comm += "])"
                self.memory.append(comm)

        return self.visitChildren(ctx)
