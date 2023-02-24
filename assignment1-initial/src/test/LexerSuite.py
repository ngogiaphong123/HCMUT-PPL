import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test1(self):
        input = """/*have a good day*/"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 101))

    def test2(self):
        input = """/*make my day \n hello*/"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 102))

    def test3(self):
        input = """/*if*//*else*/"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 103))

    def test4(self):
        input = """/*if i were a girl*/sorry*/"""
        output = """sorry,*,/,<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 104))

    def test5(self):
        input = """//lamdienchinh"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 105))

    def test6(self):
        input = """// goodbye goodbye \n /* see you later */"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 106))

    def test7(self):
        input = """// /*goodbye goodbye */ see you later */"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 107))

    # --------------- Identifier --------------------

    def test8(self):
        input = """abc"""
        expect = """abc,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test9(self):
        input = """Abc"""
        expect = """Abc,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 109))

    def test10(self):
        input = """_abc"""
        expect = """_abc,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 110))

    def test11(self):
        input = """abc123456"""
        expect = """abc123456,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 111))

    # Test 12:

    def test12(self):
        input = """___abcsd"""
        expect = """___abcsd,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 112))

    def test13(self):
        input = """___chinhlamcute~aha"""
        expect = """___chinhlamcute,Error Token ~"""
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test14(self):
        input = """___toimanhkhoe___"""
        expect = """___toimanhkhoe___,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 114))

    # --------------- Literals --------------------
    #  ----- IntLit -----
    def test15(self):
        input = """0"""
        expect = """0,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 115))

    def test16(self):
        input = """0123"""
        expect = """0,123,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 116))

    def test17(self):
        input = """1_23_231230"""
        expect = """123231230,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test18(self):
        input = """1234567890"""
        expect = """1234567890,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 118))

    def test19(self):
        input = """-999"""
        expect = """-,999,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 119))

    def test20(self):
        input = """+666"""
        expect = """+,666,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 120))

    def test21(self):
        input = """123_456_"""
        expect = """123456,_,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test22(self):
        input = """0_123_456"""
        expect = """0,_123_456,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 122))

    #  ----- FloatLit -----

    def test23(self):
        input = """0.0"""
        expect = """0.0,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test24(self):
        input = """123e8"""
        expect = """123e8,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 124))

    def test25(self):
        input = """345e+2"""
        expect = """345e+2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 125))

    def test26(self):
        input = """888e-6"""
        expect = """888e-6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 126))

    def test27(self):
        input = """0e6"""
        expect = """0e6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 127))

    def test28(self):
        input = """0e-6"""
        expect = """0e-6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 128))

    def test29(self):
        input = """0e+6"""
        expect = """0e+6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 129))

    def test30(self):
        input = """123_33e2"""
        expect = """12333e2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 130))

    def test31(self):
        input = """123_33_45e-2"""
        expect = """1233345e-2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 131))

    def test32(self):
        input = """12333_45e+2"""
        expect = """1233345e+2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 132))

    def test33(self):
        input = """.e8569"""
        expect = """.e8569,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test34(self):
        input = """.0e"""
        expect = """.,0,e,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 134))

    def test35(self):
        input = """.0e1"""
        expect = """.0e1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 135))

    def test36(self):
        input = """.0E-123"""
        expect = """.0E-123,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test37(self):
        input = """123_1234.0124"""
        expect = """1231234.0124,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 137))

    def test38(self):
        input = """123456.00"""
        expect = """123456.00,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test39(self):
        input = """1236."""
        expect = """1236.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 139))

    def test40(self):
        input = """1236.0E451"""
        expect = """1236.0E451,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test41(self):
        input = """12_3_6.0e-451"""
        expect = """1236.0e-451,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 141))

    #  ----- BooleanLit -----
    def test42(self):
        input = """true false"""
        expect = """true,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 142))

    # ----- String literal -------

    def test43(self):
        input = """ "He asked me: \\\"Where is John?\\\"" """
        expect = """He asked me: \\\"Where is John?\\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test44(self):
        input = """ "He loves me so much" """
        expect = """He loves me so much,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test45(self):
        input = """ "Co gi do ky la \\b \\t" """
        expect = """Co gi do ky la \\b \\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test46(self):
        input = """ "La qua nhi \\n \\r \\f" """
        expect = """La qua nhi \\n \\r \\f,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 146))

    def test47(self):
        input = """ "This is Chinh\'s bag" """
        expect = """This is Chinh\'s bag,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 147))

    #  ---------- Unclose String -------------

    def test48(self):
        input = """ "Chuoi khong dong\n" """
        expect = """Unclosed String: Chuoi khong dong\n"""
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test49(self):
        input = """ "Khong biet bay gio la may gio """
        expect = """Unclosed String: Khong biet bay gio la may gio """
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test50(self):
        input = """ "Ban muon gi vay\\b \\t \\r \\n """
        expect = """Unclosed String: Ban muon gi vay\\b \\t \\r \\n """
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test51(self):
        input = """ "hinh nhu chuoi nay chua dong \\\\ abc'"hello" """
        expect = """hinh nhu chuoi nay chua dong \\\\ abc',hello,Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 151))

    #  ---------- Illegal Escape In String -------------

    def test52(self):
        input = """ "Nam nay toi 21 tuoi roi do \\c" """
        expect = """Illegal Escape In String: Nam nay toi 21 tuoi roi do \\c"""
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test53(self):
        input = """ "Ke ban chu ban \\a haha \\d" """
        expect = """Illegal Escape In String: Ke ban chu ban \\a"""
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test54(self):
        input = """ "Ngay mai co\\\\ the nang\\\\ se rat dep do\\>" """
        expect = """Illegal Escape In String: Ngay mai co\\\\ the nang\\\\ se rat dep do\\>"""
        self.assertTrue(TestLexer.test(input, expect, 154))

    #  ---------- Keyword -------------

    def test55(self):
        input = """auto break boolean"""
        expect = """auto,break,boolean,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test56(self):
        input = """do else false"""
        expect = """do,else,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test57(self):
        input = """float for function"""
        expect = """float,for,function,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test58(self):
        input = """if integer return"""
        expect = """if,integer,return,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158))

    def test59(self):
        input = """string true while"""
        expect = """string,true,while,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 159))

    def test60(self):
        input = """void out continue"""
        expect = """void,out,continue,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 160))

    def test61(self):
        input = """of inherit array"""
        expect = """of,inherit,array,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 161))

    # ----------------- Other Test -------------------------
    def test62(self):
        input = """
        // One
        // True
        /* Three */
        Alonci: function array[1] of boolean (cd: auto, temp: string) {
            a=c[c[c[c[c[c12]]]]];
            b=b[1,1,1,1,,1,,];
        }"""
        expect = """Alonci,:,function,array,[,1,],of,boolean,(,cd,:,auto,,,temp,:,string,),{,a,=,c,[,c,[,c,[,c,[,c,[,c12,],],],],],;,b,=,b,[,1,,,1,,,1,,,1,,,,,1,,,,,],;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 162))

    def test63(self):
        input = """chinhLam2k2: function array[4,2,6] of void (cd: auto, temp: string) {
            ;
            ;
            ;
            ;
        }"""
        expect = """chinhLam2k2,:,function,array,[,4,,,2,,,6,],of,void,(,cd,:,auto,,,temp,:,string,),{,;,;,;,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test64(self):
        input = """se: int;
        ce: float;
        b: boolean;
        d: array[i] of boolean;
        foo: function integer () {
            printString();
        }"""
        expect = """se,:,int,;,ce,:,float,;,b,:,boolean,;,d,:,array,[,i,],of,boolean,;,foo,:,function,integer,(,),{,printString,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 164))

    def test65(self):
        input = """add: function integer (a: integer, b: integer) {
            return a+b;
        }"""
        expect = """add,:,function,integer,(,a,:,integer,,,b,:,integer,),{,return,a,+,b,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 165))

    def test66(self):
        input = """main : function void() {
            if ((b >= 2.0) && (b <= 3.0)) {
                printf("b is between 2.0 and 3.0, inclusive.\\n");
            } else {
                printf("b is not between 2.0 and 3.0, inclusive.\\n");
            }"""
        expect = """main,:,function,void,(,),{,if,(,(,b,>=,2.0,),&&,(,b,<=,3.0,),),{,printf,(,b is between 2.0 and 3.0, inclusive.\\n,),;,},else,{,printf,(,b is not between 2.0 and 3.0, inclusive.\\n,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 166))

    def test67(self):
        input = """main : function void () {
            b = a[a[89]];
        }"""
        expect = """main,:,function,void,(,),{,b,=,a,[,a,[,89,],],;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 167))

    def test68(self):
        input = """integers: array [5] of integer = [1, 7, 3, 9, 5];
        largest_int: integer = find_largest(integers);"""
        expect = """integers,:,array,[,5,],of,integer,=,[,1,,,7,,,3,,,9,,,5,],;,largest_int,:,integer,=,find_largest,(,integers,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test69(self):
        input = """
        printf("The sum of the Fibonacci numbers from the 3rd to the 10th is %d.\\n", fib_sum);"""
        expect = """printf,(,The sum of the Fibonacci numbers from the 3rd to the 10th is %d.\\n,,,fib_sum,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test70(self):
        input = """matrix: array [4, 4] of integer = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]];
        printf("The sum of the elements on the main diagonal is %d.\\n", diag_sum);"""
        expect = """matrix,:,array,[,4,,,4,],of,integer,=,[,[,1,,,2,,,3,,,4,],,,[,5,,,6,,,7,,,8,],,,[,9,,,10,,,11,,,12,],,,[,13,,,14,,,15,,,16,],],;,printf,(,The sum of the elements on the main diagonal is %d.\\n,,,diag_sum,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test71(self):
        input = """matrix: array [3, 3] of integer = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];"""
        expect = """matrix,:,array,[,3,,,3,],of,integer,=,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],,,[,7,,,8,,,9,],],;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test72(self):
        input = """if (row_sum > largest_sum) {
            largest_sum = row_sum;
            largest_sum_row = i;
        }"""
        expect = """if,(,row_sum,>,largest_sum,),{,largest_sum,=,row_sum,;,largest_sum_row,=,i,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test73(self):
        input = """// Declare and initialize variables.
        float: array [10] of integer;
        fib_nums: array [10] of integer;"""
        expect = """float,:,array,[,10,],of,integer,;,fib_nums,:,array,[,10,],of,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test74(self):
        input = """matrix: array [4, 4] of integer = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12},
            {13, 14, 15, 16}
        };"""
        expect = """matrix,:,array,[,4,,,4,],of,integer,=,{,{,1,,,2,,,3,,,4,},,,{,5,,,6,,,7,,,8,},,,{,9,,,10,,,11,,,12,},,,{,13,,,14,,,15,,,16,},},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test75(self):
        input = """printf("int: %d\n", int[0]);
        printf("int2: %d\n", int2);
        printf("bool: %s\n", bool ? "true" : "false");
        printf("string: %s\n", string);"""
        expect = """printf,(,Unclosed String: int: %d\n"""
        self.assertTrue(TestLexer.test(input, expect, 175))

    # ----------- Operators ----------------
    # --- Arithmetic Operators -----

    def test76(self):
        input = """+ - * / %"""
        expect = """+,-,*,/,%,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 176))

    # --- Boolean Operators -----

    def test77(self):
        input = """! && ||"""
        expect = """!,&&,||,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 177))

    # --- Relational Operators -----

    def test78(self):
        input = """== != < > <= >="""
        expect = """==,!=,<,>,<=,>=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 178))

    # --- String Operators -----

    def test79(self):
        input = """::"""
        expect = """::,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 179))

    # --------------- Separators ------------

    def test80(self):
        input = """{ }"""
        expect = """{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 180))

    def test81(self):
        input = """[ ]"""
        expect = """[,],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test82(self):
        input = """( )"""
        expect = """(,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test83(self):
        input = """."""
        expect = """.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test84(self):
        input = ""","""
        expect = """,,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 184))

    def test85(self):
        input = """:"""
        expect = """:,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test86(self):
        input = """;"""
        expect = """;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 186))

    # ----------------- Other Testcases -----------------

    def test87(self):
        input = """ "Hello $&@^!\{\}[]#%World" """
        expect = """Illegal Escape In String: Hello $&@^!\{"""
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test88(self):
        input = """3 + 4 - 2 * 5 / 6"""
        expect = """3,+,4,-,2,*,5,/,6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test89(self):
        input = """a && b || c || acccssdd && aaaeess"""
        expect = """a,&&,b,||,c,||,acccssdd,&&,aaaeess,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test90(self):
        input = """x == y != z > w >= v < u <= t"""
        expect = """x,==,y,!=,z,>,w,>=,v,<,u,<=,t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test91(self):
        input = """(a + b) * (c - d)"""
        expect = """(,a,+,b,),*,(,c,-,d,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test92(self):
        input = """if x > y then x = x - y else x = x + y"""
        expect = """if,x,>,y,then,x,=,x,-,y,else,x,=,x,+,y,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test93(self):
        input = """for i = 1 to 10 do print(i)"""
        expect = """for,i,=,1,to,10,do,print,(,i,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test94(self):
        input = """x = 5 // This is a comment"""
        expect = """x,=,5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test95(self):
        input = """/* This is a\nmulti-line comment\n*/ x = 5"""
        expect = """x,=,5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test96(self):
        input = """"/* This is a /* nested */ comment */"""
        expect = """Unclosed String: /* This is a /* nested */ comment */"""
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test97(self):
        input = """a(ssddd) _ass1234546ee "*&(*@^@)()*/-122@*@" """
        expect = """a,(,ssddd,),_ass1234546ee,*&(*@^@)()*/-122@*@,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test98(self):
        input = """{ "name": "John", "age": 30 }"""
        expect = """{,name,:,John,,,age,:,30,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))

    def test99(self):
        input = """Helllo haalooo 123 123123 01213 .eas2184 "aaaabbbc &&*(((@)))" """
        expect = """Helllo,haalooo,123,123123,0,1213,.,eas2184,aaaabbbc &&*(((@))),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test100(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,},main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 200))