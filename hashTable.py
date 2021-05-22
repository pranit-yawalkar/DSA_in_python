stock_prices = [["march 6", 310.0], ["march 7", 340.0], ["march 8", 380.0], [
    "march 9", 302.0], ["march 10", 297.0], ["march 11", 323.0]]

print(stock_prices[0])
# To find stock price on March 9
for element in stock_prices:
    if element[0] == "march 9":
        print(element[1])
# By doing above way the complexity of search using a list is O(n)

# Process using Python Dictionary
stock_prices = {
    "march 6": 310.0,
    "march 7": 340.0,
    "march 8": 380.0,
    "march 9": 302.0,
    "march 10": 297.0,
    "march 11": 323.0,
}
print(stock_prices["march 9"])
# Complexity of seach using dictionary is O(1)

# Implementing Hash Table


class HashTable:
    def __init__(self):
        self.MAX = 100
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


ht = HashTable()
ht["march 6"] = 310
ht["march 7"] = 420
ht["dec 2"] = 120
print(ht.arr)
del ht["march 6"]
print(ht.arr)
