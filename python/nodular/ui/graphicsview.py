#!/usr/bin/env python
# std imports
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

# internal imports
from nodular.ui.constants import *

class NodularGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self._scene = scene

        self.setup_ui()

        self.setScene(self._scene)
        self.zoomvalue = 0

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
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        # If we are clicking the middle mouse button
        if event.button() == QtCore.Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == QtCore.Qt.LeftButton:
            self.leftMouseButtonPress(event)
        elif event.button() == QtCore.Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            # Else work as it is
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        # If we are clicking the middle mouse button
        if event.button() == QtCore.Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == QtCore.Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == QtCore.Qt.RightButton:
            self.rightMouseButtonRelease(event)
        else:
            # Else work as it is
            super().mouseReleaseEvent(event)

    def leftMouseButtonPress(self, event):
        return super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event):
        return super().mouseReleaseEvent(event)

    def rightMouseButtonPress(self, event):
        return super().mousePressEvent(event)

    def rightMouseButtonRelease(self, event):
        return super().mouseReleaseEvent(event)

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

    def wheelEvent(self, event: QtGui.QWheelEvent):
        # Every time we scroll we need to change the zoome value
        if event.angleDelta().y() > 0: # We are zooming in
            zoomfactor = ZOOM_IN_FACTOR
            self.zoomvalue += 1
        else:
            zoomfactor = ZOOM_OUT_FACTOR
            self.zoomvalue -= 1
        
        if self.zoomvalue not in ZOOM_RANGE:
            if self.zoomvalue < ZOOM_RANGE[0]:
                self.zoomvalue = ZOOM_RANGE[0]
            elif self.zoomvalue > ZOOM_RANGE[-1]:
                self.zoomvalue = ZOOM_RANGE[-1]
            return event.ignore()
        #  change the scale if we are not ignoring the event
        self.scale(zoomfactor, zoomfactor)
