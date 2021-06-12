from antlr4 import *
from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from grammar.GrammarVisitor import GrammarVisitor

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.errors = []
        self.memory = []

    def visitScript(self, ctx:GrammarParser.ScriptContext):
        return self.visitChildren(ctx)

    def visitSelect(self, ctx:GrammarParser.SelectContext):
        ids = [i.getText() for i in ctx.IDENT()]
        table_name = ids[-1]
        col_names =  ids[0:-1]

        if ctx.STAR() is not None:
            self.memory.append(f'db.{table_name}.find()')
        else:
            # check if there are duplicatated collum names
            for i, ident in enumerate(col_names[:-1]):
                for seek in ids[i+1:]:
                    if ident == seek:
                        self.errors.append(f'Duplicated column name: {ident}')
                        break
            else:
                # generate equivalent mongo code
                self.memory.append('db.%s.find({%s})' % (table_name, ','.join(col_names)))

        return self.visitChildren(ctx)
