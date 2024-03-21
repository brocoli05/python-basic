"""
Time Complexity: O(1), O(n) ==> Worst Case
"""
class HashTable:
   class Node:
      def __init__(self, key, value):
         self.key = key
         self.value = value
         self.next = None
   
   def _hash(self, key):
      # returns an index in the array
      return hash(key) % self.capacity

   def __init__(self, capacity=32):
      self.capacity = capacity
      self.size = 0
      self.table = [None] * capacity

   def insert(self, key, value):
      index = self._hash(key)

      if self.table[index] is None:
         # creates a new node with the key-value pair
         self.table[index] = self.Node(key, value)
         self.size += 1
      else:
         current = self.table[index]
         while current:
            # update the value if the key already exists
            if current.key == key:
               current.value = value
               return 
            current = current.next
         # If it doesn’t find the key, it creates a new node and adds it to the head of the list
         new_node = self.Node(key, value)
         new_node.next = self.table[index]
         self.table[index] = new_node
         self.size += 1

   def modify(self, key, value):
      index = self._hash(key)
      current = self.table[index]

      while current:
         if current.key == key:
            current.value = value
            return
         current = current.next 
      
      raise KeyError(key)

   def remove(self, key):
      index = self._hash(key)

      previous = None
      current = self.table[index]
      while current:
         # searches the linked list at that index for the key
         if current.key == key:
            if previous:
               previous.next = current.next
            else:
               self.table[index] = current.next
            self.size -= 1
            return
         previous = current
         current = current.next
      
      # If it doesn’t find the key, it raises a `KeyError`
      raise KeyError(key)

   def search(self, key):
      # gets the index where the key-value pair should be stored
      index = self._hash(key)

      current = self.table[index]
      while current:
         # If it finds the key, it returns the associated value
         if current.key == key:
            return current.value        
         current = current.next
      
      raise KeyError(key)

   def capacity(self):
      return self.capacity

   def __len__(self):
      return self.size
   
   # prints the hash table
   def __str__(self):
      result = ""
      for i, bucket in enumerate(self.table):
         result += f"Bucket {i}: "
         current = bucket
         while current:
            result += f"({current.key}: {current.value}) ->"
            current  = current.next
         result += "None\n"
      return result
         
# Create a hash table with a capacity of 5 
ht = HashTable(5)

# Add some key-value pairs to the hash table 
ht.insert("apple", 3)
ht.insert("banana", 2)
ht.insert("cherry", 5)
ht.insert("orange", 1)

print(ht)

# Get the value for a key 
print(ht.search("banana"))
# print(ht.search("orange"))

# Update the value for a key 
ht.insert("banana", 4)
print(ht.search("banana"))

# Check the size of the hash table 
ht.remove("apple")
print(len(ht))