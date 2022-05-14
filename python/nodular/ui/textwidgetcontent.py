#!/usr/bin/env python
import os
import pathlib
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class TextWidgetContent(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stylesheet_name = pathlib.Path(__file__).parent / "qss/nodular.qss"
        print (type(self.stylesheet_name))

        self.init_ui()

    def init_ui(self):
        # Load the stylesheet
        self.load_style_sheet()

        self.label = QtWidgets.QLabel()
        self.label.setText("Text Box")

        self.textbox = QtWidgets.QTextEdit()
        self.textbox.setPlaceholderText("Type your text here...")
        self.widget_layout = QtWidgets.QVBoxLayout()
        self.widget_layout.setContentsMargins(0,0,0,0)

        self.widget_layout.addWidget(self.label)
        self.widget_layout.addWidget(self.textbox)

        self.setLayout(self.widget_layout)

    def load_style_sheet(self):

        file = QtCore.QFile(str(self.stylesheet_name))
        file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        _stylesheet = file.readAll()
        QtGui.QGuiApplication.instance().setStyleSheet(str(_stylesheet, 'utf-8'))
