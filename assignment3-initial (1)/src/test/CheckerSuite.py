import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_static1(self) :
    #     input_str = """delta: integer = fact(3);"""
    #     except_str = "Undeclared Function: fact"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 400))
        
    # def test_static2(self) :
    #     input_str = """x, y, z: float = 1, 2, 3;"""
    #     except_str = "No entry point"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 401))
        
    # def test_static3(self) :
    #     input_str = """main: function void () {
    #         printInteger(4);
    #     }"""
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 402))
        
    # def test_static4(self) :
    #     input_str = """x: integer = 65;
    #     inc: function void(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         a, b: integer = 1, 2;
    #         inc(x, delta);
    #         printInteger(x);
    #     }"""
    #     except_str = "Undeclared Identifier: delta"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 403))
        
    # def test_static5(self) :
    #     input_str = """program: function void() {
    #         b : string = "Hello";
    #         a : string = "World";
    #         c : auto = b :: a;
    #     }"""
    #     except_str = "No entry point"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 404))
    
    # def test_static6(self) :
    #     input_str = """
    #         multiply: function integer (x: integer, y: integer) {
    #             return x * y;
    #         }
    #         square: function integer (inherit out x: integer) {
    #             return x * x;
    #         }
    #         main: function void () inherit multiply {
    #             super(1212+2,31);
    #             a : integer = 5;
    #             b : integer = square(a);
    #         }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 405))
        
    # def test_static7(self) :
    #     input_str = """
    #     length: function integer (s: string) {
    #         return 2;
    #     }
    #     isPalindrome : function boolean (s : string) {
    #         i : integer;
    #         for (i = 0, i < length(s) / 2, i + 1) {
    #         }
    #         return true;
    #     }
    #     main: function void () {
    #         s : string= "racecar";
    #         if (isPalindrome(s)) {
    #             printString("s is a palindrome.");
    #         } else {
    #             printString("s is not a palindrome.");
    #         }
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 406))
        
    # def test_static8(self) :
    #     input_str = """
    #     length: function integer (s: string) {
    #         return 2;
    #     }
    #     reverse : function string (s : string) {
    #         result : string = "";
    #         i : integer;
    #         for (i = length(s) - 1, i >= 0, i - 1) {
    #             result = result :: "c";
    #         }
    #         return result;
    #     }
    #     main: function void () {
    #         s : string = "Hello world!";
    #         printString(reverse(s));
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 407))

    # def test_static9(self) :
    #     input_str = """
    #     main: function void () {
    #         if (x > 0) {
    #             printString("x is positive!");
    #         }
    #         else if (x < 0) {
    #             printString("x is negative!");
    #         }
    #         else {
    #             printString("x is zero!");
    #         }
    #     }
    #     """
    #     except_str = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 408))
        
    # def test_static10(self) :
    #     input_str = """
    #     isArmstrong : function boolean (n : integer) {
    #         sum : integer = 0;
    #         temp : integer = n;
    #         while (temp > 0) {
    #             digit : integer = temp % 10;
    #             sum = sum + digit * digit * digit;
    #             temp = temp / 10;
    #         }
    #         if (sum == n) {
    #             return true;
    #         } else {
    #             return false;
    #         }
    #     }
    #     main: function void () {
    #         n : integer = 153;
    #         if (isArmstrong(n)) {
    #             printString("n is an Armstrong number.");
    #         } else {
    #             printString("n is not an Armstrong number.");
    #         }
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 409))

    # def test_static11(self) :
    #     input_str = """
    #     main: function void () {
    #         a : integer = 5;
    #         b : integer = 6;
    #         if (a > b) {
    #             printString("a is greater than b.");
    #         } else if (a < b) {
    #             printString("a is less than b.");
    #         } else {
    #             printString("a is equal to b.");
    #         }
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 410))
        
    # def test_static12(self) :
    #     input_str = """
    #     length : function integer (nums : array[5] of integer) {
    #         return 5;
    #     }
    #     searchInsert : function integer (nums : array[5] of integer, target : integer) {
    #         i : integer;
    #         for (i = 0, i < length(nums), i + 1) {
    #             if (nums[i] >= target) {
    #                 return i;
    #             }
    #         }
    #         return length(nums);
    #     }
    #     main: function void () {
    #         nums : array[5] of integer = {1, 3, 5, 6};
    #         target : integer = 5;
    #         printInteger(searchInsert(nums, target));
    #     }
    #     """
    #     except_str = "Type mismatch in Variable Declaration: VarDecl(nums, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(5), IntegerLit(6)]))"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 411))
    
    # def test_static13(self):
    #     input_str = """
    #     lowestCommonAncestor : function integer (root : integer, p : integer, q : integer) {
    #         if ((p < root) && (q < root)) {
    #             rootLeft : integer = root - 1;
    #             return lowestCommonAncestor(rootLeft, p, q);
    #         } else if ((p > root) && (q > root)) {
    #             rootRight : integer = root + 1;
    #             return lowestCommonAncestor(rootRight, p, q);
    #         } else {
    #             return root;
    #         }
    #     }
    #     main: function void () {
    #         root : integer = 6;
    #         p : integer = 2;
    #         q : integer = 8;
    #         printInteger(lowestCommonAncestor(root, p, q));
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 412))
        
    # def test_static14(self) :
    #     input_str = """
    #     sumOfLeftLeaves : function integer (root : integer) {
    #         if (root == 0) {
    #             return 0;
    #         }
    #         rootLeft : integer = root - 1;
    #         rootLeftLeft : integer = rootLeft - 1;
    #         rootLeftRight : integer = rootLeft + 1;
    #         rootRight : integer = root + 1;
    #         if ((rootLeft != 0) && (rootLeftLeft == 0) && (rootLeftRight == 0)) {
    #             rootLeftVal : integer = rootLeft;
    #             return rootLeftVal + sumOfLeftLeaves(rootRight);
    #         }
    #         return sumOfLeftLeaves(rootLeft) + sumOfLeftLeaves(rootRight);
    #     }
    #     main: function void () {
    #         root : integer = 3;
    #         printInteger(sumOfLeftLeaves(root));
    #     }
    #     """
    #     except_str= ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 413))
        
    # def test_static15(self): 
    #     input_str = """
    #     reverseList : function integer (head : auto) {
    #         prev : integer = 0;
    #         curr : integer = head;
    #         while (curr != null) {
    #             nextTemp : integer = currNext;
    #             currNext = prev;
    #             prev = curr;
    #             curr = nextTemp;
    #         }
    #         return prev;
    #     }
    #     main: function void () {
    #         head : integer = 1;
    #         printInteger (reverseList(head));
    #     }
    #     """
    #     except_str = "Undeclared Identifier: null"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 414))
        
    # def test_static16(self) :
    #     input_str = """
    #     sqrt : function integer (x : integer) {
    #         if (x == 0) {
    #             return 0;
    #         }
    #         if (x < 0) {
    #             return -1;
    #         }
    #         left : integer  = 1;
    #         right  : integer  = x;
    #         while (left <= right) {
    #             mid : integer = (left + right) / 2;
    #             if (mid * mid == x) {
    #                 return mid;
    #             } else if (mid * mid < x) {
    #                 left = mid + 1;
    #             } else {
    #                 right = mid - 1;
    #             }
    #         }
    #         return right;
    #     }
    #     main: function void () {
    #         x : integer = 8;
    #         printFloat(sqrt(x));
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 415))
        
    # def test_static17(self) :
    #     input_str = """
    #     climbStairs : function integer (n : integer) {
    #         if (n == 1) {
    #             return 1;
    #         }
    #         first : integer = 1;
    #         second : integer = 2;
    #         i : integer;
    #         for (i = 3, i <= n, i + 1) {
    #             third : integer = first + second;
    #             first = second;
    #             second = third;
    #         }
    #         return second;
    #     }
    #     main: function void () {
    #         n : integer = 4;
    #         printInteger(climbStairs(n));
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 416))

    # def test_static18(self) :
    #     input_str = """
    #     countPrimes : function integer (n : integer) {
    #         if (n < 2) {
    #             return 0;
    #         }
    #         count : integer = 0;
    #         i : integer;
    #         for (i = 2, i < n, i + 1) {
    #             if (isPrime(i)) {
    #                 count = count + 1;
    #             }
    #         }
    #         return count;
    #     }
    #     isPrime : function boolean (n : integer) {
    #         if (n < 2) {
    #             return false;
    #         }
    #         i : integer;
    #         for (i = 2, i * i <= n, i + 1) {
    #             if (n % i == 0) {
    #                 return false;
    #             }
    #         }
    #         return true;
    #     }
    #     main: function void () {
    #         n : integer = 10;
    #         printInteger(countPrimes(n));
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 417))

    # def test_static19(self) :
    #     input_str = """
    #     numDecodings : function integer (s : string) {
    #         n : integer = 6;
    #         dp : array[6] of integer;
    #         dp[0] = 1;
    #         dp[1] = 1;
    #         i : integer;
    #         for (i = 2, i <= n, i + 1) {
    #             dp[i] = dp[i - 1];
    #             dp[i] = dp[i] + dp[i - 2];
    #         }
    #         return dp[n];
    #     }
    #     main: function void () {
    #         s : string = "226";
    #         printInteger(numDecodings(s));
    #     }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 418))
        
    # def test_static20(self) :
    #     input_str = """
    #         foo : function integer (a : integer) inherit goo {
    #             super(a);
    #         }
    #         goo : function integer (inherit a : integer) {}
    #         main: function void () {}
    #     """
    #     except_str = "Invalid Parameter: a"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 419))
    
    # def test_static21(self) :
    #     input_str = """
    #         foo : function auto (a : auto) inherit goo {
    #             super(2);
    #             return a + b;
    #         }
    #         goo : function integer (inherit b : integer) {}
    #         main: function void () {
    #             printInteger(foo(2));
    #         }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 420))

    # def test_static22(self) :
    #     input_str = """
    #         main: function void () {
    #             foo(2);
    #         }
    #         foo : function auto (a : auto) {
    #             return a;
    #         }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 421))
    
    # def test_static23(self) :
    #     input_str = """
    #         main: function void () {
    #             a : auto;
    #         }
    #     """
    #     except_str = "Invalid Variable: a"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 422))
    
    # def test_static24(self) :
    #     input_str = """
    #         main: function void () {
    #             a : auto = 2;
    #             printInteger(a);
    #         }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 423))
        
    # def test_static25(self) :
    #     input_str = """
    #         f : function auto (a : auto, b : integer) {
    #             return a + b;
    #         }
    #         main: function void (){
    #             f("abc", 2);
    #         }
    #     """
    #     except_str = "Type mismatch in statement: CallStmt(f, StringLit(abc), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input_str, except_str, 424))
        
    # def test_static26(self) :
    #     input_str = """
    #         f : function auto (a : auto, b : integer) {
    #             return a + b;
    #         }
    #         main: function void (){
    #             printInteger(f(2, 2));
    #         }
    #     """
    #     except_str = ""
    #     self.assertTrue(TestChecker.test(input_str, except_str, 425))
        
    # def test_static27(self) :
    #     input_str = """
    #         a: integer;
    #         foo: function integer (p: boolean) {}
    #         bar: function integer () inherit foo {
    #             super();                                              // line 4
    #         }
    #     """
    #     except_str = "Type mismatch in expression: "
    #     self.assertTrue(TestChecker.test(input_str, except_str, 426))
        
    def test_static28(self) :
        input_str = """
            goo: function void(a: auto, a: auto) inherit foo{}
        """
        except_str = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input_str, except_str, 427))
    
    def test_static29(self) :
        input_str = """
        M: function void (a: integer) inherit N {
            super(a);
        } 
        N: function void (inherit a: integer) {}
        """
        except_str = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 428))
    
    def test_static30(self) :
        input_str = """
        M: function void (a: integer) inherit N {
            super(a);
        } 
        N: function void (inherit a: integer) {}
        """
        except_str = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 429))
        
    def test_static31(self) :
        input_str = """
        secondHighest : function array[5] of integer (salary : array[5] of integer) {
                result : array[5] of integer;
                i : integer;
                for (i = 0, i < 5, i + 1) {
                    if (salary[i] > 100) {
                        break;
                    }
                }
                return result;
            }
            main: function void () {
                salary : array [5] of integer = {1, 2, 3, 4, 5};
                secondHighest(salary);
            }
            """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 430))
        
    def test_static32(self) :
        input_str = """
         main: function void () {
            arr : array [10] of integer = {1, 2, {3, 4}, 5, 6};
         }
        """
        except_str = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(3), IntegerLit(4)]), IntegerLit(5), IntegerLit(6)])"
        self.assertTrue(TestChecker.test(input_str, except_str, 431))