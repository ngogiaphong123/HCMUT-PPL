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

    def test_ast_22(self):
        input_str = """
         lowestCommonAncestor : function integer (root : integer, p : integer, q : integer) {
             if ((p < root) && (q < root)) {
                 return lowestCommonAncestor(rootLeft, p, q);
             } else if ((p > root) && (q > root)) {
                 return lowestCommonAncestor(rootRight, p, q);
             } else {
                 return root;
             }
         }
         main: function void () {
             root = 6;
             p = 2;
             q = 8;
             printInt(lowestCommonAncestor(root, p, q));
         }
         """
        expect = """Program([
	FuncDecl(lowestCommonAncestor, IntegerType, [Param(root, IntegerType), Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(<, Id(p), Id(root)), BinExpr(<, Id(q), Id(root))), BlockStmt([ReturnStmt(FuncCall(lowestCommonAncestor, [Id(rootLeft), Id(p), Id(q)]))]), IfStmt(BinExpr(&&, BinExpr(>, Id(p), Id(root)), BinExpr(>, Id(q), Id(root))), BlockStmt([ReturnStmt(FuncCall(lowestCommonAncestor, [Id(rootRight), Id(p), Id(q)]))]), BlockStmt([ReturnStmt(Id(root))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(root), IntegerLit(6)), AssignStmt(Id(p), IntegerLit(2)), AssignStmt(Id(q), IntegerLit(8)), CallStmt(printInt, FuncCall(lowestCommonAncestor, [Id(root), Id(p), Id(q)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 321))

    def test_ast_23(self):
        """Sum of left leaves function"""
        input_str = """
         sumOfLeftLeaves : function integer (root : integer) {
             if (root == null) {
                 return 0;
             }
             if ((rootLeft != null) && (rootLeftLeft == null) && (rootLeftRight == null)) {
                 return rootLeftVal + sumOfLeftLeaves(rootRight);
             }
             return sumOfLeftLeaves(rootLeft) + sumOfLeftLeaves(rootRight);
         }
         main: function void () {
             root = 3;
             printInt(sumOfLeftLeaves(root));
         }
         """
        expect = """Program([
	FuncDecl(sumOfLeftLeaves, IntegerType, [Param(root, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(root), Id(null)), BlockStmt([ReturnStmt(IntegerLit(0))])), IfStmt(BinExpr(&&, BinExpr(&&, BinExpr(!=, Id(rootLeft), Id(null)), BinExpr(==, Id(rootLeftLeft), Id(null))), BinExpr(==, Id(rootLeftRight), Id(null))), BlockStmt([ReturnStmt(BinExpr(+, Id(rootLeftVal), FuncCall(sumOfLeftLeaves, [Id(rootRight)])))])), ReturnStmt(BinExpr(+, FuncCall(sumOfLeftLeaves, [Id(rootLeft)]), FuncCall(sumOfLeftLeaves, [Id(rootRight)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(root), IntegerLit(3)), CallStmt(printInt, FuncCall(sumOfLeftLeaves, [Id(root)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 322))

    def test_ast_24(self):
        """Reverse Linked List function"""
        input_str = """
         reverseList : function integer (head : integer) {
             prev = null;
             curr = head;
             while (curr != null) {
                 nextTemp = currNext;
                 currNext = prev;
                 prev = curr;
                 curr = nextTemp;
             }
             return prev;
         }
         main: function void () {
             head = 1;
             printInt(reverseList(head));
         }
         """
        expect = """Program([
	FuncDecl(reverseList, IntegerType, [Param(head, IntegerType)], None, BlockStmt([AssignStmt(Id(prev), Id(null)), AssignStmt(Id(curr), Id(head)), WhileStmt(BinExpr(!=, Id(curr), Id(null)), BlockStmt([AssignStmt(Id(nextTemp), Id(currNext)), AssignStmt(Id(currNext), Id(prev)), AssignStmt(Id(prev), Id(curr)), AssignStmt(Id(curr), Id(nextTemp))])), ReturnStmt(Id(prev))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(head), IntegerLit(1)), CallStmt(printInt, FuncCall(reverseList, [Id(head)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 323))

    def test_ast_25(self):
        """Valid Parentheses function"""
        input_str = """
         isValid : function boolean (s : string) {
             if (length(s) % 2 != 0) {
                 return false;
             }
             for (i = 0, i < length(s), i + 1) {
                 if (s[i] == "(") {
                     push(s[i]);
                 } else if (s[i] == ")") {
                     if (top() == "(") {
                         pop();
                     } else {
                         return false;
                     }
                 }
             }
             if (isEmpty()) {
                 return true;
             } else {
                 return false;
             }
         }
         main: function void () {
             s = "((()))";
             if (isValid(s)) {
                 printString("s is valid.");
             } else {
                 printString("s is not valid.");
             }
         }
         """
        expect = """Program([
	FuncDecl(isValid, BooleanType, [Param(s, StringType)], None, BlockStmt([IfStmt(BinExpr(!=, BinExpr(%, FuncCall(length, [Id(s)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(s)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit(()), BlockStmt([CallStmt(push, ArrayCell(s, [Id(i)]))]), IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit())), BlockStmt([IfStmt(BinExpr(==, FuncCall(top, []), StringLit(()), BlockStmt([CallStmt(pop, )]), BlockStmt([ReturnStmt(BooleanLit(False))]))])))])), IfStmt(FuncCall(isEmpty, []), BlockStmt([ReturnStmt(BooleanLit(True))]), BlockStmt([ReturnStmt(BooleanLit(False))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(((())))), IfStmt(FuncCall(isValid, [Id(s)]), BlockStmt([CallStmt(printString, StringLit(s is valid.))]), BlockStmt([CallStmt(printString, StringLit(s is not valid.))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 324))

    def test_ast_26(self):
        """Square Root function"""
        input_str = """
         sqrt : function float (x : float) {
             if (x == 0) {
                 return 0;
             }
             if (x < 0) {
                 return -1;
             }
             left = 1;
             right = x;
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
             return right;
         }
         main: function void () {
             x = 8;
             printFloat(sqrt(x));
         }
         """
        expected = """Program([
	FuncDecl(sqrt, FloatType, [Param(x, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))])), IfStmt(BinExpr(<, Id(x), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), AssignStmt(Id(left), IntegerLit(1)), AssignStmt(Id(right), Id(x)), WhileStmt(BinExpr(<=, Id(left), Id(right)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), IfStmt(BinExpr(==, BinExpr(*, Id(mid), Id(mid)), Id(x)), BlockStmt([ReturnStmt(Id(mid))]), IfStmt(BinExpr(<, BinExpr(*, Id(mid), Id(mid)), Id(x)), BlockStmt([AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1)))])))])), ReturnStmt(Id(right))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), IntegerLit(8)), CallStmt(printFloat, FuncCall(sqrt, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 325))

    def test_ast_27(self):
        """Climbing Stairs function"""
        input_str = """
         climbStairs : function integer (n : integer) {
             if (n == 1) {
                 return 1;
             }
             first = 1;
             second = 2;
             for (i = 3, i <= n, i + 1) {
                 third = first + second;
                 first = second;
                 second = third;
             }
             return second;
         }
         main: function void () {
             n = 4;
             printInt(climbStairs(n));
         }
         """
        expected = """Program([
	FuncDecl(climbStairs, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))])), AssignStmt(Id(first), IntegerLit(1)), AssignStmt(Id(second), IntegerLit(2)), ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(third), BinExpr(+, Id(first), Id(second))), AssignStmt(Id(first), Id(second)), AssignStmt(Id(second), Id(third))])), ReturnStmt(Id(second))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(4)), CallStmt(printInt, FuncCall(climbStairs, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 326))

    def test_ast_28(self):
        """Count Primes function"""
        input_str = """
         countPrimes : function integer (n : integer) {
             if (n < 2) {
                 return 0;
             }
             count = 0;
             for (i = 2, i < n, i + 1) {
                 if (isPrime(i)) {
                     count = count + 1;
                 }
             }
             return count;
         }
         isPrime : function boolean (n : integer) {
             if (n < 2) {
                 return false;
             }
             for (i = 2, i * i <= n, i + 1) {
                 if (n % i == 0) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             n = 10;
             printInt(countPrimes(n));
         }
         """
        expected = """Program([
	FuncDecl(countPrimes, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(0))])), AssignStmt(Id(count), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(isPrime, [Id(i)]), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), ReturnStmt(Id(count))]))
	FuncDecl(isPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, BinExpr(*, Id(i), Id(i)), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), CallStmt(printInt, FuncCall(countPrimes, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 327))

    def test_ast_29(self):
        """Decode Ways function"""
        input_str = """
         numDecodings : function integer (s : string) {
             if (s == "") {
                 return 0;
             }
             n = length(s);
             dp : array[6] of integer;
             dp[0] = 1;
             dp[1] = 1;
             for (i = 2, i <= n, i + 1) {
                 if (s[i - 1] != "0") {
                     dp[i] = dp[i - 1];
                 }
                 if ((s[i - 2] == "1") || ((s[i - 2] == "2") && (s[i - 1] < "7"))) {
                     dp[i] = dp[i] + dp[i - 2];
                 }
             }
             return dp[n];
         }
         main: function void () {
             s = "226";
             printInt(numDecodings(s));
         }
         """
        expected = """Program([
	FuncDecl(numDecodings, IntegerType, [Param(s, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(s), StringLit()), BlockStmt([ReturnStmt(IntegerLit(0))])), AssignStmt(Id(n), FuncCall(length, [Id(s)])), BlockStmt([VarDecl(dp, ArrayType([6], IntegerType))]), AssignStmt(ArrayCell(dp, [IntegerLit(0)]), IntegerLit(1)), AssignStmt(ArrayCell(dp, [IntegerLit(1)]), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))]), StringLit(0)), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), ArrayCell(dp, [BinExpr(-, Id(i), IntegerLit(1))]))])), IfStmt(BinExpr(||, BinExpr(==, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(2))]), StringLit(1)), BinExpr(&&, BinExpr(==, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(2))]), StringLit(2)), BinExpr(<, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))]), StringLit(7)))), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), BinExpr(+, ArrayCell(dp, [Id(i)]), ArrayCell(dp, [BinExpr(-, Id(i), IntegerLit(2))])))]))])), ReturnStmt(ArrayCell(dp, [Id(n)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(226)), CallStmt(printInt, FuncCall(numDecodings, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 328))

    def test_ast_30(self):
        """Delete Node in a Linked List function"""
        input_str = """
         deleteNode : function void (node : integer) {
             nodeVal = nodeVal;
             nodeNext = nodeNext;
         }
         main: function void () {
             node = 5;
             deleteNode(node);
         }
         """
        expected = """Program([
	FuncDecl(deleteNode, VoidType, [Param(node, IntegerType)], None, BlockStmt([AssignStmt(Id(nodeVal), Id(nodeVal)), AssignStmt(Id(nodeNext), Id(nodeNext))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(node), IntegerLit(5)), CallStmt(deleteNode, Id(node))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 329))

    def test_ast_31(self):
        """Merge Two Sorted Lists function"""
        input_str = """
         mergeTwoLists : function integer (l1 : integer, l2 : integer) {
             if (l1 == null) {
                 return l2;
             }
             if (l2 == null) {
                 return l1;
             }
             if (l1Val < l2Val) {
                 l1Next = mergeTwoLists(l1Next, l2);
                 return l1;
             } else {
                 l2Next = mergeTwoLists(l1, l2Next);
                 return l2;
             }
         }
         main: function void () {
             l1 = 1;
             l2 = 2;
             printInt(mergeTwoLists(l1, l2));
         }
         """
        expected = """Program([
	FuncDecl(mergeTwoLists, IntegerType, [Param(l1, IntegerType), Param(l2, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(l1), Id(null)), BlockStmt([ReturnStmt(Id(l2))])), IfStmt(BinExpr(==, Id(l2), Id(null)), BlockStmt([ReturnStmt(Id(l1))])), IfStmt(BinExpr(<, Id(l1Val), Id(l2Val)), BlockStmt([AssignStmt(Id(l1Next), FuncCall(mergeTwoLists, [Id(l1Next), Id(l2)])), ReturnStmt(Id(l1))]), BlockStmt([AssignStmt(Id(l2Next), FuncCall(mergeTwoLists, [Id(l1), Id(l2Next)])), ReturnStmt(Id(l2))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(l1), IntegerLit(1)), AssignStmt(Id(l2), IntegerLit(2)), CallStmt(printInt, FuncCall(mergeTwoLists, [Id(l1), Id(l2)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 330))

    def test_ast_32(self):
        """Find the index of the first occurrence of a substring function"""
        input_str = """
         find : function integer (str : string, sub : string) {
             for (i = 0, i < length(str), i + 1) {
                 for (j = 0, j < length(sub), j + 1) {
                     if (str[i + j] != sub[j]) {
                         break;
                     }
                 }
                 if (j == length(sub)) {
                     return i;
                 }
             }
             return -1;
         }
         main: function void () {
             str = "Hello World!";
             sub = "World";
             printInt(find(str, sub));
         }
         """
        expected = """Program([
	FuncDecl(find, IntegerType, [Param(str, StringType), Param(sub, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), FuncCall(length, [Id(sub)])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(str, [BinExpr(+, Id(i), Id(j))]), ArrayCell(sub, [Id(j)])), BlockStmt([BreakStmt()]))])), IfStmt(BinExpr(==, Id(j), FuncCall(length, [Id(sub)])), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(str), StringLit(Hello World!)), AssignStmt(Id(sub), StringLit(World)), CallStmt(printInt, FuncCall(find, [Id(str), Id(sub)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 331))

    def test_ast_33(self):
        """Put the first letter of each word in uppercase function"""
        input_str = """
         capitalize : function string (str : string) {
             str[0] = toUpper(str[0]);
             for (i = 1, i < length(str), i + 1) {
                 if (str[i - 1] == " ") {
                     str[i] = toUpper(str[i]);
                 }
             }
             return str;
         }
         main: function void () {
             str = "hello world!";
             printStr(capitalize(str));
         }
         """
        expected = """Program([
	FuncDecl(capitalize, StringType, [Param(str, StringType)], None, BlockStmt([AssignStmt(ArrayCell(str, [IntegerLit(0)]), FuncCall(toUpper, [ArrayCell(str, [IntegerLit(0)])])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(str, [BinExpr(-, Id(i), IntegerLit(1))]), StringLit( )), BlockStmt([AssignStmt(ArrayCell(str, [Id(i)]), FuncCall(toUpper, [ArrayCell(str, [Id(i)])]))]))])), ReturnStmt(Id(str))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(str), StringLit(hello world!)), CallStmt(printStr, FuncCall(capitalize, [Id(str)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 332))

    def test_ast_34(self):
        """Find the first non-repeating character function"""
        input_str = """
         firstNonRepeating : function string (str : string) {
             for (i = 0, i < length(str), i + 1) {
                 found = false;
                 for (j = 0, j < length(str), j + 1) {
                     if ((i != j) && (str[i] == str[j])) {
                         found = true;
                         break;
                     }
                 }
                 if (!found) {
                     return str[i];
                 }
             }
             return "";
         }
         main: function void () {
             str = "Hello World!";
             printStr(firstNonRepeating(str));
         }
         """
        expected = """Program([
	FuncDecl(firstNonRepeating, StringType, [Param(str, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(found), BooleanLit(False)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), FuncCall(length, [Id(str)])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(!=, Id(i), Id(j)), BinExpr(==, ArrayCell(str, [Id(i)]), ArrayCell(str, [Id(j)]))), BlockStmt([AssignStmt(Id(found), BooleanLit(True)), BreakStmt()]))])), IfStmt(UnExpr(!, Id(found)), BlockStmt([ReturnStmt(ArrayCell(str, [Id(i)]))]))])), ReturnStmt(StringLit())]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(str), StringLit(Hello World!)), CallStmt(printStr, FuncCall(firstNonRepeating, [Id(str)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 333))

    def test_ast_35(self):
        """Isomorphic Strings function"""
        input_str = """
         isIsomorphic : function boolean (s : string, t : string) {
             n = length(s);
             if (n != length(t)) {
                 return false;
             }
             map : array [256] of integer= {};
             for (i = 0, i < n, i + 1) {
                 if (map[s[i]] == 0) {
                     map[s[i]] = t[i];
                 } else {
                     if (map[s[i]] != t[i]) {
                         return false;
                     }
                 }
             }
             return true;
         }
         main: function void () {
             s = "egg";
             t = "add";
             printBool(isIsomorphic(s, t));
         }
         """
        expected = """Program([
	FuncDecl(isIsomorphic, BooleanType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), IfStmt(BinExpr(!=, Id(n), FuncCall(length, [Id(t)])), BlockStmt([ReturnStmt(BooleanLit(False))])), BlockStmt([VarDecl(map, ArrayType([256], IntegerType), ArrayLit([]))]), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(map, [ArrayCell(s, [Id(i)])]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(map, [ArrayCell(s, [Id(i)])]), ArrayCell(t, [Id(i)]))]), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(map, [ArrayCell(s, [Id(i)])]), ArrayCell(t, [Id(i)])), BlockStmt([ReturnStmt(BooleanLit(False))]))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(egg)), AssignStmt(Id(t), StringLit(add)), CallStmt(printBool, FuncCall(isIsomorphic, [Id(s), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 334))

    def test_ast_36(self):
        """Is Subsequence function"""
        input_str = """
         isSubsequence : function boolean (s : string, t : string) {
             n = length(s);
             m = length(t);
             i = 0;
             j = 0;
             while ((i < n) && (j < m)) {
                 if (s[i] == t[j]) {
                     i = i + 1;
                 }
                 j = j + 1;
             }
             return i == n;
         }
         main: function void () {
             s = "abc";
             t = "ahbgdc";
             printBool(isSubsequence(s, t));
         }
         """
        expected = """Program([
	FuncDecl(isSubsequence, BooleanType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(m), FuncCall(length, [Id(t)])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n)), BinExpr(<, Id(j), Id(m))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), ArrayCell(t, [Id(j)])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), ReturnStmt(BinExpr(==, Id(i), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(abc)), AssignStmt(Id(t), StringLit(ahbgdc)), CallStmt(printBool, FuncCall(isSubsequence, [Id(s), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 335))

    def test_ast_37(self):
        """Find the Difference function"""
        input_str = """
         findTheDifference : function string (s : string, t : string) {
             n = length(s);
             m = length(t);
             sum = 0;
             for (i = 0, i < n, i + 1) {
                 sum = sum + ord(s[i]);
             }
             for (i = 0, i < m, i + 1) {
                 sum = sum - ord(t[i]);
             }
             return chr(-sum);
         }
         main: function void () {
             s = "abcd";
             t = "abcde";
             printString(findTheDifference(s, t));
         }
         """
        expected = """Program([
	FuncDecl(findTheDifference, StringType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(m), FuncCall(length, [Id(t)])), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), FuncCall(ord, [ArrayCell(s, [Id(i)])])))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(m)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(-, Id(sum), FuncCall(ord, [ArrayCell(t, [Id(i)])])))])), ReturnStmt(FuncCall(chr, [UnExpr(-, Id(sum))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(abcd)), AssignStmt(Id(t), StringLit(abcde)), CallStmt(printString, FuncCall(findTheDifference, [Id(s), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 336))

    def test_ast_38(self):
        """Find the Celebrity function"""
        input_str = """
         findCelebrity : function integer (n : integer) {
             candidate = 0;
             for (i = 1, i < n, i + 1) {
                 if (knows(candidate, i)) {
                     candidate = i;
                 }
             }
             for (i = 0, i < n, i + 1) {
                 if ((i != candidate) && ((knows(candidate, i)) || (!knows(i, candidate)))) {
                     return -1;
                 }
             }
             return candidate;
         }
         main: function void () {
             n = 2;
             printInt(findCelebrity(n));
         }
         """
        expected = """Program([
	FuncDecl(findCelebrity, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(candidate), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(knows, [Id(candidate), Id(i)]), BlockStmt([AssignStmt(Id(candidate), Id(i))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(!=, Id(i), Id(candidate)), BinExpr(||, FuncCall(knows, [Id(candidate), Id(i)]), UnExpr(!, FuncCall(knows, [Id(i), Id(candidate)])))), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))]))])), ReturnStmt(Id(candidate))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(2)), CallStmt(printInt, FuncCall(findCelebrity, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 337))

    def test_ast_39(self):
        """Roman to Integer function"""
        input_str = """
         romanToInt : function integer (s : string) {
             n = length(s);
             result = 0;
             for (i = 0, i < n, i + 1) {
                 if ((i > 0) && (roman[s[i]] > roman[s[i - 1]])) {
                     result = result + roman[s[i]] - 2 * roman[s[i - 1]];
                 } else {
                     result = result + roman[s[i]];
                 }
             }
             return result;
         }
         main: function void () {
             s = "MCMXCIV";
             printInt(romanToInt(s));
         }
         """
        expected = """Program([
	FuncDecl(romanToInt, IntegerType, [Param(s, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(result), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(i), IntegerLit(0)), BinExpr(>, ArrayCell(roman, [ArrayCell(s, [Id(i)])]), ArrayCell(roman, [ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))])]))), BlockStmt([AssignStmt(Id(result), BinExpr(-, BinExpr(+, Id(result), ArrayCell(roman, [ArrayCell(s, [Id(i)])])), BinExpr(*, IntegerLit(2), ArrayCell(roman, [ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))])]))))]), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(roman, [ArrayCell(s, [Id(i)])])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(MCMXCIV)), CallStmt(printInt, FuncCall(romanToInt, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 338))

    def test_ast_40(self):
        """Length of Last Word function"""
        input_str = """
         lengthOfLastWord : function integer (s : string) {
             n : integer = length(s);
             result : integer = 0;
             for (i = n - 1, i >= 0, i - 1) {
                 if (s[i] != " ") {
                     result = result + 1;
                 } else {
                     if (result > 0) {
                         break;
                     }
                 }
             }
             return result;
         }
         main: function void () {
             s = "Hello World";
             printInt(lengthOfLastWord(s));
         }
         """
        expected = """Program([
	FuncDecl(lengthOfLastWord, IntegerType, [Param(s, StringType)], None, BlockStmt([BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(s)]))]), BlockStmt([VarDecl(result, IntegerType, IntegerLit(0))]), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s, [Id(i)]), StringLit( )), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), IntegerLit(1)))]), BlockStmt([IfStmt(BinExpr(>, Id(result), IntegerLit(0)), BlockStmt([BreakStmt()]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(Hello World)), CallStmt(printInt, FuncCall(lengthOfLastWord, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 339))

    def test_ast_41(self):
        input_str = """
            main : function void() {
                if ((b >= 2.0) && (b <= 3.0)) {
                    printf("b is between 2.0 and 3.0, inclusive.\\n");
                } else {
                    printf("b is not between 2.0 and 3.0, inclusive.\\n");
                }
            }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(b), FloatLit(2.0)), BinExpr(<=, Id(b), FloatLit(3.0))), BlockStmt([CallStmt(printf, StringLit(b is between 2.0 and 3.0, inclusive.\\n))]), BlockStmt([CallStmt(printf, StringLit(b is not between 2.0 and 3.0, inclusive.\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 340))

    def test_ast_42(self):
        input_str = """
        main: function integer () {
            n = parseNumber("5");
            result : integer = 1;
            for (i = 1, i <= n, i + 1) {
                result = result * i;
            }
            return result;
        }
        """
        expected = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(n), FuncCall(parseNumber, [StringLit(5)])), BlockStmt([VarDecl(result, IntegerType, IntegerLit(1))]), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(*, Id(result), Id(i)))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 341))

    def test_ast_43(self):
        input_str = """
        main: function void () {
            algorithm = "binary tree traversal (inorder)";
            root : integer = parseTree("(3 (1 () (2)) (4 () (5)))");
            result : array[5] of integer = {};
            inorder(root, result);
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(algorithm), StringLit(binary tree traversal (inorder))), BlockStmt([VarDecl(root, IntegerType, FuncCall(parseTree, [StringLit((3 (1 () (2)) (4 () (5))))]))]), BlockStmt([VarDecl(result, ArrayType([5], IntegerType), ArrayLit([]))]), CallStmt(inorder, Id(root), Id(result))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 342))

    def test_ast_44(self):
        input_str = """
                main: function void () {
            if (a > 10) {
                if (b > 10) {
                    printFloat(1.2);
                }
                else {
                    readString();
                }
            }
            else {
                s = "Hello";
                printString(s);
            }
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(10)), BlockStmt([CallStmt(printFloat, FloatLit(1.2))]), BlockStmt([CallStmt(readString, )]))]), BlockStmt([AssignStmt(Id(s), StringLit(Hello)), CallStmt(printString, Id(s))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 343))

    def test_ast_45(self):
        input_str = """
        main: function void () {
            if (a > 10) {
                if (b > 10) {
                    printString("Both a and b are greater than 10");
                }
                else {
                    printString("Only a is greater than 10");
                }
            }
            else {
                printString("Neither a nor b is greater than 10");
            }
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(10)), BlockStmt([CallStmt(printString, StringLit(Both a and b are greater than 10))]), BlockStmt([CallStmt(printString, StringLit(Only a is greater than 10))]))]), BlockStmt([CallStmt(printString, StringLit(Neither a nor b is greater than 10))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 344))

    def test_ast_46(self):
        """Bubble sort"""
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
        }
        """
        expected = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 345))

    def test_ast_47(self):
        """Binary Search"""
        input_str = """
            binarySearch: function integer (arr: array [10] of integer, target: integer) {
                low = 0;
                high = 9;
                while (low <= high) {
                    mid = (low + high) / 2;
                    if (arr[mid] == target) {
                        return mid;
                    } else if (arr[mid] < target) {
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                return -1;
            }
        """
        expected = """Program([
	FuncDecl(binarySearch, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(target, IntegerType)], None, BlockStmt([AssignStmt(Id(low), IntegerLit(0)), AssignStmt(Id(high), IntegerLit(9)), WhileStmt(BinExpr(<=, Id(low), Id(high)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(low), Id(high)), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(arr, [Id(mid)]), Id(target)), BlockStmt([ReturnStmt(Id(mid))]), IfStmt(BinExpr(<, ArrayCell(arr, [Id(mid)]), Id(target)), BlockStmt([AssignStmt(Id(low), BinExpr(+, Id(mid), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(high), BinExpr(-, Id(mid), IntegerLit(1)))])))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 346))

    def test_ast_48(self):
        """Loop through array"""
        input_str = """
        a : integer = 3;
        program: function void () {
            a, b, c: integer;
            d, e, f: float;
            g: boolean;
        }"""
        expected = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	FuncDecl(program, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType)]), BlockStmt([VarDecl(d, FloatType), VarDecl(e, FloatType), VarDecl(f, FloatType)]), BlockStmt([VarDecl(g, BooleanType)])]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 347))

    def test_ast_49(self):
        input_str = """
        program: function void () {
            a: integer = 1;
            b: integer = 2;
            while (a <= 10) {
                b = b * 2;
                printInteger(b);
                a = a + 1;
            }
            return;
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType, IntegerLit(1))]), BlockStmt([VarDecl(b, IntegerType, IntegerLit(2))]), WhileStmt(BinExpr(<=, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2))), CallStmt(printInteger, Id(b)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 348))

    def test_ast_50(self):
        """Testing return statement:"""
        input_str = """
            factorial: function integer (n: integer) {
                if ((n == 0) || (n==1)) return 1;
                else return n * factorial(n - 1);
            }

            program: function void () {
                a: integer = factorial(5);
                return;
            }
        """
        expect = """Program([
	FuncDecl(factorial, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(program, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType, FuncCall(factorial, [IntegerLit(5)]))]), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 349))

    def test_ast_51(self):
        input_str = """
            readInt: function void () {
                a : integer = 2 + readInteger();
            }
        """
        expect = """Program([
	FuncDecl(readInt, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType, BinExpr(+, IntegerLit(2), FuncCall(readInteger, [])))])]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 350))

