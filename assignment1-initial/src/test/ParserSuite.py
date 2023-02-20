import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # case 201 : test simple program
    def testSimpleProgram(self):
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    # case 202 : test comment
    def testCppStyleCommentProgram(self):
        input = """main: function void() {
            // asdasdw wadas
            a : integer = 2;
            b : array[2,3] of string = {"abc", "def", "ghi", "jkl", "mno", "pqr"};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    # case 203 : test comment non-greedy fail case
    def testNonGreedyCommentFail(self):
        input = """main: function void() {
            /* asdasdw wadas // */ */
            a : integer = 2;
            b : array[2,3] of string = {"abc", "def", "ghi", "jkl", "mno", "pqr"};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    # case 204 : test comment non-greedy success case
    def testNonGreedyCommentSuccess(self):
        input = """main: function void() {
            /* asdasdw wadas // */
            a : integer = 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    # case 205 : test assign integer statement
    def testAssignIntegerStatement(self):
        input = """main: function void() {
            a : integer = 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    # case 206 : test assign float statement
    def testAssignFloatStatement(self):
        input = """main: function void() {
            a : float = 2.0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    # case 207 : test assign array statement
    def testAssignArrayStatement(self):
        input = """main: function void() {
            a : array[2,3] of string = {"abc", "def", "ghi", "jkl", "mno", "pqr"};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    # case 208 : test assign boolean statement

    def testAssignBooleanStatement(self):
        input = """main: function void() {
            a : boolean = true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    # case 209 : test assign string statement
    def testAssignStringStatement(self):
        input = """main: function void() {
            a : string = "abc";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    # case 210 : test assign integer array statement
    def testAssignIntegerArrayStatement(self):
        input = """main: function void() {
            a : array[6] of integer = {1, 2, 3, 4, 5, 6};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    # case 211 : test assign float array statement
    def testAssignFloatArrayStatement(self):
        input = """main: function void() {
            a : array[2,3] of float = {{1.0, 2.0}, {3.0, 4.0}, {5.0, 6.0}};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    # case 212 : test assign boolean array statement
    def testAssignBooleanArrayStatement(self):
        input = """main: function void() {
            a : array[2,3] of boolean = {true, false, true, false, true, false};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    # case 213 : test for statement
    def testForStatement(self):
        input = """main: function void() {
            for (i = 0, i < 10, i + 1) {
                a : integer = readInteger();
                printInteger(a);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    # case 214 : test while statement
    def testWhileStatement(self):
        input = """main: function void() {
            while (i < 10) {
                a : integer = readInteger();
                printInteger(a);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    # case 215 : do while statement
    def testDoWhileStatement(self):
        input = """main: function void() {
            do {
                a : integer = readInteger();
                printInteger(a);
            } while (i < 10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    # case 216 : test break statement with for
    def testBreakStatementWithFor(self):
        input = """main: function void() {
            for (i = 0, i < 10, i + 1) {
                a : integer = readInteger();
                printInteger(a);
                break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    # case 217 : test break statement with while
    def testBreakStatementWithWhile(self):
        input = """main: function void() {
            while (i < 10) {
                a : integer = readInteger();
                printInteger(a);
                break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    # case 218 : test break statement with do while
    def testBreakStatementWithDoWhile(self):
        input = """main: function void() {
            do {
                a : integer = readInteger();
                printInteger(a);
                break;
            } while (i < 10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    # case 219 : test continue statement with for
    def testContinueStatementWithFor(self):
        input = """main: function void() {
            for (i = 0, i < 10, i + 1) {
                a : integer = readInteger();
                printInteger(a);
                continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    # case 220 : test continue statement with while
    def testContinueStatementWithWhile(self):
        input = """main: function void() {
            while (i < 10) {
                a : integer = readInteger();
                printInteger(a);
                continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    # case 221 : test return with void type statement
    def testReturnStatement(self):
        input = """main: function void() {
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    # case 222 : test return with specific type statement
    def testReturnSpecificStatement(self):
        input = """main: function integer() {
            return 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    # case 223 : test call statement
    def testCallStatement(self):
        input = """main: function void() {
            a();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    # case 224 : test call statement with parameter
    def testCallStatementWithParameter(self):
        input = """main: function void() {
            a(1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    # case 225 : test call statement with multiple parameter
    def testCallStatementWithMultipleParameter(self):
        input = """main: function void() {
            a(1, 2, 3);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    # case 226 : test call statement with multiple parameter and multiple type
    def testCallStatementWithMultipleParameterAndMultipleType(self):
        input = """main: function void() {
            a(1, 2.0, "abc");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    # case 227 : test a, b, c, d: integer = 3, 4, 6;
    def testAssignMultipleVariable(self):
        input = """a, b, c, d: integer = 3, 4, 5, 6, 7;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    # case 228