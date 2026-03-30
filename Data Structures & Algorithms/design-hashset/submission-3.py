class MyHashSet:

    def __init__(self):
        self.hash_set = [[]] * 1000

    def add(self, key: int) -> None:
        idx = key % 1000
        if key not in self.hash_set[idx]:
            self.hash_set[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % 1000
        if key in self.hash_set[idx]:
            self.hash_set[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % 1000
        return key in self.hash_set[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)