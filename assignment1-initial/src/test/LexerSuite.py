import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def testLexer1(self):
        input_str = """a"""
        expect = """a,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 101))

    def testLexer2(self):
        input_str = """ "A\nstring\nwith\nnew\nlines" """
        expect = """Unclosed String: A"""
        self.assertTrue(TestLexer.test(input_str, expect, 102))

    def testLexer3(self):
        input_str = """abc\t"""
        expect = """abc,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 103))

    def testLexer4(self):
        input_str = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 104))

    def testLexer5(self):
        input_str = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 105))

    def testLexer6(self):
        input_str = """ "He asked me: \\"Where is John?\\"" """
        expect = """He asked me: \\\"Where is John?\\\",<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 106))

    def testLexer7(self):
        input_str = """ "\\"Algorithm\\" is a word" """
        expect = """\\\"Algorithm\\\" is a word,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 107))

    def testLexer8(self):
        input_str = """ "mixed escape\\" sequences: \t " """
        expect = """mixed escape\\\" sequences: \t ,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 108))

    def testLexer9(self):
        input = """5.7e-0_1"""
        expect = """5.7e-0,_1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 109))

    def testLexer10(self):
        input_str = """delta: integer = 3;"""
        expect = """delta,:,integer,=,3,;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 110))

    def testLexer11(self):
        input_str = """d , e : array[2] of integer = {1, 2}, {3, 4}, {2,1};"""
        expect = """d,,,e,:,array,[,2,],of,integer,=,{,1,,,2,},,,{,3,,,4,},,,{2,1},;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 111))

    def testLexer12(self):
        input_str = """a = 1;"""
        expect = """a,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 112))

    def testLexer13(self):
        input_str = """a = 1.0;"""
        expect = """a,=,1.0,;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 113))

    def testLexer14(self):
        input_str = """a = 1e-1;"""
        expect = """a,=,1e-1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 114))

    def testLexer15(self):
        input_str = """matrix : array[2, 2] of integer = {{1, 2}, {3, 4}};"""
        expect = """matrix,:,array,[,2,,,2,],of,integer,=,{,{,1,,,2,},,,{,3,,,4,},},;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 115))

    def testLexer16(self):
        input_str = """a = 1e-1;"""
        expect = """a,=,1e-1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 116))

    def testLexer17(self):
        input_str = """
        program: function void () {
            a: integer = 1;
            b: integer = 2;
            while (a <= 10) {
                b = b * 2;
                print(b);
                a = a + 1;
            }
            return;
        }
        """
        expect = """program,:,function,void,(,),{,a,:,integer,=,1,;,b,:,integer,=,2,;,while,(,a,<=,10,),{,b,=,b,*,2,;,print,(,b,),;,a,=,a,+,1,;,},return,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 117))

    def testLexer18(self):
        input_str = """
            "This is a string with an escaped quote: \\""
        """
        expect = """This is a string with an escaped quote: \\\",<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 118))

    def testLexer19(self):
        input_str = """&& || !"""
        expect = """&&,||,!,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 119))

    def testLexer20(self):
        input_str = """[ ]"""
        expect = """[,],<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 120))

    def testLexer21(self):
        input_str = """( )"""
        expect = """(,),<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 121))

    def testLexer22(self):
        input_str = """{ }"""
        expect = """{,},<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 122))

    def testLexer23(self):
        input_str = """+ - * / %"""
        expect = """+,-,*,/,%,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 123))

    def testLexer24(self):
        input_str = """= == != < <= > >= && || !"""
        expect = """=,==,!=,<,<=,>,>=,&&,||,!,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 124))

    def testLexer25(self):
        input_str = """.1231254123"""
        expect = """.,1231254123,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 125))

    def testLexer26(self):
        input_str = """1231254123."""
        expect = """1231254123.,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 126))

    def testLexer27(self):
        input_str = """1231254123.123123"""
        expect = """1231254123.123123,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 127))

    def testLexer28(self):
        input_str = """1231254123e-123123"""
        expect = """1231254123e-123123,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 128))

    def testLexer29(self):
        input_str = """1231254123e123123"""
        expect = """1231254123e123123,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 129))

    def testLexer30(self):
        input_str = """1231254123E+123123"""
        expect = """1231254123E+123123,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 130))

    def testLexer31(self):
        input_str = """0.0"""
        expect = """0.0,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 131))

    def testLexer32(self):
        input_str = """0.0e-123123"""
        expect = """0.0e-123123,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 132))

    def testLexer33(self):
        input_str = """{1,2,3,4}"""
        expect = """{1,2,3,4},<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 133))

    def testLexer34(self):
        input_str = """{"Kangxi","Yongzheng","Qianlong"}"""
        expect = """{"Kangxi","Yongzheng","Qianlong"},<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 134))

    def testLexer35(self):
        input_str = """{1,"Kangxi",3,4}"""
        expect = """{1,"Kangxi",3,4},<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 135))

    def testLexer36(self):
        input_str = """{1,"QianLong",true,4}"""
        expect = """{1,"QianLong",true,4},<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 136))

    def testLexer37(self):
        input_str = """ "hello \\n" """
        expect = """hello \\n,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 137))

    def testLexer38(self):
        input_str = """ "hello \\t" """
        expect = """hello \\t,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 138))

    def testLexer39(self):
        input_str = """ "hello \\\\" """
        expect = """hello \\\\,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 139))

    def testLexer40(self):
        """Mixed escape characters"""
        input_str = """ "hello \\n\t\\\\" """
        expect = """hello \\n\t\\\\,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 140))

    def testLexer41(self):
        """Illegal escape characters"""
        input_str = """ "hello \i" """
        expect = """Illegal Escape In String: hello \\i"""
        self.assertTrue(TestLexer.test(input_str, expect, 141))

    def testLexer42(self):
        input_str = """ "hello \\b" """
        expect = """hello \\b,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 142))

    def testLexer43(self):
        input_str = """ "hello \f" """
        expect = """hello \f,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 143))

    def testLexer44(self):
        input_str = """m : integer = length(grid[0]);"""
        expect = """m,:,integer,=,length,(,grid,[,0,],),;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 144))

    def testLexer45(self):
        input_str = """while ((i < n) && (s[i] == " "))"""
        expect = """while,(,(,i,<,n,),&&,(,s,[,i,],==, ,),),<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 145))

    def testLexer46(self):
        input_str = """if (i == 0)"""
        expect = """if,(,i,==,0,),<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 146))

    def testLexer47(self):
        input_str = """threeSum : function array[2] of integer (nums : array[6] of integer) {}"""
        expect = """threeSum,:,function,array,[,2,],of,integer,(,nums,:,array,[,6,],of,integer,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 147))

    def testLexer48(self):
        input_str = """
        /* This is a comment */
        // This is a comment
        s : string = "This is a string";
        """
        expect = """s,:,string,=,This is a string,;,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 148))

    def testLexer49(self):
        input_str = "__main__"
        expect = """__main__,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 149))

    def testLexer50(self):
        input_str = """
            myLove : string = "\\"Live a life you never regret\\" - J8o"
        """
        expect = "myLove,:,string,=,\\\"Live a life you never regret\\\" - J8o,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 150))

    def testLexer51(self):
        input_str = """{0.0,12.23,123.1234}"""
        expect = """{0.0,12.23,123.1234},<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 151))

    def testLexer52(self):
        input_str = """
            // This is a comment
            /* This is a comment */
            /* */ // This is a comment
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 152))

    def testLexer53(self):
        input_str = """
            // This is a comment
            123_456_
        """
        expect = "123456,_,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 153))

    def testLexer54(self):
        input_str = """
            // This is a comment
            123_456_789
        """
        expect = "123456789,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 154))

    def testLexer55(self):
        input_str = """
            // This is a comment
            123_456_789_
        """
        expect = "123456789,_,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 155))

    def testLexer56(self):
        input_str = """
            /* This is a comment */ */
        """
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 156))

    def testLexer57(self):
        input_str = """
                 main: function void () {
             nums = {1, 3, 4, 2, 2};
             printInt(findDuplicate(nums));
         }"""
        expect = "main,:,function,void,(,),{,nums,=,{,1,,,3,,,4,,,2,,,2,},;,printInt,(,findDuplicate,(,nums,),),;,},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 157))

    def testLexer58(self):
        input_str = """
            for (i = 0, i < n, i + 1) {
                 index = abs(nums[i]) - 1;
                 if (nums[index] > 0) {
                     nums[index] = -nums[index];
                 }
             }
        """
        expect = "for,(,i,=,0,,,i,<,n,,,i,+,1,),{,index,=,abs,(,nums,[,i,],),-,1,;,if,(,nums,[,index,],>,0,),{,nums,[,index,],=,-,nums,[,index,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 158))

    def testLexer59(self):
        input_str = """
                     result : array [2] of integer= {2,3};
        """
        expect = "result,:,array,[,2,],of,integer,=,{2,3},;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 159))

    def testLexer60(self):
        input_str = """
             reverse(nums, 0, k - 1);
             reverse(nums, k, n - 1);
        """
        expect = "reverse,(,nums,,,0,,,k,-,1,),;,reverse,(,nums,,,k,,,n,-,1,),;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 160))

    def testLexer61(self):
        input_str = """
                if ((nums[i] > nums[i - 1]) && (nums[i] > nums[i + 1])) {
                    return nums[i];
                }
        """
        expect = "if,(,(,nums,[,i,],>,nums,[,i,-,1,],),&&,(,nums,[,i,],>,nums,[,i,+,1,],),),{,return,nums,[,i,],;,},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 161))

    def testLexer62(self):
        input_str = """
            iwaslostwithinthedarkuntilifoundher
        """
        expect = "iwaslostwithinthedarkuntilifoundher,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 162))

    def testLexer63(self):
        input_str = """
            str = "Hello World!";
             sub = "World";
             printInt(find(str, sub));
        """
        expect = "str,=,Hello World!,;,sub,=,World,;,printInt,(,find,(,str,,,sub,),),;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 163))

    def testLexer64(self):
        input_str = """
            // This is a comment
            /* This is a comment */
            /* */ // This is a comment
            2_3.e123
        """
        expect = "23.e123,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 164))

    def testLexer65(self):
        input_str = """
            lowestCommonAncestor : function integer (root : integer, p : integer, q : integer) {
            }
        """
        expect = "lowestCommonAncestor,:,function,integer,(,root,:,integer,,,p,:,integer,,,q,:,integer,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 165))

    def testLexer66(self):
        input_str = """
        .2e123
        """
        expect = ".2e123,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 166))

    def testLexer67(self):
        input_str = """
        +123
        """
        expect = "+,123,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 167))

    def testLexer68(self):
        input_str = """
        ___maiYeuEm___
        """
        expect = "___maiYeuEm___,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 168))

    def testLexer69(self):
        input_str = """."""
        expect = """.,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 169))

    def testLexer70(self):
        input_str = """
        123__123
        """
        expect = "123,__123,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 170))

    def testLexer71(self):
        input_str = """
        123.123.123
        """
        expect = "123.123,.,123,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 171))

    def testLexer72(self):
        input_str = """?"""
        expect = """Error Token ?"""
        self.assertTrue(TestLexer.test(input_str, expect, 172))

    def testLexer73(self):
        input_str = """
        123e123
        """
        expect = "123e123,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 173))

    def testLexer74(self):
        input_str = """::"""
        expect = """::,<EOF>"""
        self.assertTrue(TestLexer.test(input_str, expect, 174))

    def testLexer75(self):
        input_str = """
        dream : string = "Neu duoc lam lai t se lam 1 hoa si;"
        """
        expect = "dream,:,string,=,Neu duoc lam lai t se lam 1 hoa si;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 175))

    def testLexer76(self):
        input_str = """
            gpxjm
        """
        expect = "gpxjm,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 176))

    def testLexer77(self):
        input_str = """
                     isAnaGram : function boolean (s1 : string, s2 : string) {
             if (length(s1) != length(s2)) {
                 return false;
             }
             for (i = 0, i < length(s1), i + 1) {
                 if (s1[i] != s2[length(s2) - i - 1]) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             s1 = "racecar";
             s2 = "racecar";
             if (isAnaGram(s1, s2)) {
                 printString("s1 and s2 are anagrams.");
             } else {
                 printString("s1 and s2 are not anagrams.");
             }
         }
        """
        expect = "isAnaGram,:,function,boolean,(,s1,:,string,,,s2,:,string,),{,if,(,length,(,s1,),!=,length,(,s2,),),{,return,false,;,},for,(,i,=,0,,,i,<,length,(,s1,),,,i,+,1,),{,if,(,s1,[,i,],!=,s2,[,length,(,s2,),-,i,-,1,],),{,return,false,;,},},return,true,;,},main,:,function,void,(,),{,s1,=,racecar,;,s2,=,racecar,;,if,(,isAnaGram,(,s1,,,s2,),),{,printString,(,s1 and s2 are anagrams.,),;,},else,{,printString,(,s1 and s2 are not anagrams.,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 177))

    def testLexer78(self):
        input_str = """
            if (a == b) {
                return true;
            } else {
                return false;
            }
        """
        expect = "if,(,a,==,b,),{,return,true,;,},else,{,return,false,;,},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 178))

    def testLexer79(self):
        input_str = """ "This is a string\\nwith\\t\\\"escape characters\\\"." """
        expect = "This is a string\\nwith\\t\\\"escape characters\\\".,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 179))

    def testLexer80(self):
        input_str = """
            1_2_3_4.12e-12
        """
        expect = "1234.12e-12,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 180))

    def testLexer81(self):
        input_str = """
            s = "Hello\\tworld!\\nThis is a\\nnew line.";
        """
        expect = "s,=,Hello\\tworld!\\nThis is a\\nnew line.,;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 181))

    def testLexer82(self):
        input_str = """
            1.2e-12
        """
        expect = "1.2e-12,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 182))

    def testLexer83(self):
        input_str = """
            s = "Hello\\tworld!\\nThis is a\\nnew \nline.";
        """
        expect = "s,=,Unclosed String: Hello\\tworld!\\nThis is a\\nnew "
        self.assertTrue(TestLexer.test(input_str, expect, 183))

    def testLexer84(self):
        input_str = """
            a : array[6,6] of integer = 
                {{1, 2, 3, 4, 5, 6},
                {7, 8, 9, 10, 11, 12},
                {13, 14, 15, 16, 17, 18},
                {19, 20, 21, 22, 23, 24},
                {25, 26, 27, 28, 29, 30},
                {31, 32, 33, 34, 35, 36}};
        """
        expect = "a,:,array,[,6,,,6,],of,integer,=,{,{,1,,,2,,,3,,,4,,,5,,,6,},,,{,7,,,8,,,9,,,10,,,11,,,12,},,,{,13,,,14,,,15,,,16,,,17,,,18,},,,{,19,,,20,,,21,,,22,,,23,,,24,},,,{,25,,,26,,,27,,,28,,,29,,,30,},,,{,31,,,32,,,33,,,34,,,35,,,36,},},;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 184))

    def testLexer85(self):
        input_str = """
            root : integer = parseTree("(3 (1 () (2)) (4 () (5)))");
        """
        expect = "root,:,integer,=,parseTree,(,(3 (1 () (2)) (4 () (5))),),;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 185))

    def testLexer86(self):
        input_str = """
            a = 1;
            b = 2;
            c = 3;
            d = 4;
            e = 5;
            f = 6;
            g = 7;
            h = 8;
            i = 9;
            j = 10;
            k = 11;
            l = 12;
            m = 13;
            n = 14;
            o = 15;
            p = 16;
            q = 17;
            r = 18;
            s = 19;
            t = 20;
            u = 21;
            v = 22;
            w = 23;
            x = 24;
            y = 25;
            z = 26;
        """
        expect = "a,=,1,;,b,=,2,;,c,=,3,;,d,=,4,;,e,=,5,;,f,=,6,;,g,=,7,;,h,=,8,;,i,=,9,;,j,=,10,;,k,=,11,;,l,=,12,;,m,=,13,;,n,=,14,;,o,=,15,;,p,=,16,;,q,=,17,;,r,=,18,;,s,=,19,;,t,=,20,;,u,=,21,;,v,=,22,;,w,=,23,;,x,=,24,;,y,=,25,;,z,=,26,;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 186))

    def testLexer87(self):
        input_str = """
            if ((p < root) && (q < root)) {
                 return lowestCommonAncestor(rootLeft, p, q);
             } else if ((p > root) && (q > root)) {
                 return lowestCommonAncestor(rootRight, p, q);
             } else {
                 return root;
             }
        """
        expect = "if,(,(,p,<,root,),&&,(,q,<,root,),),{,return,lowestCommonAncestor,(,rootLeft,,,p,,,q,),;,},else,if,(,(,p,>,root,),&&,(,q,>,root,),),{,return,lowestCommonAncestor,(,rootRight,,,p,,,q,),;,},else,{,return,root,;,},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 187))

    def testLexer88(self):
        input_str = """
            age : string = "This year I am " :: string_of_int(age) :: " years old.";
        """
        expect = "age,:,string,=,This year I am ,::,string_of_int,(,age,),::, years old.,;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 188))

    def testLexer89(self):
        input_str = """
            if ((rootLeft != null) && (rootLeftLeft == null) && (rootLeftRight == null)) {
                 return rootLeftVal + sumOfLeftLeaves(rootRight);
        """
        expect = "if,(,(,rootLeft,!=,null,),&&,(,rootLeftLeft,==,null,),&&,(,rootLeftRight,==,null,),),{,return,rootLeftVal,+,sumOfLeftLeaves,(,rootRight,),;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 189))

    def testLexer90(self):
        input_str = """
            if ((rootLeft != null) && (rootLeftLeft == null) && (rootLeftRight == null)) {
                 return rootLeftVal + sumOfLeftLeaves(rootRight);
             } else {
                 return sumOfLeftLeaves(rootLeft) + sumOfLeftLeaves(rootRight);
             }
        """
        expect = "if,(,(,rootLeft,!=,null,),&&,(,rootLeftLeft,==,null,),&&,(,rootLeftRight,==,null,),),{,return,rootLeftVal,+,sumOfLeftLeaves,(,rootRight,),;,},else,{,return,sumOfLeftLeaves,(,rootLeft,),+,sumOfLeftLeaves,(,rootRight,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 190))

    def testLexer91(self):
        input_str = """
            for (i = red + white, i < length(nums), i + 1) {
                 nums[i] = 2;
             }
        """
        expect = "for,(,i,=,red,+,white,,,i,<,length,(,nums,),,,i,+,1,),{,nums,[,i,],=,2,;,},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 191))

    def testLexer92(self):
        input_str = """
            a = a[a[[a[2]]]];
        """
        expect = "a,=,a,[,a,[,[,a,[,2,],],],],;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 192))

    def testLexer93(self):
        input_str = """
            a = a[,] + a[2];
        """
        expect = "a,=,a,[,,,],+,a,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 193))

    def testLexer94(self):
        input_str = """
            a = a[2,];
        """
        expect = "a,=,a,[,2,,,],;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 194))

    def testLexer95(self):
        input_str = """
            a = a[2, 3];
        """
        expect = "a,=,a,[,2,,,3,],;,<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 195))

    def testLexer96(self):
        input_str = """
                if (s[i] == "(") {
                     push(s[i]);
                 } else if (s[i] == ")") {
                     if (top() == "(") {
                         pop();
                     } else {
                         return false;
                     }
                 }
        """
        expect = "if,(,s,[,i,],==,(,),{,push,(,s,[,i,],),;,},else,if,(,s,[,i,],==,),),{,if,(,top,(,),==,(,),{,pop,(,),;,},else,{,return,false,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 196))

    def testLexer97(self):
        input_str = """
                     main: function void () {
             s = "((()))";
             if (isValid(s)) {
                 printString("s is valid.");
             } else {
                 printString("s is not valid.");
             }
         }
        """
        expect = "main,:,function,void,(,),{,s,=,((())),;,if,(,isValid,(,s,),),{,printString,(,s is valid.,),;,},else,{,printString,(,s is not valid.,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 197))

    def testLexer98(self):
        input_str = """             
        while (left <= right) {
                 mid = (left + right) / 2;
                 if (mid * mid == x) {
                     return mid;
                 } else if (mid * mid < x) {
                     left = mid + 1;
                 } else {
                     right = mid - 1;
                 }
             }
        """
        expect = "while,(,left,<=,right,),{,mid,=,(,left,+,right,),/,2,;,if,(,mid,*,mid,==,x,),{,return,mid,;,},else,if,(,mid,*,mid,<,x,),{,left,=,mid,+,1,;,},else,{,right,=,mid,-,1,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 198))

    def testLexer99(self):
        input_str = """
            if (root == null) {
                 return 0;
             } else {
                 return 1 + max(maxDepth(root.left), maxDepth(root.right));
             }
        """
        expect = "if,(,root,==,null,),{,return,0,;,},else,{,return,1,+,max,(,maxDepth,(,root,.,left,),,,maxDepth,(,root,.,right,),),;,},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 199))

    def testLexer100(self):
        input_str = """
            climateChange : function void (arr : array[4] of integer) {
             n = length(arr);
             for (i = 0, i < n - 1, i + 1) {
                 for (j = 0, j < n - i - 1, j + 1) {
                     if (arr[j] > arr[j + 1]) {
                         temp = arr[j];
                         arr[j] = arr[j + 1];
                         arr[j + 1] = temp;
                     }
                 }
             }
         }
        """
        expect = "climateChange,:,function,void,(,arr,:,array,[,4,],of,integer,),{,n,=,length,(,arr,),;,for,(,i,=,0,,,i,<,n,-,1,,,i,+,1,),{,for,(,j,=,0,,,j,<,n,-,i,-,1,,,j,+,1,),{,if,(,arr,[,j,],>,arr,[,j,+,1,],),{,temp,=,arr,[,j,],;,arr,[,j,],=,arr,[,j,+,1,],;,arr,[,j,+,1,],=,temp,;,},},},},<EOF>"
        self.assertTrue(TestLexer.test(input_str, expect, 200))