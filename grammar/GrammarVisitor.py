# Generated from grammar/Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#script.
    def visitScript(self, ctx:GrammarParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#select.
    def visitSelect(self, ctx:GrammarParser.SelectContext):
        return self.visitChildren(ctx)



del GrammarParser