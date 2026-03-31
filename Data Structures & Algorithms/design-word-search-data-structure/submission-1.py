class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_word = False
    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            cur.children[c] = cur.children.get(c, WordDictionary())
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self
        for i, c in enumerate(word):
            if c == '.':
                contains = False
                for k, v in cur.children.items():
                    contains |= v.search(word[i + 1:])
                return contains
            elif c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.is_word

