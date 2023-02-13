# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u019a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3")
        buf.write("-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\7\61\u0134\n")
        buf.write("\61\f\61\16\61\u0137\13\61\3\62\3\62\3\62\7\62\u013c\n")
        buf.write("\62\f\62\16\62\u013f\13\62\3\62\3\62\6\62\u0143\n\62\r")
        buf.write("\62\16\62\u0144\7\62\u0147\n\62\f\62\16\62\u014a\13\62")
        buf.write("\3\62\5\62\u014d\n\62\3\63\3\63\3\63\7\63\u0152\n\63\f")
        buf.write("\63\16\63\u0155\13\63\3\63\3\63\6\63\u0159\n\63\r\63\16")
        buf.write("\63\u015a\7\63\u015d\n\63\f\63\16\63\u0160\13\63\5\63")
        buf.write("\u0162\n\63\3\64\3\64\6\64\u0166\n\64\r\64\16\64\u0167")
        buf.write("\3\65\3\65\5\65\u016c\n\65\3\65\6\65\u016f\n\65\r\65\16")
        buf.write("\65\u0170\3\66\3\66\3\66\3\66\3\66\5\66\u0178\n\66\3\66")
        buf.write("\3\66\3\66\5\66\u017d\n\66\3\67\3\67\5\67\u0181\n\67\3")
        buf.write("8\38\38\39\39\39\59\u0189\n9\39\39\3:\6:\u018e\n:\r:\16")
        buf.write(":\u018f\3:\3:\3;\3;\3;\3<\3<\3=\3=\2\2>\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\2g\2i\2k\64m\65o\2q\66s\67u8w9y:\3\2\13")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\n\2$$))^^ddhhppttvv\4\2$$^^\5\2\13\f\17\17\"\"\2")
        buf.write("\u01a6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\3{\3\2\2\2\5\u0080\3\2\2\2\7\u0086\3\2\2")
        buf.write("\2\t\u008e\3\2\2\2\13\u0091\3\2\2\2\r\u0096\3\2\2\2\17")
        buf.write("\u009c\3\2\2\2\21\u00a2\3\2\2\2\23\u00a6\3\2\2\2\25\u00af")
        buf.write("\3\2\2\2\27\u00b2\3\2\2\2\31\u00ba\3\2\2\2\33\u00c1\3")
        buf.write("\2\2\2\35\u00c8\3\2\2\2\37\u00cd\3\2\2\2!\u00d3\3\2\2")
        buf.write("\2#\u00d8\3\2\2\2%\u00dc\3\2\2\2\'\u00e5\3\2\2\2)\u00e8")
        buf.write("\3\2\2\2+\u00f0\3\2\2\2-\u00f6\3\2\2\2/\u00f8\3\2\2\2")
        buf.write("\61\u00fa\3\2\2\2\63\u00fc\3\2\2\2\65\u00fe\3\2\2\2\67")
        buf.write("\u0100\3\2\2\29\u0102\3\2\2\2;\u0104\3\2\2\2=\u0106\3")
        buf.write("\2\2\2?\u0108\3\2\2\2A\u010a\3\2\2\2C\u010c\3\2\2\2E\u010e")
        buf.write("\3\2\2\2G\u0110\3\2\2\2I\u0112\3\2\2\2K\u0114\3\2\2\2")
        buf.write("M\u0116\3\2\2\2O\u0118\3\2\2\2Q\u011b\3\2\2\2S\u011e\3")
        buf.write("\2\2\2U\u0121\3\2\2\2W\u0124\3\2\2\2Y\u0126\3\2\2\2[\u0129")
        buf.write("\3\2\2\2]\u012b\3\2\2\2_\u012e\3\2\2\2a\u0131\3\2\2\2")
        buf.write("c\u014c\3\2\2\2e\u0161\3\2\2\2g\u0163\3\2\2\2i\u0169\3")
        buf.write("\2\2\2k\u017c\3\2\2\2m\u0180\3\2\2\2o\u0182\3\2\2\2q\u0185")
        buf.write("\3\2\2\2s\u018d\3\2\2\2u\u0193\3\2\2\2w\u0196\3\2\2\2")
        buf.write("y\u0198\3\2\2\2{|\7c\2\2|}\7w\2\2}~\7v\2\2~\177\7q\2\2")
        buf.write("\177\4\3\2\2\2\u0080\u0081\7d\2\2\u0081\u0082\7t\2\2\u0082")
        buf.write("\u0083\7g\2\2\u0083\u0084\7c\2\2\u0084\u0085\7m\2\2\u0085")
        buf.write("\6\3\2\2\2\u0086\u0087\7d\2\2\u0087\u0088\7q\2\2\u0088")
        buf.write("\u0089\7q\2\2\u0089\u008a\7n\2\2\u008a\u008b\7g\2\2\u008b")
        buf.write("\u008c\7c\2\2\u008c\u008d\7p\2\2\u008d\b\3\2\2\2\u008e")
        buf.write("\u008f\7f\2\2\u008f\u0090\7q\2\2\u0090\n\3\2\2\2\u0091")
        buf.write("\u0092\7g\2\2\u0092\u0093\7n\2\2\u0093\u0094\7u\2\2\u0094")
        buf.write("\u0095\7g\2\2\u0095\f\3\2\2\2\u0096\u0097\7h\2\2\u0097")
        buf.write("\u0098\7c\2\2\u0098\u0099\7n\2\2\u0099\u009a\7u\2\2\u009a")
        buf.write("\u009b\7g\2\2\u009b\16\3\2\2\2\u009c\u009d\7h\2\2\u009d")
        buf.write("\u009e\7n\2\2\u009e\u009f\7q\2\2\u009f\u00a0\7c\2\2\u00a0")
        buf.write("\u00a1\7v\2\2\u00a1\20\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3")
        buf.write("\u00a4\7q\2\2\u00a4\u00a5\7t\2\2\u00a5\22\3\2\2\2\u00a6")
        buf.write("\u00a7\7h\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7p\2\2\u00a9")
        buf.write("\u00aa\7e\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7k\2\2\u00ac")
        buf.write("\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae\24\3\2\2\2\u00af")
        buf.write("\u00b0\7k\2\2\u00b0\u00b1\7h\2\2\u00b1\26\3\2\2\2\u00b2")
        buf.write("\u00b3\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5")
        buf.write("\u00b6\7g\2\2\u00b6\u00b7\7i\2\2\u00b7\u00b8\7g\2\2\u00b8")
        buf.write("\u00b9\7t\2\2\u00b9\30\3\2\2\2\u00ba\u00bb\7t\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be\7w\2\2\u00be")
        buf.write("\u00bf\7t\2\2\u00bf\u00c0\7p\2\2\u00c0\32\3\2\2\2\u00c1")
        buf.write("\u00c2\7u\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4")
        buf.write("\u00c5\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7i\2\2\u00c7")
        buf.write("\34\3\2\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7t\2\2\u00ca")
        buf.write("\u00cb\7w\2\2\u00cb\u00cc\7g\2\2\u00cc\36\3\2\2\2\u00cd")
        buf.write("\u00ce\7y\2\2\u00ce\u00cf\7j\2\2\u00cf\u00d0\7k\2\2\u00d0")
        buf.write("\u00d1\7n\2\2\u00d1\u00d2\7g\2\2\u00d2 \3\2\2\2\u00d3")
        buf.write("\u00d4\7x\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7k\2\2\u00d6")
        buf.write("\u00d7\7f\2\2\u00d7\"\3\2\2\2\u00d8\u00d9\7q\2\2\u00d9")
        buf.write("\u00da\7w\2\2\u00da\u00db\7v\2\2\u00db$\3\2\2\2\u00dc")
        buf.write("\u00dd\7e\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7p\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7p\2\2\u00e2")
        buf.write("\u00e3\7w\2\2\u00e3\u00e4\7g\2\2\u00e4&\3\2\2\2\u00e5")
        buf.write("\u00e6\7q\2\2\u00e6\u00e7\7h\2\2\u00e7(\3\2\2\2\u00e8")
        buf.write("\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7j\2\2\u00eb")
        buf.write("\u00ec\7g\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7k\2\2\u00ee")
        buf.write("\u00ef\7v\2\2\u00ef*\3\2\2\2\u00f0\u00f1\7c\2\2\u00f1")
        buf.write("\u00f2\7t\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7c\2\2\u00f4")
        buf.write("\u00f5\7{\2\2\u00f5,\3\2\2\2\u00f6\u00f7\7*\2\2\u00f7")
        buf.write(".\3\2\2\2\u00f8\u00f9\7+\2\2\u00f9\60\3\2\2\2\u00fa\u00fb")
        buf.write("\7}\2\2\u00fb\62\3\2\2\2\u00fc\u00fd\7\177\2\2\u00fd\64")
        buf.write("\3\2\2\2\u00fe\u00ff\7]\2\2\u00ff\66\3\2\2\2\u0100\u0101")
        buf.write("\7_\2\2\u01018\3\2\2\2\u0102\u0103\7=\2\2\u0103:\3\2\2")
        buf.write("\2\u0104\u0105\7.\2\2\u0105<\3\2\2\2\u0106\u0107\7\60")
        buf.write("\2\2\u0107>\3\2\2\2\u0108\u0109\7<\2\2\u0109@\3\2\2\2")
        buf.write("\u010a\u010b\7?\2\2\u010bB\3\2\2\2\u010c\u010d\7-\2\2")
        buf.write("\u010dD\3\2\2\2\u010e\u010f\7/\2\2\u010fF\3\2\2\2\u0110")
        buf.write("\u0111\7,\2\2\u0111H\3\2\2\2\u0112\u0113\7\61\2\2\u0113")
        buf.write("J\3\2\2\2\u0114\u0115\7\'\2\2\u0115L\3\2\2\2\u0116\u0117")
        buf.write("\7#\2\2\u0117N\3\2\2\2\u0118\u0119\7(\2\2\u0119\u011a")
        buf.write("\7(\2\2\u011aP\3\2\2\2\u011b\u011c\7~\2\2\u011c\u011d")
        buf.write("\7~\2\2\u011dR\3\2\2\2\u011e\u011f\7?\2\2\u011f\u0120")
        buf.write("\7?\2\2\u0120T\3\2\2\2\u0121\u0122\7#\2\2\u0122\u0123")
        buf.write("\7?\2\2\u0123V\3\2\2\2\u0124\u0125\7>\2\2\u0125X\3\2\2")
        buf.write("\2\u0126\u0127\7>\2\2\u0127\u0128\7?\2\2\u0128Z\3\2\2")
        buf.write("\2\u0129\u012a\7@\2\2\u012a\\\3\2\2\2\u012b\u012c\7@\2")
        buf.write("\2\u012c\u012d\7?\2\2\u012d^\3\2\2\2\u012e\u012f\7<\2")
        buf.write("\2\u012f\u0130\7<\2\2\u0130`\3\2\2\2\u0131\u0135\t\2\2")
        buf.write("\2\u0132\u0134\t\3\2\2\u0133\u0132\3\2\2\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("b\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u014d\7\62\2\2\u0139")
        buf.write("\u013d\t\4\2\2\u013a\u013c\t\5\2\2\u013b\u013a\3\2\2\2")
        buf.write("\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3")
        buf.write("\2\2\2\u013e\u0148\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0142")
        buf.write("\7a\2\2\u0141\u0143\t\5\2\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0147\3\2\2\2\u0146\u0140\3\2\2\2\u0147\u014a\3")
        buf.write("\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b")
        buf.write("\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014d\b\62\2\2\u014c")
        buf.write("\u0138\3\2\2\2\u014c\u0139\3\2\2\2\u014dd\3\2\2\2\u014e")
        buf.write("\u0162\7\62\2\2\u014f\u0153\t\4\2\2\u0150\u0152\t\5\2")
        buf.write("\2\u0151\u0150\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151")
        buf.write("\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u015e\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0156\u0158\7a\2\2\u0157\u0159\t\5\2\2")
        buf.write("\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u0158\3")
        buf.write("\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u0156")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0161\u014e\3\2\2\2\u0161\u014f\3\2\2\2\u0162f\3\2\2")
        buf.write("\2\u0163\u0165\7\60\2\2\u0164\u0166\t\5\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168h\3\2\2\2\u0169\u016b\t\6\2\2\u016a")
        buf.write("\u016c\t\7\2\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016e\3\2\2\2\u016d\u016f\t\5\2\2\u016e\u016d\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171j\3\2\2\2\u0172\u0173\5e\63\2\u0173\u0174")
        buf.write("\5g\64\2\u0174\u017d\3\2\2\2\u0175\u0177\5e\63\2\u0176")
        buf.write("\u0178\5g\64\2\u0177\u0176\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017a\5i\65\2\u017a\u017b\b")
        buf.write("\66\3\2\u017b\u017d\3\2\2\2\u017c\u0172\3\2\2\2\u017c")
        buf.write("\u0175\3\2\2\2\u017dl\3\2\2\2\u017e\u0181\5\35\17\2\u017f")
        buf.write("\u0181\5\r\7\2\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2")
        buf.write("\u0181n\3\2\2\2\u0182\u0183\7^\2\2\u0183\u0184\t\b\2\2")
        buf.write("\u0184p\3\2\2\2\u0185\u0188\7$\2\2\u0186\u0189\n\t\2\2")
        buf.write("\u0187\u0189\5o8\2\u0188\u0186\3\2\2\2\u0188\u0187\3\2")
        buf.write("\2\2\u0189\u018a\3\2\2\2\u018a\u018b\7$\2\2\u018br\3\2")
        buf.write("\2\2\u018c\u018e\t\n\2\2\u018d\u018c\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\b:\4\2\u0192t\3\2\2\2\u0193")
        buf.write("\u0194\13\2\2\2\u0194\u0195\b;\5\2\u0195v\3\2\2\2\u0196")
        buf.write("\u0197\13\2\2\2\u0197x\3\2\2\2\u0198\u0199\13\2\2\2\u0199")
        buf.write("z\3\2\2\2\24\2\u0135\u013d\u0144\u0148\u014c\u0153\u015a")
        buf.write("\u015e\u0161\u0167\u016b\u0170\u0177\u017c\u0180\u0188")
        buf.write("\u018f\6\3\62\2\3\66\3\b\2\2\3;\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    LPAREN = 22
    RPAREN = 23
    LBRACE = 24
    RBRACE = 25
    LBRACKET = 26
    RBRACKET = 27
    SEMI = 28
    COMMA = 29
    DOT = 30
    COLON = 31
    ASSIGN = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    CLAIM = 38
    AND = 39
    OR = 40
    EQ = 41
    NEQ = 42
    LT = 43
    LTE = 44
    GT = 45
    GTE = 46
    DOUBLECOLON = 47
    IDENTIFIER = 48
    INTLIT = 49
    FLOATLIT = 50
    BOOLEANLIT = 51
    STRINGLIT = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "'.'", "':'", "'='", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
            "SEMI", "COMMA", "DOT", "COLON", "ASSIGN", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "CLAIM", "AND", "OR", "EQ", "NEQ", "LT", "LTE", 
            "GT", "GTE", "DOUBLECOLON", "IDENTIFIER", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                  "RBRACKET", "SEMI", "COMMA", "DOT", "COLON", "ASSIGN", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "CLAIM", "AND", "OR", 
                  "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "DOUBLECOLON", 
                  "IDENTIFIER", "INTLIT", "INTPART", "DECIMALPART", "EXPONENTPART", 
                  "FLOATLIT", "BOOLEANLIT", "ESC", "STRINGLIT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.INTLIT_action 
            actions[52] = self.FLOATLIT_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text.replace("_", "")

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text.replace("_", "")

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


