# DJ Applications

This is a suite of - well, more than one - applications intended to
help a DJ create playlists and control music in real time.

Hugh Fisher is the designer and programmer. Not being a musician,
he sometimes listens to Paul Wayper who would be the product owner
if you're into Agile.

Written in Python3 and Qt5, running on Fedora Linux.


**Spellbook** is for building playlists.
Assumes you already have Rhythm Box and a music collection.

**Caster** will be for real time playback of playlists.


----


Haven't thought about packaging up into distributable applications
yet. If you want to run, dependencies are Python3 and Python Qt.

For Python Qt, I'm using the PySide2 wrapper, which the doco says
to install via pip, not as an RPM.

Run from the terminal, Old School:

    cd dj_spellbook
    ./main.pyw


Even though this is a Python program, there are build steps,
to create Qt resource and i18n files. So also needs package(s):
    qt5-linguist
