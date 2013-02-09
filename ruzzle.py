import sys

class RuzzleSolver:

	def buildRuzzleBox(self):
		self.rzdata = [sys.argv[2][0],sys.argv[2][1],sys.argv[2][2],sys.argv[2][3],
			sys.argv[2][4],sys.argv[2][5],sys.argv[2][6],sys.argv[2][7],
			sys.argv[2][8],sys.argv[2][9],sys.argv[2][10],sys.argv[2][11],
			sys.argv[2][12],sys.argv[2][13],sys.argv[2][14],sys.argv[2][15]]

	def printRuzzleBox(self, state):
		for i in range(0,4):
			print state[i*4], "|",state[i*4+1], "|",state[i*4+2], "|",state[i*4+3]
	
	def loadDictionary(self):
		self.dictionary = []
		
		dictionaryfile = open("dicts/"+sys.argv[1]+".txt")
		i=0
		for line in dictionaryfile.readlines():
			self.dictionary.append(line.rstrip())
			i+=1
		
		print "loaded ", i, " words into IT dictionary"
	
	def isInSameRow(self,n,p):
		if n>=0 and n<4 and p>=0 and p<4:
			return True
		if n>=4 and n<8 and p>=4 and p<8:
			return True
		if n>=8 and n<12 and p>=8 and p<12:
			return True
		if n>=12 and n<16 and p>=12 and p<16:
			return True
		
		return False
	
	def isValidOblique(self,n,p):
		#case n is in first row
		if n>=0 and n<4 and (p>=4 and p<8):
			return True
		#second row
		if n>=4 and n<8 and ((p>=0 and p<4) or (p>=8 and p<12)):
			return True
		#third row
		if n>=8 and n<12 and ((p>=4 and p<8) or (p>=12 and p<16)):
			return True
		#forth row
		if n>=12 and n<16 and (p>=8 and p<12):
			return True
		
		return False
	
	def isValidUpDown(self,n,p):
		if p >= 0 and p < 16:
			return True
		else:
			return False
	
	def left(self,l):
		return l-1
	def right(self,l):
		return l+1
	def up(self,l):
		return l-4
	def down(self,l):
		return l+4
	def rightup(self,l):
		return l-3
	def rightdown(self,l):
		return l+5
	def leftup(self,l):
		return l-5
	def leftdown(self,l):
		return l+3
	
	def printDictionary(self):
		#printing all dictionary -- to use only for debugging purposes
		for word in self.dictionary:
			print word
	
	def cloneDictionaryWithLen(self,l):
		lendict = []
		for word in self.dictionary:
			if len(word)==l:
				lendict.append(word)
		
		return lendict
	
	def presentOnBoard(self,w):
		for letter in range(0,16):
			if w[0] == self.rzdata[letter]:
				if self.subwordOnBoard(w[1:],letter,self.rzdata[:]):
					return True
				else:
					return False
	'''
	w : word
	l : letter
	s : state
	'''
	def subwordOnBoard(self,w,l,s):
		
		if len(w)==0:
			return True
		
		#up
		if self.isValidUpDown(l,self.up(l)) and w[0] == s[self.up(l)]:
			s[l] = "#"
			if len(w) ==0:
				return True
			else:
				if self.subwordOnBoard(w[1:],self.up(l),s) :
					return True
		
		#down
		if self.isValidUpDown(l,self.down(l)) and w[0] == s[self.down(l)]:
			s[l] = "#"
			if len(w) ==0:
				return True
			else:
				if self.subwordOnBoard(w[1:],self.down(l),s) :
					return True
		
		#left
		if self.isInSameRow(l,self.left(l)) and w[0] == s[self.left(l)]:
			s[l] = "#"
			if len(w) ==0:
				return True
			else:
				if self.subwordOnBoard(w[1:],self.left(l),s):
					return True
		
		#right
		if self.isInSameRow(l,self.right(l)) and w[0] == s[self.right(l)]:
			s[l] = "#"
			if len(w) ==0:
				return True
			else:
				if self.subwordOnBoard(w[1:],self.right(l),s):
					return True
		
		#rup
		#up
		if self.isValidOblique(l,self.rightup(l)) and w[0] == s[self.rightup(l)]:
			s[l] = "#"
			if len(w) ==0:
				return True
			else:
				if self.subwordOnBoard(w[1:],self.rightup(l),s):
					return True
		
		#rdw
		if self.isValidOblique(l,self.rightdown(l)) and w[0] == s[self.rightdown(l)]:
			s[l] = "#"
			if len(w) ==0:
				return True
			else:
				if self.subwordOnBoard(w[1:],self.rightdown(l),s):
					return True
		
		#lup
		if self.isValidOblique(l,self.leftup(l)) and w[0] == s[self.leftup(l)]:
			s[l] = "#"
			if len(w) ==0:
				return True
			else:
				if self.subwordOnBoard(w[1:],self.leftup(l),s):
					return True
		
		#ldw
		if self.isValidOblique(l,self.leftdown(l)) and w[0] == s[self.leftdown(l)]:
			s[l] = "#"
			if len(w) ==0:
				return True
			else:
				if self.subwordOnBoard(w[1:],self.leftdown(l),s):
					return True
				
		return False
	
	def rsolver1(self):
		#the most efficient algorithm found so far from me
		for l in range(6,14):			
			newdict = self.cloneDictionaryWithLen(l)
			
			#print "extracted a list of possible ", len(newdict), " words"
			
			for word in newdict:
				if self.presentOnBoard(word):
					print word
		
	
	def __init__(self):
		self.buildRuzzleBox()
		self.printRuzzleBox(self.rzdata)
		self.loadDictionary()
		
		self.rsolver1()

rs = RuzzleSolver()
