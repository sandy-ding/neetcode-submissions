class Node:
    def __init__(self):
        self.isWord = False
        self.hash_map = {}

class WordDictionary:
    def __init__(self):
        self.node = Node()

    def addWord(self, word: str) -> None:
        pointer = self.node
        for ch in word:
            if ch not in pointer.hash_map:
                pointer.hash_map[ch] = Node()
            pointer = pointer.hash_map[ch]
        pointer.isWord = True

    def search(self, word: str) -> bool:
        return self.dfsSearch(self.node, word, 0)

    def dfsSearch(self, node: Node, word: str, start: int) -> bool:
        pointer = node
        for i in range(start, len(word)):
            ch = word[i]
            if ch == ".":
                for key in pointer.hash_map:
                    if self.dfsSearch(pointer.hash_map[key], word, i + 1):
                        return True
                return False
            elif ch not in pointer.hash_map:
                return False
            pointer = pointer.hash_map[ch]
        return pointer.isWord
        
