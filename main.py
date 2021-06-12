from antlr4 import *
from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from MyVisitor import MyVisitor
import sys

def main(input, output=None):
    # using the lexer make the token stream
    lexer = GrammarLexer(FileStream(input))
    stream = CommonTokenStream(lexer)

    # throwing the strem into the parser
    parser = GrammarParser(stream)

    # calling the visitor from outter grammar rule
    visitor = MyVisitor()
    visitor.visit(parser.script())

    if output:
        with open(output, 'w') as f:
            if visitor.errors:
                f.write('\n'.join(visitor.errors))
            else:
                f.write('\n'.join(visitor.memory))
    else:
        if visitor.errors:
            print('\n'.join(visitor.errors))
        else:
            print('\n'.join(visitor.memory))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
