#!/usr/bin/env python3

# Takes in two numbers as command line arguments and performs functions, using the two arguments.
# By awaraich

import sys

def function_a(num1, num2):
        print("{} divided by {} equals {} remainder {}".format(num1, num2, num1//num2, num1%num2))

def function_b():
        a = 10
        b = 56.99
        c = complex(2, 3)
        print("Variable a contains: {} which is of type: {}".format(a, str.title(a.__class__.__name__)))
        print("Variable b contains: {} which is of type: {}".format(b, str.title(b.__class__.__name__)))
        print("Variable c contains: {} which is of type: {}".format(c, str.title(c.__class__.__name__)))


def main():
        var1 = int(sys.argv[1])
        var2 = int(sys.argv[2])
        function_a(var1, var2)
        function_b()

main()
