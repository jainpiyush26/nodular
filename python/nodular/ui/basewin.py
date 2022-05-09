#!/usr/bin/env python
# std imports
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

# internal imports
from nodular.ui.graphicscene import NodularGraphicsScene
from nodular.ui.graphicsview import NodularGraphicsView


class NodularBase(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # defaults
        self.start_x = self.start_y = 200
        self.start_w = 800
        self.start_h = 600

        # initialize the window
        self.init_window()

    def init_window(self):
        """_summary_
        """
        # Set the basic geometry
        self.setGeometry(self.start_x, self.start_y, self.start_w,
        self.start_h)

        # Create the widget's layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # Set the graphics scene
        self.scene = NodularGraphicsScene()

        # Set the graphics view
        self.view = NodularGraphicsView(self.scene, self)
        
        self.layout.addWidget(self.view)
        # Set the window title
        self.setWindowTitle("Nodular")

        self.test_objects_add()

    def test_objects_add(self):

        _test_pen = QtGui.QPen(QtCore.Qt.GlobalColor.black)
        _test_pen.setWidth(2)

        rect = self.scene.addRect(-100,-100,50,80,_test_pen,
        QtGui.QColor(QtCore.Qt.GlobalColor.green))

        rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)


        test_wid_1 = QtWidgets.QWidget()
        test_layout = QtWidgets.QVBoxLayout()
        test_wid_1.setLayout(test_layout)
        test_wid_2 = QtWidgets.QPushButton("Hello There!")
        test_layout.addWidget(test_wid_2)
        proxy1 = self.scene.addWidget(test_wid_1, QtCore.Qt.Widget)
        proxy1.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

        text_box = self.scene.addText("This is a Test!")
        text_box.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable | QtWidgets.QGraphicsItem.ItemIsSelectable)

