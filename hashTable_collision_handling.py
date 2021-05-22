class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


# Collisions in Hash Table
# t = HashTable()
# print(t.get_hash("march 6"))
# print(t.get_hash("march 17"))
# t["march 6"] = 120
# t["march 8"] = 67
# t["march 9"] = 4
# t["march 17"] = 459
# print(t["march 6"])  # Here march 6 and march 17 got collided

# Collision handling using Chaining


class HashTableUsingChaining:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arrIndex = self.get_hash(key)
        for kv in self.arr[arrIndex]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for ind, element in enumerate(self.arr[h]):
            if len(element) == 2 or element[0] == key:
                self.arr[h][ind] = (key, val)
                found = True

        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arrIndex = self.get_hash(key)
        for ind, element in enumerate(self.arr[arrIndex]):
            if element[0] == key:
                print("del", ind)
                del self.arr[arrIndex][ind]


# t = HashTableUsingChaining()
# t["march 6"] = 310
# t["march 7"] = 420
# t["march 8"] = 67
# t["march 17"] = 63457
# print(t.arr)
# print(t["march 7"])
# del t["march 17"]
# print(t.arr)


# Collision handling using Linear Probing

class HashTableUsingLinearProbing:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        probe_range = self.get_probe_range(h)
        for probe_index in probe_range:
            element = self.arr[probe_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def find_slot(self, key, index):
        probe_range = self.get_probe_range(index)
        for probe_index in probe_range:
            if self.arr[probe_index] == None:
                return probe_index
            if self.arr[probe_index][0] == key:
                return probe_index
        raise Exception("Hashmap full")

    def get_probe_range(self, index):
        return [*range(index, len(self.arr))]+[*range(0, index)]

    def __delitem__(self, key):
        h = self.get_hash(key)
        probe_range = self.get_probe_range(h)
        for probe_index in probe_range:
            if self.arr[probe_index] is None:
                return
            if self.arr[probe_index][0] == key:
                self.arr[probe_index] = None
        print(self.arr)


# *range works as follows
print([*range(5, 8)]+[*range(0, 4)])

t = HashTableUsingLinearProbing()
t["march 6"] = 20
t["march 17"] = 88
t["nov 1"] = 100
t["march 31"] = 243
t["march 30"] = 211
t["march 23"] = 22
t["march 21"] = 25
t["march 22"] = 256
t["march 16"] = 259
t["march 11"] = 251

del t["march 17"]
t["march 12"] = 267
