class MyHashMap:

    def __init__(self):
        self.array = [[] for _ in range(1000)]

    def hash(self, key: int) -> int:
        return key % 1000

    def put(self, key: int, value: int) -> None:
        if (self.get(key) != -1):
            self.remove(key)
        self.array[self.hash(key)].append((key, value))

    def get(self, key: int) -> int:
        for i in self.array[self.hash(key)]:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.array[self.hash(key)]:
            if i[0] == key:
                self.array[self.hash(key)].remove(i)
                break;


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)