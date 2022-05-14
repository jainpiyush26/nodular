#!/usr/bin/env python
# std imports
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

# internal imports
from nodular.ui.graphicsscene import NodularGraphicsScene
from nodular.ui.graphicsview import NodularGraphicsView
from nodular.ui.graphicsnode import TextNodularGraphicsNode


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
        self.view = NodularGraphicsView(self.scene.nodular_scene,
        self)
        
        self.layout.addWidget(self.view)
        # Set the window title
        self.setWindowTitle("Nodular")

        # add the nodes here!
        self.add_nodes()
    
    def add_nodes(self):
        node = TextNodularGraphicsNode(self.scene, "First Node")

