# Generated from /Users/ngogiaphong/Dev/PPL/assignment2-initial/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\u020c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0088\n\3\3\4\3\4\5\4\u008c\n\4\3\5\3\5\5\5")
        buf.write("\u0090\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a7\n\t")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00ad\n\n\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00c0\n\17\3\20\3\20\3\20\5\20\u00c5\n\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00e1\n\23\3\24\3\24\3\24\3\24\5\24\u00e7")
        buf.write("\n\24\3\25\3\25\5\25\u00eb\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u00f2\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0104")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\5\32\u010e")
        buf.write("\n\32\3\33\3\33\3\33\3\33\5\33\u0114\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0121")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\5\36\u012a\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u013a\n\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\5&\u0166\n&\3\'\3\'\3\'\3\'\3\'\3(\3(\5(\u016f")
        buf.write("\n(\3)\3)\3)\3)\3)\5)\u0176\n)\3*\3*\3*\3*\3*\5*\u017d")
        buf.write("\n*\3+\3+\3+\3+\3+\5+\u0184\n+\3,\3,\3,\3,\3,\3,\7,\u018c")
        buf.write("\n,\f,\16,\u018f\13,\3-\3-\3-\3-\3-\3-\7-\u0197\n-\f-")
        buf.write("\16-\u019a\13-\3.\3.\3.\3.\3.\3.\7.\u01a2\n.\f.\16.\u01a5")
        buf.write("\13.\3/\3/\3/\5/\u01aa\n/\3\60\3\60\3\60\5\60\u01af\n")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01b7\n\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01c1\n\62\3")
        buf.write("\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u01d1\n\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\5\66\u01dd\n\66\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\39\39\39\39\3:\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\3;\3<\3<\3<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\3@\3@\2\5VXZA\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\2\4\6\2\b\b\13\13\17\17\21")
        buf.write("\21\3\2%&\2\u0207\2\u0080\3\2\2\2\4\u0087\3\2\2\2\6\u008b")
        buf.write("\3\2\2\2\b\u008f\3\2\2\2\n\u0091\3\2\2\2\f\u0096\3\2\2")
        buf.write("\2\16\u0099\3\2\2\2\20\u00a6\3\2\2\2\22\u00ac\3\2\2\2")
        buf.write("\24\u00ae\3\2\2\2\26\u00b0\3\2\2\2\30\u00b7\3\2\2\2\32")
        buf.write("\u00b9\3\2\2\2\34\u00bf\3\2\2\2\36\u00c4\3\2\2\2 \u00c6")
        buf.write("\3\2\2\2\"\u00cb\3\2\2\2$\u00e0\3\2\2\2&\u00e6\3\2\2\2")
        buf.write("(\u00ea\3\2\2\2*\u00f1\3\2\2\2,\u0103\3\2\2\2.\u0105\3")
        buf.write("\2\2\2\60\u0109\3\2\2\2\62\u010d\3\2\2\2\64\u0113\3\2")
        buf.write("\2\2\66\u0120\3\2\2\28\u0122\3\2\2\2:\u0129\3\2\2\2<\u0139")
        buf.write("\3\2\2\2>\u013b\3\2\2\2@\u0147\3\2\2\2B\u014d\3\2\2\2")
        buf.write("D\u0155\3\2\2\2F\u0158\3\2\2\2H\u015b\3\2\2\2J\u0165\3")
        buf.write("\2\2\2L\u0167\3\2\2\2N\u016e\3\2\2\2P\u0175\3\2\2\2R\u017c")
        buf.write("\3\2\2\2T\u0183\3\2\2\2V\u0185\3\2\2\2X\u0190\3\2\2\2")
        buf.write("Z\u019b\3\2\2\2\\\u01a9\3\2\2\2^\u01ae\3\2\2\2`\u01b6")
        buf.write("\3\2\2\2b\u01c0\3\2\2\2d\u01c2\3\2\2\2f\u01c6\3\2\2\2")
        buf.write("h\u01d0\3\2\2\2j\u01dc\3\2\2\2l\u01de\3\2\2\2n\u01e2\3")
        buf.write("\2\2\2p\u01e7\3\2\2\2r\u01eb\3\2\2\2t\u01f0\3\2\2\2v\u01f4")
        buf.write("\3\2\2\2x\u01f9\3\2\2\2z\u01fd\3\2\2\2|\u0202\3\2\2\2")
        buf.write("~\u0207\3\2\2\2\u0080\u0081\5\4\3\2\u0081\u0082\7\2\2")
        buf.write("\3\u0082\3\3\2\2\2\u0083\u0084\5\6\4\2\u0084\u0085\5\4")
        buf.write("\3\2\u0085\u0088\3\2\2\2\u0086\u0088\5\6\4\2\u0087\u0083")
        buf.write("\3\2\2\2\u0087\u0086\3\2\2\2\u0088\5\3\2\2\2\u0089\u008c")
        buf.write("\5\b\5\2\u008a\u008c\5\"\22\2\u008b\u0089\3\2\2\2\u008b")
        buf.write("\u008a\3\2\2\2\u008c\7\3\2\2\2\u008d\u0090\5\n\6\2\u008e")
        buf.write("\u0090\5\f\7\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\t\3\2\2\2\u0091\u0092\5\22\n\2\u0092\u0093\7#\2")
        buf.write("\2\u0093\u0094\5\36\20\2\u0094\u0095\7\37\2\2\u0095\13")
        buf.write("\3\2\2\2\u0096\u0097\5\20\t\2\u0097\u0098\7\37\2\2\u0098")
        buf.write("\r\3\2\2\2\u0099\u009a\7\66\2\2\u009a\u009b\7#\2\2\u009b")
        buf.write("\u009c\5\36\20\2\u009c\u009d\7$\2\2\u009d\u009e\5R*\2")
        buf.write("\u009e\17\3\2\2\2\u009f\u00a0\7\66\2\2\u00a0\u00a1\7 ")
        buf.write("\2\2\u00a1\u00a2\5\20\t\2\u00a2\u00a3\7 \2\2\u00a3\u00a4")
        buf.write("\5R*\2\u00a4\u00a7\3\2\2\2\u00a5\u00a7\5\16\b\2\u00a6")
        buf.write("\u009f\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\21\3\2\2\2\u00a8")
        buf.write("\u00a9\7\66\2\2\u00a9\u00aa\7 \2\2\u00aa\u00ad\5\22\n")
        buf.write("\2\u00ab\u00ad\7\66\2\2\u00ac\u00a8\3\2\2\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ad\23\3\2\2\2\u00ae\u00af\t\2\2\2\u00af\25")
        buf.write("\3\2\2\2\u00b0\u00b1\7\30\2\2\u00b1\u00b2\7\35\2\2\u00b2")
        buf.write("\u00b3\5\34\17\2\u00b3\u00b4\7\36\2\2\u00b4\u00b5\7\26")
        buf.write("\2\2\u00b5\u00b6\5\24\13\2\u00b6\27\3\2\2\2\u00b7\u00b8")
        buf.write("\7\23\2\2\u00b8\31\3\2\2\2\u00b9\u00ba\7\6\2\2\u00ba\33")
        buf.write("\3\2\2\2\u00bb\u00bc\7\67\2\2\u00bc\u00bd\7 \2\2\u00bd")
        buf.write("\u00c0\5\34\17\2\u00be\u00c0\7\67\2\2\u00bf\u00bb\3\2")
        buf.write("\2\2\u00bf\u00be\3\2\2\2\u00c0\35\3\2\2\2\u00c1\u00c5")
        buf.write("\5\32\16\2\u00c2\u00c5\5\24\13\2\u00c3\u00c5\5\26\f\2")
        buf.write("\u00c4\u00c1\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3")
        buf.write("\2\2\2\u00c5\37\3\2\2\2\u00c6\u00c7\7\66\2\2\u00c7\u00c8")
        buf.write("\7\35\2\2\u00c8\u00c9\5N(\2\u00c9\u00ca\7\36\2\2\u00ca")
        buf.write("!\3\2\2\2\u00cb\u00cc\5$\23\2\u00cc\u00cd\5\60\31\2\u00cd")
        buf.write("#\3\2\2\2\u00ce\u00cf\7\66\2\2\u00cf\u00d0\7#\2\2\u00d0")
        buf.write("\u00d1\7\r\2\2\u00d1\u00d2\5&\24\2\u00d2\u00d3\7\31\2")
        buf.write("\2\u00d3\u00d4\5(\25\2\u00d4\u00d5\7\32\2\2\u00d5\u00e1")
        buf.write("\3\2\2\2\u00d6\u00d7\7\66\2\2\u00d7\u00d8\7#\2\2\u00d8")
        buf.write("\u00d9\7\r\2\2\u00d9\u00da\5&\24\2\u00da\u00db\7\31\2")
        buf.write("\2\u00db\u00dc\5(\25\2\u00dc\u00dd\7\32\2\2\u00dd\u00de")
        buf.write("\7\27\2\2\u00de\u00df\7\66\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00ce\3\2\2\2\u00e0\u00d6\3\2\2\2\u00e1%\3\2\2\2\u00e2")
        buf.write("\u00e7\5\24\13\2\u00e3\u00e7\5\30\r\2\u00e4\u00e7\5\26")
        buf.write("\f\2\u00e5\u00e7\5\32\16\2\u00e6\u00e2\3\2\2\2\u00e6\u00e3")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7")
        buf.write("\'\3\2\2\2\u00e8\u00eb\5*\26\2\u00e9\u00eb\3\2\2\2\u00ea")
        buf.write("\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb)\3\2\2\2\u00ec")
        buf.write("\u00ed\5,\27\2\u00ed\u00ee\7 \2\2\u00ee\u00ef\5*\26\2")
        buf.write("\u00ef\u00f2\3\2\2\2\u00f0\u00f2\5,\27\2\u00f1\u00ec\3")
        buf.write("\2\2\2\u00f1\u00f0\3\2\2\2\u00f2+\3\2\2\2\u00f3\u00f4")
        buf.write("\7\66\2\2\u00f4\u00f5\7#\2\2\u00f5\u0104\5\36\20\2\u00f6")
        buf.write("\u00f7\7\27\2\2\u00f7\u00f8\7\66\2\2\u00f8\u00f9\7#\2")
        buf.write("\2\u00f9\u0104\5\36\20\2\u00fa\u00fb\7\24\2\2\u00fb\u00fc")
        buf.write("\7\66\2\2\u00fc\u00fd\7#\2\2\u00fd\u0104\5\36\20\2\u00fe")
        buf.write("\u00ff\7\27\2\2\u00ff\u0100\7\24\2\2\u0100\u0101\7\66")
        buf.write("\2\2\u0101\u0102\7#\2\2\u0102\u0104\5\36\20\2\u0103\u00f3")
        buf.write("\3\2\2\2\u0103\u00f6\3\2\2\2\u0103\u00fa\3\2\2\2\u0103")
        buf.write("\u00fe\3\2\2\2\u0104-\3\2\2\2\u0105\u0106\7\33\2\2\u0106")
        buf.write("\u0107\5\62\32\2\u0107\u0108\7\34\2\2\u0108/\3\2\2\2\u0109")
        buf.write("\u010a\5.\30\2\u010a\61\3\2\2\2\u010b\u010e\5\64\33\2")
        buf.write("\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010c\3")
        buf.write("\2\2\2\u010e\63\3\2\2\2\u010f\u0110\5\66\34\2\u0110\u0111")
        buf.write("\5\64\33\2\u0111\u0114\3\2\2\2\u0112\u0114\3\2\2\2\u0113")
        buf.write("\u010f\3\2\2\2\u0113\u0112\3\2\2\2\u0114\65\3\2\2\2\u0115")
        buf.write("\u0121\5\b\5\2\u0116\u0121\58\35\2\u0117\u0121\5<\37\2")
        buf.write("\u0118\u0121\5> \2\u0119\u0121\5@!\2\u011a\u0121\5B\"")
        buf.write("\2\u011b\u0121\5D#\2\u011c\u0121\5F$\2\u011d\u0121\5H")
        buf.write("%\2\u011e\u0121\5J&\2\u011f\u0121\5.\30\2\u0120\u0115")
        buf.write("\3\2\2\2\u0120\u0116\3\2\2\2\u0120\u0117\3\2\2\2\u0120")
        buf.write("\u0118\3\2\2\2\u0120\u0119\3\2\2\2\u0120\u011a\3\2\2\2")
        buf.write("\u0120\u011b\3\2\2\2\u0120\u011c\3\2\2\2\u0120\u011d\3")
        buf.write("\2\2\2\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121\67")
        buf.write("\3\2\2\2\u0122\u0123\5:\36\2\u0123\u0124\7$\2\2\u0124")
        buf.write("\u0125\5R*\2\u0125\u0126\7\37\2\2\u01269\3\2\2\2\u0127")
        buf.write("\u012a\7\66\2\2\u0128\u012a\5 \21\2\u0129\u0127\3\2\2")
        buf.write("\2\u0129\u0128\3\2\2\2\u012a;\3\2\2\2\u012b\u012c\7\16")
        buf.write("\2\2\u012c\u012d\7\31\2\2\u012d\u012e\5R*\2\u012e\u012f")
        buf.write("\7\32\2\2\u012f\u0130\5\66\34\2\u0130\u013a\3\2\2\2\u0131")
        buf.write("\u0132\7\16\2\2\u0132\u0133\7\31\2\2\u0133\u0134\5R*\2")
        buf.write("\u0134\u0135\7\32\2\2\u0135\u0136\5\66\34\2\u0136\u0137")
        buf.write("\7\n\2\2\u0137\u0138\5\66\34\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u012b\3\2\2\2\u0139\u0131\3\2\2\2\u013a=\3\2\2\2\u013b")
        buf.write("\u013c\7\f\2\2\u013c\u013d\7\31\2\2\u013d\u013e\7\66\2")
        buf.write("\2\u013e\u013f\7$\2\2\u013f\u0140\5R*\2\u0140\u0141\7")
        buf.write(" \2\2\u0141\u0142\5R*\2\u0142\u0143\7 \2\2\u0143\u0144")
        buf.write("\5R*\2\u0144\u0145\7\32\2\2\u0145\u0146\5\66\34\2\u0146")
        buf.write("?\3\2\2\2\u0147\u0148\7\22\2\2\u0148\u0149\7\31\2\2\u0149")
        buf.write("\u014a\5R*\2\u014a\u014b\7\32\2\2\u014b\u014c\5\66\34")
        buf.write("\2\u014cA\3\2\2\2\u014d\u014e\7\t\2\2\u014e\u014f\5\66")
        buf.write("\34\2\u014f\u0150\7\22\2\2\u0150\u0151\7\31\2\2\u0151")
        buf.write("\u0152\5R*\2\u0152\u0153\7\32\2\2\u0153\u0154\7\37\2\2")
        buf.write("\u0154C\3\2\2\2\u0155\u0156\7\7\2\2\u0156\u0157\7\37\2")
        buf.write("\2\u0157E\3\2\2\2\u0158\u0159\7\25\2\2\u0159\u015a\7\37")
        buf.write("\2\2\u015aG\3\2\2\2\u015b\u015c\7\20\2\2\u015c\u015d\5")
        buf.write("N(\2\u015d\u015e\7\37\2\2\u015eI\3\2\2\2\u015f\u0160\5")
        buf.write("j\66\2\u0160\u0161\7\37\2\2\u0161\u0166\3\2\2\2\u0162")
        buf.write("\u0163\5L\'\2\u0163\u0164\7\37\2\2\u0164\u0166\3\2\2\2")
        buf.write("\u0165\u015f\3\2\2\2\u0165\u0162\3\2\2\2\u0166K\3\2\2")
        buf.write("\2\u0167\u0168\7\66\2\2\u0168\u0169\7\31\2\2\u0169\u016a")
        buf.write("\5N(\2\u016a\u016b\7\32\2\2\u016bM\3\2\2\2\u016c\u016f")
        buf.write("\5P)\2\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016fO\3\2\2\2\u0170\u0171\5R*\2\u0171\u0172")
        buf.write("\7 \2\2\u0172\u0173\5P)\2\u0173\u0176\3\2\2\2\u0174\u0176")
        buf.write("\5R*\2\u0175\u0170\3\2\2\2\u0175\u0174\3\2\2\2\u0176Q")
        buf.write("\3\2\2\2\u0177\u0178\5T+\2\u0178\u0179\7(\2\2\u0179\u017a")
        buf.write("\5T+\2\u017a\u017d\3\2\2\2\u017b\u017d\5T+\2\u017c\u0177")
        buf.write("\3\2\2\2\u017c\u017b\3\2\2\2\u017dS\3\2\2\2\u017e\u017f")
        buf.write("\5V,\2\u017f\u0180\7\3\2\2\u0180\u0181\5V,\2\u0181\u0184")
        buf.write("\3\2\2\2\u0182\u0184\5V,\2\u0183\u017e\3\2\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184U\3\2\2\2\u0185\u0186\b,\1\2\u0186\u0187")
        buf.write("\5X-\2\u0187\u018d\3\2\2\2\u0188\u0189\f\4\2\2\u0189\u018a")
        buf.write("\7\4\2\2\u018a\u018c\5X-\2\u018b\u0188\3\2\2\2\u018c\u018f")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("W\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\b-\1\2\u0191")
        buf.write("\u0192\5Z.\2\u0192\u0198\3\2\2\2\u0193\u0194\f\4\2\2\u0194")
        buf.write("\u0195\t\3\2\2\u0195\u0197\5Z.\2\u0196\u0193\3\2\2\2\u0197")
        buf.write("\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199Y\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\b.\1\2")
        buf.write("\u019c\u019d\5\\/\2\u019d\u01a3\3\2\2\2\u019e\u019f\f")
        buf.write("\4\2\2\u019f\u01a0\7\5\2\2\u01a0\u01a2\5\\/\2\u01a1\u019e")
        buf.write("\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4[\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6")
        buf.write("\u01a7\7\'\2\2\u01a7\u01aa\5\\/\2\u01a8\u01aa\5^\60\2")
        buf.write("\u01a9\u01a6\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa]\3\2\2")
        buf.write("\2\u01ab\u01ac\7&\2\2\u01ac\u01af\5^\60\2\u01ad\u01af")
        buf.write("\5`\61\2\u01ae\u01ab\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af")
        buf.write("_\3\2\2\2\u01b0\u01b1\7\66\2\2\u01b1\u01b2\7\35\2\2\u01b2")
        buf.write("\u01b3\5P)\2\u01b3\u01b4\7\36\2\2\u01b4\u01b7\3\2\2\2")
        buf.write("\u01b5\u01b7\5b\62\2\u01b6\u01b0\3\2\2\2\u01b6\u01b5\3")
        buf.write("\2\2\2\u01b7a\3\2\2\2\u01b8\u01c1\7\67\2\2\u01b9\u01c1")
        buf.write("\78\2\2\u01ba\u01c1\7:\2\2\u01bb\u01c1\7\65\2\2\u01bc")
        buf.write("\u01c1\7\66\2\2\u01bd\u01c1\5f\64\2\u01be\u01c1\5h\65")
        buf.write("\2\u01bf\u01c1\5d\63\2\u01c0\u01b8\3\2\2\2\u01c0\u01b9")
        buf.write("\3\2\2\2\u01c0\u01ba\3\2\2\2\u01c0\u01bb\3\2\2\2\u01c0")
        buf.write("\u01bc\3\2\2\2\u01c0\u01bd\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c0\u01bf\3\2\2\2\u01c1c\3\2\2\2\u01c2\u01c3\7\33\2")
        buf.write("\2\u01c3\u01c4\5N(\2\u01c4\u01c5\7\34\2\2\u01c5e\3\2\2")
        buf.write("\2\u01c6\u01c7\7\31\2\2\u01c7\u01c8\5R*\2\u01c8\u01c9")
        buf.write("\7\32\2\2\u01c9g\3\2\2\2\u01ca\u01d1\5j\66\2\u01cb\u01cc")
        buf.write("\7\66\2\2\u01cc\u01cd\7\31\2\2\u01cd\u01ce\5N(\2\u01ce")
        buf.write("\u01cf\7\32\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ca\3\2\2")
        buf.write("\2\u01d0\u01cb\3\2\2\2\u01d1i\3\2\2\2\u01d2\u01dd\5l\67")
        buf.write("\2\u01d3\u01dd\5n8\2\u01d4\u01dd\5p9\2\u01d5\u01dd\5r")
        buf.write(":\2\u01d6\u01dd\5t;\2\u01d7\u01dd\5v<\2\u01d8\u01dd\5")
        buf.write("x=\2\u01d9\u01dd\5z>\2\u01da\u01dd\5|?\2\u01db\u01dd\5")
        buf.write("~@\2\u01dc\u01d2\3\2\2\2\u01dc\u01d3\3\2\2\2\u01dc\u01d4")
        buf.write("\3\2\2\2\u01dc\u01d5\3\2\2\2\u01dc\u01d6\3\2\2\2\u01dc")
        buf.write("\u01d7\3\2\2\2\u01dc\u01d8\3\2\2\2\u01dc\u01d9\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dc\u01db\3\2\2\2\u01ddk\3\2\2")
        buf.write("\2\u01de\u01df\7)\2\2\u01df\u01e0\7\31\2\2\u01e0\u01e1")
        buf.write("\7\32\2\2\u01e1m\3\2\2\2\u01e2\u01e3\7*\2\2\u01e3\u01e4")
        buf.write("\7\31\2\2\u01e4\u01e5\5R*\2\u01e5\u01e6\7\32\2\2\u01e6")
        buf.write("o\3\2\2\2\u01e7\u01e8\7+\2\2\u01e8\u01e9\7\31\2\2\u01e9")
        buf.write("\u01ea\7\32\2\2\u01eaq\3\2\2\2\u01eb\u01ec\7,\2\2\u01ec")
        buf.write("\u01ed\7\31\2\2\u01ed\u01ee\5R*\2\u01ee\u01ef\7\32\2\2")
        buf.write("\u01efs\3\2\2\2\u01f0\u01f1\7-\2\2\u01f1\u01f2\7\31\2")
        buf.write("\2\u01f2\u01f3\7\32\2\2\u01f3u\3\2\2\2\u01f4\u01f5\7.")
        buf.write("\2\2\u01f5\u01f6\7\31\2\2\u01f6\u01f7\5R*\2\u01f7\u01f8")
        buf.write("\7\32\2\2\u01f8w\3\2\2\2\u01f9\u01fa\7/\2\2\u01fa\u01fb")
        buf.write("\7\31\2\2\u01fb\u01fc\7\32\2\2\u01fcy\3\2\2\2\u01fd\u01fe")
        buf.write("\7\60\2\2\u01fe\u01ff\7\31\2\2\u01ff\u0200\5R*\2\u0200")
        buf.write("\u0201\7\32\2\2\u0201{\3\2\2\2\u0202\u0203\7\61\2\2\u0203")
        buf.write("\u0204\7\31\2\2\u0204\u0205\5N(\2\u0205\u0206\7\32\2\2")
        buf.write("\u0206}\3\2\2\2\u0207\u0208\7\62\2\2\u0208\u0209\7\31")
        buf.write("\2\2\u0209\u020a\7\32\2\2\u020a\177\3\2\2\2!\u0087\u008b")
        buf.write("\u008f\u00a6\u00ac\u00bf\u00c4\u00e0\u00e6\u00ea\u00f1")
        buf.write("\u0103\u010d\u0113\u0120\u0129\u0139\u0165\u016e\u0175")
        buf.write("\u017c\u0183\u018d\u0198\u01a3\u01a9\u01ae\u01b6\u01c0")
        buf.write("\u01d0\u01dc")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
                     "'float'", "'for'", "'function'", "'if'", "'integer'", 
                     "'return'", "'string'", "'while'", "'void'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "<INVALID>", 
                     "<INVALID>", "':'", "'='", "'+'", "'-'", "'!'", "'::'", 
                     "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
                     "'readBoolean'", "'printBoolean'", "'readString'", 
                     "'printString'", "'super'", "'preventDefault'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "COMPARE", "ANDOR", "MULDIVMOD", "AUTO", 
                      "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                      "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                      "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "SEMI", "COMMA", "QUOTE", "DQUOTE", "COLON", 
                      "ASSIGN", "ADD", "SUB", "CLAIM", "CONCAT", "READINTEGER", 
                      "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", "READBOOLEAN", 
                      "PRINTBOOLEAN", "READSTRING", "PRINTSTRING", "SUPER", 
                      "PREVENTDEFAULT", "CSTYLE", "LINECOMMENT", "BOOLEANLIT", 
                      "IDENTIFIER", "INTLIT", "FLOATLIT", "DOT", "STRINGLIT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declarationList = 1
    RULE_declaration = 2
    RULE_varDeclaration = 3
    RULE_initVarDeclaration = 4
    RULE_fullVarDeclaration = 5
    RULE_baseVarDeclaration = 6
    RULE_helper = 7
    RULE_idList = 8
    RULE_atomicType = 9
    RULE_arrayType = 10
    RULE_voidType = 11
    RULE_autoType = 12
    RULE_dimensions = 13
    RULE_typeSpecifier = 14
    RULE_arrayCell = 15
    RULE_funcDeclaration = 16
    RULE_functionPrototype = 17
    RULE_returnType = 18
    RULE_parameters = 19
    RULE_parameterList = 20
    RULE_parameter = 21
    RULE_blockStatement = 22
    RULE_functionBody = 23
    RULE_statements = 24
    RULE_statementList = 25
    RULE_statement = 26
    RULE_assignmentStatement = 27
    RULE_leftHandSide = 28
    RULE_ifStatement = 29
    RULE_forStatement = 30
    RULE_whileStatement = 31
    RULE_doWhileStatement = 32
    RULE_breakStatement = 33
    RULE_continueStatement = 34
    RULE_returnStatement = 35
    RULE_callStatement = 36
    RULE_call = 37
    RULE_expressions = 38
    RULE_expressionList = 39
    RULE_expression = 40
    RULE_expression1 = 41
    RULE_expression2 = 42
    RULE_expression3 = 43
    RULE_expression4 = 44
    RULE_expression5 = 45
    RULE_expression6 = 46
    RULE_expression7 = 47
    RULE_expression8 = 48
    RULE_arrayLit = 49
    RULE_subExpression = 50
    RULE_callExpression = 51
    RULE_specialFunctionCall = 52
    RULE_readIntegerCall = 53
    RULE_printIntegerCall = 54
    RULE_readFloatCall = 55
    RULE_writeFloatCall = 56
    RULE_readBooleanCall = 57
    RULE_printBooleanCall = 58
    RULE_readStringCall = 59
    RULE_printStringCall = 60
    RULE_superCall = 61
    RULE_preventDefaultCall = 62

    ruleNames =  [ "program", "declarationList", "declaration", "varDeclaration", 
                   "initVarDeclaration", "fullVarDeclaration", "baseVarDeclaration", 
                   "helper", "idList", "atomicType", "arrayType", "voidType", 
                   "autoType", "dimensions", "typeSpecifier", "arrayCell", 
                   "funcDeclaration", "functionPrototype", "returnType", 
                   "parameters", "parameterList", "parameter", "blockStatement", 
                   "functionBody", "statements", "statementList", "statement", 
                   "assignmentStatement", "leftHandSide", "ifStatement", 
                   "forStatement", "whileStatement", "doWhileStatement", 
                   "breakStatement", "continueStatement", "returnStatement", 
                   "callStatement", "call", "expressions", "expressionList", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "expression8", "arrayLit", "subExpression", "callExpression", 
                   "specialFunctionCall", "readIntegerCall", "printIntegerCall", 
                   "readFloatCall", "writeFloatCall", "readBooleanCall", 
                   "printBooleanCall", "readStringCall", "printStringCall", 
                   "superCall", "preventDefaultCall" ]

    EOF = Token.EOF
    COMPARE=1
    ANDOR=2
    MULDIVMOD=3
    AUTO=4
    BREAK=5
    BOOLEAN=6
    DO=7
    ELSE=8
    FLOAT=9
    FOR=10
    FUNCTION=11
    IF=12
    INTEGER=13
    RETURN=14
    STRING=15
    WHILE=16
    VOID=17
    OUT=18
    CONTINUE=19
    OF=20
    INHERIT=21
    ARRAY=22
    LPAREN=23
    RPAREN=24
    LBRACE=25
    RBRACE=26
    LBRACKET=27
    RBRACKET=28
    SEMI=29
    COMMA=30
    QUOTE=31
    DQUOTE=32
    COLON=33
    ASSIGN=34
    ADD=35
    SUB=36
    CLAIM=37
    CONCAT=38
    READINTEGER=39
    PRINTINTEGER=40
    READFLOAT=41
    WRITEFLOAT=42
    READBOOLEAN=43
    PRINTBOOLEAN=44
    READSTRING=45
    PRINTSTRING=46
    SUPER=47
    PREVENTDEFAULT=48
    CSTYLE=49
    LINECOMMENT=50
    BOOLEANLIT=51
    IDENTIFIER=52
    INTLIT=53
    FLOATLIT=54
    DOT=55
    STRINGLIT=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58
    WS=59
    ERROR_CHAR=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationList(self):
            return self.getTypedRuleContext(MT22Parser.DeclarationListContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.declarationList()
            self.state = 127
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MT22Parser.DeclarationContext,0)


        def declarationList(self):
            return self.getTypedRuleContext(MT22Parser.DeclarationListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declarationList




    def declarationList(self):

        localctx = MT22Parser.DeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarationList)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.declaration()
                self.state = 130
                self.declarationList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.VarDeclarationContext,0)


        def funcDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.FuncDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declaration




    def declaration(self):

        localctx = MT22Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.varDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.funcDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initVarDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.InitVarDeclarationContext,0)


        def fullVarDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.FullVarDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_varDeclaration




    def varDeclaration(self):

        localctx = MT22Parser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.initVarDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.fullVarDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitVarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(MT22Parser.IdListContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(MT22Parser.TypeSpecifierContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_initVarDeclaration




    def initVarDeclaration(self):

        localctx = MT22Parser.InitVarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_initVarDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.idList()
            self.state = 144
            self.match(MT22Parser.COLON)
            self.state = 145
            self.typeSpecifier()
            self.state = 146
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FullVarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def helper(self):
            return self.getTypedRuleContext(MT22Parser.HelperContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_fullVarDeclaration




    def fullVarDeclaration(self):

        localctx = MT22Parser.FullVarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fullVarDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.helper()
            self.state = 149
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseVarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(MT22Parser.TypeSpecifierContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_baseVarDeclaration




    def baseVarDeclaration(self):

        localctx = MT22Parser.BaseVarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_baseVarDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MT22Parser.IDENTIFIER)
            self.state = 152
            self.match(MT22Parser.COLON)
            self.state = 153
            self.typeSpecifier()
            self.state = 154
            self.match(MT22Parser.ASSIGN)
            self.state = 155
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HelperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def helper(self):
            return self.getTypedRuleContext(MT22Parser.HelperContext,0)


        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def baseVarDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.BaseVarDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_helper




    def helper(self):

        localctx = MT22Parser.HelperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_helper)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(MT22Parser.IDENTIFIER)
                self.state = 158
                self.match(MT22Parser.COMMA)
                self.state = 159
                self.helper()
                self.state = 160
                self.match(MT22Parser.COMMA)
                self.state = 161
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.baseVarDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def idList(self):
            return self.getTypedRuleContext(MT22Parser.IdListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idList




    def idList(self):

        localctx = MT22Parser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idList)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(MT22Parser.IDENTIFIER)
                self.state = 167
                self.match(MT22Parser.COMMA)
                self.state = 168
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(MT22Parser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomicType




    def atomicType(self):

        localctx = MT22Parser.AtomicTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atomicType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LBRACKET(self):
            return self.getToken(MT22Parser.LBRACKET, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def RBRACKET(self):
            return self.getToken(MT22Parser.RBRACKET, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomicType(self):
            return self.getTypedRuleContext(MT22Parser.AtomicTypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arrayType




    def arrayType(self):

        localctx = MT22Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MT22Parser.ARRAY)
            self.state = 175
            self.match(MT22Parser.LBRACKET)
            self.state = 176
            self.dimensions()
            self.state = 177
            self.match(MT22Parser.RBRACKET)
            self.state = 178
            self.match(MT22Parser.OF)
            self.state = 179
            self.atomicType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_voidType




    def voidType(self):

        localctx = MT22Parser.VoidTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_voidType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MT22Parser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutoTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_autoType




    def autoType(self):

        localctx = MT22Parser.AutoTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_autoType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MT22Parser.AUTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimensions




    def dimensions(self):

        localctx = MT22Parser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dimensions)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(MT22Parser.INTLIT)
                self.state = 186
                self.match(MT22Parser.COMMA)
                self.state = 187
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(MT22Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def autoType(self):
            return self.getTypedRuleContext(MT22Parser.AutoTypeContext,0)


        def atomicType(self):
            return self.getTypedRuleContext(MT22Parser.AtomicTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_typeSpecifier




    def typeSpecifier(self):

        localctx = MT22Parser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typeSpecifier)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.autoType()
                pass
            elif token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.atomicType()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayCellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(MT22Parser.LBRACKET, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RBRACKET(self):
            return self.getToken(MT22Parser.RBRACKET, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayCell




    def arrayCell(self):

        localctx = MT22Parser.ArrayCellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrayCell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MT22Parser.IDENTIFIER)
            self.state = 197
            self.match(MT22Parser.LBRACKET)
            self.state = 198
            self.expressions()
            self.state = 199
            self.match(MT22Parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionPrototype(self):
            return self.getTypedRuleContext(MT22Parser.FunctionPrototypeContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(MT22Parser.FunctionBodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcDeclaration




    def funcDeclaration(self):

        localctx = MT22Parser.FuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funcDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.functionPrototype()
            self.state = 202
            self.functionBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionPrototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IDENTIFIER)
            else:
                return self.getToken(MT22Parser.IDENTIFIER, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def returnType(self):
            return self.getTypedRuleContext(MT22Parser.ReturnTypeContext,0)


        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(MT22Parser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functionPrototype




    def functionPrototype(self):

        localctx = MT22Parser.FunctionPrototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionPrototype)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(MT22Parser.IDENTIFIER)
                self.state = 205
                self.match(MT22Parser.COLON)
                self.state = 206
                self.match(MT22Parser.FUNCTION)
                self.state = 207
                self.returnType()
                self.state = 208
                self.match(MT22Parser.LPAREN)
                self.state = 209
                self.parameters()
                self.state = 210
                self.match(MT22Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(MT22Parser.IDENTIFIER)
                self.state = 213
                self.match(MT22Parser.COLON)
                self.state = 214
                self.match(MT22Parser.FUNCTION)
                self.state = 215
                self.returnType()
                self.state = 216
                self.match(MT22Parser.LPAREN)
                self.state = 217
                self.parameters()
                self.state = 218
                self.match(MT22Parser.RPAREN)
                self.state = 219
                self.match(MT22Parser.INHERIT)
                self.state = 220
                self.match(MT22Parser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomicType(self):
            return self.getTypedRuleContext(MT22Parser.AtomicTypeContext,0)


        def voidType(self):
            return self.getTypedRuleContext(MT22Parser.VoidTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def autoType(self):
            return self.getTypedRuleContext(MT22Parser.AutoTypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnType




    def returnType(self):

        localctx = MT22Parser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returnType)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.atomicType()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.voidType()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.arrayType()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 227
                self.autoType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterList(self):
            return self.getTypedRuleContext(MT22Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameters




    def parameters(self):

        localctx = MT22Parser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameters)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.parameterList()
                pass
            elif token in [MT22Parser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MT22Parser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def parameterList(self):
            return self.getTypedRuleContext(MT22Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameterList




    def parameterList(self):

        localctx = MT22Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameterList)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.parameter()
                self.state = 235
                self.match(MT22Parser.COMMA)
                self.state = 236
                self.parameterList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(MT22Parser.TypeSpecifierContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(MT22Parser.IDENTIFIER)
                self.state = 242
                self.match(MT22Parser.COLON)
                self.state = 243
                self.typeSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(MT22Parser.INHERIT)
                self.state = 245
                self.match(MT22Parser.IDENTIFIER)
                self.state = 246
                self.match(MT22Parser.COLON)
                self.state = 247
                self.typeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(MT22Parser.OUT)
                self.state = 249
                self.match(MT22Parser.IDENTIFIER)
                self.state = 250
                self.match(MT22Parser.COLON)
                self.state = 251
                self.typeSpecifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.match(MT22Parser.INHERIT)
                self.state = 253
                self.match(MT22Parser.OUT)
                self.state = 254
                self.match(MT22Parser.IDENTIFIER)
                self.state = 255
                self.match(MT22Parser.COLON)
                self.state = 256
                self.typeSpecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MT22Parser.LBRACE, 0)

        def statements(self):
            return self.getTypedRuleContext(MT22Parser.StatementsContext,0)


        def RBRACE(self):
            return self.getToken(MT22Parser.RBRACE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockStatement




    def blockStatement(self):

        localctx = MT22Parser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MT22Parser.LBRACE)
            self.state = 260
            self.statements()
            self.state = 261
            self.match(MT22Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionBody




    def functionBody(self):

        localctx = MT22Parser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_functionBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(MT22Parser.StatementListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statements




    def statements(self):

        localctx = MT22Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statements)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(MT22Parser.StatementListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statementList




    def statementList(self):

        localctx = MT22Parser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statementList)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.LBRACE, MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.READBOOLEAN, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.statement()
                self.state = 270
                self.statementList()
                pass
            elif token in [MT22Parser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.VarDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(MT22Parser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MT22Parser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MT22Parser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MT22Parser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(MT22Parser.DoWhileStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(MT22Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(MT22Parser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MT22Parser.ReturnStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(MT22Parser.CallStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.varDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.assignmentStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 278
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 279
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 280
                self.doWhileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 281
                self.breakStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 282
                self.continueStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 283
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 284
                self.callStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 285
                self.blockStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leftHandSide(self):
            return self.getTypedRuleContext(MT22Parser.LeftHandSideContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignmentStatement




    def assignmentStatement(self):

        localctx = MT22Parser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.leftHandSide()
            self.state = 289
            self.match(MT22Parser.ASSIGN)
            self.state = 290
            self.expression()
            self.state = 291
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftHandSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def arrayCell(self):
            return self.getTypedRuleContext(MT22Parser.ArrayCellContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_leftHandSide




    def leftHandSide(self):

        localctx = MT22Parser.LeftHandSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_leftHandSide)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.arrayCell()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifStatement




    def ifStatement(self):

        localctx = MT22Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_ifStatement)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(MT22Parser.IF)
                self.state = 298
                self.match(MT22Parser.LPAREN)
                self.state = 299
                self.expression()
                self.state = 300
                self.match(MT22Parser.RPAREN)
                self.state = 301
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(MT22Parser.IF)
                self.state = 304
                self.match(MT22Parser.LPAREN)
                self.state = 305
                self.expression()
                self.state = 306
                self.match(MT22Parser.RPAREN)
                self.state = 307
                self.statement()
                self.state = 308
                self.match(MT22Parser.ELSE)
                self.state = 309
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forStatement




    def forStatement(self):

        localctx = MT22Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(MT22Parser.FOR)
            self.state = 314
            self.match(MT22Parser.LPAREN)
            self.state = 315
            self.match(MT22Parser.IDENTIFIER)
            self.state = 316
            self.match(MT22Parser.ASSIGN)
            self.state = 317
            self.expression()
            self.state = 318
            self.match(MT22Parser.COMMA)
            self.state = 319
            self.expression()
            self.state = 320
            self.match(MT22Parser.COMMA)
            self.state = 321
            self.expression()
            self.state = 322
            self.match(MT22Parser.RPAREN)
            self.state = 323
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whileStatement




    def whileStatement(self):

        localctx = MT22Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MT22Parser.WHILE)
            self.state = 326
            self.match(MT22Parser.LPAREN)
            self.state = 327
            self.expression()
            self.state = 328
            self.match(MT22Parser.RPAREN)
            self.state = 329
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_doWhileStatement




    def doWhileStatement(self):

        localctx = MT22Parser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MT22Parser.DO)
            self.state = 332
            self.statement()
            self.state = 333
            self.match(MT22Parser.WHILE)
            self.state = 334
            self.match(MT22Parser.LPAREN)
            self.state = 335
            self.expression()
            self.state = 336
            self.match(MT22Parser.RPAREN)
            self.state = 337
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakStatement




    def breakStatement(self):

        localctx = MT22Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(MT22Parser.BREAK)
            self.state = 340
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continueStatement




    def continueStatement(self):

        localctx = MT22Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MT22Parser.CONTINUE)
            self.state = 343
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_returnStatement




    def returnStatement(self):

        localctx = MT22Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(MT22Parser.RETURN)
            self.state = 346
            self.expressions()
            self.state = 347
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specialFunctionCall(self):
            return self.getTypedRuleContext(MT22Parser.SpecialFunctionCallContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def call(self):
            return self.getTypedRuleContext(MT22Parser.CallContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_callStatement




    def callStatement(self):

        localctx = MT22Parser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_callStatement)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.READBOOLEAN, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.specialFunctionCall()
                self.state = 350
                self.match(MT22Parser.SEMI)
                pass
            elif token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.call()
                self.state = 353
                self.match(MT22Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call




    def call(self):

        localctx = MT22Parser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(MT22Parser.IDENTIFIER)
            self.state = 358
            self.match(MT22Parser.LPAREN)
            self.state = 359
            self.expressions()
            self.state = 360
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expressions




    def expressions(self):

        localctx = MT22Parser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expressions)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LPAREN, MT22Parser.LBRACE, MT22Parser.SUB, MT22Parser.CLAIM, MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.READBOOLEAN, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.BOOLEANLIT, MT22Parser.IDENTIFIER, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.expressionList()
                pass
            elif token in [MT22Parser.RPAREN, MT22Parser.RBRACE, MT22Parser.RBRACKET, MT22Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expressionList




    def expressionList(self):

        localctx = MT22Parser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expressionList)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.expression()
                self.state = 367
                self.match(MT22Parser.COMMA)
                self.state = 368
                self.expressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expression1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expression1Context,i)


        def CONCAT(self):
            return self.getToken(MT22Parser.CONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expression)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.expression1()
                self.state = 374
                self.match(MT22Parser.CONCAT)
                self.state = 375
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expression2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expression2Context,i)


        def COMPARE(self):
            return self.getToken(MT22Parser.COMPARE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression1




    def expression1(self):

        localctx = MT22Parser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expression1)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.expression2(0)
                self.state = 381
                self.match(MT22Parser.COMPARE)
                self.state = 382
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MT22Parser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MT22Parser.Expression2Context,0)


        def ANDOR(self):
            return self.getToken(MT22Parser.ANDOR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 390
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 391
                    self.match(MT22Parser.ANDOR)
                    self.state = 392
                    self.expression3(0) 
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MT22Parser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MT22Parser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 401
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 402
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 403
                    self.expression4(0) 
                self.state = 408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MT22Parser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MT22Parser.Expression4Context,0)


        def MULDIVMOD(self):
            return self.getToken(MT22Parser.MULDIVMOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expression4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 412
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 413
                    self.match(MT22Parser.MULDIVMOD)
                    self.state = 414
                    self.expression5() 
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLAIM(self):
            return self.getToken(MT22Parser.CLAIM, 0)

        def expression5(self):
            return self.getTypedRuleContext(MT22Parser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MT22Parser.Expression6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression5




    def expression5(self):

        localctx = MT22Parser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expression5)
        try:
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CLAIM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(MT22Parser.CLAIM)
                self.state = 421
                self.expression5()
                pass
            elif token in [MT22Parser.LPAREN, MT22Parser.LBRACE, MT22Parser.SUB, MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.READBOOLEAN, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.BOOLEANLIT, MT22Parser.IDENTIFIER, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.expression6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MT22Parser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(MT22Parser.Expression7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression6




    def expression6(self):

        localctx = MT22Parser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expression6)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.match(MT22Parser.SUB)
                self.state = 426
                self.expression6()
                pass
            elif token in [MT22Parser.LPAREN, MT22Parser.LBRACE, MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.READBOOLEAN, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT, MT22Parser.BOOLEANLIT, MT22Parser.IDENTIFIER, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(MT22Parser.LBRACKET, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionListContext,0)


        def RBRACKET(self):
            return self.getToken(MT22Parser.RBRACKET, 0)

        def expression8(self):
            return self.getTypedRuleContext(MT22Parser.Expression8Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression7




    def expression7(self):

        localctx = MT22Parser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expression7)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(MT22Parser.IDENTIFIER)
                self.state = 431
                self.match(MT22Parser.LBRACKET)
                self.state = 432
                self.expressionList()
                self.state = 433
                self.match(MT22Parser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.expression8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(MT22Parser.BOOLEANLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def subExpression(self):
            return self.getTypedRuleContext(MT22Parser.SubExpressionContext,0)


        def callExpression(self):
            return self.getTypedRuleContext(MT22Parser.CallExpressionContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MT22Parser.ArrayLitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression8




    def expression8(self):

        localctx = MT22Parser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expression8)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 441
                self.match(MT22Parser.BOOLEANLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 442
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 443
                self.subExpression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 444
                self.callExpression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 445
                self.arrayLit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MT22Parser.LBRACE, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RBRACE(self):
            return self.getToken(MT22Parser.RBRACE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayLit




    def arrayLit(self):

        localctx = MT22Parser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(MT22Parser.LBRACE)
            self.state = 449
            self.expressions()
            self.state = 450
            self.match(MT22Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subExpression




    def subExpression(self):

        localctx = MT22Parser.SubExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_subExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(MT22Parser.LPAREN)
            self.state = 453
            self.expression()
            self.state = 454
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specialFunctionCall(self):
            return self.getTypedRuleContext(MT22Parser.SpecialFunctionCallContext,0)


        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callExpression




    def callExpression(self):

        localctx = MT22Parser.CallExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_callExpression)
        try:
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER, MT22Parser.PRINTINTEGER, MT22Parser.READFLOAT, MT22Parser.WRITEFLOAT, MT22Parser.READBOOLEAN, MT22Parser.PRINTBOOLEAN, MT22Parser.READSTRING, MT22Parser.PRINTSTRING, MT22Parser.SUPER, MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.specialFunctionCall()
                pass
            elif token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(MT22Parser.IDENTIFIER)
                self.state = 458
                self.match(MT22Parser.LPAREN)
                self.state = 459
                self.expressions()
                self.state = 460
                self.match(MT22Parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialFunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readIntegerCall(self):
            return self.getTypedRuleContext(MT22Parser.ReadIntegerCallContext,0)


        def printIntegerCall(self):
            return self.getTypedRuleContext(MT22Parser.PrintIntegerCallContext,0)


        def readFloatCall(self):
            return self.getTypedRuleContext(MT22Parser.ReadFloatCallContext,0)


        def writeFloatCall(self):
            return self.getTypedRuleContext(MT22Parser.WriteFloatCallContext,0)


        def readBooleanCall(self):
            return self.getTypedRuleContext(MT22Parser.ReadBooleanCallContext,0)


        def printBooleanCall(self):
            return self.getTypedRuleContext(MT22Parser.PrintBooleanCallContext,0)


        def readStringCall(self):
            return self.getTypedRuleContext(MT22Parser.ReadStringCallContext,0)


        def printStringCall(self):
            return self.getTypedRuleContext(MT22Parser.PrintStringCallContext,0)


        def superCall(self):
            return self.getTypedRuleContext(MT22Parser.SuperCallContext,0)


        def preventDefaultCall(self):
            return self.getTypedRuleContext(MT22Parser.PreventDefaultCallContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_specialFunctionCall




    def specialFunctionCall(self):

        localctx = MT22Parser.SpecialFunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_specialFunctionCall)
        try:
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.READINTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.readIntegerCall()
                pass
            elif token in [MT22Parser.PRINTINTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.printIntegerCall()
                pass
            elif token in [MT22Parser.READFLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 466
                self.readFloatCall()
                pass
            elif token in [MT22Parser.WRITEFLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 467
                self.writeFloatCall()
                pass
            elif token in [MT22Parser.READBOOLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 468
                self.readBooleanCall()
                pass
            elif token in [MT22Parser.PRINTBOOLEAN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 469
                self.printBooleanCall()
                pass
            elif token in [MT22Parser.READSTRING]:
                self.enterOuterAlt(localctx, 7)
                self.state = 470
                self.readStringCall()
                pass
            elif token in [MT22Parser.PRINTSTRING]:
                self.enterOuterAlt(localctx, 8)
                self.state = 471
                self.printStringCall()
                pass
            elif token in [MT22Parser.SUPER]:
                self.enterOuterAlt(localctx, 9)
                self.state = 472
                self.superCall()
                pass
            elif token in [MT22Parser.PREVENTDEFAULT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 473
                self.preventDefaultCall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadIntegerCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READINTEGER(self):
            return self.getToken(MT22Parser.READINTEGER, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readIntegerCall




    def readIntegerCall(self):

        localctx = MT22Parser.ReadIntegerCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_readIntegerCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(MT22Parser.READINTEGER)
            self.state = 477
            self.match(MT22Parser.LPAREN)
            self.state = 478
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintIntegerCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTINTEGER(self):
            return self.getToken(MT22Parser.PRINTINTEGER, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printIntegerCall




    def printIntegerCall(self):

        localctx = MT22Parser.PrintIntegerCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_printIntegerCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(MT22Parser.PRINTINTEGER)
            self.state = 481
            self.match(MT22Parser.LPAREN)
            self.state = 482
            self.expression()
            self.state = 483
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadFloatCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READFLOAT(self):
            return self.getToken(MT22Parser.READFLOAT, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readFloatCall




    def readFloatCall(self):

        localctx = MT22Parser.ReadFloatCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_readFloatCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(MT22Parser.READFLOAT)
            self.state = 486
            self.match(MT22Parser.LPAREN)
            self.state = 487
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteFloatCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITEFLOAT(self):
            return self.getToken(MT22Parser.WRITEFLOAT, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_writeFloatCall




    def writeFloatCall(self):

        localctx = MT22Parser.WriteFloatCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_writeFloatCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(MT22Parser.WRITEFLOAT)
            self.state = 490
            self.match(MT22Parser.LPAREN)
            self.state = 491
            self.expression()
            self.state = 492
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadBooleanCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READBOOLEAN(self):
            return self.getToken(MT22Parser.READBOOLEAN, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readBooleanCall




    def readBooleanCall(self):

        localctx = MT22Parser.ReadBooleanCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_readBooleanCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(MT22Parser.READBOOLEAN)
            self.state = 495
            self.match(MT22Parser.LPAREN)
            self.state = 496
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintBooleanCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTBOOLEAN(self):
            return self.getToken(MT22Parser.PRINTBOOLEAN, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printBooleanCall




    def printBooleanCall(self):

        localctx = MT22Parser.PrintBooleanCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_printBooleanCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MT22Parser.PRINTBOOLEAN)
            self.state = 499
            self.match(MT22Parser.LPAREN)
            self.state = 500
            self.expression()
            self.state = 501
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStringCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READSTRING(self):
            return self.getToken(MT22Parser.READSTRING, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_readStringCall




    def readStringCall(self):

        localctx = MT22Parser.ReadStringCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_readStringCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(MT22Parser.READSTRING)
            self.state = 504
            self.match(MT22Parser.LPAREN)
            self.state = 505
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStringCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTSTRING(self):
            return self.getToken(MT22Parser.PRINTSTRING, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_printStringCall




    def printStringCall(self):

        localctx = MT22Parser.PrintStringCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_printStringCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(MT22Parser.PRINTSTRING)
            self.state = 508
            self.match(MT22Parser.LPAREN)
            self.state = 509
            self.expression()
            self.state = 510
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUPER(self):
            return self.getToken(MT22Parser.SUPER, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def expressions(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionsContext,0)


        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_superCall




    def superCall(self):

        localctx = MT22Parser.SuperCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_superCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(MT22Parser.SUPER)
            self.state = 513
            self.match(MT22Parser.LPAREN)
            self.state = 514
            self.expressions()
            self.state = 515
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreventDefaultCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREVENTDEFAULT(self):
            return self.getToken(MT22Parser.PREVENTDEFAULT, 0)

        def LPAREN(self):
            return self.getToken(MT22Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MT22Parser.RPAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_preventDefaultCall




    def preventDefaultCall(self):

        localctx = MT22Parser.PreventDefaultCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_preventDefaultCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(MT22Parser.PREVENTDEFAULT)
            self.state = 518
            self.match(MT22Parser.LPAREN)
            self.state = 519
            self.match(MT22Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[42] = self.expression2_sempred
        self._predicates[43] = self.expression3_sempred
        self._predicates[44] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




