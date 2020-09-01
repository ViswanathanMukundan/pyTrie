#Define a trie in  python 
#Elements are stored only using lowercase characters for simplicity 
#Consider all entries as completely lowercase
#Convert entries to lowercase before searching, hence making the search operation case-insensitive

class TrieNode:		#Template for defining individual nodes of the trie.

	def __init__(self):
		self.children = [None]*26	#One child for each letter of the alphabet 

		self.terminator = False		#If terminator is true => end of the word


class Trie:

	def __init__(self):
		self.root = self.newNode()

	def newNode(self):
		return TrieNode()

	def insertNode(self, word):   #The number of characters in the word define the number of levels occupied in the trie.
		word = word.lower()
		trieRoot = self.root
		wordLength = len(word) 
		for letter in word:
			letterNo = ord(letter) - ord('a')

			if not trieRoot.children[letterNo]:
				trieRoot.children[letterNo] = self.newNode()
			trieRoot = trieRoot.children[letterNo]
						
		trieRoot.terminator = True		#mark the end of the word

	def search(self, word):
		lowerCaseWord = word.lower()
		trieRoot = self.root
		wordLength = len(lowerCaseWord)
		for letter in lowerCaseWord:
			letterNo = ord(letter) - ord('a')
			if not trieRoot.children[letterNo]:
				return False
			trieRoot = trieRoot.children[letterNo]
		return trieRoot.terminator and trieRoot is not None 


words = ['app','apple','apply','application','bee','beware']
wordTrie = Trie()

for word in words:
	wordTrie.insertNode(word)

for word in words:
	print(wordTrie.search(word))
print(wordTrie.search('BEwArE'))
