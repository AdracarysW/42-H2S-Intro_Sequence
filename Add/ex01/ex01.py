#!/usr/bin/env python3

# List all the natural numbers below a certain number that are multiples of 3 or 5 and find the sum of those multiples.
# By awaraich

import sys

def function_a(num):
	var = 0
	sum = 0
	while var < num:
		if (var % 3 == 0):
			sum += var
		elif (var % 5 == 0):
			sum += var
		var += 1
	print(sum)

def function_b(num):
	var = 0
	sum = 0
	while var > num:
		if (var % 3 == 0):
			sum += var
		elif (var % 5 == 0):
			sum += var
		var -= 1
	print(sum)

def main():
    num = int(sys.argv[1])
    if (num >= 0):
        function_a(num)
    else:
        function_b(num)
    print("?>")
main()
