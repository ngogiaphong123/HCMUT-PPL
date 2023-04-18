import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test01(self):
        """Simple program: int main() {} """
        input = """
        main: function void () {
            a: integer = 1;
            b: integer = 2;
            while (a <= 10) {
                b = b * 2;
                a = a + 1;
                if(a == 5) {
                    a = a + 1;
                }
                for (a = 1, a < 10, a + 1) {
                    b = b + 1;
                    break;
                }
            }
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))