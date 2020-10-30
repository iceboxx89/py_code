#!/usr/bin/env python

# Function to draw the patten from question 01

__author__ = "Jagadish Kumar P"
__email__ = "jagadish123@gmail.com"

def drawRect():
	n = 10
	for x in range(n): print("#"*n) if not x%3 else ("#.."* (n/3) + "#")

if __name__ == '__main__':
	drawRect()