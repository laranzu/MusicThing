
# Hugh Fisher Dec 2021
# Turns out we do have some build steps even
# for this Python application!

default: app

app: resfile

clean:
	rm __pycache__/*
	rm qrc_resources.py

resfile: resources/icon128x128.png
	pyrcc5 resources/resources.qrc -o ./qrc_resources.py

