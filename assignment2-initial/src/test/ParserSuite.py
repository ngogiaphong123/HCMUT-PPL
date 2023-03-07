import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def testBkel1(self):
        """ Testcase from BKEL submission"""
        input_str = """delta: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 201))

    def testBkelTest2(self):
        """Testcase from BKEL submission"""
        input_str = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 202))

    def testBkelTest3(self):
        """Testcase from BKEL submission"""
        input_str = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input_str, expect, 203))

    def testBkelTest4(self):
        """Testcase from BKEL submission"""
        input_str = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 204))

    def testBkelTest5(self):
        """Testcase from BKEL submission"""
        input_str = """x: integer = 65;
         fact: function integer (n: integer) {
             if (n == 0) return 1;
             else return n * fact(n - 1);
         }
         inc: function void(out n: integer, delta: integer) {
             n = n + delta;
         }
         main: function void() {
             delta: integer = fact(3);
             inc(x, delta);
             printInteger(x);
         }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 205))

    def testParser6(self):
        """Testing variable declaration:"""
        input_str = """
        a : integer = 3;
        program: function void () {
            a, b, c: integer;
            d, e, f: float;
            g: boolean;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 206))

    def testParser7(self):
        """Testing variable declaration with initial values:"""
        input_str = """
            program: function void () {
                a: integer = 10;
                b: float = 3.14e-7;
                c: boolean = true;
                d , e : array[2] of integer = {1, 2}, {3, 4}, {2,1};
            }
        """
        expect = "Error on line 6 col 60: ,"
        self.assertTrue(TestParser.test(input_str, expect, 207))

    def testParser8(self):
        """Testing function declaration with parameter:"""
        input_str = """
            factorial: function integer (n: integer) {
                if (n == 0) return 1;
                else return n * factorial(n - 1);
            }
            n : integer = factorial(5);
            main : function void () {
                printInteger(n);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 208))

    def testParser9(self):
        """Testing special function in statement:"""
        input_str = """
            print_hello: function void () {
                printString("Hello world!");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 209))

    def testParser10(self):
        """Testing special function in expression:"""
        input_str = """
            readInt: function void () {
                a : integer = 2 + readInteger();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 210))

    def testParser11(self):
        """Testing if statement:"""
        input_str = """
            main: function void () {
                if (a == b) {
                    printString("a == b");
                }
                else {
                    printString("a != b");
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 211))

    def testParser12(self):
        """Testing if statement with no else statement:"""
        input_str = """
            main: function void () {
                if (a == b) {
                    printString("a == b");
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 212))

    def testParser13(self):
        """Testing if statement with no else statement:"""
        input_str = """
            program: function void () {
                for (i = 1, i <= 10, i + 1) {
                    preventDefault();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 213))

    def testParser14(self):
        """Testing return statement:"""
        input_str = """
            factorial: function integer (n: integer) {
                if ((n == 0) || (n==1)) return 1;
                else return n * factorial(n - 1);
            }

            program: function void () {
                a: integer = factorial(5);
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 214))

    def testParser15(self):
        input_str = """
        program: function void () {
            a: integer = 1;
            b: integer = 2;
            while (a <= 10) {
                b = b * 2;
                print(b);
                a = a + 1;
            }
            return;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 215))

    def testParser16(self):
        """Loop through array"""
        input_str = """program: function void() {
            a: integer = 1;
            b: integer = 2;
            c: integer = 3;
            d: integer = 4;
            e: integer = 5;
            arr: array [5] of integer = {a, b, c, d, e};
            for (i = 0, i < 5, 1) {
                if (arr[i] % 2 == 0) {
                    print("even");
                }
                else {
                    print("odd");
                }
            }
        }"""
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 216))

    def testParser17(self):
        """Testing break statement"""
        input_str = """program: function void() {
            for (i = 0, i < 10, 1) {
                if (i == 5) break;
            }
        }"""
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 217))

    def testParser18(self):
        """Quick sort"""
        input_string = """
        program: function void (arr: array [10] of integer, low: integer, high: integer) {
            if (low < high) {
                pi = partition(arr, low, high);
                sort(arr, low, pi - 1);
                sort(arr, pi + 1, high);
            }
        }

        partition: function integer (arr: array [10] of integer, low: integer, high: integer) {
            pivot = arr[high];
            i = low - 1;
            for (j = low, j < high, j + 1) {
                if (arr[j] < pivot) {
                    i = i + 1;
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
            temp = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = temp;
            return i + 1;
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_string, expected, 218))

    def testParser19(self):
        """Binary Search"""
        input_str = """
            binarySearch: function integer (arr: array [10] of integer, target: integer) {
                low = 0;
                high = 9;
                while (low <= high) {
                    mid = (low + high) / 2;
                    if (arr[mid] == target) {
                        return mid;
                    } else if (arr[mid] < target) {
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                return -1;
            }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 219))

    def testParser20(self):
        """Testing continue statement"""
        input_str = """program: function void() {
            for (i = 0, i < 10, 1) {
                if (i == 5) continue;
            }
        }"""
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 220))

    def testParser21(self):
        input = """
        // Assert that comment is not parsed
        /* Assert that comment is not parsed */
        main: function array[1] of boolean (cd: auto, temp: string) {
            a=c[d[e[s["string"]]]];
            b=b[1,2,,3];
            return b;
        }"""
        expect = "Error on line 6 col 20: ,"
        self.assertTrue(TestParser.test(input, expect, 221))

    def testParser22(self):
        input = """
        program: function void (arr: array [10] of integer, left: integer, right: integer) {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def testParser23(self):
        """Bubble sort"""
        input_str = """
        program: function void (arr: array [10] of integer) {
            n = 10;
            for (i = 0, i < n - 1, i + 1) {
                for (j = 0, j < n - i - 1, j + 1) {
                    if (arr[j] > arr[j + 1]) {
                        temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 223))

    def testParser24(self):
        """Testing for concatenation"""
        input_str = """program: function void() {
            a = "a" :: "b";
        }"""
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 224))

    def testParser25(self):
        """Testing for concatenation"""
        input_str = """program: function void() {
            a = ("a" :: "b") :: "c";
        }"""
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 225))

    def testParser26(self):
        """Testing for inheritance"""
        input_str = """
            multiply: function integer (x: integer, y: integer) {
                return x * y;
            }
            square: function integer (inherit out x: integer) {
                return x * x;
            }
            main: function void () inherit multiply {
                a = super(1212+2,31);
                b = square(a);
            }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 226))

    def testParser27(self):
        """Testing for inheritance"""
        input_str = """
            multiply: function integer (x: integer, y: integer) {
                return x * y;
            }
            square: function integer (inherit out x: integer) {
                return x * x;
            }
            main: function void () inherit multiply {
                a = super(1212+2,31);
                b = square(a);
            }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 227))

    def testParser28(self):
        input_str = """
        program: function void (arr: array [10] of integer) {
            n = 10;
            swapped = true;
            while (swapped) {
                swapped = false;
                for (i = 0, i < n - 1, i + 1) {
                    if (arr[i] > arr[i + 1]) {
                        temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                        swapped = true;
                    }
                }
            }
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 228))

    def testParser29(self):
        input_str = """
        program: function void () {
            a: array[3] of integer = {1, 2, 3};
            b: array[2,2] of integer = {{1, 2}, {3, 4}};
            c: array[4] of float;
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 229))

    def testParser30(self):
        input_str = """
        main: function void () {
            if (a > 10) {
                if (b > 10) {
                    printString("Both a and b are greater than 10");
                }
                else {
                    printString("Only a is greater than 10");
                }
            }
            else {
                printString("Neither a nor b is greater than 10");
            }
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 230))

    def testParser31(self):
        input_str = """
        main: function void () {
            if (a > 10) {
                if (b > 10) {
                    printFloat(1.2);
                }
                else {
                    readString();
                }
            }
            else {
                s = "Hello";
                printString(s);
            }
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 231))

    def testParser32(self):
        input_str = """
        main: function void () {
            algorithm = "binary tree traversal (inorder)";
            root : integer = parseTree("(3 (1 () (2)) (4 () (5)))");
            result : array[5] of integer = {};
            inorder(root, result);
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 232))

    def testParser33(self):
        input_str = """
        main: function integer () {
            n = parseNumber("5");
            result : integer = 1;
            for (i = 1, i <= n, i + 1) {
                result = result * i;
            }
            return result
        }
        """
        expected = "Error on line 9 col 8: }"
        self.assertTrue(TestParser.test(input_str, expected, 233))

    def testParser34(self):
        input_str = """
        main: function integer () {
            n = parseNumber("5");
            result : integer = 1;
            for (i = 1, i <= n, i + 1) {
                result = result * i;
            }
            return result;
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 234))

    def testParser35(self):
        input_str = """
            main : function void() {
                if (b >= 2.0 && b <= 3.0) {
                    printf("b is between 2.0 and 3.0, inclusive.\\n");
                } else {
                    printf("b is not between 2.0 and 3.0, inclusive.\\n");
                }
            }
        """
        expected = "Error on line 3 col 34: <="
        self.assertTrue(TestParser.test(input_str, expected, 235))

    def testParser36(self):
        input_str = """
            main : function void() {
                if ((b >= 2.0) && (b <= 3.0)) {
                    printf("b is between 2.0 and 3.0, inclusive.\\n");
                } else {
                    printf("b is not between 2.0 and 3.0, inclusive.\\n");
                }
            }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 236))

    def testParser37(self):
        """Empty program"""
        input_str = """"""
        expected = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input_str, expected, 237))

    def testParser38(self):
        """Empty program"""
        input_str = """
            main : function void() {
                return ;;
            }
        """
        expected = "Error on line 3 col 24: ;"
        self.assertTrue(TestParser.test(input_str, expected, 238))

    def testParser39(self):
        """Call function outside function"""
        input_str = """
        printString("hello");
        }"""
        expect = "Error on line 2 col 8: printString"
        self.assertTrue(TestParser.test(input_str, expect, 239))

    def testParser40(self):
        """For outside function"""
        input_str = """
            for (i = 0, i < 10, i + 1) {
                printString("hello");
            }
        """
        expect = "Error on line 2 col 12: for"
        self.assertTrue(TestParser.test(input_str, expect, 240))

    def testParser41(self):
        """If outside function"""
        input_str = """
            if (a > 10) {
                printString("hello");
            }
        """
        expect = "Error on line 2 col 12: if"
        self.assertTrue(TestParser.test(input_str, expect, 241))

    def testParser42(self):
        """While outside function"""
        input_str = """
            while (a > 10) {
                printString("hello");
            }
        """
        expect = "Error on line 2 col 12: while"
        self.assertTrue(TestParser.test(input_str, expect, 242))

    def testParser43(self):
        """Empty function"""
        input_str = """
            main : function void() {
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 243))

    def testParser44(self):
        """Matrix"""
        input_str = """
            main : function void() {
                a : array[6,6] of integer = 
                {{1, 2, 3, 4, 5, 6},
                {7, 8, 9, 10, 11, 12},
                {13, 14, 15, 16, 17, 18},
                {19, 20, 21, 22, 23, 24},
                {25, 26, 27, 28, 29, 30},
                {31, 32, 33, 34, 35, 36}};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_str, expect, 244))

    def testParser45(self):
        input_str = """
        main: function void () {
            x = 10;
            y = 20;
            z = x + y * 2;
            printInt(z);
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 245))

    def testParser46(self):
        input_str = """
        main: function void () {
            s = "Hello\\tworld!\\nThis is a\\nnew line.";
            printString(s);
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 246))

    def testParser47(self):
        input_str = """
        main: function void () {
            s = "This is a string\\nwith\\t\\\"escape characters\\\".";
            printString(s);
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 247))

    def testParser48(self):
        input_str = """
        main: function void () {
            s = "The path to the file is C:\\\\folder1\\\\file.txt";
            printString(s);
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 248))

    def testParser49(self):
        input_str = """main: function void () {};"""
        expected = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.test(input_str, expected, 249))

    def testParser50(self):
        input_str = """
        main: function void () {
            if (x > 0) {
                printString("x is positive!");
        }
        """
        expected = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input_str, expected, 250))

    def testParser51(self):
        """Function double array elements"""
        input_str = """
         double : function array[5] of integer (input : array[5] of integer) {
             for (i = 0, i < 5, i + 1) {
                 input[i] = input[i] * 2;
             }
             return input;
         }
         main: function void () {
             a : array[5] of integer = {1, 2, 3, 4, 5};
             a = double(a);
             for (i = 0, i < 5, i + 1) {
                 printInt(a[i]);
             }
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 251))

    def testParser52(self):
        """isPrime function"""
        input_str = """
         isPrime : function boolean (n : integer) {
             if (n <= 1) {
                 return false;
             }
             for (i = 2, i < n, i + 1) {
                 if (n % i == 0) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             n = 10;
             if (isPrime(n)) {
                 printString("n is a prime number.");
             } else {
                 printString("n is not a prime number.");
             }
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 252))

    def testParser53(self):
        """is Palindrome function"""
        input_str = """
         isPalindrome : function boolean (s : string) {
             for (i = 0, i < length(s) / 2, i + 1) {
                 if (s[i] != s[length(s) - i - 1]) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             s = "racecar";
             if (isPalindrome(s)) {
                 printString("s is a palindrome.");
             } else {
                 printString("s is not a palindrome.");
             }
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 253))

    def testParser54(self):
        """Reverse string function"""
        input_str = """
         reverse : function string (s : string) {
             result = "";
             for (i = length(s) - 1, i >= 0, i - 1) {
                 result = result + s[i];
             }
             return result;
         }
         main: function void () {
             s = "Hello world!";
             printString(reverse(s));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 254))

    def testParser55(self):
        """Reverse int function"""
        input_str = """
         reverse : function integer (n : integer) {
             result = 0;
             while (n > 0) {
                 result = result * 10 + n % 10;
                 n = n / 10;
             }
             return result;
         }
         main: function void () {
             n = 12345;
             printInt(reverse(n));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 255))

    def testParser56(self):
        """Search insert position function"""
        input_str = """
         searchInsert : function integer (nums : array[5] of integer, target : integer) {
             for (i = 0, i < length(nums), i + 1) {
                 if (nums[i] >= target) {
                     return i;
                 }
             }
             return length(nums);
         }
         main: function void () {
             nums = {1, 3, 5, 6};
             target = 5;
             printInt(searchInsert(nums, target));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 256))

    def testParser57(self):
        """Remove duplicates function"""
        input_str = """
         removeDuplicates : function integer (nums : array[5] of integer) {
             if (length(nums) == 0) {
                 return 0;
             }
             i = 0;
             for (j = 1, j < length(nums), j + 1) {
                 if (nums[j] != nums[i]) {
                     i = i + 1;
                     nums[i] = nums[j];
                 }
             }
             return i + 1;
         }
         main: function void () {
             nums = {1, 1, 2};
             printInt(removeDuplicates(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 257))

    def testParser58(self):
        input_str = """
        main: function integer() {
            arr: array[5] of integer = {3, 7, 9, 2, 4};
            target: integer = 9;
            n: integer = 5;
            found: boolean = false;
            index: integer = -1;
            for (i = 0, i < n, i + 1) {
                if (arr[i] == target) {
                    found = true;
                    index = i;
                    break;
                }
            }
            if (found) {
                return index;
            }
            else {
                return -1;
            }
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 258))

    def testParser59(self):
        input_str = """
        main: function void () {
            if (x > 0) {
                printString("x is positive!");
            }
            else if (x < 0) {
                printString("x is negative!");
            }
            else {
                printString("x is zero!");
            }
        }
        """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 259))

    def testParser60(self):
        """is Armstrong number function"""
        input_str = """
         isArmstrong : function boolean (n : integer) {
             sum = 0;
             temp = n;
             while (temp > 0) {
                 digit = temp % 10;
                 sum = sum + digit * digit * digit;
                 temp = temp / 10;
             }
             if (sum == n) {
                 return true;
             } else {
                 return false;
             }
         }
         main: function void () {
             n = 153;
             if (isArmstrong(n)) {
                 printString("n is an Armstrong number.");
             } else {
                 printString("n is not an Armstrong number.");
             }
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 260))

    def testParser61(self):
        """is anaGram function"""
        input_str = """
         isAnaGram : function boolean (s1 : string, s2 : string) {
             if (length(s1) != length(s2)) {
                 return false;
             }
             for (i = 0, i < length(s1), i + 1) {
                 if (s1[i] != s2[length(s2) - i - 1]) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             s1 = "racecar";
             s2 = "racecar";
             if (isAnaGram(s1, s2)) {
                 printString("s1 and s2 are anagrams.");
             } else {
                 printString("s1 and s2 are not anagrams.");
             }
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 261))

    def testParser62(self):
        """Lowest Common Ancestor function"""
        input_str = """
         lowestCommonAncestor : function integer (root : integer, p : integer, q : integer) {
             if ((p < root) && (q < root)) {
                 return lowestCommonAncestor(rootLeft, p, q);
             } else if ((p > root) && (q > root)) {
                 return lowestCommonAncestor(rootRight, p, q);
             } else {
                 return root;
             }
         }
         main: function void () {
             root = 6;
             p = 2;
             q = 8;
             printInt(lowestCommonAncestor(root, p, q));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 262))

    def testParser63(self):
        """Sum of left leaves function"""
        input_str = """
         sumOfLeftLeaves : function integer (root : integer) {
             if (root == null) {
                 return 0;
             }
             if ((rootLeft != null) && (rootLeftLeft == null) && (rootLeftRight == null)) {
                 return rootLeftVal + sumOfLeftLeaves(rootRight);
             }
             return sumOfLeftLeaves(rootLeft) + sumOfLeftLeaves(rootRight);
         }
         main: function void () {
             root = 3;
             printInt(sumOfLeftLeaves(root));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 263))

    def testParser64(self):
        """Next Greater Element function"""
        input_str = """
         nextGreaterElement : function integer (nums1 : array[4] of integer, nums2 : array[4] of integer) {
             for (i = 0, i < length(nums1), i + 1) {
                 found = false;
                 for (j = 0, j < length(nums2), j + 1) {
                     if (nums1[i] == nums2[j]) {
                         found = true;
                     }
                     if (found && (nums2[j] > nums1[i])) {
                         return nums2[j];
                     }
                 }
             }
             return -1;
         }
         main: function void () {
             nums1 = {4, 1, 2};
             nums2 = {1, 3, 4, 2};
             printInt(nextGreaterElement(nums1, nums2));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 264))

    def testParser65(self):
        """Reverse Linked List function"""
        input_str = """
         reverseList : function integer (head : integer) {
             prev = null;
             curr = head;
             while (curr != null) {
                 nextTemp = currNext;
                 currNext = prev;
                 prev = curr;
                 curr = nextTemp;
             }
             return prev;
         }
         main: function void () {
             head = 1;
             printInt(reverseList(head));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 265))

    def testParser66(self):
        """Sort Colors function"""
        input_str = """
         sortColors : function void (nums : array[4] of integer) {
             red = 0;
             white = 0;
             blue = 0;
             for (i = 0, i < length(nums), i + 1) {
                 if (nums[i] == 0) {
                     red = red + 1;
                 } else if (nums[i] == 1) {
                     white = white + 1;
                 } else {
                     blue = blue + 1;
                 }
             }
             for (i = 0, i < red, i + 1) {
                 nums[i] = 0;
             }
             for (i = red, i < red + white, i + 1) {
                 nums[i] = 1;
             }
             for (i = red + white, i < length(nums), i + 1) {
                 nums[i] = 2;
             }
         }
         main: function void () {
             nums = {2, 0, 2, 1, 1, 0};
             sortColors(nums);
             printInt(nums);
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 266))

    def testParser67(self):
        """Valid Parentheses function"""
        input_str = """
         isValid : function boolean (s : string) {
             if (length(s) % 2 != 0) {
                 return false;
             }
             for (i = 0, i < length(s), i + 1) {
                 if (s[i] == "(") {
                     push(s[i]);
                 } else if (s[i] == ")") {
                     if (top() == "(") {
                         pop();
                     } else {
                         return false;
                     }
                 }
             }
             if (isEmpty()) {
                 return true;
             } else {
                 return false;
             }
         }
         main: function void () {
             s = "((()))";
             if (isValid(s)) {
                 printString("s is valid.");
             } else {
                 printString("s is not valid.");
             }
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 267))

    def testParser68(self):
        """Square Root function"""
        input_str = """
         sqrt : function float (x : float) {
             if (x == 0) {
                 return 0;
             }
             if (x < 0) {
                 return -1;
             }
             left = 1;
             right = x;
             while (left <= right) {
                 mid = (left + right) / 2;
                 if (mid * mid == x) {
                     return mid;
                 } else if (mid * mid < x) {
                     left = mid + 1;
                 } else {
                     right = mid - 1;
                 }
             }
             return right;
         }
         main: function void () {
             x = 8;
             printFloat(sqrt(x));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 268))

    def testParser69(self):
        """Climate Change function"""
        input_str = """
         climateChange : function void (arr : array[4] of integer) {
             n = length(arr);
             for (i = 0, i < n - 1, i + 1) {
                 for (j = 0, j < n - i - 1, j + 1) {
                     if (arr[j] > arr[j + 1]) {
                         temp = arr[j];
                         arr[j] = arr[j + 1];
                         arr[j + 1] = temp;
                     }
                 }
             }
         }
         main: function void () {
             arr = {64, 34, 25, 12, 22, 11, 90};
             climateChange(arr);
             printInt(arr);
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 269))

    def testParser70(self):
        """Climbing Stairs function"""
        input_str = """
         climbStairs : function integer (n : integer) {
             if (n == 1) {
                 return 1;
             }
             first = 1;
             second = 2;
             for (i = 3, i <= n, i + 1) {
                 third = first + second;
                 first = second;
                 second = third;
             }
             return second;
         }
         main: function void () {
             n = 4;
             printInt(climbStairs(n));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 270))

    def testParser71(self):
        """Coin Change function"""
        input_str = """
         coinChange : function integer (coins : array[4] of integer, amount : integer) {
             if (amount == 0) {
                 return 0;
             }
             if (amount < 0) {
                 return -1;
             }
             min = 999999999;
             for (i = 0, i < length(coins), i + 1) {
                 res = coinChange(coins, amount - coins[i]);
                 if ((res != -1) && (res < min)) {
                     min = res + 1;
                 }
             }
             if (min == 999999999) {
                 return -1;
             } else {
                 return min;
             }
         }
         main: function void () {
             coins = {1, 2, 5};
             amount = 11;
             printInt(coinChange(coins, amount));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 271))

    def testParser72(self):
        """Coin Change 2 function"""
        input_str = """
         change : function integer (amount : integer, coins : array[4] of integer) {
             dp : array[5] of integer;
             dp[0] = 1;
             for (i = 0, i < length(coins), i + 1) {
                 for (j = coins[i], j <= amount, j + 1) {
                     dp[j] = dp[j] + dp[j - coins[i]];
                 }
             }
             return dp[amount];
         }
         main: function void () {
             amount = 5;
             coins = {1, 2, 5};
             printInt(change(amount, coins));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 272))

    def testParser73(self):
        """Count Primes function"""
        input_str = """
         countPrimes : function integer (n : integer) {
             if (n < 2) {
                 return 0;
             }
             count = 0;
             for (i = 2, i < n, i + 1) {
                 if (isPrime(i)) {
                     count = count + 1;
                 }
             }
             return count;
         }
         isPrime : function boolean (n : integer) {
             if (n < 2) {
                 return false;
             }
             for (i = 2, i * i <= n, i + 1) {
                 if (n % i == 0) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             n = 10;
             printInt(countPrimes(n));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 273))

    def testParser74(self):
        """Decode Ways function"""
        input_str = """
         numDecodings : function integer (s : string) {
             if (s == "") {
                 return 0;
             }
             n = length(s);
             dp : array[6] of integer;
             dp[0] = 1;
             dp[1] = 1;
             for (i = 2, i <= n, i + 1) {
                 if (s[i - 1] != "0") {
                     dp[i] = dp[i - 1];
                 }
                 if ((s[i - 2] == "1") || ((s[i - 2] == "2") && (s[i - 1] < "7"))) {
                     dp[i] = dp[i] + dp[i - 2];
                 }
             }
             return dp[n];
         }
         main: function void () {
             s = "226";
             printInt(numDecodings(s));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 274))

    def testParser75(self):
        """Find the index of the first occurrence of a substring function"""
        input_str = """
         find : function integer (str : string, sub : string) {
             for (i = 0, i < length(str), i + 1) {
                 for (j = 0, j < length(sub), j + 1) {
                     if (str[i + j] != sub[j]) {
                         break;
                     }
                 }
                 if (j == length(sub)) {
                     return i;
                 }
             }
             return -1;
         }
         main: function void () {
             str = "Hello World!";
             sub = "World";
             printInt(find(str, sub));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 275))

    def testParser76(self):
        """Find the index of the last occurrence of a substring function"""
        input_str = """
         find : function integer (str : string, sub : string) {
             for (i = length(str) - 1, i >= 0, i - 1) {
                 for (j = 0, j < length(sub), j + 1) {
                     if (str[i + j] != sub[j]) {
                         break;
                     }
                 }
                 if (j == length(sub)) {
                     return i;
                 }
             }
             return -1;
         }
         main: function void () {
             str = "Hello World!";
             sub = "World";
             printInt(find(str, sub));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 276))

    def testParser77(self):
        """Put the first letter of each word in uppercase function"""
        input_str = """
         capitalize : function string (str : string) {
             str[0] = toUpper(str[0]);
             for (i = 1, i < length(str), i + 1) {
                 if (str[i - 1] == " ") {
                     str[i] = toUpper(str[i]);
                 }
             }
             return str;
         }
         main: function void () {
             str = "hello world!";
             printStr(capitalize(str));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 277))

    def testParser78(self):
        """Plus One function"""
        input_str = """
         plusOne : function array[4] of integer (digits : array[4] of integer) {
             n = length(digits);
             for (i = n - 1, i >= 0, i - 1) {
                 if (digits[i] < 9) {
                     digits[i] = digits[i] + 1;
                     return digits;
                 }
                 digits[i] = 0;
             }
             digits = {1};
             for (i = 1, i < n, i + 1) {
                 digits[i] = 0;
             }
             return digits;
         }
         main: function void () {
             digits = {1, 2, 3};
             printInt(plusOne(digits));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 278))

    def testParser79(self):
        """Find the first non-repeating character function"""
        input_str = """
         firstNonRepeating : function string (str : string) {
             for (i = 0, i < length(str), i + 1) {
                 found = false;
                 for (j = 0, j < length(str), j + 1) {
                     if ((i != j) && (str[i] == str[j])) {
                         found = true;
                         break;
                     }
                 }
                 if (!found) {
                     return str[i];
                 }
             }
             return "";
         }
         main: function void () {
             str = "Hello World!";
             printStr(firstNonRepeating(str));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 279))

    def testParser80(self):
        """Single Number function"""
        input_str = """
         singleNumber : function integer (nums : array[6] of integer) {
             result = 0;
             for (i = 0, i < length(nums), i + 1) {
                 result = result * nums[i];
             }
             return result;
         }
         main: function void () {
             nums = {2, 2, 1};
             printInt(singleNumber(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 280))

    def testParser81(self):
        """Find Peak Element function"""
        input_str = """
         findPeakElement : function integer (nums : array[6] of integer) {
             n = length(nums);
             if (n == 1) {
                 return 0;
             }
             if (nums[0] > nums[1]) {
                 return 0;
             }
             if (nums[n - 1] > nums[n - 2]) {
                 return n - 1;
             }
             for (i = 1, i < n - 1, i + 1) {
                 if ((nums[i] > nums[i - 1]) && (nums[i] > nums[i + 1])) {
                     return i;
                 }
             }
             return -1;
         }
         main: function void () {
             nums = {1, 2, 3, 1};
             printInt(findPeakElement(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 281))

    def testParser82(self):
        """Rotate Array function"""
        input_str = """
         rotate : function void (nums : array[7] of integer, k : integer) {
             n = length(nums);
             k = k % n;
             if (k == 0) {
                 return;
             }
             reverse(nums, 0, n - 1);
             reverse(nums, 0, k - 1);
             reverse(nums, k, n - 1);
         }
         main: function void () {
             nums = {1, 2, 3, 4, 5, 6, 7};
             k = 3;
             rotate(nums, k);
             printInt(nums);
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 282))

    def testParser83(self):
        """Majority Element function"""
        input_str = """
         majorityElement : function integer (nums : array[7] of integer) {
             n = length(nums);
             count = 0;
             for (i = 0, i < n, i + 1) {
                 if (count == 0) {
                     candidate = nums[i];
                 }
                 if (nums[i] == candidate) {
                     count = count + 1;
                 } else {
                     count = count - 1;
                 }
             }
             return candidate;
         }
         main: function void () {
             nums = {2, 2, 1, 1, 1, 2, 2};
             printInt(majorityElement(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 283))

    def testParser84(self):
        """Contains Duplicate function"""
        input_str = """
         containsDuplicate : function boolean (nums : array[5] of integer) {
             n = length(nums);
             for (i = 0, i < n, i + 1) {
                 for (j = i + 1, j < n, j + 1) {
                     if (nums[i] == nums[j]) {
                         return true;
                     }
                 }
             }
             return false;
         }
         main: function void () {
             nums = {1, 2, 3, 1};
             printBool(containsDuplicate(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 284))

    def testParser85(self):
        """Two Sum function"""
        input_str = """
         twoSum : function array[2] of integer (nums : array[4] of integer, target : integer) {
             n = length(nums);
             for (i = 0, i < n, i + 1) {
                 for (j = i + 1, j < n, j + 1) {
                     if (nums[i] + nums[j] == target) {
                         return {i, j};
                     }
                 }
             }
             return {-1, -1};
         }
         main: function void () {
             nums = {2, 7, 11, 15};
             target = 9;
             printInt(twoSum(nums, target));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 285))

    def testParser86(self):
        """Missing Number function"""
        input_str = """
         missingNumber : function integer (nums : array[4] of integer) {
             n = length(nums);
             sum = 0;
             for (i = 0, i < n, i + 1) {
                 sum = sum + nums[i];
             }
             return (n * (n + 1)) / 2 - sum;
         }
         main: function void () {
             nums = {3, 0, 1};
             printInt(missingNumber(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 286))

    def testParser87(self):
        """Intersection of Two Arrays II function"""
        input_str = """
         intersect : function array[2] of integer (nums1 : array[4] of integer, nums2 : array[2] of integer) {
             n1 = length(nums1);
             n2 = length(nums2);
             result : array [2] of integer= {};
             for (i = 0, i < n1, i + 1) {
                 for (j = 0, j < n2, j + 1) {
                     if (nums1[i] == nums2[j]) {
                         result = append(result, nums1[i]);
                         nums2[j] = -1;
                         break;
                     }
                 }
             }
             return result;
         }
         main: function void () {
             nums1 = {1, 2, 2, 1};
             nums2 = {2, 2};
             printInt(intersect(nums1, nums2));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 287))

    def testParser88(self):
        """Find All Numbers Disappeared in an Array function"""
        input_str = """
         findDisappearedNumbers : function array[2] of integer (nums : array[4] of integer) {
             n = length(nums);
             result : array [2] of integer= {};
             for (i = 0, i < n, i + 1) {
                 index = abs(nums[i]) - 1;
                 if (nums[index] > 0) {
                     nums[index] = -nums[index];
                 }
             }
             for (i = 0, i < n, i + 1) {
                 if (nums[i] > 0) {
                     result = append(result, i + 1);
                 }
             }
             return result;
         }
         main: function void () {
             nums = {4, 3, 2, 7, 8, 2, 3, 1};
             printInt(findDisappearedNumbers(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 288))

    def testParser89(self):
        """Find All Duplicates in an Array function"""
        input_str = """
         findDuplicates : function array[2] of integer (nums : array[8] of integer) {
             n = length(nums);
             result : array [2] of integer= {};
             for (i = 0, i < n, i + 1) {
                 index = abs(nums[i]) - 1;
                 if (nums[index] < 0) {
                     result = append(result, abs(nums[i]));
                 }
                 nums[index] = -nums[index];
             }
             return result;
         }
         main: function void () {
             nums = {4, 3, 2, 7, 8, 2, 3, 1};
             printInt(findDuplicates(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 289))

    def testParser90(self):
        """Isomorphic Strings function"""
        input_str = """
         isIsomorphic : function boolean (s : string, t : string) {
             n = length(s);
             if (n != length(t)) {
                 return false;
             }
             map : array [256] of integer= {};
             for (i = 0, i < n, i + 1) {
                 if (map[s[i]] == 0) {
                     map[s[i]] = t[i];
                 } else {
                     if (map[s[i]] != t[i]) {
                         return false;
                     }
                 }
             }
             return true;
         }
         main: function void () {
             s = "egg";
             t = "add";
             printBool(isIsomorphic(s, t));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 290))

    def testParser91(self):
        """Is Subsequence function"""
        input_str = """
         isSubsequence : function boolean (s : string, t : string) {
             n = length(s);
             m = length(t);
             i = 0;
             j = 0;
             while ((i < n) && (j < m)) {
                 if (s[i] == t[j]) {
                     i = i + 1;
                 }
                 j = j + 1;
             }
             return i == n;
         }
         main: function void () {
             s = "abc";
             t = "ahbgdc";
             printBool(isSubsequence(s, t));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 291))

    def testParser92(self):
        """Find the Difference function"""
        input_str = """
         findTheDifference : function string (s : string, t : string) {
             n = length(s);
             m = length(t);
             sum = 0;
             for (i = 0, i < n, i + 1) {
                 sum = sum + ord(s[i]);
             }
             for (i = 0, i < m, i + 1) {
                 sum = sum - ord(t[i]);
             }
             return chr(-sum);
         }
         main: function void () {
             s = "abcd";
             t = "abcde";
             printString(findTheDifference(s, t));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 292))

    def testParser93(self):
        """Find the Duplicate Number function"""
        input_str = """
         findDuplicate : function integer (nums : array[5] of integer) {
             n = length(nums);
             slow = nums[0];
             fast = nums[nums[0]];
             while (slow != fast) {
                 slow = nums[slow];
                 fast = nums[nums[fast]];
             }
             fast = 0;
             while (slow != fast) {
                 slow = nums[slow];
                 fast = nums[fast];
             }
             return slow;
         }
         main: function void () {
             nums = {1, 3, 4, 2, 2};
             printInt(findDuplicate(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 293))

    def testParser94(self):
        """Find the Celebrity function"""
        input_str = """
         findCelebrity : function integer (n : integer) {
             candidate = 0;
             for (i = 1, i < n, i + 1) {
                 if (knows(candidate, i)) {
                     candidate = i;
                 }
             }
             for (i = 0, i < n, i + 1) {
                 if ((i != candidate) && ((knows(candidate, i)) || (!knows(i, candidate)))) {
                     return -1;
                 }
             }
             return candidate;
         }
         main: function void () {
             n = 2;
             printInt(findCelebrity(n));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 294))

    def testParser95(self):
        """3 Sum function"""
        input_str = """
         threeSum : function array[2] of integer (nums : array[6] of integer) {
             n = length(nums);
             sort(nums);
             result : array [2] of integer= {};
             for (i = 0, i < n, i + 1) {
                 if ((i > 0) && (nums[i] == nums[i - 1])) {
                     continue;
                 }
                 target : integer = -nums[i];
                 left : integer = i + 1;
                 right : integer = n - 1;
                 while (left < right) {
                     if ((nums[left] + nums[right]) == target) {
                         result = append(result, {nums[i], nums[left], nums[right]});
                         left = left + 1;
                         while ((left < right) && (nums[left] == nums[left - 1])) {
                             left = left + 1;
                         }
                         right = right - 1;
                         while ((left < right) && (nums[right] == nums[right + 1])) {
                             right = right - 1;
                         }
                     } else {
                         if ((nums[left] + nums[right]) < target) {
                             left = left + 1;
                         } else {
                             right = right - 1;
                         }
                     }
                 }
             }
             return result;
         }
         main: function void () {
             nums = {-1, 0, 1, 2, -1, -4};
             printInt(threeSum(nums));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 295))

    def testParser96(self):
        """Roman to Integer function"""
        input_str = """
         romanToInt : function integer (s : string) {
             n = length(s);
             result = 0;
             for (i = 0, i < n, i + 1) {
                 if ((i > 0) && (roman[s[i]] > roman[s[i - 1]])) {
                     result = result + roman[s[i]] - 2 * roman[s[i - 1]];
                 } else {
                     result = result + roman[s[i]];
                 }
             }
             return result;
         }
         main: function void () {
             s = "MCMXCIV";
             printInt(romanToInt(s));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 296))

    def testParser97(self):
        """Length of Last Word function"""
        input_str = """
         lengthOfLastWord : function integer (s : string) {
             n : integer = length(s);
             result : integer = 0;
             for (i = n - 1, i >= 0, i - 1) {
                 if (s[i] != " ") {
                     result = result + 1;
                 } else {
                     if (result > 0) {
                         break;
                     }
                 }
             }
             return result;
         }
         main: function void () {
             s = "Hello World";
             printInt(lengthOfLastWord(s));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 297))

    def testParser98(self):
        """Reverse Words in a String function"""
        input_str = """
         reverseWords : function string (s : string) {
             n : integer = length(s);
             result : integer = "";
             i : integer = 0;
             while (i < n) {
                 while ((i < n) && (s[i] == " ")) {
                     i = i + 1;
                 }
                 if (i >= n) {
                     break;
                 }
                 start = i;
                 while ((i < n) && (s[i] != " ")) {
                     i = i + 1;
                 }
                 sub = substring(s, start, i - start);
                 if (result == "") {
                     result = sub;
                 } else {
                     result = sub + " " + result;
                 }
             }
             return result;
         }
         main: function void () {
             s = "the sky is blue";
             printString(reverseWords(s));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 298))

    def testParser99(self):
        """Move Zeroes function"""
        input_str = """
         moveZeroes : function void (nums : array[5] of integer) {
             n = length(nums);
             lastNonZeroFoundAt = 0;
             for (i = 0, i < n, i + 1) {
                 if (nums[i] != 0) {
                     nums[lastNonZeroFoundAt] = nums[i];
                     lastNonZeroFoundAt = lastNonZeroFoundAt + 1;
                 }
             }
             for (i = lastNonZeroFoundAt, i < n, i + 1) {
                 nums[i] = 0;
             }
         }
         main: function void () {
             nums = {0, 1, 0, 3, 12};
             moveZeroes(nums);
             printInt(nums);
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 299))

    def testParser100(self):
        """islandPerimeter function"""
        input_str = """
         islandPerimeter : function integer (grid : array[4,4] of integer) {
             n : integer = length(grid);
             m : integer = length(grid[0]);
             result : integer = 0;
             for (i = 0, i < n, i + 1) {
                 for (j = 0, j < m, j + 1) {
                     if (grid[i,j] == 1) {
                         result = result + 4;
                         if ((i > 0) && (grid[i - 1,j] == 1)) {
                             result = result - 2;
                         }
                         if ((j > 0) && (grid[i,j - 1] == 1)) {
                             result = result - 2;
                         }
                     }
                 }
             }
             return result;
         }
         main: function void () {
             grid : array [4,4] of integer = {{0, 1, 0, 0},
                     {1, 1, 1, 0},
                     {0, 1, 0, 0},
                     {1, 1, 0, 0}};
             printInt(islandPerimeter(grid));
         }
         """
        expected = "successful"
        self.assertTrue(TestParser.test(input_str, expected, 300))