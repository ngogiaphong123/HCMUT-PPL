import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # case 101 : test valid identifiers
    def test_lowercase_identifier(self):
        """test identifiers"""
        input = "0a"
        expect = "Error Token 1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

    # case 102 : test uppercase identifiers
    def test_uppercase_identifier(self):
        """test identifiers"""
        input = "ABC"
        expect = "error,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))

    # case 103 : test underscore identifiers
    def test_underscore_identifier(self):
        """test identifiers"""
        input = "_abc"
        expect = "_abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))

    # case 104 : test digit identifiers
    def test_digit_identifier(self):
        """test identifiers"""
        input = "1ac"
        expect = "error,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))
