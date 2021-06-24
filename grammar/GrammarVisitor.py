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


    # Visit a parse tree produced by GrammarParser#select_base_field.
    def visitSelect_base_field(self, ctx:GrammarParser.Select_base_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#select_base_table.
    def visitSelect_base_table(self, ctx:GrammarParser.Select_base_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#select_base.
    def visitSelect_base(self, ctx:GrammarParser.Select_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#join_type.
    def visitJoin_type(self, ctx:GrammarParser.Join_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#join_base.
    def visitJoin_base(self, ctx:GrammarParser.Join_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#simple_select_command.
    def visitSimple_select_command(self, ctx:GrammarParser.Simple_select_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#select_with_join_command.
    def visitSelect_with_join_command(self, ctx:GrammarParser.Select_with_join_commandContext):
        return self.visitChildren(ctx)



del GrammarParser