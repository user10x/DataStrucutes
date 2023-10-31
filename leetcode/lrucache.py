from typing import List, Dict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.hash_map = {}

    def get(self, key) -> bool:
        if key not in self.map:
            return False

        self.cache.remove(key)
        self.cache.append(key)

    def refer(self,key)->None:
        if self.get(key):
            return
        self.put(key)

    def put(self, key):
        if len(self.cache) == self.capacity:
            first_key = self.cache.pop(0)
            del self.hash_map[first_key]

        self.cache.append(key)
        self.map[key]  = len(self.cache) -1

if __name__ ==  "__main__":
    c = LRUCache(10)
    c.get()