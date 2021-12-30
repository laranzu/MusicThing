#!/usr/bin/python3

# Main application for playing music


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
        self.setWindowTitle(self.tr("DJ Caster") + " " + __version__)
        self.initDisplay()
        self.initStatus()
        self.initMenus()
        self.restoreSettings()
        self.statusBar().showMessage(self.tr("Ready"))

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
        fileMenu = self.menuBar().addMenu(self.tr("File"))
        doAbout = self.createAction(self.tr("About..."), self.showAbout, "Ctrl+A",
                        self.tr("About this application"))
        doExit = self.createAction(self.tr("Exit"), self.close, QKeySequence.Quit,
                        self.tr("End application"))
        fileMenu.addAction(doAbout)
        fileMenu.addSeparator()
        fileMenu.addAction(doExit)

    ##  Application state between runs

    # Strings are keys into file, so don't i18n

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
        # Load text from file so can do i18n
        htmlFile = QFile(":/about.html")
        if htmlFile.open(QIODevice.ReadOnly | QIODevice.Text):
            content = QTextStream(htmlFile).readAll()
            htmlFile.close()
        else:
            raise IOError("Cannot open about.html file from resources")
        QMessageBox.about(self, self.tr("About this application"), content)


    ##  Shutting down

    def closeEvent(self, event):
        """Override so can save state"""
        self.saveSettings()
        super().closeEvent(event)

####

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("EvilAliensInc")
    app.setApplicationName("DJ_Caster")
    #  i18n setup...
    locale = QLocale.system().name()
    # Use system Qt for built in widgets
    qtTranslation = QTranslator()
    if qtTranslation.load("qt_" + locale, QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
        app.installTranslator(qtTranslation)
    else:
        print("ERR could not load Qt translation for {}".format(locale))
    # App-specific translation in resource file
    appTranslation = QTranslator()
    if appTranslation.load("spellbook_" + locale, ":/translations"):
        app.installTranslator(appTranslation)
    else:
        print("Application has not been translated for {}".format(locale))
    #
    app.setWindowIcon(QIcon(":/icon.png"))
    win = AppWindow()
    win.show()
    app.exec_()

