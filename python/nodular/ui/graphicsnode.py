#!/usr/bin/env python
# std imports
from ctypes.wintypes import RECT
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

# internal imports
from nodular.ui.constants import *


class NodularGraphicsNode:
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene
        self.title = title
        
        self.nodular_node = _NodularGraphicsNode(self, self.title)

        self.scene.add_node(self.nodular_node)


        self.inputs = list()
        self.outputs = list()


class _NodularGraphicsNode(QtWidgets.QGraphicsItem):
    def __init__(self, node, title, parent=None):
        super().__init__(parent)
        self.node = node
        self.init_ui()

        # Pen used for painting
        self._pen_default = QtGui.QPen(QtGui.QColor(PEN_COLOR))
        self._pen_default.setWidth(PEN_WIDTH)
        self._pen_selected = QtGui.QPen(QtGui.QColor(PEN_COLOR_SEL))
        self._pen_selected.setWidthF(PEN_WIDTH_SEL)

        # Brush objects
        self._brush_title = QtGui.QBrush(QtGui.QColor(TITLE_BRUSH_COLOR))
        self._brush_bg = QtGui.QBrush(QtGui.QColor(BG_BRUSH_COLOR))

        # Let set the properties
        self.title = title
        self.title_color = QtCore.Qt.white

    def set_flags(self):
        self.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable | QtWidgets.QGraphicsItem.ItemIsMovable)

    def init_ui(self):
        self.set_flags()
        self.init_title()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self.title)
        self.title_item.setPos(TITLE_PADDING, 0)

    @property
    def title_color(self):
        return self._title_color
    @title_color.setter
    def title_color(self, value):
        self._title_color = value
        self.title_item.setDefaultTextColor(self.title_color)

    def paint(self, painter: QtGui.QPainter, option: 'QtWidgets.QStyleOptionGraphicsItem', widget=None) -> None:
        # Title 
        path_title = QtGui.QPainterPath()
        path_title.setFillRule(QtCore.Qt.WindingFill)
        path_title.addRoundedRect(0, 0, WIDTH, TITLE_HEIGHT, RECT_RADIUS,
        RECT_RADIUS)
        path_title.addRect(0, TITLE_HEIGHT-RECT_RADIUS, RECT_RADIUS,
        RECT_RADIUS)
        path_title.addRect(WIDTH-RECT_RADIUS, TITLE_HEIGHT-RECT_RADIUS,
        RECT_RADIUS,RECT_RADIUS)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())

        # Content
        path_content = QtGui.QPainterPath()
        path_content.setFillRule(QtCore.Qt.WindingFill)
        path_content.addRoundedRect(0, TITLE_HEIGHT,
        WIDTH, HEIGHT-TITLE_HEIGHT, RECT_RADIUS, RECT_RADIUS)
        path_content.addRect(0,TITLE_HEIGHT, RECT_RADIUS,
        RECT_RADIUS)
        path_content.addRect(WIDTH-RECT_RADIUS, TITLE_HEIGHT, RECT_RADIUS,
        RECT_RADIUS)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self._brush_bg)
        painter.drawPath(path_content.simplified())

        # OUTLINE 
        path_outline = QtGui.QPainterPath()
        path_outline.addRoundedRect(0 ,0, WIDTH, HEIGHT, RECT_RADIUS,
        RECT_RADIUS)

        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawPath(path_outline.simplified())

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, 2*RECT_RADIUS+WIDTH,
        2*RECT_RADIUS+HEIGHT).normalized()

    def init_title(self):
        self.title_item = QtWidgets.QGraphicsTextItem(self)

