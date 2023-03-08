# Generated from /Users/ngogiaphong/Dev/PPL/assignment2-initial/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u027e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u00a4\n\2\3")
        buf.write("\3\3\3\5\3\u00a8\n\3\3\4\3\4\3\4\5\4\u00ad\n\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\38\38\38\38\38\38\38\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\7?\u01de\n?\f?\16")
        buf.write("?\u01e1\13?\3?\3?\3?\3?\3?\3@\3@\3@\3@\7@\u01ec\n@\f@")
        buf.write("\16@\u01ef\13@\3@\3@\3A\3A\5A\u01f5\nA\3B\3B\7B\u01f9")
        buf.write("\nB\fB\16B\u01fc\13B\3C\3C\3C\7C\u0201\nC\fC\16C\u0204")
        buf.write("\13C\3C\3C\6C\u0208\nC\rC\16C\u0209\7C\u020c\nC\fC\16")
        buf.write("C\u020f\13C\3C\5C\u0212\nC\3D\3D\3D\7D\u0217\nD\fD\16")
        buf.write("D\u021a\13D\3D\3D\6D\u021e\nD\rD\16D\u021f\7D\u0222\n")
        buf.write("D\fD\16D\u0225\13D\5D\u0227\nD\3E\3E\7E\u022b\nE\fE\16")
        buf.write("E\u022e\13E\3F\3F\5F\u0232\nF\3F\6F\u0235\nF\rF\16F\u0236")
        buf.write("\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5")
        buf.write("G\u024a\nG\3H\3H\3I\3I\3I\3J\3J\3J\7J\u0254\nJ\fJ\16J")
        buf.write("\u0257\13J\3J\3J\3J\3K\3K\3K\7K\u025f\nK\fK\16K\u0262")
        buf.write("\13K\3K\5K\u0265\nK\3K\3K\3L\3L\3L\7L\u026c\nL\fL\16L")
        buf.write("\u026f\13L\3L\3L\3L\3L\3M\6M\u0276\nM\rM\16M\u0277\3M")
        buf.write("\3M\3N\3N\3N\3\u01df\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\2\25\2\27\13\31\f\33\r\35\16\37\17!\20#\21%\22")
        buf.write("\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35")
        buf.write("=\36?\37A C!E\"G#I$K%M&O\2Q\2S\2U\'W\2Y\2[\2]\2_\2a\2")
        buf.write("c\2e\2g(i)k*m+o,q-s.u/w\60y\61{\62}\63\177\64\u0081\65")
        buf.write("\u0083\66\u0085\67\u0087\2\u0089\2\u008b\2\u008d8\u008f")
        buf.write("9\u0091\2\u0093:\u0095;\u0097<\u0099=\u009b>\3\2\17\3")
        buf.write("\2))\3\2$$\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2")
        buf.write("\63;\3\2\62;\4\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\5\2\f")
        buf.write("\f$$^^\3\3\f\f\5\2\13\f\17\17\"\"\2\u028d\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2U\3\2\2\2\2g")
        buf.write("\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2")
        buf.write("q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\3\u00a3\3\2\2\2\5\u00a7")
        buf.write("\3\2\2\2\7\u00ac\3\2\2\2\t\u00ae\3\2\2\2\13\u00b3\3\2")
        buf.write("\2\2\r\u00b9\3\2\2\2\17\u00c1\3\2\2\2\21\u00c4\3\2\2\2")
        buf.write("\23\u00c9\3\2\2\2\25\u00ce\3\2\2\2\27\u00d4\3\2\2\2\31")
        buf.write("\u00da\3\2\2\2\33\u00de\3\2\2\2\35\u00e7\3\2\2\2\37\u00ea")
        buf.write("\3\2\2\2!\u00f2\3\2\2\2#\u00f9\3\2\2\2%\u0100\3\2\2\2")
        buf.write("\'\u0106\3\2\2\2)\u010b\3\2\2\2+\u010f\3\2\2\2-\u0118")
        buf.write("\3\2\2\2/\u011b\3\2\2\2\61\u0123\3\2\2\2\63\u0129\3\2")
        buf.write("\2\2\65\u012b\3\2\2\2\67\u012d\3\2\2\29\u012f\3\2\2\2")
        buf.write(";\u0131\3\2\2\2=\u0133\3\2\2\2?\u0135\3\2\2\2A\u0137\3")
        buf.write("\2\2\2C\u0139\3\2\2\2E\u013b\3\2\2\2G\u013d\3\2\2\2I\u013f")
        buf.write("\3\2\2\2K\u0141\3\2\2\2M\u0143\3\2\2\2O\u0145\3\2\2\2")
        buf.write("Q\u0147\3\2\2\2S\u0149\3\2\2\2U\u014b\3\2\2\2W\u014d\3")
        buf.write("\2\2\2Y\u0150\3\2\2\2[\u0153\3\2\2\2]\u0156\3\2\2\2_\u0159")
        buf.write("\3\2\2\2a\u015b\3\2\2\2c\u015e\3\2\2\2e\u0160\3\2\2\2")
        buf.write("g\u0163\3\2\2\2i\u0166\3\2\2\2k\u0172\3\2\2\2m\u017f\3")
        buf.write("\2\2\2o\u0189\3\2\2\2q\u0194\3\2\2\2s\u01a0\3\2\2\2u\u01ad")
        buf.write("\3\2\2\2w\u01b8\3\2\2\2y\u01c4\3\2\2\2{\u01ca\3\2\2\2")
        buf.write("}\u01d9\3\2\2\2\177\u01e7\3\2\2\2\u0081\u01f4\3\2\2\2")
        buf.write("\u0083\u01f6\3\2\2\2\u0085\u0211\3\2\2\2\u0087\u0226\3")
        buf.write("\2\2\2\u0089\u0228\3\2\2\2\u008b\u022f\3\2\2\2\u008d\u0249")
        buf.write("\3\2\2\2\u008f\u024b\3\2\2\2\u0091\u024d\3\2\2\2\u0093")
        buf.write("\u0250\3\2\2\2\u0095\u025b\3\2\2\2\u0097\u0268\3\2\2\2")
        buf.write("\u0099\u0275\3\2\2\2\u009b\u027b\3\2\2\2\u009d\u00a4\5")
        buf.write("[.\2\u009e\u00a4\5]/\2\u009f\u00a4\5_\60\2\u00a0\u00a4")
        buf.write("\5c\62\2\u00a1\u00a4\5a\61\2\u00a2\u00a4\5e\63\2\u00a3")
        buf.write("\u009d\3\2\2\2\u00a3\u009e\3\2\2\2\u00a3\u009f\3\2\2\2")
        buf.write("\u00a3\u00a0\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3")
        buf.write("\2\2\2\u00a4\4\3\2\2\2\u00a5\u00a8\5W,\2\u00a6\u00a8\5")
        buf.write("Y-\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\6\3")
        buf.write("\2\2\2\u00a9\u00ad\5O(\2\u00aa\u00ad\5Q)\2\u00ab\u00ad")
        buf.write("\5S*\2\u00ac\u00a9\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ad\b\3\2\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7w\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7q\2\2\u00b2\n")
        buf.write("\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7m\2\2\u00b8\f")
        buf.write("\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7p\2\2\u00c0\16\3\2\2\2\u00c1\u00c2")
        buf.write("\7f\2\2\u00c2\u00c3\7q\2\2\u00c3\20\3\2\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\22\3\2\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7g\2\2\u00cd\24")
        buf.write("\3\2\2\2\u00ce\u00cf\7h\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7g\2\2\u00d3\26")
        buf.write("\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7v\2\2\u00d9\30")
        buf.write("\3\2\2\2\u00da\u00db\7h\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd")
        buf.write("\7t\2\2\u00dd\32\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0")
        buf.write("\7w\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\34\3\2\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7h\2\2\u00e9\36\3\2\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7i\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7t\2\2\u00f1 \3")
        buf.write("\2\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\"\3\2\2\2\u00f9\u00fa\7u\2\2\u00fa\u00fb")
        buf.write("\7v\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe\u00ff\7i\2\2\u00ff$\3\2\2\2\u0100\u0101")
        buf.write("\7y\2\2\u0101\u0102\7j\2\2\u0102\u0103\7k\2\2\u0103\u0104")
        buf.write("\7n\2\2\u0104\u0105\7g\2\2\u0105&\3\2\2\2\u0106\u0107")
        buf.write("\7x\2\2\u0107\u0108\7q\2\2\u0108\u0109\7k\2\2\u0109\u010a")
        buf.write("\7f\2\2\u010a(\3\2\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7w\2\2\u010d\u010e\7v\2\2\u010e*\3\2\2\2\u010f\u0110")
        buf.write("\7e\2\2\u0110\u0111\7q\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\u0114\7k\2\2\u0114\u0115\7p\2\2\u0115\u0116")
        buf.write("\7w\2\2\u0116\u0117\7g\2\2\u0117,\3\2\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\u011a\7h\2\2\u011a.\3\2\2\2\u011b\u011c")
        buf.write("\7k\2\2\u011c\u011d\7p\2\2\u011d\u011e\7j\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f\u0120\7t\2\2\u0120\u0121\7k\2\2\u0121\u0122")
        buf.write("\7v\2\2\u0122\60\3\2\2\2\u0123\u0124\7c\2\2\u0124\u0125")
        buf.write("\7t\2\2\u0125\u0126\7t\2\2\u0126\u0127\7c\2\2\u0127\u0128")
        buf.write("\7{\2\2\u0128\62\3\2\2\2\u0129\u012a\7*\2\2\u012a\64\3")
        buf.write("\2\2\2\u012b\u012c\7+\2\2\u012c\66\3\2\2\2\u012d\u012e")
        buf.write("\7}\2\2\u012e8\3\2\2\2\u012f\u0130\7\177\2\2\u0130:\3")
        buf.write("\2\2\2\u0131\u0132\7]\2\2\u0132<\3\2\2\2\u0133\u0134\7")
        buf.write("_\2\2\u0134>\3\2\2\2\u0135\u0136\7=\2\2\u0136@\3\2\2\2")
        buf.write("\u0137\u0138\7.\2\2\u0138B\3\2\2\2\u0139\u013a\t\2\2\2")
        buf.write("\u013aD\3\2\2\2\u013b\u013c\t\3\2\2\u013cF\3\2\2\2\u013d")
        buf.write("\u013e\7<\2\2\u013eH\3\2\2\2\u013f\u0140\7?\2\2\u0140")
        buf.write("J\3\2\2\2\u0141\u0142\7-\2\2\u0142L\3\2\2\2\u0143\u0144")
        buf.write("\7/\2\2\u0144N\3\2\2\2\u0145\u0146\7,\2\2\u0146P\3\2\2")
        buf.write("\2\u0147\u0148\7\61\2\2\u0148R\3\2\2\2\u0149\u014a\7\'")
        buf.write("\2\2\u014aT\3\2\2\2\u014b\u014c\7#\2\2\u014cV\3\2\2\2")
        buf.write("\u014d\u014e\7(\2\2\u014e\u014f\7(\2\2\u014fX\3\2\2\2")
        buf.write("\u0150\u0151\7~\2\2\u0151\u0152\7~\2\2\u0152Z\3\2\2\2")
        buf.write("\u0153\u0154\7?\2\2\u0154\u0155\7?\2\2\u0155\\\3\2\2\2")
        buf.write("\u0156\u0157\7#\2\2\u0157\u0158\7?\2\2\u0158^\3\2\2\2")
        buf.write("\u0159\u015a\7>\2\2\u015a`\3\2\2\2\u015b\u015c\7>\2\2")
        buf.write("\u015c\u015d\7?\2\2\u015db\3\2\2\2\u015e\u015f\7@\2\2")
        buf.write("\u015fd\3\2\2\2\u0160\u0161\7@\2\2\u0161\u0162\7?\2\2")
        buf.write("\u0162f\3\2\2\2\u0163\u0164\7<\2\2\u0164\u0165\7<\2\2")
        buf.write("\u0165h\3\2\2\2\u0166\u0167\7t\2\2\u0167\u0168\7g\2\2")
        buf.write("\u0168\u0169\7c\2\2\u0169\u016a\7f\2\2\u016a\u016b\7K")
        buf.write("\2\2\u016b\u016c\7p\2\2\u016c\u016d\7v\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e\u016f\7i\2\2\u016f\u0170\7g\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171j\3\2\2\2\u0172\u0173\7r\2\2\u0173\u0174")
        buf.write("\7t\2\2\u0174\u0175\7k\2\2\u0175\u0176\7p\2\2\u0176\u0177")
        buf.write("\7v\2\2\u0177\u0178\7K\2\2\u0178\u0179\7p\2\2\u0179\u017a")
        buf.write("\7v\2\2\u017a\u017b\7g\2\2\u017b\u017c\7i\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d\u017e\7t\2\2\u017el\3\2\2\2\u017f\u0180")
        buf.write("\7t\2\2\u0180\u0181\7g\2\2\u0181\u0182\7c\2\2\u0182\u0183")
        buf.write("\7f\2\2\u0183\u0184\7H\2\2\u0184\u0185\7n\2\2\u0185\u0186")
        buf.write("\7q\2\2\u0186\u0187\7c\2\2\u0187\u0188\7v\2\2\u0188n\3")
        buf.write("\2\2\2\u0189\u018a\7y\2\2\u018a\u018b\7t\2\2\u018b\u018c")
        buf.write("\7k\2\2\u018c\u018d\7v\2\2\u018d\u018e\7g\2\2\u018e\u018f")
        buf.write("\7H\2\2\u018f\u0190\7n\2\2\u0190\u0191\7q\2\2\u0191\u0192")
        buf.write("\7c\2\2\u0192\u0193\7v\2\2\u0193p\3\2\2\2\u0194\u0195")
        buf.write("\7t\2\2\u0195\u0196\7g\2\2\u0196\u0197\7c\2\2\u0197\u0198")
        buf.write("\7f\2\2\u0198\u0199\7D\2\2\u0199\u019a\7q\2\2\u019a\u019b")
        buf.write("\7q\2\2\u019b\u019c\7n\2\2\u019c\u019d\7g\2\2\u019d\u019e")
        buf.write("\7c\2\2\u019e\u019f\7p\2\2\u019fr\3\2\2\2\u01a0\u01a1")
        buf.write("\7r\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3\7k\2\2\u01a3\u01a4")
        buf.write("\7p\2\2\u01a4\u01a5\7v\2\2\u01a5\u01a6\7D\2\2\u01a6\u01a7")
        buf.write("\7q\2\2\u01a7\u01a8\7q\2\2\u01a8\u01a9\7n\2\2\u01a9\u01aa")
        buf.write("\7g\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac\7p\2\2\u01act\3")
        buf.write("\2\2\2\u01ad\u01ae\7t\2\2\u01ae\u01af\7g\2\2\u01af\u01b0")
        buf.write("\7c\2\2\u01b0\u01b1\7f\2\2\u01b1\u01b2\7U\2\2\u01b2\u01b3")
        buf.write("\7v\2\2\u01b3\u01b4\7t\2\2\u01b4\u01b5\7k\2\2\u01b5\u01b6")
        buf.write("\7p\2\2\u01b6\u01b7\7i\2\2\u01b7v\3\2\2\2\u01b8\u01b9")
        buf.write("\7r\2\2\u01b9\u01ba\7t\2\2\u01ba\u01bb\7k\2\2\u01bb\u01bc")
        buf.write("\7p\2\2\u01bc\u01bd\7v\2\2\u01bd\u01be\7U\2\2\u01be\u01bf")
        buf.write("\7v\2\2\u01bf\u01c0\7t\2\2\u01c0\u01c1\7k\2\2\u01c1\u01c2")
        buf.write("\7p\2\2\u01c2\u01c3\7i\2\2\u01c3x\3\2\2\2\u01c4\u01c5")
        buf.write("\7u\2\2\u01c5\u01c6\7w\2\2\u01c6\u01c7\7r\2\2\u01c7\u01c8")
        buf.write("\7g\2\2\u01c8\u01c9\7t\2\2\u01c9z\3\2\2\2\u01ca\u01cb")
        buf.write("\7r\2\2\u01cb\u01cc\7t\2\2\u01cc\u01cd\7g\2\2\u01cd\u01ce")
        buf.write("\7x\2\2\u01ce\u01cf\7g\2\2\u01cf\u01d0\7p\2\2\u01d0\u01d1")
        buf.write("\7v\2\2\u01d1\u01d2\7F\2\2\u01d2\u01d3\7g\2\2\u01d3\u01d4")
        buf.write("\7h\2\2\u01d4\u01d5\7c\2\2\u01d5\u01d6\7w\2\2\u01d6\u01d7")
        buf.write("\7n\2\2\u01d7\u01d8\7v\2\2\u01d8|\3\2\2\2\u01d9\u01da")
        buf.write("\7\61\2\2\u01da\u01db\7,\2\2\u01db\u01df\3\2\2\2\u01dc")
        buf.write("\u01de\13\2\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2")
        buf.write("\2\u01df\u01e0\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e2")
        buf.write("\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3\7,\2\2\u01e3")
        buf.write("\u01e4\7\61\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\b?\2\2")
        buf.write("\u01e6~\3\2\2\2\u01e7\u01e8\7\61\2\2\u01e8\u01e9\7\61")
        buf.write("\2\2\u01e9\u01ed\3\2\2\2\u01ea\u01ec\n\4\2\2\u01eb\u01ea")
        buf.write("\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2")
        buf.write("\u01f0\u01f1\b@\2\2\u01f1\u0080\3\2\2\2\u01f2\u01f5\5")
        buf.write("\23\n\2\u01f3\u01f5\5\25\13\2\u01f4\u01f2\3\2\2\2\u01f4")
        buf.write("\u01f3\3\2\2\2\u01f5\u0082\3\2\2\2\u01f6\u01fa\t\5\2\2")
        buf.write("\u01f7\u01f9\t\6\2\2\u01f8\u01f7\3\2\2\2\u01f9\u01fc\3")
        buf.write("\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u0084")
        buf.write("\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u0212\7\62\2\2\u01fe")
        buf.write("\u0202\t\7\2\2\u01ff\u0201\t\b\2\2\u0200\u01ff\3\2\2\2")
        buf.write("\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3")
        buf.write("\2\2\2\u0203\u020d\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0207")
        buf.write("\7a\2\2\u0206\u0208\t\b\2\2\u0207\u0206\3\2\2\2\u0208")
        buf.write("\u0209\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2")
        buf.write("\u020a\u020c\3\2\2\2\u020b\u0205\3\2\2\2\u020c\u020f\3")
        buf.write("\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u0210")
        buf.write("\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0212\bC\3\2\u0211")
        buf.write("\u01fd\3\2\2\2\u0211\u01fe\3\2\2\2\u0212\u0086\3\2\2\2")
        buf.write("\u0213\u0227\7\62\2\2\u0214\u0218\t\7\2\2\u0215\u0217")
        buf.write("\t\b\2\2\u0216\u0215\3\2\2\2\u0217\u021a\3\2\2\2\u0218")
        buf.write("\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u0223\3\2\2\2")
        buf.write("\u021a\u0218\3\2\2\2\u021b\u021d\7a\2\2\u021c\u021e\t")
        buf.write("\b\2\2\u021d\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0222\3\2\2\2\u0221")
        buf.write("\u021b\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2")
        buf.write("\u0223\u0224\3\2\2\2\u0224\u0227\3\2\2\2\u0225\u0223\3")
        buf.write("\2\2\2\u0226\u0213\3\2\2\2\u0226\u0214\3\2\2\2\u0227\u0088")
        buf.write("\3\2\2\2\u0228\u022c\5\u008fH\2\u0229\u022b\t\b\2\2\u022a")
        buf.write("\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2")
        buf.write("\u022c\u022d\3\2\2\2\u022d\u008a\3\2\2\2\u022e\u022c\3")
        buf.write("\2\2\2\u022f\u0231\t\t\2\2\u0230\u0232\t\n\2\2\u0231\u0230")
        buf.write("\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0234\3\2\2\2\u0233")
        buf.write("\u0235\t\b\2\2\u0234\u0233\3\2\2\2\u0235\u0236\3\2\2\2")
        buf.write("\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u008c\3")
        buf.write("\2\2\2\u0238\u0239\5\u0087D\2\u0239\u023a\5\u0089E\2\u023a")
        buf.write("\u023b\bG\4\2\u023b\u024a\3\2\2\2\u023c\u023d\5\u0087")
        buf.write("D\2\u023d\u023e\5\u008bF\2\u023e\u023f\bG\5\2\u023f\u024a")
        buf.write("\3\2\2\2\u0240\u0241\5\u0089E\2\u0241\u0242\5\u008bF\2")
        buf.write("\u0242\u0243\bG\6\2\u0243\u024a\3\2\2\2\u0244\u0245\5")
        buf.write("\u0087D\2\u0245\u0246\5\u0089E\2\u0246\u0247\5\u008bF")
        buf.write("\2\u0247\u0248\bG\7\2\u0248\u024a\3\2\2\2\u0249\u0238")
        buf.write("\3\2\2\2\u0249\u023c\3\2\2\2\u0249\u0240\3\2\2\2\u0249")
        buf.write("\u0244\3\2\2\2\u024a\u008e\3\2\2\2\u024b\u024c\7\60\2")
        buf.write("\2\u024c\u0090\3\2\2\2\u024d\u024e\7^\2\2\u024e\u024f")
        buf.write("\t\13\2\2\u024f\u0092\3\2\2\2\u0250\u0255\7$\2\2\u0251")
        buf.write("\u0254\5\u0091I\2\u0252\u0254\n\f\2\2\u0253\u0251\3\2")
        buf.write("\2\2\u0253\u0252\3\2\2\2\u0254\u0257\3\2\2\2\u0255\u0253")
        buf.write("\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0258\3\2\2\2\u0257")
        buf.write("\u0255\3\2\2\2\u0258\u0259\7$\2\2\u0259\u025a\bJ\b\2\u025a")
        buf.write("\u0094\3\2\2\2\u025b\u0260\7$\2\2\u025c\u025f\n\f\2\2")
        buf.write("\u025d\u025f\5\u0091I\2\u025e\u025c\3\2\2\2\u025e\u025d")
        buf.write("\3\2\2\2\u025f\u0262\3\2\2\2\u0260\u025e\3\2\2\2\u0260")
        buf.write("\u0261\3\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2")
        buf.write("\u0263\u0265\t\r\2\2\u0264\u0263\3\2\2\2\u0265\u0266\3")
        buf.write("\2\2\2\u0266\u0267\bK\t\2\u0267\u0096\3\2\2\2\u0268\u026d")
        buf.write("\7$\2\2\u0269\u026c\n\f\2\2\u026a\u026c\5\u0091I\2\u026b")
        buf.write("\u0269\3\2\2\2\u026b\u026a\3\2\2\2\u026c\u026f\3\2\2\2")
        buf.write("\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u0270\3")
        buf.write("\2\2\2\u026f\u026d\3\2\2\2\u0270\u0271\7^\2\2\u0271\u0272")
        buf.write("\n\13\2\2\u0272\u0273\bL\n\2\u0273\u0098\3\2\2\2\u0274")
        buf.write("\u0276\t\16\2\2\u0275\u0274\3\2\2\2\u0276\u0277\3\2\2")
        buf.write("\2\u0277\u0275\3\2\2\2\u0277\u0278\3\2\2\2\u0278\u0279")
        buf.write("\3\2\2\2\u0279\u027a\bM\2\2\u027a\u009a\3\2\2\2\u027b")
        buf.write("\u027c\13\2\2\2\u027c\u027d\bN\13\2\u027d\u009c\3\2\2")
        buf.write("\2\36\2\u00a3\u00a7\u00ac\u01df\u01ed\u01f4\u01fa\u0202")
        buf.write("\u0209\u020d\u0211\u0218\u021f\u0223\u0226\u022c\u0231")
        buf.write("\u0236\u0249\u0253\u0255\u025e\u0260\u0264\u026b\u026d")
        buf.write("\u0277\f\b\2\2\3C\2\3G\3\3G\4\3G\5\3G\6\3J\7\3K\b\3L\t")
        buf.write("\3N\n")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMPARE = 1
    ANDOR = 2
    MULDIVMOD = 3
    AUTO = 4
    BREAK = 5
    BOOLEAN = 6
    DO = 7
    ELSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    WHILE = 16
    VOID = 17
    OUT = 18
    CONTINUE = 19
    OF = 20
    INHERIT = 21
    ARRAY = 22
    LPAREN = 23
    RPAREN = 24
    LBRACE = 25
    RBRACE = 26
    LBRACKET = 27
    RBRACKET = 28
    SEMI = 29
    COMMA = 30
    QUOTE = 31
    DQUOTE = 32
    COLON = 33
    ASSIGN = 34
    ADD = 35
    SUB = 36
    CLAIM = 37
    CONCAT = 38
    READINTEGER = 39
    PRINTINTEGER = 40
    READFLOAT = 41
    WRITEFLOAT = 42
    READBOOLEAN = 43
    PRINTBOOLEAN = 44
    READSTRING = 45
    PRINTSTRING = 46
    SUPER = 47
    PREVENTDEFAULT = 48
    CSTYLE = 49
    LINECOMMENT = 50
    BOOLEANLIT = 51
    IDENTIFIER = 52
    INTLIT = 53
    FLOATLIT = 54
    DOT = 55
    STRINGLIT = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    WS = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "':'", "'='", "'+'", "'-'", "'!'", "'::'", "'readInteger'", 
            "'printInteger'", "'readFloat'", "'writeFloat'", "'readBoolean'", 
            "'printBoolean'", "'readString'", "'printString'", "'super'", 
            "'preventDefault'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "COMPARE", "ANDOR", "MULDIVMOD", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
            "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
            "RBRACKET", "SEMI", "COMMA", "QUOTE", "DQUOTE", "COLON", "ASSIGN", 
            "ADD", "SUB", "CLAIM", "CONCAT", "READINTEGER", "PRINTINTEGER", 
            "READFLOAT", "WRITEFLOAT", "READBOOLEAN", "PRINTBOOLEAN", "READSTRING", 
            "PRINTSTRING", "SUPER", "PREVENTDEFAULT", "CSTYLE", "LINECOMMENT", 
            "BOOLEANLIT", "IDENTIFIER", "INTLIT", "FLOATLIT", "DOT", "STRINGLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    ruleNames = [ "COMPARE", "ANDOR", "MULDIVMOD", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "TRUE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                  "SEMI", "COMMA", "QUOTE", "DQUOTE", "COLON", "ASSIGN", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "CLAIM", "AND", "OR", 
                  "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "CONCAT", "READINTEGER", 
                  "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", "READBOOLEAN", 
                  "PRINTBOOLEAN", "READSTRING", "PRINTSTRING", "SUPER", 
                  "PREVENTDEFAULT", "CSTYLE", "LINECOMMENT", "BOOLEANLIT", 
                  "IDENTIFIER", "INTLIT", "INTPART", "DECIMALPART", "EXPONENTPART", 
                  "FLOATLIT", "DOT", "ESC", "STRINGLIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

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
            actions[65] = self.INTLIT_action 
            actions[69] = self.FLOATLIT_action 
            actions[72] = self.STRINGLIT_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.ERROR_CHAR_action 
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

     

        if actionIndex == 3:

            self.text = self.text.replace("_", "")

     

        if actionIndex == 4:

            self.text = self.text.replace("_", "")

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            temp=str(self.text)
            newLineChar ='\n'
            if temp[-1] in newLineChar:
            	raise UncloseString(temp[1:-1])
            else:
            	raise UncloseString(temp[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            	raise IllegalEscape(str(self.text[1:]))

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise ErrorToken(self.text)
     


