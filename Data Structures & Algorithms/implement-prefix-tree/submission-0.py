class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        cur = self
        for i, c in enumerate(word):
            cur.children[c] = cur.children.get(c, PrefixTree())
            if i == len(word) - 1:
                cur.is_word = True
                break
            else:
                cur = cur.children[c]

    def search(self, word: str) -> bool:
        cur = self
        for i, c in enumerate(word):
            if c not in cur.children:
                return False
            elif i == len(word) - 1 and cur.is_word != True:
                return False
            else:
                cur = cur.children[c]
        
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        