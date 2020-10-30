#!/usr/bin/env python

# A simple class encapsulating the pattern 
# functions form the previous questions

__author__ = "Jagadish Kumar P"
__email__ = "jagadish123@gmail.com"

class DrawPattern():

	def __init__(self):
		self.setRadius(15)
	
	def getRadius(self):
		return self.radius

	def setRadius(self, radius):
		self.radius = radius

	def printAnswer(self, pattern):
		print pattern

	def drawCircle(self):
		r = self.getRadius()
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
		self.printAnswer( drawPattern )
		return

	def drawRect(self):
		n = 10
		for x in range(n): print("#"*n) if not x%3 else ("#.."* (n/3) + "#")

if __name__ == '__main__':
	p = DrawPattern()
	print "Rectangle Pattern:"
	print "------------------"
	p.drawRect()
	print "----------------"
	print "Circle Pattern:"
	print "----------------"
	p.drawCircle()