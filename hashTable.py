class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [{} for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.max

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val


t = HashTable()
t.get_hash("march 6")
t.get_hash("march 17")
t["march 6"] = 120
t["march 8"] = 67
