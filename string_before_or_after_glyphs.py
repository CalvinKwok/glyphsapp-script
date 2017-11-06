#MenuTitle: Tab with string before and after selected glyphs (UI)
# -*- coding: utf-8 -*-
__doc__="""
New Tab with string before and/or after selected glyphs with UI
"""

#..................................................................
#
# --> Shout out to Mark2Mark & zar-nicolas20 @ GitHub
# --> github.com/CalvinKwok
#
#..................................................................


import GlyphsApp
import vanilla

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers
listOfGlyphNames = [thisLayer.parent.name for thisLayer in selectedLayers]




class OpenTab(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow((500, 100), "Open new tab with:")
		self.w.myTextBox = vanilla.TextBox((128, 35, -10, 40), "/(Selected Glyphs)/")
		self.w.editTextLeft = vanilla.EditText((20, 20, 100, 50), sizeStyle='small', callback=self.editTextCallbackLeft)
		self.w.editTextRight = vanilla.EditText((260, 20, 100, 50), sizeStyle='small', callback=self.editTextCallbackRight)
		self.w.myButton = vanilla.Button((380, 35, -10, 20), "Generate", sizeStyle='small', callback=self.buttonCallback) 
		self.w.open()
	
	
	def editTextCallbackLeft(self, sender):
		print "Left entry:", sender.get()
		
	def editTextCallbackRight(self, sender):
		print "Right entry:", sender.get()


	def buttonCallback(self, sender):
		
		leftList = []
		for character in self.w.editTextLeft.get():
			if ord(character) > 0xffff:
				unicodeValue = "%05X" % ord(character)
			else:
				unicodeValue = "%04X" % ord(character)
			
			#niceLeftName = Glyphs.glyphInfoForUnicode(unicodeValue).name

			targetDict = {glyph.unicode:glyph.name for glyph in Font.glyphs}
			if targetDict.has_key(unicodeValue):
				niceLeftName = targetDict[unicodeValue]
			
			if niceLeftName:
				leftList.append("/" + str(niceLeftName))
			else:
				print "None information for uni%s" % unicodeValue
		
		leftString = ""
		for each_glyph in leftList:
			leftString += each_glyph
		#print leftString
		

		rightList = []
		for character in self.w.editTextRight.get():
			if ord(character) > 0xffff:
				unicodeValue = "%05X" % ord(character)
			else:
				unicodeValue = "%04X" % ord(character)
			
			#niceRightName = Glyphs.glyphInfoForUnicode(unicodeValue).name
			targetDict = {glyph.unicode:glyph.name for glyph in Font.glyphs}
			if targetDict.has_key(unicodeValue):
				niceRightName = targetDict[unicodeValue]
			
			if niceRightName:
				rightList.append("/" + str(niceRightName))
			else:
				print "None information for uni%s" % unicodeValue
		
		rightString = ""
		for each_glyph in rightList:
			rightString += each_glyph
		#print rightString
		
		
		full = ''
		for each_glyph in listOfGlyphNames:
			full += leftString + '/' + each_glyph + rightString
		print "String:" + full	

		
		Glyphs.currentDocument.windowController().addTabWithString_( full )
		self.w.close()	
		
OpenTab()
