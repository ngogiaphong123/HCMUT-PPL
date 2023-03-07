# Generated from /Users/ngogiaphong/Dev/PPL/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("n\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\7\21S\n\21\f\21\16\21V")
        buf.write("\13\21\3\22\6\22Y\n\22\r\22\16\22Z\3\23\3\23\3\23\3\23")
        buf.write("\7\23a\n\23\f\23\16\23d\13\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26\3\2\7\4\2C\\c|\5\2\62;C\\c|\3\2\62;\3\2")
        buf.write("$$\5\2\13\f\17\17\"\"\2q\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\3+\3\2\2\2\5-\3\2\2\2\7/\3\2\2\2\t\62\3\2\2\2\13\64\3")
        buf.write("\2\2\2\r\66\3\2\2\2\179\3\2\2\2\21;\3\2\2\2\23=\3\2\2")
        buf.write("\2\25?\3\2\2\2\27A\3\2\2\2\31C\3\2\2\2\33E\3\2\2\2\35")
        buf.write("K\3\2\2\2\37N\3\2\2\2!P\3\2\2\2#X\3\2\2\2%\\\3\2\2\2\'")
        buf.write("g\3\2\2\2)k\3\2\2\2+,\7=\2\2,\4\3\2\2\2-.\7.\2\2.\6\3")
        buf.write("\2\2\2/\60\7,\2\2\60\61\7,\2\2\61\b\3\2\2\2\62\63\7*\2")
        buf.write("\2\63\n\3\2\2\2\64\65\7+\2\2\65\f\3\2\2\2\66\67\7A\2\2")
        buf.write("\678\7A\2\28\16\3\2\2\29:\7\60\2\2:\20\3\2\2\2;<\7,\2")
        buf.write("\2<\22\3\2\2\2=>\7\61\2\2>\24\3\2\2\2?@\7\'\2\2@\26\3")
        buf.write("\2\2\2AB\7-\2\2B\30\3\2\2\2CD\7/\2\2D\32\3\2\2\2EF\7c")
        buf.write("\2\2FG\7t\2\2GH\7t\2\2HI\7c\2\2IJ\7{\2\2J\34\3\2\2\2K")
        buf.write("L\7?\2\2LM\7@\2\2M\36\3\2\2\2NO\7?\2\2O \3\2\2\2PT\t\2")
        buf.write("\2\2QS\t\3\2\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2")
        buf.write("U\"\3\2\2\2VT\3\2\2\2WY\t\4\2\2XW\3\2\2\2YZ\3\2\2\2ZX")
        buf.write("\3\2\2\2Z[\3\2\2\2[$\3\2\2\2\\b\7$\2\2]a\n\5\2\2^_\7^")
        buf.write("\2\2_a\7$\2\2`]\3\2\2\2`^\3\2\2\2ad\3\2\2\2b`\3\2\2\2")
        buf.write("bc\3\2\2\2ce\3\2\2\2db\3\2\2\2ef\7$\2\2f&\3\2\2\2gh\t")
        buf.write("\6\2\2hi\3\2\2\2ij\b\24\2\2j(\3\2\2\2kl\13\2\2\2lm\b\25")
        buf.write("\3\2m*\3\2\2\2\7\2TZ`b\4\b\2\2\3\25\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SEMI = 1
    COMMA = 2
    DSTAR = 3
    LP = 4
    RP = 5
    DQUES = 6
    DOT = 7
    MUL = 8
    DIV = 9
    MOD = 10
    ADD = 11
    SUB = 12
    ARRAY = 13
    ARROW = 14
    EQ = 15
    VARNAME = 16
    INTLIT = 17
    STRINGLIT = 18
    WS = 19
    ERROR_CHAR = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'**'", "'('", "')'", "'??'", "'.'", "'*'", "'/'", 
            "'%'", "'+'", "'-'", "'array'", "'=>'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "SEMI", "COMMA", "DSTAR", "LP", "RP", "DQUES", "DOT", "MUL", 
            "DIV", "MOD", "ADD", "SUB", "ARRAY", "ARROW", "EQ", "VARNAME", 
            "INTLIT", "STRINGLIT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "SEMI", "COMMA", "DSTAR", "LP", "RP", "DQUES", "DOT", 
                  "MUL", "DIV", "MOD", "ADD", "SUB", "ARRAY", "ARROW", "EQ", 
                  "VARNAME", "INTLIT", "STRINGLIT", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[19] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


