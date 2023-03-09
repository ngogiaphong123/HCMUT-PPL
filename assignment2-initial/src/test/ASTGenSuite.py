import unittest
from TestUtils import TestAST
from AST import *

from src.main.mt22.utils.AST import *


class ASTGenSuite(unittest.TestCase):
    def test_ast_1(self):
        input_str = """delta: integer = fact(3);"""
        expect = """Program([
	VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 300))

    def test_ast_2(self):
        input_str = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 301))

    def test_ast_3(self):
        input_str = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input_str, expect, 302))

    def test_ast_4(self):
        """Simple program"""
        input_str = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 303))

    def test_ast_5(self):
        """More complex program"""
        input_str = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 304))

    def test_ast_6(self):
        """More complex program"""
        input_str = """x: integer = 65;
         inc: function void(out n: integer, delta: integer) {
             n = n + delta;
         }
         main: function void() {
             a, b: integer = 1, 2;
             inc(x, delta);
             printInteger(x);
         }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2))]), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 305))

    def test_ast_7(self):
        input_str = """a, b, c: integer = 3, 4, 6;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 306))

    def test_ast_8(self):
        input_str = """a, b, c: integer = 3, 4, 6;
        d, e, f: float;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
	VarDecl(d, FloatType)
	VarDecl(e, FloatType)
	VarDecl(f, FloatType)
])"""
        self.assertTrue(TestAST.test(input_str, expect, 307))

    def test_ast_9(self):
        input_str = """
        a : integer = 3;
        program: function void () {
            a, b, c: integer;
            d, e, f: float;
            g: boolean;
        }"""
        expect_str = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	FuncDecl(program, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType)]), BlockStmt([VarDecl(d, FloatType), VarDecl(e, FloatType), VarDecl(f, FloatType)]), BlockStmt([VarDecl(g, BooleanType)])]))
])"""
        self.assertTrue(TestAST.test(input_str, expect_str, 308))

    def test_ast_10(self):
        input_str = """
        program: function void (arr: array [10,12] of integer, left: integer, right: integer) {
            if (left < right) {
                mid = (left + right)/2;
                sort(arr, left, mid);
                sort(arr, mid + 1, right);
                merge(arr, left, mid, right);
            }
        }
        merge: function void (arr: array [10] of integer, left: integer, mid: integer, right: integer) {
            n1 = mid - left + 1;
            n2 = right - mid;
            left_arr : array [10] of integer;
            right_arr : array [10] of integer;
            for (i = 0, i < n1, i + 1) {
                left_arr[i] = arr[left + i];
            }
            for (j = 0, j < n2, j + 1) {
                right_arr[j] = arr[mid + 1 + j];
            }

            i = 0;
            j = 0;
            k = left;

            while ((i < n1) && (j < n2)) {
                if (left_arr[i] <= right_arr[j]) {
                    arr[k] = left_arr[i];
                    i = i + 1;
                }
                else {
                    arr[k] = right_arr[j];
                    j = j + 1;
                }
                k = k + 1;
            }

            while (i < n1) {
                arr[k] = left_arr[i];
                i = i + 1;
                k = k + 1;
            }

            while (j < n2) {
                arr[k] = right_arr[j];
                j = j + 1;
                k = k + 1;
            }
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10, 12], IntegerType)), Param(left, IntegerType), Param(right, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(left), Id(right)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), CallStmt(sort, Id(arr), Id(left), Id(mid)), CallStmt(sort, Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(right)), CallStmt(merge, Id(arr), Id(left), Id(mid), Id(right))]))]))
	FuncDecl(merge, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(left, IntegerType), Param(mid, IntegerType), Param(right, IntegerType)], None, BlockStmt([AssignStmt(Id(n1), BinExpr(+, BinExpr(-, Id(mid), Id(left)), IntegerLit(1))), AssignStmt(Id(n2), BinExpr(-, Id(right), Id(mid))), BlockStmt([VarDecl(left_arr, ArrayType([10], IntegerType))]), BlockStmt([VarDecl(right_arr, ArrayType([10], IntegerType))]), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(left_arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(left), Id(i))]))])), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(n2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(right_arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, BinExpr(+, Id(mid), IntegerLit(1)), Id(j))]))])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), AssignStmt(Id(k), Id(left)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n1)), BinExpr(<, Id(j), Id(n2))), BlockStmt([IfStmt(BinExpr(<=, ArrayCell(left_arr, [Id(i)]), ArrayCell(right_arr, [Id(j)])), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(left_arr, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(right_arr, [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(i), Id(n1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(left_arr, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(j), Id(n2)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(right_arr, [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 309))

    def test_ast_11(self):
        input_str = """
                program: function void (arr: array [10] of integer) {
            n = 10;
            for (i = 0, i < n - 1, i + 1) {
                for (j = 0, j < n - i - 1, j + 1) {
                    if (arr[j] > arr[j + 1]) {
                        temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 310))

    def test_ast_12(self):
        input_str = """program: function void() {
            a = ("a" :: "b") :: "c";
        }"""
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(::, StringLit(a), StringLit(b)), StringLit(c)))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 311))

    def test_ast_13(self):
        """Testing for inheritance"""
        input_str = """
            multiply: function integer (x: integer, y: integer) {
                return x * y;
            }
            square: function integer (inherit out x: integer) {
                return x * x;
            }
            main: function void () inherit multiply {
                a = super(1212+2,31);
                b = square(a);
            }
        """
        expect = """Program([
	FuncDecl(multiply, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(y)))]))
	FuncDecl(square, IntegerType, [InheritOutParam(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(x)))]))
	FuncDecl(main, VoidType, [], multiply, BlockStmt([AssignStmt(Id(a), FuncCall(super, [BinExpr(+, IntegerLit(1212), IntegerLit(2)), IntegerLit(31)])), AssignStmt(Id(b), FuncCall(square, [Id(a)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 312))

    def test_ast_14(self):
        input_str = """
        program: function void (arr: array [10] of integer) {
            n = 10;
            swapped = true;
            while (swapped) {
                swapped = false;
                for (i = 0, i < n - 1, i + 1) {
                    if (arr[i] > arr[i + 1]) {
                        temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                        swapped = true;
                    }
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(swapped), BooleanLit(True)), WhileStmt(Id(swapped), BlockStmt([AssignStmt(Id(swapped), BooleanLit(False)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))]), Id(temp)), AssignStmt(Id(swapped), BooleanLit(True))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 313))

    def test_ast_15(self):
        input_str = """
         isPalindrome : function boolean (s : string) {
             for (i = 0, i < length(s) / 2, i + 1) {
                 if (s[i] != s[length(s) - i - 1]) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             s = "racecar";
             if (isPalindrome(s)) {
                 printString("s is a palindrome.");
             } else {
                 printString("s is not a palindrome.");
             }
         }
         """
        expect = """Program([
	FuncDecl(isPalindrome, BooleanType, [Param(s, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, FuncCall(length, [Id(s)]), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s, [Id(i)]), ArrayCell(s, [BinExpr(-, BinExpr(-, FuncCall(length, [Id(s)]), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(racecar)), IfStmt(FuncCall(isPalindrome, [Id(s)]), BlockStmt([CallStmt(printString, StringLit(s is a palindrome.))]), BlockStmt([CallStmt(printString, StringLit(s is not a palindrome.))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 314))

    def test_ast_16(self):
        """Reverse string function"""
        input_str = """
         reverse : function string (s : string) {
             result = "";
             for (i = length(s) - 1, i >= 0, i - 1) {
                 result = result + s[i];
             }
             return result;
         }
         main: function void () {
             s = "Hello world!";
             printString(reverse(s));
         }
         """
        expect = """Program([
	FuncDecl(reverse, StringType, [Param(s, StringType)], None, BlockStmt([AssignStmt(Id(result), StringLit()), ForStmt(AssignStmt(Id(i), BinExpr(-, FuncCall(length, [Id(s)]), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(s, [Id(i)])))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(Hello world!)), CallStmt(printString, FuncCall(reverse, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 315))

    def test_ast_17(self):
        """Reverse int function"""
        input_str = """
         reverse : function integer (n : integer) {
             result = 0;
             while (n > 0) {
                 result = result * 10 + n % 10;
                 n = n / 10;
             }
             return result;
         }
         main: function void () {
             n = 12345;
             printInt(reverse(n));
         }
         """
        expect = """Program([
	FuncDecl(reverse, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), WhileStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(result), BinExpr(+, BinExpr(*, Id(result), IntegerLit(10)), BinExpr(%, Id(n), IntegerLit(10)))), AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(10)))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(12345)), CallStmt(printInt, FuncCall(reverse, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 316))

    def test_ast_18(self):
        """Search insert position function"""
        input_str = """
         searchInsert : function integer (nums : array[5] of integer, target : integer) {
             for (i = 0, i < length(nums), i + 1) {
                 if (nums[i] >= target) {
                     return i;
                 }
             }
             return length(nums);
         }
         main: function void () {
             nums = 21;
             target = 5;
             printInt(searchInsert(nums, target));
         }
         """
        expect = """Program([
	FuncDecl(searchInsert, IntegerType, [Param(nums, ArrayType([5], IntegerType)), Param(target, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, ArrayCell(nums, [Id(i)]), Id(target)), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(FuncCall(length, [Id(nums)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), IntegerLit(21)), AssignStmt(Id(target), IntegerLit(5)), CallStmt(printInt, FuncCall(searchInsert, [Id(nums), Id(target)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 317))

    def test_ast_19(self):
        input_str = """
        main: function void () {
            if (x > 0) {
                printString("x is positive!");
            }
            else if (x < 0) {
                printString("x is negative!");
            }
            else {
                printString("x is zero!");
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(x is positive!))]), IfStmt(BinExpr(<, Id(x), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(x is negative!))]), BlockStmt([CallStmt(printString, StringLit(x is zero!))])))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 318))

    def test_ast_20(self):
        input_str = """
                 isArmstrong : function boolean (n : integer) {
             sum = 0;
             temp = n;
             while (temp > 0) {
                 digit = temp % 10;
                 sum = sum + digit * digit * digit;
                 temp = temp / 10;
             }
             if (sum == n) {
                 return true;
             } else {
                 return false;
             }
         }
         main: function void () {
             n = 153;
             if (isArmstrong(n)) {
                 printString("n is an Armstrong number.");
             } else {
                 printString("n is not an Armstrong number.");
             }
         }
         """
        expect = """Program([
	FuncDecl(isArmstrong, BooleanType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), AssignStmt(Id(temp), Id(n)), WhileStmt(BinExpr(>, Id(temp), IntegerLit(0)), BlockStmt([AssignStmt(Id(digit), BinExpr(%, Id(temp), IntegerLit(10))), AssignStmt(Id(sum), BinExpr(+, Id(sum), BinExpr(*, BinExpr(*, Id(digit), Id(digit)), Id(digit)))), AssignStmt(Id(temp), BinExpr(/, Id(temp), IntegerLit(10)))])), IfStmt(BinExpr(==, Id(sum), Id(n)), BlockStmt([ReturnStmt(BooleanLit(True))]), BlockStmt([ReturnStmt(BooleanLit(False))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(153)), IfStmt(FuncCall(isArmstrong, [Id(n)]), BlockStmt([CallStmt(printString, StringLit(n is an Armstrong number.))]), BlockStmt([CallStmt(printString, StringLit(n is not an Armstrong number.))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 319))

    def test_ast_21(self):
        """is anaGram function"""
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
        expect = """Program([
	FuncDecl(isAnaGram, BooleanType, [Param(s1, StringType), Param(s2, StringType)], None, BlockStmt([IfStmt(BinExpr(!=, FuncCall(length, [Id(s1)]), FuncCall(length, [Id(s2)])), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(s1)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s1, [Id(i)]), ArrayCell(s2, [BinExpr(-, BinExpr(-, FuncCall(length, [Id(s2)]), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s1), StringLit(racecar)), AssignStmt(Id(s2), StringLit(racecar)), IfStmt(FuncCall(isAnaGram, [Id(s1), Id(s2)]), BlockStmt([CallStmt(printString, StringLit(s1 and s2 are anagrams.))]), BlockStmt([CallStmt(printString, StringLit(s1 and s2 are not anagrams.))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 320))