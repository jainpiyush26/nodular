#!/usr/bin/env python
# std imports
import math
from turtle import right
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

# internal imports
from nodular.ui.constants import *

class NodularGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._grid_pen = QtGui.QPen(QtGui.QColor(LIGHTGRAY))
        self._grid_pen.setWidth(GRIDPENWIDTH)

        self._grid_pen_dark = QtGui.QPen(QtGui.QColor(GRAY))
        self._grid_pen_dark.setWidth(GRIDPENWIDTH_DARK)

        # How big will be the scene
        self.setSceneRect(-SCENE_WIDTH//2, -SCENE_HEIGHT//2,
                          SCENE_WIDTH, SCENE_HEIGHT)

        self.setBackgroundBrush(QtGui.QColor(DARKGRAY))

    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        super().drawBackground(painter, rect)

        # creating the grid
        _left = int(math.floor(rect.left()))
        _right = int(math.ceil(rect.right()))
        _top = int(math.floor(rect.top()))
        _bottom = int(math.floor(rect.bottom()))

        _first_left = _left - (_left % GRIDSIZE)
        _first_top = _top - (_top % GRIDSIZE)

        # lines we want to draw these on
        ln_list, ln_list_darker = list(), list()
        for x in range(_first_left, _right, GRIDSIZE):
            if x % (GRIDSIZE*GRIDSQUARE) != 0:
                ln_list.append(QtCore.QLine(x, _top, x, _bottom))
            else:
                ln_list_darker.append(QtCore.QLine(x, _top, x, _bottom))
        for y in range(_first_top, _bottom, GRIDSIZE):
            if y % (GRIDSIZE*GRIDSQUARE) != 0:
                ln_list.append(QtCore.QLine(_left, y, _right, y))
            else:
                ln_list_darker.append(QtCore.QLine(_left, y, _right, y))


        painter.setPen(self._grid_pen)
        painter.drawLines(*ln_list)

        painter.setPen(self._grid_pen_dark)
        painter.drawLines(*ln_list_darker)
