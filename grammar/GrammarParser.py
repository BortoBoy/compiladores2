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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\3\3\3\3\3\3\3\7\3\32")
        buf.write("\n\3\f\3\16\3\35\13\3\3\3\5\3 \n\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\n\f\2")
        buf.write("\66\2\22\3\2\2\2\4\25\3\2\2\2\6$\3\2\2\2\b&\3\2\2\2\n")
        buf.write("\61\3\2\2\2\f\64\3\2\2\2\16\21\5\n\6\2\17\21\5\f\7\2\20")
        buf.write("\16\3\2\2\2\20\17\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2")
        buf.write("\22\23\3\2\2\2\23\3\3\2\2\2\24\22\3\2\2\2\25\37\7\3\2")
        buf.write("\2\26\33\7\16\2\2\27\30\7\7\2\2\30\32\7\16\2\2\31\27\3")
        buf.write("\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34 \3")
        buf.write("\2\2\2\35\33\3\2\2\2\36 \7\5\2\2\37\26\3\2\2\2\37\36\3")
        buf.write("\2\2\2 !\3\2\2\2!\"\7\4\2\2\"#\7\16\2\2#\5\3\2\2\2$%\t")
        buf.write("\2\2\2%\7\3\2\2\2&\'\5\6\4\2\'(\7\16\2\2()\7\r\2\2)*\7")
        buf.write("\16\2\2*+\7\b\2\2+,\7\16\2\2,-\7\t\2\2-.\7\16\2\2./\7")
        buf.write("\b\2\2/\60\7\16\2\2\60\t\3\2\2\2\61\62\5\4\3\2\62\63\7")
        buf.write("\6\2\2\63\13\3\2\2\2\64\65\5\4\3\2\65\66\5\b\5\2\66\67")
        buf.write("\7\6\2\2\67\r\3\2\2\2\6\20\22\33\37")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'from'", "'*'", "';'", "','", 
                     "'.'", "'='", "'inner join'", "'right join'", "'left join'", 
                     "'on'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "STAR", "SEMI_COLUMN", 
                      "COMMA", "POINT", "EQUALS", "INNER_JOIN", "RIGHT_JOIN", 
                      "LEFT_JOIN", "ON", "IDENT", "WS" ]

    RULE_script = 0
    RULE_select_base = 1
    RULE_join_type = 2
    RULE_join_base = 3
    RULE_simple_select_command = 4
    RULE_select_with_join_command = 5

    ruleNames =  [ "script", "select_base", "join_type", "join_base", "simple_select_command", 
                   "select_with_join_command" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    STAR=3
    SEMI_COLUMN=4
    COMMA=5
    POINT=6
    EQUALS=7
    INNER_JOIN=8
    RIGHT_JOIN=9
    LEFT_JOIN=10
    ON=11
    IDENT=12
    WS=13

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

        def simple_select_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Simple_select_commandContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Simple_select_commandContext,i)


        def select_with_join_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Select_with_join_commandContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Select_with_join_commandContext,i)


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
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.SELECT:
                self.state = 14
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.simple_select_command()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.select_with_join_command()
                    pass


                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_baseContext(ParserRuleContext):
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

        def STAR(self):
            return self.getToken(GrammarParser.STAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_select_base

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_base" ):
                return visitor.visitSelect_base(self)
            else:
                return visitor.visitChildren(self)




    def select_base(self):

        localctx = GrammarParser.Select_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(GrammarParser.SELECT)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.IDENT]:
                self.state = 20
                self.match(GrammarParser.IDENT)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.COMMA:
                    self.state = 21
                    self.match(GrammarParser.COMMA)
                    self.state = 22
                    self.match(GrammarParser.IDENT)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [GrammarParser.STAR]:
                self.state = 28
                self.match(GrammarParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 31
            self.match(GrammarParser.FROM)
            self.state = 32
            self.match(GrammarParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INNER_JOIN(self):
            return self.getToken(GrammarParser.INNER_JOIN, 0)

        def RIGHT_JOIN(self):
            return self.getToken(GrammarParser.RIGHT_JOIN, 0)

        def LEFT_JOIN(self):
            return self.getToken(GrammarParser.LEFT_JOIN, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_join_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoin_type" ):
                return visitor.visitJoin_type(self)
            else:
                return visitor.visitChildren(self)




    def join_type(self):

        localctx = GrammarParser.Join_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_join_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.INNER_JOIN) | (1 << GrammarParser.RIGHT_JOIN) | (1 << GrammarParser.LEFT_JOIN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_baseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def join_type(self):
            return self.getTypedRuleContext(GrammarParser.Join_typeContext,0)


        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENT)
            else:
                return self.getToken(GrammarParser.IDENT, i)

        def ON(self):
            return self.getToken(GrammarParser.ON, 0)

        def POINT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.POINT)
            else:
                return self.getToken(GrammarParser.POINT, i)

        def EQUALS(self):
            return self.getToken(GrammarParser.EQUALS, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_join_base

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoin_base" ):
                return visitor.visitJoin_base(self)
            else:
                return visitor.visitChildren(self)




    def join_base(self):

        localctx = GrammarParser.Join_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_join_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.join_type()
            self.state = 37
            self.match(GrammarParser.IDENT)
            self.state = 38
            self.match(GrammarParser.ON)
            self.state = 39
            self.match(GrammarParser.IDENT)
            self.state = 40
            self.match(GrammarParser.POINT)
            self.state = 41
            self.match(GrammarParser.IDENT)
            self.state = 42
            self.match(GrammarParser.EQUALS)
            self.state = 43
            self.match(GrammarParser.IDENT)
            self.state = 44
            self.match(GrammarParser.POINT)
            self.state = 45
            self.match(GrammarParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_select_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_base(self):
            return self.getTypedRuleContext(GrammarParser.Select_baseContext,0)


        def SEMI_COLUMN(self):
            return self.getToken(GrammarParser.SEMI_COLUMN, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_simple_select_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_select_command" ):
                return visitor.visitSimple_select_command(self)
            else:
                return visitor.visitChildren(self)




    def simple_select_command(self):

        localctx = GrammarParser.Simple_select_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simple_select_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.select_base()
            self.state = 48
            self.match(GrammarParser.SEMI_COLUMN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_with_join_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_base(self):
            return self.getTypedRuleContext(GrammarParser.Select_baseContext,0)


        def join_base(self):
            return self.getTypedRuleContext(GrammarParser.Join_baseContext,0)


        def SEMI_COLUMN(self):
            return self.getToken(GrammarParser.SEMI_COLUMN, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_select_with_join_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_with_join_command" ):
                return visitor.visitSelect_with_join_command(self)
            else:
                return visitor.visitChildren(self)




    def select_with_join_command(self):

        localctx = GrammarParser.Select_with_join_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_select_with_join_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.select_base()
            self.state = 51
            self.join_base()
            self.state = 52
            self.match(GrammarParser.SEMI_COLUMN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





