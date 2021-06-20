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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13\2\3\3\3")
        buf.write("\3\5\3\34\n\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\5\4&\n")
        buf.write("\4\3\5\3\5\3\5\3\5\7\5,\n\5\f\5\16\5/\13\5\3\5\5\5\62")
        buf.write("\n\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\2\2\n\2")
        buf.write("\4\6\b\n\f\16\20\2\3\3\2\n\13\2I\2\26\3\2\2\2\4\33\3\2")
        buf.write("\2\2\6\"\3\2\2\2\b\'\3\2\2\2\n\66\3\2\2\2\f8\3\2\2\2\16")
        buf.write("C\3\2\2\2\20F\3\2\2\2\22\25\5\16\b\2\23\25\5\20\t\2\24")
        buf.write("\22\3\2\2\2\24\23\3\2\2\2\25\30\3\2\2\2\26\24\3\2\2\2")
        buf.write("\26\27\3\2\2\2\27\3\3\2\2\2\30\26\3\2\2\2\31\32\7\16\2")
        buf.write("\2\32\34\7\b\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\35\3\2")
        buf.write("\2\2\35 \7\16\2\2\36\37\7\r\2\2\37!\7\16\2\2 \36\3\2\2")
        buf.write("\2 !\3\2\2\2!\5\3\2\2\2\"%\7\16\2\2#$\7\r\2\2$&\7\16\2")
        buf.write("\2%#\3\2\2\2%&\3\2\2\2&\7\3\2\2\2\'\61\7\3\2\2(-\5\4\3")
        buf.write("\2)*\7\7\2\2*,\5\4\3\2+)\3\2\2\2,/\3\2\2\2-+\3\2\2\2-")
        buf.write(".\3\2\2\2.\62\3\2\2\2/-\3\2\2\2\60\62\7\5\2\2\61(\3\2")
        buf.write("\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\64\7\4\2\2\64\65\5")
        buf.write("\6\4\2\65\t\3\2\2\2\66\67\t\2\2\2\67\13\3\2\2\289\5\n")
        buf.write("\6\29:\5\6\4\2:;\7\f\2\2;<\7\16\2\2<=\7\b\2\2=>\7\16\2")
        buf.write("\2>?\7\t\2\2?@\7\16\2\2@A\7\b\2\2AB\7\16\2\2B\r\3\2\2")
        buf.write("\2CD\5\b\5\2DE\7\6\2\2E\17\3\2\2\2FG\5\b\5\2GH\5\f\7\2")
        buf.write("HI\7\6\2\2I\21\3\2\2\2\t\24\26\33 %-\61")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'from'", "'*'", "';'", "','", 
                     "'.'", "'='", "'right join'", "'left join'", "'on'", 
                     "'as'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "STAR", "SEMI_COLUMN", 
                      "COMMA", "POINT", "EQUALS", "RIGHT_JOIN", "LEFT_JOIN", 
                      "ON", "AS", "IDENT", "WS", "LINE_COMMENT" ]

    RULE_script = 0
    RULE_select_base_field = 1
    RULE_select_base_table = 2
    RULE_select_base = 3
    RULE_join_type = 4
    RULE_join_base = 5
    RULE_simple_select_command = 6
    RULE_select_with_join_command = 7

    ruleNames =  [ "script", "select_base_field", "select_base_table", "select_base", 
                   "join_type", "join_base", "simple_select_command", "select_with_join_command" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    STAR=3
    SEMI_COLUMN=4
    COMMA=5
    POINT=6
    EQUALS=7
    RIGHT_JOIN=8
    LEFT_JOIN=9
    ON=10
    AS=11
    IDENT=12
    WS=13
    LINE_COMMENT=14

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
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.SELECT:
                self.state = 18
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.simple_select_command()
                    pass

                elif la_ == 2:
                    self.state = 17
                    self.select_with_join_command()
                    pass


                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_base_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.table = None # Token
            self.field = None # Token
            self.alias = None # Token

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENT)
            else:
                return self.getToken(GrammarParser.IDENT, i)

        def POINT(self):
            return self.getToken(GrammarParser.POINT, 0)

        def AS(self):
            return self.getToken(GrammarParser.AS, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_select_base_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_base_field" ):
                return visitor.visitSelect_base_field(self)
            else:
                return visitor.visitChildren(self)




    def select_base_field(self):

        localctx = GrammarParser.Select_base_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select_base_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 23
                localctx.table = self.match(GrammarParser.IDENT)
                self.state = 24
                self.match(GrammarParser.POINT)


            self.state = 27
            localctx.field = self.match(GrammarParser.IDENT)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.AS:
                self.state = 28
                self.match(GrammarParser.AS)
                self.state = 29
                localctx.alias = self.match(GrammarParser.IDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_base_tableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.table = None # Token
            self.alias = None # Token

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENT)
            else:
                return self.getToken(GrammarParser.IDENT, i)

        def AS(self):
            return self.getToken(GrammarParser.AS, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_select_base_table

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_base_table" ):
                return visitor.visitSelect_base_table(self)
            else:
                return visitor.visitChildren(self)




    def select_base_table(self):

        localctx = GrammarParser.Select_base_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_select_base_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            localctx.table = self.match(GrammarParser.IDENT)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.AS:
                self.state = 33
                self.match(GrammarParser.AS)
                self.state = 34
                localctx.alias = self.match(GrammarParser.IDENT)


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

        def select_base_table(self):
            return self.getTypedRuleContext(GrammarParser.Select_base_tableContext,0)


        def STAR(self):
            return self.getToken(GrammarParser.STAR, 0)

        def select_base_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Select_base_fieldContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Select_base_fieldContext,i)


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
        self.enterRule(localctx, 6, self.RULE_select_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(GrammarParser.SELECT)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.IDENT]:
                self.state = 38
                self.select_base_field()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.COMMA:
                    self.state = 39
                    self.match(GrammarParser.COMMA)
                    self.state = 40
                    self.select_base_field()
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [GrammarParser.STAR]:
                self.state = 46
                self.match(GrammarParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 49
            self.match(GrammarParser.FROM)
            self.state = 50
            self.select_base_table()
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
        self.enterRule(localctx, 8, self.RULE_join_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==GrammarParser.RIGHT_JOIN or _la==GrammarParser.LEFT_JOIN):
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
            self.left_table = None # Token
            self.left_field = None # Token
            self.right_table = None # Token
            self.right_field = None # Token

        def join_type(self):
            return self.getTypedRuleContext(GrammarParser.Join_typeContext,0)


        def select_base_table(self):
            return self.getTypedRuleContext(GrammarParser.Select_base_tableContext,0)


        def ON(self):
            return self.getToken(GrammarParser.ON, 0)

        def POINT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.POINT)
            else:
                return self.getToken(GrammarParser.POINT, i)

        def EQUALS(self):
            return self.getToken(GrammarParser.EQUALS, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENT)
            else:
                return self.getToken(GrammarParser.IDENT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_join_base

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoin_base" ):
                return visitor.visitJoin_base(self)
            else:
                return visitor.visitChildren(self)




    def join_base(self):

        localctx = GrammarParser.Join_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_join_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.join_type()
            self.state = 55
            self.select_base_table()
            self.state = 56
            self.match(GrammarParser.ON)
            self.state = 57
            localctx.left_table = self.match(GrammarParser.IDENT)
            self.state = 58
            self.match(GrammarParser.POINT)
            self.state = 59
            localctx.left_field = self.match(GrammarParser.IDENT)
            self.state = 60
            self.match(GrammarParser.EQUALS)
            self.state = 61
            localctx.right_table = self.match(GrammarParser.IDENT)
            self.state = 62
            self.match(GrammarParser.POINT)
            self.state = 63
            localctx.right_field = self.match(GrammarParser.IDENT)
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
        self.enterRule(localctx, 12, self.RULE_simple_select_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.select_base()
            self.state = 66
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
        self.enterRule(localctx, 14, self.RULE_select_with_join_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.select_base()
            self.state = 69
            self.join_base()
            self.state = 70
            self.match(GrammarParser.SEMI_COLUMN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





