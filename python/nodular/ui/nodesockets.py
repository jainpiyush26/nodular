#!/usr/bin/env python
# std imports
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

# internal imports
from nodular.ui.constants import *

class _Sockets(QtWidgets.QGraphicsItem):
    def __init__(self, index=0, parent=None):
        super().__init__(parent)

        self.radius = SOCKET_RADIUS
        self.width = SOCKET_WIDTH
        self.colour_bg = QtGui.QColor(SOCKET_BG_COLOUR[index])
        self.colour_outline = QtGui.QColor(SOCKET_OUTLINE_COLOUR)

        self.pen = QtGui.QPen(self.colour_outline)
        self.pen.setWidthF(self.width)
        self.brush = QtGui.QBrush(self.colour_bg)

    def paint(self, painter: QtGui.QPainter,
              option: 'QtCore.QStyleOptionGraphicsItem',
              widget: None) -> None:

        # Let's paint a circle
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawEllipse(-self.radius, -self.radius, 2*self.radius, 2*self.radius)

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(-self.radius - self.width,
                             -self.radius - self.width,
                             2*(self.radius - self.width),
                             2*(self.radius - self.width)
                             )


class Sockets():
    def __init__(self, node, index=0, position=LEFT_TOP):

        self.node = node

        self.index = index

        self.position = position
        self.gr_socket = _Sockets(index=self.index-1,
                                  parent=self.node.nodular_node)
        self.gr_socket.setPos(*self._set_socket_position())

    def _set_socket_position(self):
        # we use the WIDTH constant to get the size of the nodes
        if self.position in [LEFT_TOP, LEFT_MIDDLE, LEFT_BOTTOM]:
            x_pos = 0
        else:
            x_pos = WIDTH

        if self.position in [LEFT_TOP, RIGHT_TOP]:
            y_pos = self.index * SOCKET_DISTANCE
        elif self.position in [LEFT_MIDDLE, RIGHT_MIDDLE]:
            y_pos = HEIGHT/2 + self.index * SOCKET_DISTANCE
        else:
            y_pos = HEIGHT - (self.index * SOCKET_DISTANCE)

        return x_pos, y_pos
