import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """u = array(a1 => 3 . 4, a2 => 3 + (u2 % 901324));"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """abc = 1 + 2 ?? 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input, expect, 203))
