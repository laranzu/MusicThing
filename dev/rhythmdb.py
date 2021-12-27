
"""	Loader for Rhythm Box database and playlists
"""

from os import path
from xml.etree import ElementTree
from xml.etree.ElementTree import iterparse


def xmlDataDir(userDir=None):
	"""Return path to Rhythm Box directory where XML files live"""
	if userDir is None:
		userDir = path.expanduser("~")
	rbDir = path.join(path.abspath(userDir), ".local","share","rhythmbox")
	if path.exists(rbDir) and path.isdir(rbDir):
		return rbDir
	else:
		raise NotADirectoryError("Cannot find Rhythm Box directory")


def playlistsFile(xmlDir=None):
	"""Name of Rhythm Box playlists file, if present"""
	if xmlDir is None:
		xmlDir = xmlDataDir()
	name = path.join(xmlDir, "playlists.xml")
	if path.exists(name) and path.isfile(name):
		return name
	else:
		raise FileNotFoundError("Cannot find Rhythm Box playlists XML file")

def musicFile(xmlDir=None):
	"""Name of Rhythm Box song (radio, etc) file, if present"""
	if xmlDir is None:
		xmlDir = xmlDataDir()
	name = path.join(xmlDir, "rhythmdb.xml")
	if path.exists(name) and path.isfile(name):
		return name
	else:
		raise FileNotFoundError("Cannot find Rhythm Box main database XML file")

##


def loadPlaylists(xmlFileName, nodeCallback, tagTargets=["playlist"]):
	"""Parse the playlists XML file, pass each playlist to callback"""
	for (event, node) in iterparse(xmlFileName, ["end"]):
		if node.tag in tagTargets:
			nodeCallback(node)


def loadMusic(xmlFileName, nodeCallback, typeTargets=["song"], tagTargets=["entry"]):
	"""Parse the main rhythm box XML file, pass song entries to callback"""
	for (event, node) in iterparse(xmlFileName, ["end"]):
		if node.tag in tagTargets:
			nType = node.attrib.get("type")
			if nType in typeTargets:
				nodeCallback(node)


##

def printXML(element):
	source = ElementTree.tostring(element, 'unicode')
	print(source)


if __name__ == "__main__":
	base = xmlDataDir()
	print("## Rhythm Box files are in", base)

	playName = playlistsFile(base)
	print("## Playlists in", playName)
	loadPlaylists(playlistsFile(), printXML)

	musicName = musicFile(base)
	print("## Music data in", musicName)
	loadMusic(musicFile(), printXML)

	print("## Done.")
