#!/usr/bin/env python
# std imports
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

# internal imports
from nodular.ui.constants import *
from nodular.ui.textwidgetcontent import TextWidgetContent
from nodular.ui.nodesockets import Sockets


class NodularGraphicsNode:
    def __init__(self, scene, node_content, inputs=[], outputs=[],
                 title="Undefined Node"):
        self.scene = scene
        self.title = title

        self.inputs = inputs
        self.outputs = outputs

        self.node_content = node_content

        self.nodular_node = _NodularGraphicsNode(self)

        self.scene.add_node(self.nodular_node)


class _NodularGraphicsNode(QtWidgets.QGraphicsItem):
    def __init__(self, node, parent=None):
        super().__init__(parent)
        self.node = node
        self.content = self.node.node_content
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
        self.title = self.node.title
        self.title_color = QtCore.Qt.white

    def set_flags(self):
        self.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable |\
            QtWidgets.QGraphicsItem.ItemIsMovable)

    def init_ui(self):
        self.set_flags()
        self.init_title()
        self.init_sockets()
        self.init_content()

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

    def paint(self, painter: QtGui.QPainter,
              option: 'QtWidgets.QStyleOptionGraphicsItem',
              widget=None) -> None:
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

        painter.setPen(self._pen_default if not self.isSelected() \
            else self._pen_selected)
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawPath(path_outline.simplified())

    def boundingRect(self) -> QtCore.QRectF:
        return QtCore.QRectF(0, 0, WIDTH,HEIGHT).normalized()

    def init_title(self):
        self.title_item = QtWidgets.QGraphicsTextItem(self)

    def init_content(self):
        self.gr_content = QtWidgets.QGraphicsProxyWidget(self)
        self.content.setGeometry(RECT_RADIUS, TITLE_HEIGHT+RECT_RADIUS,
                                 WIDTH-2*RECT_RADIUS,
                                 HEIGHT-2*RECT_RADIUS-TITLE_HEIGHT)
        self.gr_content.setWidget(self.content)

    def init_sockets(self):
        pass


class TextNodularGraphicsNode(NodularGraphicsNode):
    def __init__(self, scene, title):
        self.node_content = TextWidgetContent()
        self.scene = scene
        self.title = title
        super().__init__(scene=scene, node_content=self.node_content,
                         title=self.title)

        _input_count=TEXT_NODE_INPUTS
        _input_position=LEFT_BOTTOM
        _output_count=TEXT_NODE_OUTPUTS
        _ouput_position=RIGHT_TOP

        for index in range(1,_input_count+1):
            self.inputs.append(Sockets(node=self,
                                       index=index,
                                       position=_input_position))

        for index in range(1, _output_count+1):
            self.outputs.append(Sockets(node=self,
                                        index=index,
                                        position=_ouput_position))
