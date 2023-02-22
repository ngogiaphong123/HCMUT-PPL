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
        buf.write("\u0246\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\13>\3?\3?\3?\7?\u01e0\n?\f?\16?\u01e3\13?\3?\3?\6?\u01e7")
        buf.write("\n?\r?\16?\u01e8\7?\u01eb\n?\f?\16?\u01ee\13?\3?\5?\u01f1")
        buf.write("\n?\3@\3@\3@\7@\u01f6\n@\f@\16@\u01f9\13@\3@\3@\6@\u01fd")
        buf.write("\n@\r@\16@\u01fe\7@\u0201\n@\f@\16@\u0204\13@\5@\u0206")
        buf.write("\n@\3A\3A\6A\u020a\nA\rA\16A\u020b\3B\3B\5B\u0210\nB\3")
        buf.write("B\6B\u0213\nB\rB\16B\u0214\3C\3C\3C\3C\3C\3C\5C\u021d")
        buf.write("\nC\3C\3C\3C\5C\u0222\nC\3D\3D\3D\3E\3E\3E\7E\u022a\n")
        buf.write("E\fE\16E\u022d\13E\3E\3E\3E\3F\3F\7F\u0234\nF\fF\16F\u0237")
        buf.write("\13F\3F\3F\3G\6G\u023c\nG\rG\16G\u023d\3G\3G\3H\3H\3H")
        buf.write("\3I\3I\3\u01c2\2J\3\3\5\4\7\5\t\6\13\7\r\2\17\2\21\b\23")
        buf.write("\t\25\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22\'\23)")
        buf.write("\24+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36?\37")
        buf.write("A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64")
        buf.write("k\65m\66o\67q8s9u:w;y<{=}>\177\2\u0081\2\u0083\2\u0085")
        buf.write("?\u0087\2\u0089@\u008bA\u008dB\u008fC\u0091D\3\2\f\4\2")
        buf.write("\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\4\2$$^^\5\2\13\f\17")
        buf.write("\17\"\"\2\u0254\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\u0085\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3")
        buf.write("\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2")
        buf.write("\3\u0093\3\2\2\2\5\u0098\3\2\2\2\7\u009e\3\2\2\2\t\u00a6")
        buf.write("\3\2\2\2\13\u00a9\3\2\2\2\r\u00ae\3\2\2\2\17\u00b3\3\2")
        buf.write("\2\2\21\u00b9\3\2\2\2\23\u00bf\3\2\2\2\25\u00c3\3\2\2")
        buf.write("\2\27\u00cc\3\2\2\2\31\u00cf\3\2\2\2\33\u00d7\3\2\2\2")
        buf.write("\35\u00de\3\2\2\2\37\u00e5\3\2\2\2!\u00eb\3\2\2\2#\u00f0")
        buf.write("\3\2\2\2%\u00f4\3\2\2\2\'\u00fd\3\2\2\2)\u0100\3\2\2\2")
        buf.write("+\u0108\3\2\2\2-\u010e\3\2\2\2/\u0110\3\2\2\2\61\u0112")
        buf.write("\3\2\2\2\63\u0114\3\2\2\2\65\u0116\3\2\2\2\67\u0118\3")
        buf.write("\2\2\29\u011a\3\2\2\2;\u011c\3\2\2\2=\u011e\3\2\2\2?\u0120")
        buf.write("\3\2\2\2A\u0122\3\2\2\2C\u0124\3\2\2\2E\u0126\3\2\2\2")
        buf.write("G\u0128\3\2\2\2I\u012a\3\2\2\2K\u012c\3\2\2\2M\u012e\3")
        buf.write("\2\2\2O\u0130\3\2\2\2Q\u0133\3\2\2\2S\u0136\3\2\2\2U\u0139")
        buf.write("\3\2\2\2W\u013c\3\2\2\2Y\u013e\3\2\2\2[\u0141\3\2\2\2")
        buf.write("]\u0143\3\2\2\2_\u0146\3\2\2\2a\u0149\3\2\2\2c\u0155\3")
        buf.write("\2\2\2e\u0162\3\2\2\2g\u016c\3\2\2\2i\u0177\3\2\2\2k\u0183")
        buf.write("\3\2\2\2m\u0190\3\2\2\2o\u019b\3\2\2\2q\u01a7\3\2\2\2")
        buf.write("s\u01ad\3\2\2\2u\u01bc\3\2\2\2w\u01c8\3\2\2\2y\u01d3\3")
        buf.write("\2\2\2{\u01d5\3\2\2\2}\u01f0\3\2\2\2\177\u0205\3\2\2\2")
        buf.write("\u0081\u0207\3\2\2\2\u0083\u020d\3\2\2\2\u0085\u0221\3")
        buf.write("\2\2\2\u0087\u0223\3\2\2\2\u0089\u0226\3\2\2\2\u008b\u0231")
        buf.write("\3\2\2\2\u008d\u023b\3\2\2\2\u008f\u0241\3\2\2\2\u0091")
        buf.write("\u0244\3\2\2\2\u0093\u0094\7c\2\2\u0094\u0095\7w\2\2\u0095")
        buf.write("\u0096\7v\2\2\u0096\u0097\7q\2\2\u0097\4\3\2\2\2\u0098")
        buf.write("\u0099\7d\2\2\u0099\u009a\7t\2\2\u009a\u009b\7g\2\2\u009b")
        buf.write("\u009c\7c\2\2\u009c\u009d\7m\2\2\u009d\6\3\2\2\2\u009e")
        buf.write("\u009f\7d\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7q\2\2\u00a1")
        buf.write("\u00a2\7n\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7c\2\2\u00a4")
        buf.write("\u00a5\7p\2\2\u00a5\b\3\2\2\2\u00a6\u00a7\7f\2\2\u00a7")
        buf.write("\u00a8\7q\2\2\u00a8\n\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa")
        buf.write("\u00ab\7n\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\f\3\2\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7t\2\2\u00b0")
        buf.write("\u00b1\7w\2\2\u00b1\u00b2\7g\2\2\u00b2\16\3\2\2\2\u00b3")
        buf.write("\u00b4\7h\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6\7n\2\2\u00b6")
        buf.write("\u00b7\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\20\3\2\2\2\u00b9")
        buf.write("\u00ba\7h\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7q\2\2\u00bc")
        buf.write("\u00bd\7c\2\2\u00bd\u00be\7v\2\2\u00be\22\3\2\2\2\u00bf")
        buf.write("\u00c0\7h\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7t\2\2\u00c2")
        buf.write("\24\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7w\2\2\u00c5")
        buf.write("\u00c6\7p\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8\7v\2\2\u00c8")
        buf.write("\u00c9\7k\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7p\2\2\u00cb")
        buf.write("\26\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7h\2\2\u00ce")
        buf.write("\30\3\2\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7p\2\2\u00d1")
        buf.write("\u00d2\7v\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7i\2\2\u00d4")
        buf.write("\u00d5\7g\2\2\u00d5\u00d6\7t\2\2\u00d6\32\3\2\2\2\u00d7")
        buf.write("\u00d8\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7v\2\2\u00da")
        buf.write("\u00db\7w\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7p\2\2\u00dd")
        buf.write("\34\3\2\2\2\u00de\u00df\7u\2\2\u00df\u00e0\7v\2\2\u00e0")
        buf.write("\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7i\2\2\u00e4\36\3\2\2\2\u00e5\u00e6\7y\2\2\u00e6")
        buf.write("\u00e7\7j\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7n\2\2\u00e9")
        buf.write("\u00ea\7g\2\2\u00ea \3\2\2\2\u00eb\u00ec\7x\2\2\u00ec")
        buf.write("\u00ed\7q\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7f\2\2\u00ef")
        buf.write("\"\3\2\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7w\2\2\u00f2")
        buf.write("\u00f3\7v\2\2\u00f3$\3\2\2\2\u00f4\u00f5\7e\2\2\u00f5")
        buf.write("\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7v\2\2\u00f8")
        buf.write("\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7w\2\2\u00fb")
        buf.write("\u00fc\7g\2\2\u00fc&\3\2\2\2\u00fd\u00fe\7q\2\2\u00fe")
        buf.write("\u00ff\7h\2\2\u00ff(\3\2\2\2\u0100\u0101\7k\2\2\u0101")
        buf.write("\u0102\7p\2\2\u0102\u0103\7j\2\2\u0103\u0104\7g\2\2\u0104")
        buf.write("\u0105\7t\2\2\u0105\u0106\7k\2\2\u0106\u0107\7v\2\2\u0107")
        buf.write("*\3\2\2\2\u0108\u0109\7c\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("\u010b\7t\2\2\u010b\u010c\7c\2\2\u010c\u010d\7{\2\2\u010d")
        buf.write(",\3\2\2\2\u010e\u010f\7*\2\2\u010f.\3\2\2\2\u0110\u0111")
        buf.write("\7+\2\2\u0111\60\3\2\2\2\u0112\u0113\7}\2\2\u0113\62\3")
        buf.write("\2\2\2\u0114\u0115\7\177\2\2\u0115\64\3\2\2\2\u0116\u0117")
        buf.write("\7]\2\2\u0117\66\3\2\2\2\u0118\u0119\7_\2\2\u01198\3\2")
        buf.write("\2\2\u011a\u011b\7=\2\2\u011b:\3\2\2\2\u011c\u011d\7.")
        buf.write("\2\2\u011d<\3\2\2\2\u011e\u011f\7\60\2\2\u011f>\3\2\2")
        buf.write("\2\u0120\u0121\7<\2\2\u0121@\3\2\2\2\u0122\u0123\7?\2")
        buf.write("\2\u0123B\3\2\2\2\u0124\u0125\7-\2\2\u0125D\3\2\2\2\u0126")
        buf.write("\u0127\7/\2\2\u0127F\3\2\2\2\u0128\u0129\7,\2\2\u0129")
        buf.write("H\3\2\2\2\u012a\u012b\7\61\2\2\u012bJ\3\2\2\2\u012c\u012d")
        buf.write("\7\'\2\2\u012dL\3\2\2\2\u012e\u012f\7#\2\2\u012fN\3\2")
        buf.write("\2\2\u0130\u0131\7(\2\2\u0131\u0132\7(\2\2\u0132P\3\2")
        buf.write("\2\2\u0133\u0134\7~\2\2\u0134\u0135\7~\2\2\u0135R\3\2")
        buf.write("\2\2\u0136\u0137\7?\2\2\u0137\u0138\7?\2\2\u0138T\3\2")
        buf.write("\2\2\u0139\u013a\7#\2\2\u013a\u013b\7?\2\2\u013bV\3\2")
        buf.write("\2\2\u013c\u013d\7>\2\2\u013dX\3\2\2\2\u013e\u013f\7>")
        buf.write("\2\2\u013f\u0140\7?\2\2\u0140Z\3\2\2\2\u0141\u0142\7@")
        buf.write("\2\2\u0142\\\3\2\2\2\u0143\u0144\7@\2\2\u0144\u0145\7")
        buf.write("?\2\2\u0145^\3\2\2\2\u0146\u0147\7<\2\2\u0147\u0148\7")
        buf.write("<\2\2\u0148`\3\2\2\2\u0149\u014a\7t\2\2\u014a\u014b\7")
        buf.write("g\2\2\u014b\u014c\7c\2\2\u014c\u014d\7f\2\2\u014d\u014e")
        buf.write("\7K\2\2\u014e\u014f\7p\2\2\u014f\u0150\7v\2\2\u0150\u0151")
        buf.write("\7g\2\2\u0151\u0152\7i\2\2\u0152\u0153\7g\2\2\u0153\u0154")
        buf.write("\7t\2\2\u0154b\3\2\2\2\u0155\u0156\7r\2\2\u0156\u0157")
        buf.write("\7t\2\2\u0157\u0158\7k\2\2\u0158\u0159\7p\2\2\u0159\u015a")
        buf.write("\7v\2\2\u015a\u015b\7K\2\2\u015b\u015c\7p\2\2\u015c\u015d")
        buf.write("\7v\2\2\u015d\u015e\7g\2\2\u015e\u015f\7i\2\2\u015f\u0160")
        buf.write("\7g\2\2\u0160\u0161\7t\2\2\u0161d\3\2\2\2\u0162\u0163")
        buf.write("\7t\2\2\u0163\u0164\7g\2\2\u0164\u0165\7c\2\2\u0165\u0166")
        buf.write("\7f\2\2\u0166\u0167\7H\2\2\u0167\u0168\7n\2\2\u0168\u0169")
        buf.write("\7q\2\2\u0169\u016a\7c\2\2\u016a\u016b\7v\2\2\u016bf\3")
        buf.write("\2\2\2\u016c\u016d\7y\2\2\u016d\u016e\7t\2\2\u016e\u016f")
        buf.write("\7k\2\2\u016f\u0170\7v\2\2\u0170\u0171\7g\2\2\u0171\u0172")
        buf.write("\7H\2\2\u0172\u0173\7n\2\2\u0173\u0174\7q\2\2\u0174\u0175")
        buf.write("\7c\2\2\u0175\u0176\7v\2\2\u0176h\3\2\2\2\u0177\u0178")
        buf.write("\7t\2\2\u0178\u0179\7g\2\2\u0179\u017a\7c\2\2\u017a\u017b")
        buf.write("\7f\2\2\u017b\u017c\7D\2\2\u017c\u017d\7q\2\2\u017d\u017e")
        buf.write("\7q\2\2\u017e\u017f\7n\2\2\u017f\u0180\7g\2\2\u0180\u0181")
        buf.write("\7c\2\2\u0181\u0182\7p\2\2\u0182j\3\2\2\2\u0183\u0184")
        buf.write("\7r\2\2\u0184\u0185\7t\2\2\u0185\u0186\7k\2\2\u0186\u0187")
        buf.write("\7p\2\2\u0187\u0188\7v\2\2\u0188\u0189\7D\2\2\u0189\u018a")
        buf.write("\7q\2\2\u018a\u018b\7q\2\2\u018b\u018c\7n\2\2\u018c\u018d")
        buf.write("\7g\2\2\u018d\u018e\7c\2\2\u018e\u018f\7p\2\2\u018fl\3")
        buf.write("\2\2\2\u0190\u0191\7t\2\2\u0191\u0192\7g\2\2\u0192\u0193")
        buf.write("\7c\2\2\u0193\u0194\7f\2\2\u0194\u0195\7U\2\2\u0195\u0196")
        buf.write("\7v\2\2\u0196\u0197\7t\2\2\u0197\u0198\7k\2\2\u0198\u0199")
        buf.write("\7p\2\2\u0199\u019a\7i\2\2\u019an\3\2\2\2\u019b\u019c")
        buf.write("\7r\2\2\u019c\u019d\7t\2\2\u019d\u019e\7k\2\2\u019e\u019f")
        buf.write("\7p\2\2\u019f\u01a0\7v\2\2\u01a0\u01a1\7U\2\2\u01a1\u01a2")
        buf.write("\7v\2\2\u01a2\u01a3\7t\2\2\u01a3\u01a4\7k\2\2\u01a4\u01a5")
        buf.write("\7p\2\2\u01a5\u01a6\7i\2\2\u01a6p\3\2\2\2\u01a7\u01a8")
        buf.write("\7u\2\2\u01a8\u01a9\7w\2\2\u01a9\u01aa\7r\2\2\u01aa\u01ab")
        buf.write("\7g\2\2\u01ab\u01ac\7t\2\2\u01acr\3\2\2\2\u01ad\u01ae")
        buf.write("\7r\2\2\u01ae\u01af\7t\2\2\u01af\u01b0\7g\2\2\u01b0\u01b1")
        buf.write("\7x\2\2\u01b1\u01b2\7g\2\2\u01b2\u01b3\7p\2\2\u01b3\u01b4")
        buf.write("\7v\2\2\u01b4\u01b5\7F\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7")
        buf.write("\7h\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9\7w\2\2\u01b9\u01ba")
        buf.write("\7n\2\2\u01ba\u01bb\7v\2\2\u01bbt\3\2\2\2\u01bc\u01bd")
        buf.write("\7\61\2\2\u01bd\u01be\7,\2\2\u01be\u01c2\3\2\2\2\u01bf")
        buf.write("\u01c1\13\2\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4\3\2\2")
        buf.write("\2\u01c2\u01c3\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c5")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\7,\2\2\u01c6")
        buf.write("\u01c7\7\61\2\2\u01c7v\3\2\2\2\u01c8\u01c9\7\61\2\2\u01c9")
        buf.write("\u01ca\7\61\2\2\u01ca\u01ce\3\2\2\2\u01cb\u01cd\n\2\2")
        buf.write("\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cfx\3\2\2\2\u01d0\u01ce")
        buf.write("\3\2\2\2\u01d1\u01d4\5\r\7\2\u01d2\u01d4\5\17\b\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4z\3\2\2\2\u01d5")
        buf.write("\u01d9\t\3\2\2\u01d6\u01d8\t\4\2\2\u01d7\u01d6\3\2\2\2")
        buf.write("\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3")
        buf.write("\2\2\2\u01da|\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01f1")
        buf.write("\7\62\2\2\u01dd\u01e1\t\5\2\2\u01de\u01e0\t\6\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e1\u01e2\3\2\2\2\u01e2\u01ec\3\2\2\2\u01e3\u01e1\3")
        buf.write("\2\2\2\u01e4\u01e6\7a\2\2\u01e5\u01e7\t\6\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9\u01eb\3\2\2\2\u01ea\u01e4\3\2\2\2")
        buf.write("\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3")
        buf.write("\2\2\2\u01ed\u01ef\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f1")
        buf.write("\b?\2\2\u01f0\u01dc\3\2\2\2\u01f0\u01dd\3\2\2\2\u01f1")
        buf.write("~\3\2\2\2\u01f2\u0206\7\62\2\2\u01f3\u01f7\t\5\2\2\u01f4")
        buf.write("\u01f6\t\6\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2")
        buf.write("\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u0202\3")
        buf.write("\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fc\7a\2\2\u01fb\u01fd")
        buf.write("\t\6\2\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0201\3\2\2\2")
        buf.write("\u0200\u01fa\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3")
        buf.write("\2\2\2\u0202\u0203\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0202")
        buf.write("\3\2\2\2\u0205\u01f2\3\2\2\2\u0205\u01f3\3\2\2\2\u0206")
        buf.write("\u0080\3\2\2\2\u0207\u0209\7\60\2\2\u0208\u020a\t\6\2")
        buf.write("\2\u0209\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u0082\3\2\2\2\u020d")
        buf.write("\u020f\t\7\2\2\u020e\u0210\t\b\2\2\u020f\u020e\3\2\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210\u0212\3\2\2\2\u0211\u0213\t")
        buf.write("\6\2\2\u0212\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0212")
        buf.write("\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0084\3\2\2\2\u0216")
        buf.write("\u0217\5\177@\2\u0217\u0218\5\u0081A\2\u0218\u0219\bC")
        buf.write("\3\2\u0219\u0222\3\2\2\2\u021a\u021c\5\177@\2\u021b\u021d")
        buf.write("\5\u0081A\2\u021c\u021b\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021e\u021f\5\u0083B\2\u021f\u0220\bC\4")
        buf.write("\2\u0220\u0222\3\2\2\2\u0221\u0216\3\2\2\2\u0221\u021a")
        buf.write("\3\2\2\2\u0222\u0086\3\2\2\2\u0223\u0224\7^\2\2\u0224")
        buf.write("\u0225\t\t\2\2\u0225\u0088\3\2\2\2\u0226\u022b\7$\2\2")
        buf.write("\u0227\u022a\n\n\2\2\u0228\u022a\5\u0087D\2\u0229\u0227")
        buf.write("\3\2\2\2\u0229\u0228\3\2\2\2\u022a\u022d\3\2\2\2\u022b")
        buf.write("\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022e\3\2\2\2")
        buf.write("\u022d\u022b\3\2\2\2\u022e\u022f\7$\2\2\u022f\u0230\b")
        buf.write("E\5\2\u0230\u008a\3\2\2\2\u0231\u0235\7$\2\2\u0232\u0234")
        buf.write("\n\n\2\2\u0233\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\3\2\2\2")
        buf.write("\u0237\u0235\3\2\2\2\u0238\u0239\bF\6\2\u0239\u008c\3")
        buf.write("\2\2\2\u023a\u023c\t\13\2\2\u023b\u023a\3\2\2\2\u023c")
        buf.write("\u023d\3\2\2\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2")
        buf.write("\u023e\u023f\3\2\2\2\u023f\u0240\bG\7\2\u0240\u008e\3")
        buf.write("\2\2\2\u0241\u0242\13\2\2\2\u0242\u0243\bH\b\2\u0243\u0090")
        buf.write("\3\2\2\2\u0244\u0245\13\2\2\2\u0245\u0092\3\2\2\2\30\2")
        buf.write("\u01c2\u01ce\u01d3\u01d9\u01e1\u01e8\u01ec\u01f0\u01f7")
        buf.write("\u01fe\u0202\u0205\u020b\u020f\u0214\u021c\u0221\u0229")
        buf.write("\u022b\u0235\u023d\t\3?\2\3C\3\3C\4\3E\5\3F\6\b\2\2\3")
        buf.write("H\7")
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
    UNCLOSE_STRING = 63
    WS = 64
    ERROR_CHAR = 65
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
            "STRINGLIT", "UNCLOSE_STRING", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

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
                  "FLOATLIT", "ESC", "STRINGLIT", "UNCLOSE_STRING", "WS", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

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
            actions[67] = self.STRINGLIT_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[70] = self.ERROR_CHAR_action 
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

            raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


