

class Hashset:
    """"
        we can also use dict for extraperformance now itself we can use this listor array is enough
    """
    def __init__(self,capacity = 10):
        self.table = [[] for _ in range(capacity)]
        self.capacity = capacity

    def hash(self,key):
        return sum(ord(char) for char in key) % self.capacity
    def append(self,key):
        hash_key = self.hash(key)
        print(hash_key)
        self.table[hash_key].append(key)
    def isexist(self,key):
        hash_key = self.hash(key)
        bucket =  hash_key in self.table
        return bucket
    def print(self):
        for idx,key in enumerate(self.table):
            print(idx,key)
hashset = Hashset()

items = [
    "admin",
    "user",
    "guest",
    "superuser",
    "root",
    "moderator",
    "tester",
    "developer",
    "analyst",
    "manager"
]

for item in items:
    hashset.append(item)
print(hashset.print())