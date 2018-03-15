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
		pass
	
	def argumentParser(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('--xlable', help)



##--------------------------------------

x = np.random.normal(size=10)
y = np.random.normal(size=10)
#print x
print ('\033[94m' + "... Hello ..." + '\033[0m')
pg.plot(x, y, symbol='o')  ## setting pen=None disables line drawing


## Start Qt event loop unless running in interactive mode or pyside
if __name__ == '__main__':
	import sys
	rospy.init_node("Visualize_Plots")
	if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
		pg.QtGui.QApplication.exec_() 

