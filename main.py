from antlr4 import *
from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarVisitor import GrammarVisitor
from grammar.GrammarParser import GrammarParser
import sys

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = []

    def __del__(self):
        with open('output.txt', 'w') as f:
            for line in self.memory:
                f.write('\n'.join(memory))

    # sobrescrever métodos do GrammarVisitor e armazenas linhas do mongo em self.memory

def main(argv):
    # using the lexer make the token stream
    lexer = GrammarLexer(FileStream(argv[1]))
    stream = CommonTokenStream(lexer)

    # throwing the strem into the parser
    parser = GrammarParser(stream)

    # calling the visiotr from outter grammar rule
    visitor = MyVisitor()
    visitor.vist(parser.program())


if __name__ == '__main__':
    main(sys.argv)
