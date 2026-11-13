class LRUCache:

    def __init__(self, capacity: int):
        self.keys = deque()
        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.keys.append(key)
            return self.cache[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache or len(self.cache) < self.capacity :
            self.cache[key] = value
            self.keys.append(key)
        else:
            lru = self.keys.popleft()
            while lru in self.keys:
                lru = self.keys.popleft()
            del self.cache[lru]
            self.cache[key] = value
            self.keys.append(key)