# Generated from grammar/Grammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\35\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\3")
        buf.write("\3\3\3\3\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\3\5\3\27\n")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\35\2\t\3\2\2\2")
        buf.write("\4\f\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13\3\2\2\2\t\7")
        buf.write("\3\2\2\2\t\n\3\2\2\2\n\3\3\2\2\2\13\t\3\2\2\2\f\26\7\3")
        buf.write("\2\2\r\22\7\b\2\2\16\17\7\7\2\2\17\21\7\b\2\2\20\16\3")
        buf.write("\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\27")
        buf.write("\3\2\2\2\24\22\3\2\2\2\25\27\7\5\2\2\26\r\3\2\2\2\26\25")
        buf.write("\3\2\2\2\27\30\3\2\2\2\30\31\7\4\2\2\31\32\7\b\2\2\32")
        buf.write("\33\7\6\2\2\33\5\3\2\2\2\5\t\22\26")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'from'", "'*'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "STAR", "SEMI_COLUMN", 
                      "COMMA", "IDENT", "WS" ]

    RULE_script = 0
    RULE_select = 1

    ruleNames =  [ "script", "select" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    STAR=3
    SEMI_COLUMN=4
    COMMA=5
    IDENT=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.SelectContext)
            else:
                return self.getTypedRuleContext(GrammarParser.SelectContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_script

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = GrammarParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.SELECT:
                self.state = 4
                self.select()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GrammarParser.SELECT, 0)

        def FROM(self):
            return self.getToken(GrammarParser.FROM, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENT)
            else:
                return self.getToken(GrammarParser.IDENT, i)

        def SEMI_COLUMN(self):
            return self.getToken(GrammarParser.SEMI_COLUMN, 0)

        def STAR(self):
            return self.getToken(GrammarParser.STAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_select

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect" ):
                return visitor.visitSelect(self)
            else:
                return visitor.visitChildren(self)




    def select(self):

        localctx = GrammarParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(GrammarParser.SELECT)
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.IDENT]:
                self.state = 11
                self.match(GrammarParser.IDENT)
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.COMMA:
                    self.state = 12
                    self.match(GrammarParser.COMMA)
                    self.state = 13
                    self.match(GrammarParser.IDENT)
                    self.state = 18
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [GrammarParser.STAR]:
                self.state = 19
                self.match(GrammarParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 22
            self.match(GrammarParser.FROM)
            self.state = 23
            self.match(GrammarParser.IDENT)
            self.state = 24
            self.match(GrammarParser.SEMI_COLUMN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





