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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u026f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00a2\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4\u00a9\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write("-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\3")
        buf.write("8\38\38\38\38\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\7>\u01d8\n>\f>\16>")
        buf.write("\u01db\13>\3>\3>\3>\3>\3>\3?\3?\3?\3?\7?\u01e6\n?\f?\16")
        buf.write("?\u01e9\13?\3?\3?\3@\3@\5@\u01ef\n@\3A\3A\7A\u01f3\nA")
        buf.write("\fA\16A\u01f6\13A\3B\3B\3B\7B\u01fb\nB\fB\16B\u01fe\13")
        buf.write("B\3B\3B\6B\u0202\nB\rB\16B\u0203\7B\u0206\nB\fB\16B\u0209")
        buf.write("\13B\3B\5B\u020c\nB\3C\3C\3C\7C\u0211\nC\fC\16C\u0214")
        buf.write("\13C\3C\3C\6C\u0218\nC\rC\16C\u0219\7C\u021c\nC\fC\16")
        buf.write("C\u021f\13C\5C\u0221\nC\3D\3D\6D\u0225\nD\rD\16D\u0226")
        buf.write("\3E\3E\5E\u022b\nE\3E\6E\u022e\nE\rE\16E\u022f\3F\3F\3")
        buf.write("F\3F\3F\3F\5F\u0238\nF\3F\3F\3F\5F\u023d\nF\3G\3G\3G\3")
        buf.write("H\3H\3H\7H\u0245\nH\fH\16H\u0248\13H\3H\3H\3H\3I\3I\3")
        buf.write("I\7I\u0250\nI\fI\16I\u0253\13I\3I\5I\u0256\nI\3I\3I\3")
        buf.write("J\3J\3J\7J\u025d\nJ\fJ\16J\u0260\13J\3J\3J\3J\3J\3K\6")
        buf.write("K\u0267\nK\rK\16K\u0268\3K\3K\3L\3L\3L\3\u01d9\2M\3\3")
        buf.write("\5\2\7\2\t\4\13\5\r\6\17\7\21\b\23\2\25\2\27\t\31\n\33")
        buf.write("\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25\61\26\63")
        buf.write("\27\65\30\67\319\32;\33=\34?\35A\36C\2E\37G I!K\"M#O$")
        buf.write("Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67")
        buf.write("w8y9{:};\177<\u0081=\u0083>\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("?\u008d\2\u008f@\u0091A\u0093B\u0095C\u0097D\3\2\r\4\2")
        buf.write("\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\5\2\f\f$$^^\3\3\f\f")
        buf.write("\5\2\13\f\17\17\"\"\2\u0282\2\3\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2E\3\2\2\2")
        buf.write("\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2")
        buf.write("\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2")
        buf.write("\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3")
        buf.write("\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u008b\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009d\3\2\2\2\7\u00a8")
        buf.write("\3\2\2\2\t\u00aa\3\2\2\2\13\u00af\3\2\2\2\r\u00b5\3\2")
        buf.write("\2\2\17\u00bd\3\2\2\2\21\u00c0\3\2\2\2\23\u00c5\3\2\2")
        buf.write("\2\25\u00ca\3\2\2\2\27\u00d0\3\2\2\2\31\u00d6\3\2\2\2")
        buf.write("\33\u00da\3\2\2\2\35\u00e3\3\2\2\2\37\u00e6\3\2\2\2!\u00ee")
        buf.write("\3\2\2\2#\u00f5\3\2\2\2%\u00fc\3\2\2\2\'\u0102\3\2\2\2")
        buf.write(")\u0107\3\2\2\2+\u010b\3\2\2\2-\u0114\3\2\2\2/\u0117\3")
        buf.write("\2\2\2\61\u011f\3\2\2\2\63\u0125\3\2\2\2\65\u0127\3\2")
        buf.write("\2\2\67\u0129\3\2\2\29\u012b\3\2\2\2;\u012d\3\2\2\2=\u012f")
        buf.write("\3\2\2\2?\u0131\3\2\2\2A\u0133\3\2\2\2C\u0135\3\2\2\2")
        buf.write("E\u0137\3\2\2\2G\u0139\3\2\2\2I\u013b\3\2\2\2K\u013d\3")
        buf.write("\2\2\2M\u013f\3\2\2\2O\u0141\3\2\2\2Q\u0143\3\2\2\2S\u0145")
        buf.write("\3\2\2\2U\u0147\3\2\2\2W\u014a\3\2\2\2Y\u014d\3\2\2\2")
        buf.write("[\u0150\3\2\2\2]\u0153\3\2\2\2_\u0155\3\2\2\2a\u0158\3")
        buf.write("\2\2\2c\u015a\3\2\2\2e\u015d\3\2\2\2g\u0160\3\2\2\2i\u016c")
        buf.write("\3\2\2\2k\u0179\3\2\2\2m\u0183\3\2\2\2o\u018e\3\2\2\2")
        buf.write("q\u019a\3\2\2\2s\u01a7\3\2\2\2u\u01b2\3\2\2\2w\u01be\3")
        buf.write("\2\2\2y\u01c4\3\2\2\2{\u01d3\3\2\2\2}\u01e1\3\2\2\2\177")
        buf.write("\u01ee\3\2\2\2\u0081\u01f0\3\2\2\2\u0083\u020b\3\2\2\2")
        buf.write("\u0085\u0220\3\2\2\2\u0087\u0222\3\2\2\2\u0089\u0228\3")
        buf.write("\2\2\2\u008b\u023c\3\2\2\2\u008d\u023e\3\2\2\2\u008f\u0241")
        buf.write("\3\2\2\2\u0091\u024c\3\2\2\2\u0093\u0259\3\2\2\2\u0095")
        buf.write("\u0266\3\2\2\2\u0097\u026c\3\2\2\2\u0099\u009a\5\67\34")
        buf.write("\2\u009a\u009b\5\5\3\2\u009b\u009c\59\35\2\u009c\4\3\2")
        buf.write("\2\2\u009d\u00a1\5\7\4\2\u009e\u009f\5A!\2\u009f\u00a0")
        buf.write("\5\5\3\2\u00a0\u00a2\3\2\2\2\u00a1\u009e\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\6\3\2\2\2\u00a3\u00a9\5\u0083B\2")
        buf.write("\u00a4\u00a9\5\u008bF\2\u00a5\u00a9\5\u008fH\2\u00a6\u00a9")
        buf.write("\5\177@\2\u00a7\u00a9\5\u0081A\2\u00a8\u00a3\3\2\2\2\u00a8")
        buf.write("\u00a4\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a8\u00a7\3\2\2\2\u00a9\b\3\2\2\2\u00aa\u00ab\7c\2")
        buf.write("\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7")
        buf.write("q\2\2\u00ae\n\3\2\2\2\u00af\u00b0\7d\2\2\u00b0\u00b1\7")
        buf.write("t\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7m\2\2\u00b4\f\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7")
        buf.write("\7q\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7p\2\2\u00bc\16")
        buf.write("\3\2\2\2\u00bd\u00be\7f\2\2\u00be\u00bf\7q\2\2\u00bf\20")
        buf.write("\3\2\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3")
        buf.write("\7u\2\2\u00c3\u00c4\7g\2\2\u00c4\22\3\2\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\24\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc")
        buf.write("\7c\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\26\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\30\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\u00d9\7t\2\2\u00d9\32\3\2\2\2\u00da\u00db")
        buf.write("\7h\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7e\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\34\3\2\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7h\2\2\u00e5\36\3\2\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\u00eb\7i\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed \3\2\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7p\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7u\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7i\2\2\u00fb$\3")
        buf.write("\2\2\2\u00fc\u00fd\7y\2\2\u00fd\u00fe\7j\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7g\2\2\u0101&\3")
        buf.write("\2\2\2\u0102\u0103\7x\2\2\u0103\u0104\7q\2\2\u0104\u0105")
        buf.write("\7k\2\2\u0105\u0106\7f\2\2\u0106(\3\2\2\2\u0107\u0108")
        buf.write("\7q\2\2\u0108\u0109\7w\2\2\u0109\u010a\7v\2\2\u010a*\3")
        buf.write("\2\2\2\u010b\u010c\7e\2\2\u010c\u010d\7q\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e\u010f\7v\2\2\u010f\u0110\7k\2\2\u0110\u0111")
        buf.write("\7p\2\2\u0111\u0112\7w\2\2\u0112\u0113\7g\2\2\u0113,\3")
        buf.write("\2\2\2\u0114\u0115\7q\2\2\u0115\u0116\7h\2\2\u0116.\3")
        buf.write("\2\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7j\2\2\u011a\u011b\7g\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7v\2\2\u011e\60\3\2\2\2\u011f\u0120")
        buf.write("\7c\2\2\u0120\u0121\7t\2\2\u0121\u0122\7t\2\2\u0122\u0123")
        buf.write("\7c\2\2\u0123\u0124\7{\2\2\u0124\62\3\2\2\2\u0125\u0126")
        buf.write("\7*\2\2\u0126\64\3\2\2\2\u0127\u0128\7+\2\2\u0128\66\3")
        buf.write("\2\2\2\u0129\u012a\7}\2\2\u012a8\3\2\2\2\u012b\u012c\7")
        buf.write("\177\2\2\u012c:\3\2\2\2\u012d\u012e\7]\2\2\u012e<\3\2")
        buf.write("\2\2\u012f\u0130\7_\2\2\u0130>\3\2\2\2\u0131\u0132\7=")
        buf.write("\2\2\u0132@\3\2\2\2\u0133\u0134\7.\2\2\u0134B\3\2\2\2")
        buf.write("\u0135\u0136\7\60\2\2\u0136D\3\2\2\2\u0137\u0138\7<\2")
        buf.write("\2\u0138F\3\2\2\2\u0139\u013a\7?\2\2\u013aH\3\2\2\2\u013b")
        buf.write("\u013c\7-\2\2\u013cJ\3\2\2\2\u013d\u013e\7/\2\2\u013e")
        buf.write("L\3\2\2\2\u013f\u0140\7,\2\2\u0140N\3\2\2\2\u0141\u0142")
        buf.write("\7\61\2\2\u0142P\3\2\2\2\u0143\u0144\7\'\2\2\u0144R\3")
        buf.write("\2\2\2\u0145\u0146\7#\2\2\u0146T\3\2\2\2\u0147\u0148\7")
        buf.write("(\2\2\u0148\u0149\7(\2\2\u0149V\3\2\2\2\u014a\u014b\7")
        buf.write("~\2\2\u014b\u014c\7~\2\2\u014cX\3\2\2\2\u014d\u014e\7")
        buf.write("?\2\2\u014e\u014f\7?\2\2\u014fZ\3\2\2\2\u0150\u0151\7")
        buf.write("#\2\2\u0151\u0152\7?\2\2\u0152\\\3\2\2\2\u0153\u0154\7")
        buf.write(">\2\2\u0154^\3\2\2\2\u0155\u0156\7>\2\2\u0156\u0157\7")
        buf.write("?\2\2\u0157`\3\2\2\2\u0158\u0159\7@\2\2\u0159b\3\2\2\2")
        buf.write("\u015a\u015b\7@\2\2\u015b\u015c\7?\2\2\u015cd\3\2\2\2")
        buf.write("\u015d\u015e\7<\2\2\u015e\u015f\7<\2\2\u015ff\3\2\2\2")
        buf.write("\u0160\u0161\7t\2\2\u0161\u0162\7g\2\2\u0162\u0163\7c")
        buf.write("\2\2\u0163\u0164\7f\2\2\u0164\u0165\7K\2\2\u0165\u0166")
        buf.write("\7p\2\2\u0166\u0167\7v\2\2\u0167\u0168\7g\2\2\u0168\u0169")
        buf.write("\7i\2\2\u0169\u016a\7g\2\2\u016a\u016b\7t\2\2\u016bh\3")
        buf.write("\2\2\2\u016c\u016d\7r\2\2\u016d\u016e\7t\2\2\u016e\u016f")
        buf.write("\7k\2\2\u016f\u0170\7p\2\2\u0170\u0171\7v\2\2\u0171\u0172")
        buf.write("\7K\2\2\u0172\u0173\7p\2\2\u0173\u0174\7v\2\2\u0174\u0175")
        buf.write("\7g\2\2\u0175\u0176\7i\2\2\u0176\u0177\7g\2\2\u0177\u0178")
        buf.write("\7t\2\2\u0178j\3\2\2\2\u0179\u017a\7t\2\2\u017a\u017b")
        buf.write("\7g\2\2\u017b\u017c\7c\2\2\u017c\u017d\7f\2\2\u017d\u017e")
        buf.write("\7H\2\2\u017e\u017f\7n\2\2\u017f\u0180\7q\2\2\u0180\u0181")
        buf.write("\7c\2\2\u0181\u0182\7v\2\2\u0182l\3\2\2\2\u0183\u0184")
        buf.write("\7y\2\2\u0184\u0185\7t\2\2\u0185\u0186\7k\2\2\u0186\u0187")
        buf.write("\7v\2\2\u0187\u0188\7g\2\2\u0188\u0189\7H\2\2\u0189\u018a")
        buf.write("\7n\2\2\u018a\u018b\7q\2\2\u018b\u018c\7c\2\2\u018c\u018d")
        buf.write("\7v\2\2\u018dn\3\2\2\2\u018e\u018f\7t\2\2\u018f\u0190")
        buf.write("\7g\2\2\u0190\u0191\7c\2\2\u0191\u0192\7f\2\2\u0192\u0193")
        buf.write("\7D\2\2\u0193\u0194\7q\2\2\u0194\u0195\7q\2\2\u0195\u0196")
        buf.write("\7n\2\2\u0196\u0197\7g\2\2\u0197\u0198\7c\2\2\u0198\u0199")
        buf.write("\7p\2\2\u0199p\3\2\2\2\u019a\u019b\7r\2\2\u019b\u019c")
        buf.write("\7t\2\2\u019c\u019d\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f")
        buf.write("\7v\2\2\u019f\u01a0\7D\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a2")
        buf.write("\7q\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4\7g\2\2\u01a4\u01a5")
        buf.write("\7c\2\2\u01a5\u01a6\7p\2\2\u01a6r\3\2\2\2\u01a7\u01a8")
        buf.write("\7t\2\2\u01a8\u01a9\7g\2\2\u01a9\u01aa\7c\2\2\u01aa\u01ab")
        buf.write("\7f\2\2\u01ab\u01ac\7U\2\2\u01ac\u01ad\7v\2\2\u01ad\u01ae")
        buf.write("\7t\2\2\u01ae\u01af\7k\2\2\u01af\u01b0\7p\2\2\u01b0\u01b1")
        buf.write("\7i\2\2\u01b1t\3\2\2\2\u01b2\u01b3\7r\2\2\u01b3\u01b4")
        buf.write("\7t\2\2\u01b4\u01b5\7k\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7")
        buf.write("\7v\2\2\u01b7\u01b8\7U\2\2\u01b8\u01b9\7v\2\2\u01b9\u01ba")
        buf.write("\7t\2\2\u01ba\u01bb\7k\2\2\u01bb\u01bc\7p\2\2\u01bc\u01bd")
        buf.write("\7i\2\2\u01bdv\3\2\2\2\u01be\u01bf\7u\2\2\u01bf\u01c0")
        buf.write("\7w\2\2\u01c0\u01c1\7r\2\2\u01c1\u01c2\7g\2\2\u01c2\u01c3")
        buf.write("\7t\2\2\u01c3x\3\2\2\2\u01c4\u01c5\7r\2\2\u01c5\u01c6")
        buf.write("\7t\2\2\u01c6\u01c7\7g\2\2\u01c7\u01c8\7x\2\2\u01c8\u01c9")
        buf.write("\7g\2\2\u01c9\u01ca\7p\2\2\u01ca\u01cb\7v\2\2\u01cb\u01cc")
        buf.write("\7F\2\2\u01cc\u01cd\7g\2\2\u01cd\u01ce\7h\2\2\u01ce\u01cf")
        buf.write("\7c\2\2\u01cf\u01d0\7w\2\2\u01d0\u01d1\7n\2\2\u01d1\u01d2")
        buf.write("\7v\2\2\u01d2z\3\2\2\2\u01d3\u01d4\7\61\2\2\u01d4\u01d5")
        buf.write("\7,\2\2\u01d5\u01d9\3\2\2\2\u01d6\u01d8\13\2\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01da\3\2\2\2")
        buf.write("\u01d9\u01d7\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3")
        buf.write("\2\2\2\u01dc\u01dd\7,\2\2\u01dd\u01de\7\61\2\2\u01de\u01df")
        buf.write("\3\2\2\2\u01df\u01e0\b>\2\2\u01e0|\3\2\2\2\u01e1\u01e2")
        buf.write("\7\61\2\2\u01e2\u01e3\7\61\2\2\u01e3\u01e7\3\2\2\2\u01e4")
        buf.write("\u01e6\n\2\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e9\3\2\2\2")
        buf.write("\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01ea\3")
        buf.write("\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01eb\b?\2\2\u01eb~\3")
        buf.write("\2\2\2\u01ec\u01ef\5\23\n\2\u01ed\u01ef\5\25\13\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u0080\3\2\2\2")
        buf.write("\u01f0\u01f4\t\3\2\2\u01f1\u01f3\t\4\2\2\u01f2\u01f1\3")
        buf.write("\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u0082\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7")
        buf.write("\u020c\7\62\2\2\u01f8\u01fc\t\5\2\2\u01f9\u01fb\t\6\2")
        buf.write("\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa")
        buf.write("\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u0207\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01ff\u0201\7a\2\2\u0200\u0202\t\6\2\2")
        buf.write("\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0201\3")
        buf.write("\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u01ff")
        buf.write("\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0208\3\2\2\2\u0208\u020a\3\2\2\2\u0209\u0207\3\2\2\2")
        buf.write("\u020a\u020c\bB\3\2\u020b\u01f7\3\2\2\2\u020b\u01f8\3")
        buf.write("\2\2\2\u020c\u0084\3\2\2\2\u020d\u0221\7\62\2\2\u020e")
        buf.write("\u0212\t\5\2\2\u020f\u0211\t\6\2\2\u0210\u020f\3\2\2\2")
        buf.write("\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0213\3")
        buf.write("\2\2\2\u0213\u021d\3\2\2\2\u0214\u0212\3\2\2\2\u0215\u0217")
        buf.write("\7a\2\2\u0216\u0218\t\6\2\2\u0217\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u021a\u021c\3\2\2\2\u021b\u0215\3\2\2\2\u021c\u021f\3")
        buf.write("\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0221")
        buf.write("\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u020d\3\2\2\2\u0220")
        buf.write("\u020e\3\2\2\2\u0221\u0086\3\2\2\2\u0222\u0224\5C\"\2")
        buf.write("\u0223\u0225\t\6\2\2\u0224\u0223\3\2\2\2\u0225\u0226\3")
        buf.write("\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0088")
        buf.write("\3\2\2\2\u0228\u022a\t\7\2\2\u0229\u022b\t\b\2\2\u022a")
        buf.write("\u0229\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022d\3\2\2\2")
        buf.write("\u022c\u022e\t\6\2\2\u022d\u022c\3\2\2\2\u022e\u022f\3")
        buf.write("\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u008a")
        buf.write("\3\2\2\2\u0231\u0232\5\u0085C\2\u0232\u0233\5\u0087D\2")
        buf.write("\u0233\u0234\bF\4\2\u0234\u023d\3\2\2\2\u0235\u0237\5")
        buf.write("\u0085C\2\u0236\u0238\5\u0087D\2\u0237\u0236\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a\5\u0089")
        buf.write("E\2\u023a\u023b\bF\5\2\u023b\u023d\3\2\2\2\u023c\u0231")
        buf.write("\3\2\2\2\u023c\u0235\3\2\2\2\u023d\u008c\3\2\2\2\u023e")
        buf.write("\u023f\7^\2\2\u023f\u0240\t\t\2\2\u0240\u008e\3\2\2\2")
        buf.write("\u0241\u0246\7$\2\2\u0242\u0245\5\u008dG\2\u0243\u0245")
        buf.write("\n\n\2\2\u0244\u0242\3\2\2\2\u0244\u0243\3\2\2\2\u0245")
        buf.write("\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247\3\2\2\2")
        buf.write("\u0247\u0249\3\2\2\2\u0248\u0246\3\2\2\2\u0249\u024a\7")
        buf.write("$\2\2\u024a\u024b\bH\6\2\u024b\u0090\3\2\2\2\u024c\u0251")
        buf.write("\7$\2\2\u024d\u0250\n\n\2\2\u024e\u0250\5\u008dG\2\u024f")
        buf.write("\u024d\3\2\2\2\u024f\u024e\3\2\2\2\u0250\u0253\3\2\2\2")
        buf.write("\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0255\3")
        buf.write("\2\2\2\u0253\u0251\3\2\2\2\u0254\u0256\t\13\2\2\u0255")
        buf.write("\u0254\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\bI\7\2")
        buf.write("\u0258\u0092\3\2\2\2\u0259\u025e\7$\2\2\u025a\u025d\n")
        buf.write("\n\2\2\u025b\u025d\5\u008dG\2\u025c\u025a\3\2\2\2\u025c")
        buf.write("\u025b\3\2\2\2\u025d\u0260\3\2\2\2\u025e\u025c\3\2\2\2")
        buf.write("\u025e\u025f\3\2\2\2\u025f\u0261\3\2\2\2\u0260\u025e\3")
        buf.write("\2\2\2\u0261\u0262\7^\2\2\u0262\u0263\n\t\2\2\u0263\u0264")
        buf.write("\bJ\b\2\u0264\u0094\3\2\2\2\u0265\u0267\t\f\2\2\u0266")
        buf.write("\u0265\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u0266\3\2\2\2")
        buf.write("\u0268\u0269\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026b\b")
        buf.write("K\2\2\u026b\u0096\3\2\2\2\u026c\u026d\13\2\2\2\u026d\u026e")
        buf.write("\bL\t\2\u026e\u0098\3\2\2\2\36\2\u00a1\u00a8\u01d9\u01e7")
        buf.write("\u01ee\u01f4\u01fc\u0203\u0207\u020b\u0212\u0219\u021d")
        buf.write("\u0220\u0226\u022a\u022f\u0237\u023c\u0244\u0246\u024f")
        buf.write("\u0251\u0255\u025c\u025e\u0268\n\b\2\2\3B\2\3F\3\3F\4")
        buf.write("\3H\5\3I\6\3J\7\3L\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAYLIT = 1
    AUTO = 2
    BREAK = 3
    BOOLEAN = 4
    DO = 5
    ELSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    WHILE = 14
    VOID = 15
    OUT = 16
    CONTINUE = 17
    OF = 18
    INHERIT = 19
    ARRAY = 20
    LPAREN = 21
    RPAREN = 22
    LBRACE = 23
    RBRACE = 24
    LBRACKET = 25
    RBRACKET = 26
    SEMI = 27
    COMMA = 28
    COLON = 29
    ASSIGN = 30
    ADD = 31
    SUB = 32
    MUL = 33
    DIV = 34
    MOD = 35
    CLAIM = 36
    AND = 37
    OR = 38
    EQ = 39
    NEQ = 40
    LT = 41
    LTE = 42
    GT = 43
    GTE = 44
    CONCAT = 45
    READINTEGER = 46
    PRINTINTEGER = 47
    READFLOAT = 48
    WRITEFLOAT = 49
    READBOOLEAN = 50
    PRINTBOOLEAN = 51
    READSTRING = 52
    PRINTSTRING = 53
    SUPER = 54
    PREVENTDEFAULT = 55
    CSTYLE = 56
    LINECOMMENT = 57
    BOOLEANLIT = 58
    IDENTIFIER = 59
    INTLIT = 60
    FLOATLIT = 61
    STRINGLIT = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    WS = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "':'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'::'", "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'" ]

    symbolicNames = [ "<INVALID>",
            "ARRAYLIT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
            "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMI", 
            "COMMA", "COLON", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "CLAIM", "AND", "OR", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", 
            "CONCAT", "READINTEGER", "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", 
            "READBOOLEAN", "PRINTBOOLEAN", "READSTRING", "PRINTSTRING", 
            "SUPER", "PREVENTDEFAULT", "CSTYLE", "LINECOMMENT", "BOOLEANLIT", 
            "IDENTIFIER", "INTLIT", "FLOATLIT", "STRINGLIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    ruleNames = [ "ARRAYLIT", "ELEMENTS", "ELEMENT", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "TRUE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                  "SEMI", "COMMA", "DOT", "COLON", "ASSIGN", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "CLAIM", "AND", "OR", "EQ", "NEQ", 
                  "LT", "LTE", "GT", "GTE", "CONCAT", "READINTEGER", "PRINTINTEGER", 
                  "READFLOAT", "WRITEFLOAT", "READBOOLEAN", "PRINTBOOLEAN", 
                  "READSTRING", "PRINTSTRING", "SUPER", "PREVENTDEFAULT", 
                  "CSTYLE", "LINECOMMENT", "BOOLEANLIT", "IDENTIFIER", "INTLIT", 
                  "INTPART", "DECIMALPART", "EXPONENTPART", "FLOATLIT", 
                  "ESC", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "WS", "ERROR_CHAR" ]

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
            actions[64] = self.INTLIT_action 
            actions[68] = self.FLOATLIT_action 
            actions[70] = self.STRINGLIT_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
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

     

        if actionIndex == 2:

            self.text = self.text.replace("_", "")

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            temp=str(self.text)
            newLineChar ='\n'
            if temp[-1] in newLineChar:
            	raise UncloseString(temp[1:-1])
            else:
            	raise UncloseString(temp[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise IllegalEscape(str(self.text[1:]))

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


