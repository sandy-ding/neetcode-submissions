class Node:
    def __init__(self):
        self.map_ = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        pointer = self.root
        for ch in word:
            if ch not in pointer.map_:
                pointer.map_[ch] = Node()
            pointer = pointer.map_[ch]
        pointer.isWord = True


    def search(self, word: str) -> bool:
        pointer = self.root
        for ch in word:
            if ch not in pointer.map_:
                return False
            pointer = pointer.map_[ch]
        return pointer.isWord

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for ch in prefix:
            if ch not in pointer.map_:
                return False
            pointer = pointer.map_[ch]
        return True
        