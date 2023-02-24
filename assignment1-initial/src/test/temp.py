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
        expected = "Error on line 1 col 25:"
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
