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
	FuncDecl(program, VoidType, [Param(arr, ArrayType([[, 1, 0, ,,  , 1, 2, ]], IntegerType)), Param(left, IntegerType), Param(right, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(left), Id(right)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), CallStmt(sort, Id(arr), Id(left), Id(mid)), CallStmt(sort, Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(right)), CallStmt(merge, Id(arr), Id(left), Id(mid), Id(right))]))]))
	FuncDecl(merge, VoidType, [Param(arr, ArrayType([[, 1, 0, ]], IntegerType)), Param(left, IntegerType), Param(mid, IntegerType), Param(right, IntegerType)], None, BlockStmt([AssignStmt(Id(n1), BinExpr(+, BinExpr(-, Id(mid), Id(left)), IntegerLit(1))), AssignStmt(Id(n2), BinExpr(-, Id(right), Id(mid))), BlockStmt([VarDecl(left_arr, ArrayType([[, 1, 0, ]], IntegerType))]), BlockStmt([VarDecl(right_arr, ArrayType([[, 1, 0, ]], IntegerType))]), ForStmt(AssignStmt(Id(i), [340 299 290 291 291 291 291 286 281 284 230 158 154 152 148]), BinExpr(<, Id(i), Id(n1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(left_arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(left), Id(i))]))])), ForStmt(AssignStmt(Id(j), [340 299 290 291 291 291 291 291 286 281 284 230 158 154 152 148]), BinExpr(<, Id(j), Id(n2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(right_arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, BinExpr(+, Id(mid), IntegerLit(1)), Id(j))]))])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), AssignStmt(Id(k), Id(left)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n1)), BinExpr(<, Id(j), Id(n2))), BlockStmt([IfStmt(BinExpr(<=, ArrayCell(left_arr, [Id(i)]), ArrayCell(right_arr, [Id(j)])), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(left_arr, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(right_arr, [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(i), Id(n1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(left_arr, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(j), Id(n2)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(right_arr, [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 309))
