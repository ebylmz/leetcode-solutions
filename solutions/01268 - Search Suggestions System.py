class TrieNode():
    def __init__(self):
        self.children = {}
        self.words = []   # Stores up to 3 lexicographically smallest words that share the current prefix

class Solution(object):
    """
        IDEA: Use Trie data structure to store the best three matching
        Time Complexity: O(n*logn(n) + n*l), where n: number of products, l: average word length
        Space Complexity: O(n*l)
    """
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            # Words comes in lexicographic order. Therefore no need to keep more than 3 words
            if len(node.words) < 3:
                node.words.append(word)

    def suggestedProducts(self, products, search_word):
        # Sort products in order to add them lexicographical order 
        products.sort()
        for word in products:
            self.add(word)
        
        result = [[] for _ in search_word]
        node = self.root
        for i, c in enumerate(search_word):
            if c not in node.children:
                break
            node = node.children[c]
            result[i] = node.words
        return result