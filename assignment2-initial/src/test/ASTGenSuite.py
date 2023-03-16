import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test_case_101(self):
        input = """a,b,c : integer = 2,124,2;
            main : function void () {
                a,b,c : integer = 2,124,2;
                a : integer = 2;
                b : float = .e1;
                c : string = "abc";
                d,jk : array [2,3] of integer = {1,2,3,4,5,6} , 12.2e9;
            }
        """
        expect = """Program([
	VarDecl(x, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 101))
