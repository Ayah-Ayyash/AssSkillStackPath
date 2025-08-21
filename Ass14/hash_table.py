class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, key, i):
        return (self._hash(key) + i**2) % self.size

    def _rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        for entry in old_table:
            if entry and entry != "DELETED":
                self.insert(entry[0], entry[1])

    def insert(self, key, value):
        if self.count / self.size > 0.7:
            self._rehash()
        i = 0
        while True:
            index = self._probe(key, i)
            if self.table[index] is None or self.table[index] == "DELETED":
                self.table[index] = (key, value)
                self.count += 1
                return
            elif self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            i += 1

    def search(self, key):
        i = 0
        while i < self.size:
            index = self._probe(key, i)
            if self.table[index] is None:
                return None
            if self.table[index] != "DELETED" and self.table[index][0] == key:
                return self.table[index][1]
            i += 1
        return None

    def delete(self, key):
        i = 0
        while i < self.size:
            index = self._probe(key, i)
            if self.table[index] is None:
                return False
            if self.table[index] != "DELETED" and self.table[index][0] == key:
                self.table[index] = "DELETED"
                self.count -= 1
                return True
            i += 1
        return False

    def __str__(self):
        return str([entry for entry in self.table if entry and entry != "DELETED"])
