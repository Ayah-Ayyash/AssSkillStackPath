from hash_table import HashTable

ht = HashTable()

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)
ht.insert("grape", 40)
ht.insert("kiwi", 50)
ht.insert("melon", 60)

print("Hash Table:", ht)

print("Search 'banana':", ht.search("banana"))
print("Search 'mango':", ht.search("mango"))

ht.delete("orange")
print("After deleting 'orange':", ht)

ht.insert("pear", 70)
ht.insert("peach", 80)
print("After inserting 'pear' and 'peach' (rehash may occur):", ht)
