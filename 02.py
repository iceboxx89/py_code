#!/usr/bin/env python

# Function to draw the patten from question 02

__author__ = "Jagadish Kumar P"
__email__ = "jagadish123@gmail.com"

def drawCircleBoundByRect(area):
	"""
	function to draw a circle bound by rectangle
	"""
	r = area
	diameter = 2*r+(r/2)
	drawPattern = ''
	for i in range(-((r/2)-2), diameter-1):
		for j in range(-((r/2)-2), diameter-1):
			xAxis = (i-r)
			yAxis = (j-r)
			if( (xAxis*xAxis) + (yAxis*yAxis) <= (r*r) ):
				drawPattern+='#'
			elif( ( (xAxis*xAxis) + (yAxis*yAxis)) >= ( (r*r)*1.5) ):
				drawPattern+='#'
			else:
				drawPattern+='.'
		drawPattern+='\n'
	print(drawPattern)
	return
if __name__ == '__main__':
	drawCircleBoundByRect(15)