
from os import path

import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class AppView(QLabel):      # QWidget
    """Main application view. Display and most interaction."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(1280, 720)
        self.setText("<h1>Main Application View</h1>")
        self.prevKey = None

    ##  Rendering


    def paintEvent(self, event):
        """Custom renderer"""
        super().paintEvent(event)
        return
        ctx = QPainter(self)
        # Done, force painter to be free'd
        ctx = None
        print("Paint")

    ##  Other events

    def resizeEvent(self, event):
        """Anything special?"""
        super().resizeEvent(event)

    def  keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape and self.prevKey == key:
            self.parent().close()
        self.prevKey = key


