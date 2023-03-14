import unittest
from TestUtils import TestAST
from AST import *

from src.main.mt22.utils.AST import *


class ASTGenSuite(unittest.TestCase):
    def test_case_151(self):
        input = """func: function string () {
                while ( i <= 1) 
                    {
                        for (i = 0, v < 10, t + 1)
                        {
                        if (a == 1 ) a, b: integer;

                        a: integer = 10;
                        }
                        a: integer = 10;
                    }
            }"""
        expect = """Program([
    	FuncDecl(func, StringType, [], None, BlockStmt([WhileStmt(BinExpr(<=, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, Id(v), IntegerLit(10)), BinExpr(+, Id(t), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(10)))]))]))]))
    ])"""
        self.assertTrue(TestAST.test(input, expect, 1))
