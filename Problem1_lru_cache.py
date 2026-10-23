from collections import OrderedDict


class LRUCache:
    """A fixed-capacity cache that removes the least recently used item."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    print(cache.get(1))  # 100
    cache.put(3, 300)
    print(cache.get(2))  # -1
    print(cache.get(3))  # 300
