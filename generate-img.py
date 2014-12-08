#!/usr/bin/env python
#
# converts the html file passed in as first command line argument into
# an image (specified as second argument)
#

#determines how the web page renders
ZOOM_FACTOR = 0.6
WINDOW_SIZE = (400, 700)
#determines the final crop & size of the image
IMAGE_SIZE = (380, 545)
IMAGE_STARTPOS = (-10, -25)

from PyQt4 import QtWebKit, QtGui, QtCore
import sys
import os

try:
	htmlPath = sys.argv[1]
	imgPath = sys.argv[2]
except IndexError:
	print >> sys.stderr, "Usage: generate-img.py html_path img_path"
	sys.exit()

app = QtGui.QApplication(sys.argv)
view = QtWebKit.QWebView()
view.setUrl(QtCore.QUrl("file://" + os.path.abspath(htmlPath)))
view.setZoomFactor(ZOOM_FACTOR)
view.resize(*WINDOW_SIZE)
@view.loadFinished.connect
def onLoad():
	pixmap = QtGui.QPixmap.grabWidget(view)
	pixmap2 = QtGui.QPixmap(*IMAGE_SIZE)
	painter = QtGui.QPainter(pixmap2)
	painter.drawPixmap(QtCore.QPoint(*IMAGE_STARTPOS), pixmap)
	painter.end()
	pixmap2.save(imgPath)
	app.quit()
app.exec_()
