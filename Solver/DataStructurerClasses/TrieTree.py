class TrieNode():
    def __init__(self):
        self.isWord = False
        self.children = {}

class TrieTree():
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word): 
        node = self.root
        for letter in word: 
            if(letter not in node.children): 
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True
    
    def search(self, word): 
        node = self.root 
        for letter in word: 
            if(letter not in node.children): 
                return False
            node = node.children[letter]
        return node.isWord

    
