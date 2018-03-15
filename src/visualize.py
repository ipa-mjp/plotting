#!/usr/bin/python
import rospy

import argparse
from datetime import datetime

import pyqtgraph as pg
import numpy as np

#---------------------------------------

class Plotting():
	# Constractor
	def __init__(self):
		self.xlable = ""
		self.ylable = ""
		self.title = ""
	
	def argumentParser(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('--xlable', help='plot x-axis lable')
		parser.add_argument('--zlable', help='plot y-axis lable')
		parser.add_argument('--title', help='plot title')
		args, unknown = parser.parse_known_args()
		
		rospy.spin()
		
		self.xlable = rospy.get_param('~xlable')
		self.ylable = rospy.get_param('~ylable')
		self.title = rospy.get_param('~title')
		
		## Defualt lable setting
		if args.xlable is None:
			self.xlable = "time in s"
		if self.ylable is None:
			self.ylable = "Value"
		if self.title is None:
			self.title = self.ylable + "Vs" + self.xlable
					
	def RunScript(self):
		print ('\033[94m' + "... Running scripting ..." + '\033[0m')
		self.argumentParser()
		x = np.random.normal(size=10)
		y = np.random.normal(size=10)
		print ('\033[94m' + "... plotting ..." + '\033[0m')
		pg.plot(x, y, symbol='o')  ## setting pen=None disables line drawing
				
			
##--------------------------------------

## Start Qt event loop unless running in interactive mode or pyside
if __name__ == '__main__':
	import sys
	rospy.init_node("Visualize_Plots")
	SCRIPT = Plotting()
	SCRIPT.RunScript()
	if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
		pg.QtGui.QApplication.exec_() 

