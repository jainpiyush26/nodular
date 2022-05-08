#!/usr/bin/env python
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class NodularGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self._scene = scene
        
        self.setup_ui()

        self.setScene(self._scene)

    def setup_ui(self):

        # Setting up anti aliasing to avoid image or text artifacts
        self.setRenderHints(QtGui.QPainter.Antialiasing | \
            QtGui.QPainter.HighQualityAntialiasing | \
            QtGui.QPainter.TextAntialiasing | \
            QtGui.QPainter.SmoothPixmapTransform)
        # Setting up the viewport to stop overdrawing when we move the 
        # objects on the scene
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        # Disabling scroll bars (we will implement our own)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        # If we are clicking the middle mouse button
        if event.button() == QtCore.Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        else:
            # Else work as it is
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        # If we are clicking the middle mouse button
        if event.button() == QtCore.Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        else:
            # Else work as it is
            super().mouseReleaseEvent(event)

    def middleMouseButtonPress(self, event):
        release_event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease,
        event.localPos(), event.screenPos(), QtCore.Qt.LeftButton,
        QtCore.Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(release_event)

        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

        overld_event = QtGui.QMouseEvent(event.type(), event.localPos(),
        event.screenPos(), QtCore.Qt.LeftButton,
        event.buttons() | QtCore.Qt.LeftButton, event.modifiers())
        super().mousePressEvent(overld_event)
        
        

    def middleMouseButtonRelease(self, event):
        
        overld_event = QtGui.QMouseEvent(event.type(), event.localPos(),
        event.screenPos(), QtCore.Qt.LeftButton,
        event.buttons() & ~QtCore.Qt.LeftButton, event.modifiers())
        super().mouseReleaseEvent(overld_event)
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)