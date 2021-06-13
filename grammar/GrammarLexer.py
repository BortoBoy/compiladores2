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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\7\rY\n\r\f\r\16\r")
        buf.write("\\\13\r\3\16\3\16\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\5\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2a\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3")
        buf.write("\2\2\2\5$\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13-\3\2\2\2\r")
        buf.write("/\3\2\2\2\17\61\3\2\2\2\21\63\3\2\2\2\23>\3\2\2\2\25I")
        buf.write("\3\2\2\2\27S\3\2\2\2\31V\3\2\2\2\33]\3\2\2\2\35\36\7u")
        buf.write("\2\2\36\37\7g\2\2\37 \7n\2\2 !\7g\2\2!\"\7e\2\2\"#\7v")
        buf.write("\2\2#\4\3\2\2\2$%\7h\2\2%&\7t\2\2&\'\7q\2\2\'(\7o\2\2")
        buf.write("(\6\3\2\2\2)*\7,\2\2*\b\3\2\2\2+,\7=\2\2,\n\3\2\2\2-.")
        buf.write("\7.\2\2.\f\3\2\2\2/\60\7\60\2\2\60\16\3\2\2\2\61\62\7")
        buf.write("?\2\2\62\20\3\2\2\2\63\64\7k\2\2\64\65\7p\2\2\65\66\7")
        buf.write("p\2\2\66\67\7g\2\2\678\7t\2\289\7\"\2\29:\7l\2\2:;\7q")
        buf.write("\2\2;<\7k\2\2<=\7p\2\2=\22\3\2\2\2>?\7t\2\2?@\7k\2\2@")
        buf.write("A\7i\2\2AB\7j\2\2BC\7v\2\2CD\7\"\2\2DE\7l\2\2EF\7q\2\2")
        buf.write("FG\7k\2\2GH\7p\2\2H\24\3\2\2\2IJ\7n\2\2JK\7g\2\2KL\7h")
        buf.write("\2\2LM\7v\2\2MN\7\"\2\2NO\7l\2\2OP\7q\2\2PQ\7k\2\2QR\7")
        buf.write("p\2\2R\26\3\2\2\2ST\7q\2\2TU\7p\2\2U\30\3\2\2\2VZ\t\2")
        buf.write("\2\2WY\t\3\2\2XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2")
        buf.write("\2[\32\3\2\2\2\\Z\3\2\2\2]^\t\4\2\2^_\3\2\2\2_`\b\16\2")
        buf.write("\2`\34\3\2\2\2\4\2Z\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SELECT = 1
    FROM = 2
    STAR = 3
    SEMI_COLUMN = 4
    COMMA = 5
    POINT = 6
    EQUALS = 7
    INNER_JOIN = 8
    RIGHT_JOIN = 9
    LEFT_JOIN = 10
    ON = 11
    IDENT = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'select'", "'from'", "'*'", "';'", "','", "'.'", "'='", "'inner join'", 
            "'right join'", "'left join'", "'on'" ]

    symbolicNames = [ "<INVALID>",
            "SELECT", "FROM", "STAR", "SEMI_COLUMN", "COMMA", "POINT", "EQUALS", 
            "INNER_JOIN", "RIGHT_JOIN", "LEFT_JOIN", "ON", "IDENT", "WS" ]

    ruleNames = [ "SELECT", "FROM", "STAR", "SEMI_COLUMN", "COMMA", "POINT", 
                  "EQUALS", "INNER_JOIN", "RIGHT_JOIN", "LEFT_JOIN", "ON", 
                  "IDENT", "WS" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


