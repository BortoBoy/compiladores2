from antlr4 import *
from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarListener import GrammarListener
from grammar.GrammarParser import GrammarParser
import sys

class GrammarPrintListener(GrammarListener):
    def enterHi(self, ctx):
        print("Grammar: %s" % ctx.ID())

def main(argv):
    lexer = GrammarLexer(FileStream(argv[1]))
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.hi()
    printer = GrammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
