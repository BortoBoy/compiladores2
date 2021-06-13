import os
import sys
from antlr4 import *
from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from MyVisitor import MyVisitor

def main(input, output=None):
    # if input is folder execute recursivelly
    if os.path.isdir(input):
        # files base names
        base_names = os.listdir(input)
        full_names = [os.path.join(input, name) for name in base_names]
        output_folder = output
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        for name in full_names:
            output = os.path.join(output_folder,os.path.basename(name))
            main(name, output)
        return

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
