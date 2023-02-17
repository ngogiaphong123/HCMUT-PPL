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
        buf.write("\u023d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*")
        buf.write("\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\3")
        buf.write("8\38\38\38\38\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\7;\u01c1\n;\f;\16;")
        buf.write("\u01c4\13;\3;\3;\3;\3<\3<\3<\3<\7<\u01cd\n<\f<\16<\u01d0")
        buf.write("\13<\3=\3=\5=\u01d4\n=\3>\3>\7>\u01d8\n>\f>\16>\u01db")
        buf.write("\13>\3?\3?\7?\u01df\n?\f?\16?\u01e2\13?\3?\3?\6?\u01e6")
        buf.write("\n?\r?\16?\u01e7\7?\u01ea\n?\f?\16?\u01ed\13?\3?\3?\5")
        buf.write("?\u01f1\n?\3@\3@\3@\7@\u01f6\n@\f@\16@\u01f9\13@\3@\3")
        buf.write("@\6@\u01fd\n@\r@\16@\u01fe\7@\u0201\n@\f@\16@\u0204\13")
        buf.write("@\5@\u0206\n@\3A\3A\6A\u020a\nA\rA\16A\u020b\3B\3B\5B")
        buf.write("\u0210\nB\3B\6B\u0213\nB\rB\16B\u0214\3C\3C\3C\3C\3C\5")
        buf.write("C\u021c\nC\3C\3C\3C\5C\u0221\nC\3D\3D\3D\3E\3E\3E\7E\u0229")
        buf.write("\nE\fE\16E\u022c\13E\3E\3E\3F\6F\u0231\nF\rF\16F\u0232")
        buf.write("\3F\3F\3G\3G\3G\3H\3H\3I\3I\3\u01c2\2J\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\2\17\2\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37")
        buf.write("\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32")
        buf.write("\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]")
        buf.write("._/a\60c\61e\62g\63i\64k\65m\66o\67q8s9u:w;y<{=}>\177")
        buf.write("\2\u0081\2\u0083\2\u0085?\u0087\2\u0089@\u008bA\u008d")
        buf.write("B\u008fC\u0091D\3\2\f\4\2\f\f\17\17\4\2aac|\6\2\62;C\\")
        buf.write("aac|\3\2\63;\3\2\62;\4\2GGgg\4\2--//\n\2$$))^^ddhhppt")
        buf.write("tvv\4\2$$^^\5\2\13\f\17\17\"\"\2\u024a\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0085\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0098\3\2\2\2\7\u009e")
        buf.write("\3\2\2\2\t\u00a6\3\2\2\2\13\u00a9\3\2\2\2\r\u00ae\3\2")
        buf.write("\2\2\17\u00b3\3\2\2\2\21\u00b9\3\2\2\2\23\u00bf\3\2\2")
        buf.write("\2\25\u00c3\3\2\2\2\27\u00cc\3\2\2\2\31\u00cf\3\2\2\2")
        buf.write("\33\u00d7\3\2\2\2\35\u00de\3\2\2\2\37\u00e5\3\2\2\2!\u00eb")
        buf.write("\3\2\2\2#\u00f0\3\2\2\2%\u00f4\3\2\2\2\'\u00fd\3\2\2\2")
        buf.write(")\u0100\3\2\2\2+\u0108\3\2\2\2-\u010e\3\2\2\2/\u0110\3")
        buf.write("\2\2\2\61\u0112\3\2\2\2\63\u0114\3\2\2\2\65\u0116\3\2")
        buf.write("\2\2\67\u0118\3\2\2\29\u011a\3\2\2\2;\u011c\3\2\2\2=\u011e")
        buf.write("\3\2\2\2?\u0120\3\2\2\2A\u0122\3\2\2\2C\u0124\3\2\2\2")
        buf.write("E\u0126\3\2\2\2G\u0128\3\2\2\2I\u012a\3\2\2\2K\u012c\3")
        buf.write("\2\2\2M\u012e\3\2\2\2O\u0130\3\2\2\2Q\u0133\3\2\2\2S\u0136")
        buf.write("\3\2\2\2U\u0139\3\2\2\2W\u013c\3\2\2\2Y\u013e\3\2\2\2")
        buf.write("[\u0141\3\2\2\2]\u0143\3\2\2\2_\u0146\3\2\2\2a\u0149\3")
        buf.write("\2\2\2c\u0155\3\2\2\2e\u0162\3\2\2\2g\u016c\3\2\2\2i\u0177")
        buf.write("\3\2\2\2k\u0183\3\2\2\2m\u0190\3\2\2\2o\u019b\3\2\2\2")
        buf.write("q\u01a7\3\2\2\2s\u01ad\3\2\2\2u\u01bc\3\2\2\2w\u01c8\3")
        buf.write("\2\2\2y\u01d3\3\2\2\2{\u01d5\3\2\2\2}\u01f0\3\2\2\2\177")
        buf.write("\u0205\3\2\2\2\u0081\u0207\3\2\2\2\u0083\u020d\3\2\2\2")
        buf.write("\u0085\u0220\3\2\2\2\u0087\u0222\3\2\2\2\u0089\u0225\3")
        buf.write("\2\2\2\u008b\u0230\3\2\2\2\u008d\u0236\3\2\2\2\u008f\u0239")
        buf.write("\3\2\2\2\u0091\u023b\3\2\2\2\u0093\u0094\7c\2\2\u0094")
        buf.write("\u0095\7w\2\2\u0095\u0096\7v\2\2\u0096\u0097\7q\2\2\u0097")
        buf.write("\4\3\2\2\2\u0098\u0099\7d\2\2\u0099\u009a\7t\2\2\u009a")
        buf.write("\u009b\7g\2\2\u009b\u009c\7c\2\2\u009c\u009d\7m\2\2\u009d")
        buf.write("\6\3\2\2\2\u009e\u009f\7d\2\2\u009f\u00a0\7q\2\2\u00a0")
        buf.write("\u00a1\7q\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3\7g\2\2\u00a3")
        buf.write("\u00a4\7c\2\2\u00a4\u00a5\7p\2\2\u00a5\b\3\2\2\2\u00a6")
        buf.write("\u00a7\7f\2\2\u00a7\u00a8\7q\2\2\u00a8\n\3\2\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac\7u\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad\f\3\2\2\2\u00ae\u00af\7v\2\2\u00af")
        buf.write("\u00b0\7t\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2\7g\2\2\u00b2")
        buf.write("\16\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5\7c\2\2\u00b5")
        buf.write("\u00b6\7n\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7g\2\2\u00b8")
        buf.write("\20\3\2\2\2\u00b9\u00ba\7h\2\2\u00ba\u00bb\7n\2\2\u00bb")
        buf.write("\u00bc\7q\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\22\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1\7q\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\24\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4")
        buf.write("\u00c5\7w\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7e\2\2\u00c7")
        buf.write("\u00c8\7v\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7q\2\2\u00ca")
        buf.write("\u00cb\7p\2\2\u00cb\26\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7h\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\7k\2\2\u00d0")
        buf.write("\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\u00d4\7i\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\32\3\2\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7g\2\2\u00d9")
        buf.write("\u00da\7v\2\2\u00da\u00db\7w\2\2\u00db\u00dc\7t\2\2\u00dc")
        buf.write("\u00dd\7p\2\2\u00dd\34\3\2\2\2\u00de\u00df\7u\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2")
        buf.write("\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4\36\3\2\2\2\u00e5")
        buf.write("\u00e6\7y\2\2\u00e6\u00e7\7j\2\2\u00e7\u00e8\7k\2\2\u00e8")
        buf.write("\u00e9\7n\2\2\u00e9\u00ea\7g\2\2\u00ea \3\2\2\2\u00eb")
        buf.write("\u00ec\7x\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7k\2\2\u00ee")
        buf.write("\u00ef\7f\2\2\u00ef\"\3\2\2\2\u00f0\u00f1\7q\2\2\u00f1")
        buf.write("\u00f2\7w\2\2\u00f2\u00f3\7v\2\2\u00f3$\3\2\2\2\u00f4")
        buf.write("\u00f5\7e\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f8\7v\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa")
        buf.write("\u00fb\7w\2\2\u00fb\u00fc\7g\2\2\u00fc&\3\2\2\2\u00fd")
        buf.write("\u00fe\7q\2\2\u00fe\u00ff\7h\2\2\u00ff(\3\2\2\2\u0100")
        buf.write("\u0101\7k\2\2\u0101\u0102\7p\2\2\u0102\u0103\7j\2\2\u0103")
        buf.write("\u0104\7g\2\2\u0104\u0105\7t\2\2\u0105\u0106\7k\2\2\u0106")
        buf.write("\u0107\7v\2\2\u0107*\3\2\2\2\u0108\u0109\7c\2\2\u0109")
        buf.write("\u010a\7t\2\2\u010a\u010b\7t\2\2\u010b\u010c\7c\2\2\u010c")
        buf.write("\u010d\7{\2\2\u010d,\3\2\2\2\u010e\u010f\7*\2\2\u010f")
        buf.write(".\3\2\2\2\u0110\u0111\7+\2\2\u0111\60\3\2\2\2\u0112\u0113")
        buf.write("\7}\2\2\u0113\62\3\2\2\2\u0114\u0115\7\177\2\2\u0115\64")
        buf.write("\3\2\2\2\u0116\u0117\7]\2\2\u0117\66\3\2\2\2\u0118\u0119")
        buf.write("\7_\2\2\u01198\3\2\2\2\u011a\u011b\7=\2\2\u011b:\3\2\2")
        buf.write("\2\u011c\u011d\7.\2\2\u011d<\3\2\2\2\u011e\u011f\7\60")
        buf.write("\2\2\u011f>\3\2\2\2\u0120\u0121\7<\2\2\u0121@\3\2\2\2")
        buf.write("\u0122\u0123\7?\2\2\u0123B\3\2\2\2\u0124\u0125\7-\2\2")
        buf.write("\u0125D\3\2\2\2\u0126\u0127\7/\2\2\u0127F\3\2\2\2\u0128")
        buf.write("\u0129\7,\2\2\u0129H\3\2\2\2\u012a\u012b\7\61\2\2\u012b")
        buf.write("J\3\2\2\2\u012c\u012d\7\'\2\2\u012dL\3\2\2\2\u012e\u012f")
        buf.write("\7#\2\2\u012fN\3\2\2\2\u0130\u0131\7(\2\2\u0131\u0132")
        buf.write("\7(\2\2\u0132P\3\2\2\2\u0133\u0134\7~\2\2\u0134\u0135")
        buf.write("\7~\2\2\u0135R\3\2\2\2\u0136\u0137\7?\2\2\u0137\u0138")
        buf.write("\7?\2\2\u0138T\3\2\2\2\u0139\u013a\7#\2\2\u013a\u013b")
        buf.write("\7?\2\2\u013bV\3\2\2\2\u013c\u013d\7>\2\2\u013dX\3\2\2")
        buf.write("\2\u013e\u013f\7>\2\2\u013f\u0140\7?\2\2\u0140Z\3\2\2")
        buf.write("\2\u0141\u0142\7@\2\2\u0142\\\3\2\2\2\u0143\u0144\7@\2")
        buf.write("\2\u0144\u0145\7?\2\2\u0145^\3\2\2\2\u0146\u0147\7<\2")
        buf.write("\2\u0147\u0148\7<\2\2\u0148`\3\2\2\2\u0149\u014a\7t\2")
        buf.write("\2\u014a\u014b\7g\2\2\u014b\u014c\7c\2\2\u014c\u014d\7")
        buf.write("f\2\2\u014d\u014e\7K\2\2\u014e\u014f\7p\2\2\u014f\u0150")
        buf.write("\7v\2\2\u0150\u0151\7g\2\2\u0151\u0152\7i\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153\u0154\7t\2\2\u0154b\3\2\2\2\u0155\u0156")
        buf.write("\7r\2\2\u0156\u0157\7t\2\2\u0157\u0158\7k\2\2\u0158\u0159")
        buf.write("\7p\2\2\u0159\u015a\7v\2\2\u015a\u015b\7K\2\2\u015b\u015c")
        buf.write("\7p\2\2\u015c\u015d\7v\2\2\u015d\u015e\7g\2\2\u015e\u015f")
        buf.write("\7i\2\2\u015f\u0160\7g\2\2\u0160\u0161\7t\2\2\u0161d\3")
        buf.write("\2\2\2\u0162\u0163\7t\2\2\u0163\u0164\7g\2\2\u0164\u0165")
        buf.write("\7c\2\2\u0165\u0166\7f\2\2\u0166\u0167\7H\2\2\u0167\u0168")
        buf.write("\7n\2\2\u0168\u0169\7q\2\2\u0169\u016a\7c\2\2\u016a\u016b")
        buf.write("\7v\2\2\u016bf\3\2\2\2\u016c\u016d\7y\2\2\u016d\u016e")
        buf.write("\7t\2\2\u016e\u016f\7k\2\2\u016f\u0170\7v\2\2\u0170\u0171")
        buf.write("\7g\2\2\u0171\u0172\7H\2\2\u0172\u0173\7n\2\2\u0173\u0174")
        buf.write("\7q\2\2\u0174\u0175\7c\2\2\u0175\u0176\7v\2\2\u0176h\3")
        buf.write("\2\2\2\u0177\u0178\7t\2\2\u0178\u0179\7g\2\2\u0179\u017a")
        buf.write("\7c\2\2\u017a\u017b\7f\2\2\u017b\u017c\7D\2\2\u017c\u017d")
        buf.write("\7q\2\2\u017d\u017e\7q\2\2\u017e\u017f\7n\2\2\u017f\u0180")
        buf.write("\7g\2\2\u0180\u0181\7c\2\2\u0181\u0182\7p\2\2\u0182j\3")
        buf.write("\2\2\2\u0183\u0184\7r\2\2\u0184\u0185\7t\2\2\u0185\u0186")
        buf.write("\7k\2\2\u0186\u0187\7p\2\2\u0187\u0188\7v\2\2\u0188\u0189")
        buf.write("\7D\2\2\u0189\u018a\7q\2\2\u018a\u018b\7q\2\2\u018b\u018c")
        buf.write("\7n\2\2\u018c\u018d\7g\2\2\u018d\u018e\7c\2\2\u018e\u018f")
        buf.write("\7p\2\2\u018fl\3\2\2\2\u0190\u0191\7t\2\2\u0191\u0192")
        buf.write("\7g\2\2\u0192\u0193\7c\2\2\u0193\u0194\7f\2\2\u0194\u0195")
        buf.write("\7U\2\2\u0195\u0196\7v\2\2\u0196\u0197\7t\2\2\u0197\u0198")
        buf.write("\7k\2\2\u0198\u0199\7p\2\2\u0199\u019a\7i\2\2\u019an\3")
        buf.write("\2\2\2\u019b\u019c\7r\2\2\u019c\u019d\7t\2\2\u019d\u019e")
        buf.write("\7k\2\2\u019e\u019f\7p\2\2\u019f\u01a0\7v\2\2\u01a0\u01a1")
        buf.write("\7U\2\2\u01a1\u01a2\7v\2\2\u01a2\u01a3\7t\2\2\u01a3\u01a4")
        buf.write("\7k\2\2\u01a4\u01a5\7p\2\2\u01a5\u01a6\7i\2\2\u01a6p\3")
        buf.write("\2\2\2\u01a7\u01a8\7u\2\2\u01a8\u01a9\7w\2\2\u01a9\u01aa")
        buf.write("\7r\2\2\u01aa\u01ab\7g\2\2\u01ab\u01ac\7t\2\2\u01acr\3")
        buf.write("\2\2\2\u01ad\u01ae\7r\2\2\u01ae\u01af\7t\2\2\u01af\u01b0")
        buf.write("\7g\2\2\u01b0\u01b1\7x\2\2\u01b1\u01b2\7g\2\2\u01b2\u01b3")
        buf.write("\7p\2\2\u01b3\u01b4\7v\2\2\u01b4\u01b5\7F\2\2\u01b5\u01b6")
        buf.write("\7g\2\2\u01b6\u01b7\7h\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9")
        buf.write("\7w\2\2\u01b9\u01ba\7n\2\2\u01ba\u01bb\7v\2\2\u01bbt\3")
        buf.write("\2\2\2\u01bc\u01bd\7\61\2\2\u01bd\u01be\7,\2\2\u01be\u01c2")
        buf.write("\3\2\2\2\u01bf\u01c1\13\2\2\2\u01c0\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c4\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c2\u01c0\3\2\2\2")
        buf.write("\u01c3\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\7")
        buf.write(",\2\2\u01c6\u01c7\7\61\2\2\u01c7v\3\2\2\2\u01c8\u01c9")
        buf.write("\7\61\2\2\u01c9\u01ca\7\61\2\2\u01ca\u01ce\3\2\2\2\u01cb")
        buf.write("\u01cd\n\2\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cfx\3\2\2")
        buf.write("\2\u01d0\u01ce\3\2\2\2\u01d1\u01d4\5\r\7\2\u01d2\u01d4")
        buf.write("\5\17\b\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4")
        buf.write("z\3\2\2\2\u01d5\u01d9\t\3\2\2\u01d6\u01d8\t\4\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da|\3\2\2\2\u01db\u01d9\3\2\2")
        buf.write("\2\u01dc\u01e0\t\5\2\2\u01dd\u01df\t\6\2\2\u01de\u01dd")
        buf.write("\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0")
        buf.write("\u01e1\3\2\2\2\u01e1\u01eb\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e3\u01e5\7a\2\2\u01e4\u01e6\t\6\2\2\u01e5\u01e4\3")
        buf.write("\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e3\3\2\2\2\u01ea")
        buf.write("\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2")
        buf.write("\u01ec\u01f1\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01ef\7")
        buf.write("\62\2\2\u01ef\u01f1\b?\2\2\u01f0\u01dc\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f1~\3\2\2\2\u01f2\u0206\7\62\2\2\u01f3\u01f7")
        buf.write("\t\5\2\2\u01f4\u01f6\t\6\2\2\u01f5\u01f4\3\2\2\2\u01f6")
        buf.write("\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u0202\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fc\7")
        buf.write("a\2\2\u01fb\u01fd\t\6\2\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0201\3\2\2\2\u0200\u01fa\3\2\2\2\u0201\u0204\3\2\2\2")
        buf.write("\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0206\3")
        buf.write("\2\2\2\u0204\u0202\3\2\2\2\u0205\u01f2\3\2\2\2\u0205\u01f3")
        buf.write("\3\2\2\2\u0206\u0080\3\2\2\2\u0207\u0209\7\60\2\2\u0208")
        buf.write("\u020a\t\6\2\2\u0209\u0208\3\2\2\2\u020a\u020b\3\2\2\2")
        buf.write("\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u0082\3")
        buf.write("\2\2\2\u020d\u020f\t\7\2\2\u020e\u0210\t\b\2\2\u020f\u020e")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0212\3\2\2\2\u0211")
        buf.write("\u0213\t\6\2\2\u0212\u0211\3\2\2\2\u0213\u0214\3\2\2\2")
        buf.write("\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0084\3")
        buf.write("\2\2\2\u0216\u0217\5\177@\2\u0217\u0218\5\u0081A\2\u0218")
        buf.write("\u0221\3\2\2\2\u0219\u021b\5\177@\2\u021a\u021c\5\u0081")
        buf.write("A\2\u021b\u021a\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021d")
        buf.write("\3\2\2\2\u021d\u021e\5\u0083B\2\u021e\u021f\bC\3\2\u021f")
        buf.write("\u0221\3\2\2\2\u0220\u0216\3\2\2\2\u0220\u0219\3\2\2\2")
        buf.write("\u0221\u0086\3\2\2\2\u0222\u0223\7^\2\2\u0223\u0224\t")
        buf.write("\t\2\2\u0224\u0088\3\2\2\2\u0225\u022a\7$\2\2\u0226\u0229")
        buf.write("\n\n\2\2\u0227\u0229\5\u0087D\2\u0228\u0226\3\2\2\2\u0228")
        buf.write("\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2")
        buf.write("\u022a\u022b\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022d\u022e\7$\2\2\u022e\u008a\3\2\2\2\u022f\u0231")
        buf.write("\t\13\2\2\u0230\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232")
        buf.write("\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234\3\2\2\2")
        buf.write("\u0234\u0235\bF\4\2\u0235\u008c\3\2\2\2\u0236\u0237\13")
        buf.write("\2\2\2\u0237\u0238\bG\5\2\u0238\u008e\3\2\2\2\u0239\u023a")
        buf.write("\13\2\2\2\u023a\u0090\3\2\2\2\u023b\u023c\13\2\2\2\u023c")
        buf.write("\u0092\3\2\2\2\27\2\u01c2\u01ce\u01d3\u01d9\u01e0\u01e7")
        buf.write("\u01eb\u01f0\u01f7\u01fe\u0202\u0205\u020b\u020f\u0214")
        buf.write("\u021b\u0220\u0228\u022a\u0232\6\3?\2\3C\3\b\2\2\3G\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FLOAT = 6
    FOR = 7
    FUNCTION = 8
    IF = 9
    INTEGER = 10
    RETURN = 11
    STRING = 12
    WHILE = 13
    VOID = 14
    OUT = 15
    CONTINUE = 16
    OF = 17
    INHERIT = 18
    ARRAY = 19
    LPAREN = 20
    RPAREN = 21
    LBRACE = 22
    RBRACE = 23
    LBRACKET = 24
    RBRACKET = 25
    SEMI = 26
    COMMA = 27
    DOT = 28
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
    WS = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "'.'", "':'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'::'", "'readInteger'", "'printInteger'", "'readFloat'", 
            "'writeFloat'", "'readBoolean'", "'printBoolean'", "'readString'", 
            "'printString'", "'super'", "'preventDefault'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "LPAREN", "RPAREN", "LBRACE", 
            "RBRACE", "LBRACKET", "RBRACKET", "SEMI", "COMMA", "DOT", "COLON", 
            "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "CLAIM", "AND", 
            "OR", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "CONCAT", "READINTEGER", 
            "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", "READBOOLEAN", "PRINTBOOLEAN", 
            "READSTRING", "PRINTSTRING", "SUPER", "PREVENTDEFAULT", "CSTYLE", 
            "LINECOMMENT", "BOOLEANLIT", "IDENTIFIER", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "TRUE", "FALSE", 
                  "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
                  "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                  "RBRACKET", "SEMI", "COMMA", "DOT", "COLON", "ASSIGN", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "CLAIM", "AND", "OR", 
                  "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "CONCAT", "READINTEGER", 
                  "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", "READBOOLEAN", 
                  "PRINTBOOLEAN", "READSTRING", "PRINTSTRING", "SUPER", 
                  "PREVENTDEFAULT", "CSTYLE", "LINECOMMENT", "BOOLEANLIT", 
                  "IDENTIFIER", "INTLIT", "INTPART", "DECIMALPART", "EXPONENTPART", 
                  "FLOATLIT", "ESC", "STRINGLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[61] = self.INTLIT_action 
            actions[65] = self.FLOATLIT_action 
            actions[69] = self.ERROR_CHAR_action 
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
     


