
# Hugh Fisher Dec 2021
# Turns out we do have some build steps even
# for this Python application!

default: app

app: resources

clean:
	rm __pycache__/*
	rm qrc_resources.py

RESFILES = \
	resources/icon128x128.png	\
	resources/about.html		\

resources: $(RESFILES)
	pyrcc5 resources/resources.qrc -o ./qrc_resources.py

