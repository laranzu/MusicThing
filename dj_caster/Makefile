
# Hugh Fisher Dec 2021
# Resource file embeds runtime images and text,
# plus the i18n translations of program strings.

default: app

app: i18n resources

clean:
	rm __pycache__/*
	rm qrc_resources.py

#

RESFILES = \
	resources/icon128x128.png	\
	resources/about.html		\

resources: $(RESFILES) resources/resources.qrc
	pyrcc5 resources/resources.qrc -o ./qrc_resources.py

# Extract target creates .ts files for translation
# i18n target builds .qm runtime to be included in resource

extract:
	pylupdate5 -verbose qbuild.pro

i18n: qbuild.pro
	lrelease-qt5 -verbose qbuild.pro


