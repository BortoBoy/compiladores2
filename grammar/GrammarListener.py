# Generated from grammar/Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#hi.
    def enterHi(self, ctx:GrammarParser.HiContext):
        pass

    # Exit a parse tree produced by GrammarParser#hi.
    def exitHi(self, ctx:GrammarParser.HiContext):
        pass



del GrammarParser