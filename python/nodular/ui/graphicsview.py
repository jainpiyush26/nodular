#!/usr/bin/env python
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class NodularGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self._scene = scene
        
        self.setScene(self._scene)