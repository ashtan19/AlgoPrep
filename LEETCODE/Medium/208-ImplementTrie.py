# Leetcode: 208. Implement Trie (Prefix Tree)

# Completed: Y
# Acheived Ideal: Y

# Time Complexity:
# Space Complexity:

# Solving process:
# Problems Encountered:

# Other Solutions: Use Defaultdict


class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def CharToIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        currNode = self.root
        for level in range(len(word)):
            index = self.CharToIndex(word[level])
            if currNode.children[index] == None:
                currNode.children[index] = TrieNode()
            currNode = currNode.children[index]
        currNode.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currNode = self.root
        for level in range(len(word)):
            index = self.CharToIndex(word[level])
            if currNode.children[index]:
                currNode = currNode.children[index]
            else:
                return False
        return currNode.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currNode = self.root
        for level in range(len(prefix)):
            index = self.CharToIndex(prefix[level])
            if currNode.children[index]:
                currNode = currNode.children[index]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
