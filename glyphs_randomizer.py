#MenuTitle: Tab with selected letters randomized
# -*- coding: utf-8 -*-
__doc__="""
New Tab with selected characters randomized
"""

#..................................................................
#
# --> Shout out to zar-nicolas20 @ GitHub
# --> github.com/CalvinKwok
#
#..................................................................


from PyObjCTools.AppHelper import callAfter
from random import shuffle
import copy

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

namesOfSelectedGlyphs = ["/" + l.parent.name for l in selectedLayers]

random_list = copy.copy(namesOfSelectedGlyphs)

before_string = ""

for GlyphName in namesOfSelectedGlyphs:
	before_string += GlyphName
print before_string

shuffle(random_list)

randomized_string = ""

print "Randomizing..."

for GlyphName in random_list:
	randomized_string += GlyphName
print "Output:" + randomized_string

callAfter(Glyphs.currentDocument.windowController().addTabWithString_, randomized_string)
