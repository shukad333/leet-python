class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode();

    def _charToIndex(self,ch):

        return ord(ch) - ord('a')

    def insert(self,word):
        current = self.root
        length = len(word)
        for w in word:
            #print(w)
            ascci = self._charToIndex(w)


            if not current.children[ascci]:
                current.children[ascci] = self.getNode()
            current = current.children[ascci]

        current.endOfWord = True

    def search(self,word):
        length = len(word)
        current = self.root
        for w in word:
            node = current.children[self._charToIndex(w)]
            if not node:
                return False
            current = node
        return current.endOfWord and current!=None

t = Trie()
t.insert("Shuhail")
t.insert("Naoor")

print(t.search("Naoor"))



