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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\r\3\r\7\rS\n\r\f\r\16\rV\13\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\7\17^\n\17\f\17\16\17a\13\17\3\17\3\17\2\2\20")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\4\2\f\f\17\17\2e\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2")
        buf.write("\2\2\5&\3\2\2\2\7+\3\2\2\2\t-\3\2\2\2\13/\3\2\2\2\r\61")
        buf.write("\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2\23@\3\2\2\2\25J\3")
        buf.write("\2\2\2\27M\3\2\2\2\31P\3\2\2\2\33W\3\2\2\2\35[\3\2\2\2")
        buf.write("\37 \7u\2\2 !\7g\2\2!\"\7n\2\2\"#\7g\2\2#$\7e\2\2$%\7")
        buf.write("v\2\2%\4\3\2\2\2&\'\7h\2\2\'(\7t\2\2()\7q\2\2)*\7o\2\2")
        buf.write("*\6\3\2\2\2+,\7,\2\2,\b\3\2\2\2-.\7=\2\2.\n\3\2\2\2/\60")
        buf.write("\7.\2\2\60\f\3\2\2\2\61\62\7\60\2\2\62\16\3\2\2\2\63\64")
        buf.write("\7?\2\2\64\20\3\2\2\2\65\66\7t\2\2\66\67\7k\2\2\678\7")
        buf.write("i\2\289\7j\2\29:\7v\2\2:;\7\"\2\2;<\7l\2\2<=\7q\2\2=>")
        buf.write("\7k\2\2>?\7p\2\2?\22\3\2\2\2@A\7n\2\2AB\7g\2\2BC\7h\2")
        buf.write("\2CD\7v\2\2DE\7\"\2\2EF\7l\2\2FG\7q\2\2GH\7k\2\2HI\7p")
        buf.write("\2\2I\24\3\2\2\2JK\7q\2\2KL\7p\2\2L\26\3\2\2\2MN\7c\2")
        buf.write("\2NO\7u\2\2O\30\3\2\2\2PT\t\2\2\2QS\t\3\2\2RQ\3\2\2\2")
        buf.write("SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\32\3\2\2\2VT\3\2\2\2W")
        buf.write("X\t\4\2\2XY\3\2\2\2YZ\b\16\2\2Z\34\3\2\2\2[_\7%\2\2\\")
        buf.write("^\n\5\2\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3")
        buf.write("\2\2\2a_\3\2\2\2bc\b\17\2\2c\36\3\2\2\2\5\2T_\3\b\2\2")
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
    RIGHT_JOIN = 8
    LEFT_JOIN = 9
    ON = 10
    AS = 11
    IDENT = 12
    WS = 13
    LINE_COMMENT = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'select'", "'from'", "'*'", "';'", "','", "'.'", "'='", "'right join'", 
            "'left join'", "'on'", "'as'" ]

    symbolicNames = [ "<INVALID>",
            "SELECT", "FROM", "STAR", "SEMI_COLUMN", "COMMA", "POINT", "EQUALS", 
            "RIGHT_JOIN", "LEFT_JOIN", "ON", "AS", "IDENT", "WS", "LINE_COMMENT" ]

    ruleNames = [ "SELECT", "FROM", "STAR", "SEMI_COLUMN", "COMMA", "POINT", 
                  "EQUALS", "RIGHT_JOIN", "LEFT_JOIN", "ON", "AS", "IDENT", 
                  "WS", "LINE_COMMENT" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


