# Generated from grammar/Grammar.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write(".\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\7\7&\n\7\f\7\16\7)")
        buf.write("\13\7\3\b\3\b\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\3\2\5\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"")
        buf.write("\2.\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\30")
        buf.write("\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r#\3\2")
        buf.write("\2\2\17*\3\2\2\2\21\22\7u\2\2\22\23\7g\2\2\23\24\7n\2")
        buf.write("\2\24\25\7g\2\2\25\26\7e\2\2\26\27\7v\2\2\27\4\3\2\2\2")
        buf.write("\30\31\7h\2\2\31\32\7t\2\2\32\33\7q\2\2\33\34\7o\2\2\34")
        buf.write("\6\3\2\2\2\35\36\7,\2\2\36\b\3\2\2\2\37 \7=\2\2 \n\3\2")
        buf.write("\2\2!\"\7.\2\2\"\f\3\2\2\2#\'\t\2\2\2$&\t\3\2\2%$\3\2")
        buf.write("\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\16\3\2\2\2)\'\3")
        buf.write("\2\2\2*+\t\4\2\2+,\3\2\2\2,-\b\b\2\2-\20\3\2\2\2\4\2\'")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SELECT = 1
    FROM = 2
    STAR = 3
    SEMI_COLUMN = 4
    COMMA = 5
    IDENT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'select'", "'from'", "'*'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "SELECT", "FROM", "STAR", "SEMI_COLUMN", "COMMA", "IDENT", "WS" ]

    ruleNames = [ "SELECT", "FROM", "STAR", "SEMI_COLUMN", "COMMA", "IDENT", 
                  "WS" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


