import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 101))

    def test_uppercase_identifier(self):
        """test identifiers"""
        input = "ABC"
        expect = "ABC,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 102))
