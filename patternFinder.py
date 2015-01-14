from random import randint

'''
The baisc idea behind this problem is that you're given a series of test cases
  with 2 inputs [pattern, input].

pattern - A series of characters that define the pattern that you're looking for
	  [ex: 'abba']
input   - A string that may or may not follow the above pattern
	  [ex: 'redbluebluered' (does follow), 'redredblueblue' (does not follow)
'''

#sample 'input' strings
i = ["blueredredblue", "blueblueredred", "monkeybread", "snakemaster"]
#sample patterns
p = ["abba","abba","q","qp"]


#Here I'm making a dictionary and filling it with all of the substrings of i.
#It also keeps track of how many times that substring appears within i.
# posPat = makePosPats(i)
def makePosPats(i,p):
	posPat = {}
	if (len(i) <= 3):
		for pos in i:
			if pos in posPat:
				posPat[pos] += 1
			else:
				posPat[pos] = 1
	for f in range(0,len(i)-1):
		for l in range(f+1,len(i)):
			pos = i[f:l+1]
			if pos in posPat:
				posPat[pos] += 1
			else:
				posPat[pos] = 1
#	print posPat
	return posPat

#Here I'm looking at all of the unique characters in pattern, and counting
# how many times they appear.
# charCount = countChars(p)
def countChars(p):
	charCount = {}
	for c in p:
		if c in charCount:
			charCount[c] += 1
		else:
			charCount[c] = 1
#	print charCount
	return charCount

#Here I'm making an array of the substrings in input that appear as many times
# as the unique characters in pattern.
# posChar = makeLists(posPat, charCount)
def makeLists(posPat, charCount):
	posChar = {}
	for c in charCount:
		pc = []
		for pos in posPat:
			if charCount[c] is posPat[pos]:
				pc.append(pos)
		posChar[c] = pc
#	print posChar
	return posChar

#I realized that I can cut down on the possibilies for the substring of the
# first and last characters by cutting out all of the ones from their lists
# that don't contain the first character in input (for the first character
# in pattern) and that last character in input (for the last character in
# pattern).
# posChar, posCombo = cutStrings(p, i, posChar)
def cutStrings(p, i, posChar):
	posCombo = 1
	posChar[p[0]] = filter(lambda x: x[0] == i[0], posChar[p[0]])
	posChar[p[-1]] = filter(lambda x: x[-1] == i[-1], posChar[p[-1]])
	for char in posChar:
		posCombo *= len(posChar[char])
#	print posCombo
#	print posChar
	return posChar, posCombo

#Now I need to figure out the best way for finding all possible combinations
# of the substrings in posChar's arrays in order to identify the ones that
# match input. This is something I have, but I don't think its the best.

#I make a table (I know I'm using them a lot, but I just learned about them,
# and so I just want to use the crap out of them.) called triedThat, which
# stores all of the random combos of substrings that I've already tested out.
#If the string of randomly generated numbers is already in triedThat, it calls
# the function again to get another set of numbers.
# MAJOR FLAW: If I use too many unique characters in the pattern, I get an
#  error when the recursion runs too deep (which is bound to happen).
def getRands(posChar, triedThat):
	rands = {}
	s = ""
	for pos in posChar:
		l = len(posChar[pos]) - 1
		rands[pos] = randint(0,l)
		s += str(rands[pos])
	if (s in triedThat):
		return getRands(posChar, triedThat)
	else:
		triedThat[s] = rands
		return rands, s

#So I assign tryThis to the randomly generated numbers, and then create a
# string s that's puts the combos of substrings all together and junk. 

def putItAllTogether(p,i):
	hold_it = i
	posPat = makePosPats(i,p)
	charCount = countChars(p)

	found = False
	triedThat = {}
	posChar = makeLists(posPat, charCount)
	posChar, posCombo = cutStrings(p,i,posChar)
	for x in range(0,posCombo):
	        tryThis, n = getRands(posChar, triedThat)
	        s = ""
	        for c in p:
	                s += posChar[c][tryThis[c]]
		if s == hold_it:
			found = True
			break
	        triedThat[n] = s

	if found:
	        print "'" + i + "' DOES fit the pattern '" + p + "'"
	else:
	        print "'" + i + "' does NOT fit the pattern '" + p + "'"


#Testin out the booty code.
for z in range(len(i)):
	putItAllTogether(p[z],i[z])
#Test out the booty code?
'''
ans = raw_input("Would you like to give it a try? (y/n) ")
while (ans is 'y'):
	p = raw_input("Type a pattern: ")
	i = raw_input("Now a string that may or may not fit it: ")
	putItAllTogether(p,i)
	ans = raw_input("Would you like to try again? (y/n) ")
'''
