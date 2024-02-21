# HashMap
# node has three elements: key, value, the address of index node

class Node:
   def __init__(self, key, value):
      self.key = key
      self.value = value
      self.next = None

   def get_value(self): # outside the class --> need getters and setters
      return self.value

   def get_key(self):
      return self.key
   
   def set_value(self, value):
      self.value = value
   
class HashMap: # put(), get() is COMMON function for hashmap
   def __init__(self, size):
      self.size = size
      self.table = [None] * size # array, HashMap ALWAYS needs a table
   
   def put(self, key, value): # push, insert
      hash_value = key % self.size
      node = self.table[hash_value] # going to specific index, possiblity to go 'None' or 'node'

      if node is None: # node is empty
         self.table[hash_value] = Node(key, value) # create new node
      else:
         while node.next is not None: # find the last node
            if node.get_key() == key: # if the key is the same
               node.set_value(value) # modify the value of the node
               return
            node = node.next # otherwise keep going

         if node.get_key() == key:
            node.set_value(value)
            return 
         
         node.next = Node(key, value) # link with the node to put the address into the previous node

   def get(self, key): # return the value when passing the key, NOT search function
      hash_value = key % self.size
      node = self.table[hash_value]

      while node is not None:
         if node.get_key() == key:
            return node.get_value()
         node = node.next
      
      return -1

   def search_key(self, key):
      hash_value = key % self.size
      node = self.table[hash_value]

      while node is not None:
         if node.get_key() == key:
            return node.get_value()
         node = node.next # If no match is found, it moves to the next node.
      
      return None

   
   def search_value(self, value):
      for i in range(self.size):
         node = self.table[i]
         while node is not None:
               if node.get_value() == value:
                  return node.get_key()
               node = node.next
      return None


   def remove(self, key):
      hash_value = key % self.size
      node = self.table[hash_value]
      prev_node = None

      while node is not None:
         if node.get_key() == key:
            if prev_node is None: # no previous node
               self.table[hash_value] = node.next
            else:
               prev_node.next = node.next # updates the next reference of the previous node
            return
         prev_node = node
         node = node.next
      
      return None

   def update(self, key, new_value):
         hash_value = key % self.size
         node = self.table[hash_value]

         while node is not None:
               if node.get_key() == key:
                  node.set_value(new_value)
                  return
               node = node.next

   def display(self):
      for i in range(self.size):
         node = self.table[i]
         while node is not None:
            print("Key: {}, Value: {}".format(node.get_key(), node.get_value()))
            node = node.next

hashMap = HashMap(10)
hashMap.put(1, 25)
hashMap.put(2, 35)
hashMap.put(3, 45)
hashMap.put(4, 55)
hashMap.put(5, 65)
hashMap.put(6, 75)
hashMap.remove(50)
hashMap.update(3, 50)
hashMap.display()

key = 5
result = hashMap.get(key)
if result == -1:
   print("No value found at that key")
else:
   print("Value at {}: {}".format(key, result))

key = 7
print("Value at {}: {}".format(key, hashMap.search_key(key)))
key = 3
print("Value at {}: {}".format(key, hashMap.search_key(key)))

value = 65
print("Value {} found at {}".format(value, hashMap.search_value(value)))
value = 60
print("Value {} found at {}".format(value, hashMap.search_value(value)))