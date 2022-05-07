#!/usr/bin/env python
# std imports
import sys
from PyQt5 import QtWidgets

# internal imports
from nodular.ui.basewin import NodularBase

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    nodular_window = NodularBase()
    nodular_window.show()
    sys.exit(app.exec_())