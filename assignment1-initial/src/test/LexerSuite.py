import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # case 101 : test valid identifiers
    def testValidIdentifier(self):
        """test identifiers"""
        input = """12_23.2"""
        expect = "aA_a"
        self.assertTrue(TestLexer.test(input, expect, 101))

