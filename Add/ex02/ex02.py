#!/usr/bin/env python3

# This program prints the prime factors, in increasing order, of the number given as an argument.
# By awaraich

import sys

def function_a(v1):
	copy = v1
	i = 2
	if v1 == 0 or v1 == 1:
		print (v1)
	else:
		while i <= copy:
			if copy % i == 0:
				print(str(i)+",", end="")
				copy /= i
			else:
				i += 1

def main():
	v1 = int(sys.argv[1])
	function_a(v1)

main()
