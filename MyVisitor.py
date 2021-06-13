from antlr4 import *
from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from grammar.GrammarVisitor import GrammarVisitor

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.errors = []
        self.memory = []

    def visitSimple_select_command(self, ctx:GrammarParser.Simple_select_commandContext):
        table_name, col_names = self.get_select_identifiers(ctx.select_base())

        if ctx.select_base().STAR() is not None:
            self.memory.append(f'db.{table_name}.find()')
        else:
            # check if there are duplicatated collum names
            for i, ident in enumerate(col_names[:-1]):
                for seek in col_names[i+1:]:
                    if ident == seek:
                        self.errors.append(f'Duplicated column name: {ident}')
                        break
            else:
                # generate equivalent mongo code
                self.memory.append('db.%s.find({%s})' % (table_name, ','.join(col_names)))

        return self.visitChildren(ctx)

    def visitSelect_with_join_command(self, ctx:GrammarParser.Select_with_join_commandContext):
        table_name, col_names = self.get_select_identifiers(ctx.select_base())
        join_type = ctx.join_base().join_type().getText().split(' ')[0]
        join_table, table1_name, table1_column, table2_name, table2_column = [i.getText() for i in ctx.join_base().IDENT()]
        error = False

        # check self join
        if table_name == join_table:
            self.errors.append('Main table and join table should not be the same')
            error = True

        # check table names after on
        aux = [table_name, join_table]
        aux2 = [table1_name, table2_name]
        aux.sort()
        aux2.sort()
        if not aux == aux2:
            error = True
            if table1_name not in aux:
                self.errors.append(f'Invalid table name into join: \'{table1_name}\'')
            if table2_name not in aux:
                self.errors.append(f'Invalid table name into join: \'{table2_name}\'')

        if not error:
            # make the column projection
            project = ""
            for i, col in enumerate(col_names):
                project += col + ": 1"
                if i < len(col_names)-1:
                    project += ", "

            # set the fields
            collection = table_name
            from_table = join_table
            localField = table1_column if table1_name == table_name else table2_column
            foreignField = table2_column if table1_name == table_name else table1_column

            # invert things when right join
            if join_type == 'right':
                aux = collection
                collection = from_table
                from_table = aux
                aux = localField
                localField = foreignField
                foreignField = aux

            comm  = "db.%s.aggregate([\n" % collection
            comm += "   {\n"
            comm += "     $lookup:\n"
            comm += "       {\n"
            comm += "         from: \"%s\",\n" % from_table
            comm += "         localField: \"%s\",\n" % localField
            comm += "         foreignField: \"%s\"\n" % foreignField
            comm += "       }\n"
            comm += "  },\n"
            comm += "  {\n"
            comm += "    $project: {%s}\n" % project
            comm += "  }\n"
            comm += "])"
            self.memory.append(comm)

        return self.visitChildren(ctx)

    def get_select_identifiers(self, ctx:GrammarParser.Select_baseContext):
        ids = [i.getText() for i in ctx.IDENT()]
        table_name = ids[-1]
        col_names =  ids[0:-1]
        return table_name, col_names
