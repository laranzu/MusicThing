#!/usr/bin/python3

# Main application for (non-realtime) viewing and classifying
# music assets and whatnot. Starts with the info available
# from Rhythm Box.


import os, platform, sys

import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import qrc_resources, appview


__version__ = "0.1"

class AppWindow(QMainWindow):
    """The application window. Handles menu commands"""

    ##  Setup

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("DJ Spellbook " + __version__)
        self.initDisplay()
        self.initStatus()
        self.initMenus()
        self.restoreSettings()
        self.statusBar().showMessage("Ready")

    def initDisplay(self):
        """Display widget for main window"""
        self.display = appview.AppView(self)
        self.setCentralWidget(self.display)
        self.display.setFocus()

    def initStatus(self):
        """Set up status bar at bottom"""
        # Will auto-create on first use
        status = self.statusBar()
        status.setSizeGripEnabled(False)

    ##  Menu setup

    def createAction(self, text, slot=None, shortcut=None, tip=None, checkable=False, signal="triggered()"):
        """Create simple action"""
        action = QAction(text, self)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if checkable:
            action.setCheckable(True)
        if slot is not None:
            action.triggered.connect(slot)
        return action

    def initMenus(self):
        """Just the file menu with a few actions"""
        fileMenu = self.menuBar().addMenu("File")
        doAbout = self.createAction("About...", self.showAbout, "Ctrl+A", "About this application")
        doExit = self.createAction("Exit", self.close, QKeySequence.Quit, "End application")
        fileMenu.addAction(doAbout)
        fileMenu.addSeparator()
        fileMenu.addAction(doExit)

    ##  Application state between runs

    def restoreSettings(self):
        """Reload window geometry"""
        settings = QSettings()
        # Window
        pos = settings.value("MainWindow/position", QPoint(0, 0))
        size = settings.value("MainWindow/size", QSize(1280, 720))
        state = settings.value("MainWindow/state")
        self.move(pos)
        self.resize(size)
        if state:
            self.restoreState(state)
        # TODO other stuff

    def saveSettings(self):
        """Save main window geometry"""
        settings = QSettings()
        settings.setValue("MainWindow/position", self.pos())
        settings.setValue("MainWindow/size", self.size())
        settings.setValue("MainWindow/state", self.saveState())
        # TODO other stuff

    ##  Menu commands

    def showAbout(self):
        """Guilty parties"""
        # The about box can use simple HTML
        # (Not having /p tags is deliberate)
        QMessageBox.about(self, "About This Application",
            """
            <b>DJ Spellbook</b>
            <p>DJ expert: Paul Wayper
            <p>Code mangler: Hugh Fisher
            <p>Written in Python with PyQt
            """
            )


    ##  Shutting down

    def closeEvent(self, event):
        """Override so can save state"""
        self.saveSettings()
        super().closeEvent(event)

####

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("EvilAliensInc")
    app.setApplicationName("DJ_Spellbook")
    app.setWindowIcon(QIcon(":/icon.png"))
    win = AppWindow()
    win.show()
    app.exec_()

