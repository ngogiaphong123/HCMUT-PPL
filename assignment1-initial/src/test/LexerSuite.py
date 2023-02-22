import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # case 101 : test valid identifiers
    def testValidIdentifier1(self):
        """test identifiers"""
        input = """a123"""
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 101))

    # Test case 102: a123. Expected result: Valid identifier.
    def testValidIdentifier2(self):
        """test identifiers"""
        input = """a123"""
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 102))

    # Test case 103: ABC. Expected result: Valid identifier.
    def testValidIdentifier3(self):
        """test identifiers"""
        input = """ABC"""
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 103))

    # Test case 104: _test. Expected result: Valid identifier.
    def testValidIdentifier4(self):
        """test identifiers"""
        input = """_test"""
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 104))

    # Test case 105: 123abc. Expected result: Invalid identifier (begins with a digit).
    def testInvalidIdentifier1(self):
        """test identifiers"""
        input = """123abc"""
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 105))

    # Test case 106: Test_123. Expected result: Valid identifier.
    def testValidIdentifier5(self):
        """test identifiers"""
        input = """Test_123"""
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 106))

    # Test case 107: Writeln. Expected result: Valid identifier.
    def testValidIdentifier6(self):
        """test identifiers"""
        input = """Writeln"""
        expect = "Error Token Writeln"
        self.assertTrue(TestLexer.test(input, expect, 107))

    # Test case 108: writeln. Expected result: Valid identifier (case-sensitive).
    def testValidIdentifier7(self):
        """test identifiers"""
        input = """writeln"""
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 108))

    # Test case 109: WRITELN. Expected result: Valid identifier (case-sensitive).
    def testValidIdentifier8(self):
        """test identifiers"""
        input = """WRITELN"""
        expect = "Error Token WRITELN"
        self.assertTrue(TestLexer.test(input, expect, 109))

    # Test case 110: #test. Expected result: Invalid identifier (begins with a special character).
    def testInvalidIdentifier2(self):
        """test identifiers"""
        input = """#test"""
        expect = "Error Token #test"
        self.assertTrue(TestLexer.test(input, expect, 110))

    # Test case 111: test!. Expected result: Invalid identifier (contains a special character).
    def testInvalidIdentifier3(self):
        """test identifiers"""
        input = """test!"""
        expect = "Error Token test!"
        self.assertTrue(TestLexer.test(input, expect, 111))

    # Test case 112: "Hello, world!" Expected result: Valid string.
    def testValidString1(self):
        """test string"""
        input = """ "Hello, world!" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 112))

    # Test case 113 :  "This string contains a single quote: \'"  Expected result: Valid string.
    def testValidString2(self):
        """test string"""
        input = """ "This string contains a single quote: \'" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 113))

    # Test case 114 : "This string contains a double quote: \"" Expected result: Valid string.
    def testValidString3(self):
        """test string"""
        input = """ "This string contains a double quote: \"" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 114))

    # Test case 115 : "A\ttab\tseparated\tstring" Expected result: Valid string.
    def testValidString4(self):
        """test string"""
        input = """ "A\ttab\tseparated\tstring" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 115))

    # Test case 116 : "A\nstring\nwith\nnew\nlines" Expected result: Valid string.
    def testValidString5(self):
        """test string"""
        input = """ "A\nstring\nwith\nnew\nlines" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 116))

    # Test case 117 : "This string contains a backslash: \\" Expected result: Valid string.
    def testValidString6(self):
        """test string"""
        input = """ "This string contains a backslash: \\" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 117))

    # Test case 118 : "This string contains a carriage return: \r" Expected result: Valid string.
    def testValidString7(self):
        """test string"""
        input = """ "This string contains a carriage return: \r" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 118))

    # Test case 119 : "This string contains a form feed: \f" Expected result: Valid string.
    def testValidString8(self):
        """test string"""
        input = """ "This string contains a form feed: \f" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 119))

    # Test case 120 : "This string has an unclosed quote: ' Expected result: Invalid string (unclosed quote).
    def testInvalidString1(self):
        """test string"""
        input = """ "This string has an unclosed quote: ' """
        expect = "Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 120))

    # Test case 121 : "mixed escape sequences: \"\n\t" Expected result: Valid string.
    def testValidString9(self):
        """test string"""
        input = """ "mixed escape sequences: \n\t " """
        expect = "successful"
        self.assertTrue(TestLexer.test(input, expect, 121))

