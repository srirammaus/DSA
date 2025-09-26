

class HashTable():
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [None] * capacity
    def hash(self, key):
        # you can also use unicode get by using ord but our python has inbuilt hash function
        return sum(ord(char) for char in key) % self.capacity
    def set_hash_table(self, key): #for normal hash table
        """
        So by using this you , there is collsion prlm so we update to hash set , they do have collision problm  , there we more updates
        :param key:
        :return:
        """
        hash_key = self.hash(key)
        if self.table[hash_key] != None:
            print("Hash Table Already Set")
            print(self.table[hash_key])
            print(hash_key)
        self.table[hash_key] = key

#
# hashtable = HashTable(10)
#
# keys = ["apple", "banana", "cherry", "date", "elderberry",
#         "fig", "grape", "honeydew", "kiwi", "lemon"]
# for key in keys:
#     hashtable.set_hash_table(key)
#
# print(hashtable.table)

