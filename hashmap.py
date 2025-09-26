

class Hashmap:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
    def hash(self, key):

        list_id = sum(int(integer) for integer in key if integer.isdigit()) % self.capacity
        print(list_id)
        return list_id % self.capacity
    def set_hash_map(self, key,value,mode="dict"):
        self.mode =  mode
        self.key = key
        self.value = value

        hash_key = self.hash(key)
        data = self.pack_data()
        self.table[hash_key].append(data)
    def pack_data(self):
        if self.mode == "dict":
            return {self.key: self.value}
        else:
            return (self.key, self.value)

    def print_table(self):
        for idx, data in enumerate(self.table):
            print(idx, data)

hashmap = Hashmap()

hashmap.set_hash_map("123456789", "admin")
hashmap.set_hash_map("987654321", "user")
hashmap.set_hash_map("111222333", "guest")
hashmap.set_hash_map("444555666", "superuser")
hashmap.set_hash_map("777888999", "root")
hashmap.set_hash_map("222333444", "moderator","tuple")
hashmap.set_hash_map("555666777", "tester")
hashmap.set_hash_map("999000111", "developer")
hashmap.set_hash_map("333444555", "analyst")
hashmap.set_hash_map("666777888", "manager")

hashmap.print_table()
