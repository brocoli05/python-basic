# Array
# : (time) need to assign the size of the array, faster than linked list(stacked in a row)

# linked list
# : (memory) has nodes, flexibility(grow the size of the list depending on the RAM size), 
# : X provide fixed size, they are not next to each other, 
# : cannot go dirct to the location(always start from the first node)
# front: always going to the first node
# back: always going to the last node
# time complexity: O(n)

# doubly linked list
# : previous pointer, data, next pointer

class LinkedList:
   class Node:
      def __init__(self, data, next=None, pre=None):
         self.data = data
         self.next = next
         self.pre = pre

   def __init__(self):
      self.front = None # not pointing anywhere, no linked list
      self.back = None

   def push_front(self, data):
      node = self.Node(data, self.front) # new node
      # self.front ==> first node, self.front.next ==> second node

      if self.front is None: # linked list is empty
         self.back = None
      else: # at lest one element in the linked list
         self.front.pre = node   # connect to the new node 
      
      self.front = node # change the first node to the new node
   
   def pop_front(self): # delete the first node
      if self.front is not None:
         temp = self.front
         self.front = self.front.next # move to the next
         if self.front is None:
            self.back = None
         else:
            self.front.pre = None

   def display_nodes(self):
      current = self.front
      while current is not None:
         print(current.data)
         current = current.next

linked_list = LinkedList()
linked_list.push_front(12)
linked_list.push_front(3)
linked_list.push_front(6)
linked_list.push_front(2)
linked_list.display_nodes()
print("After deletion\n")
linked_list.pop_front()
linked_list.display_nodes()

## sentinel nodes
# : never empty nodes to avoid program crash
# front sentinel, back sentinel
# : no need to check whether self.front is None

## Stack
# : FILO
# ex) Ctrl + z, back button in browser
class Stack:
   def __init__(self):
      self.stack = []
   
   def is_empty(self):
      return len(self.stack) == 0
   
   def push(self, data):
      self.stack.append(data)

   def pop(self):
      if self.is_empty():
         print("Stack is empty")
      return self.stack.pop()
   
   def size(self):
      return len(self.stack)
   
   def display(self):
      if self.is_empty():
         print("Stack is empty")
      else:
         print(self.stack[::-1]) # ::-1 print reverse order

s = Stack()
s.push(2)
s.push(5)
s.push(1)
s.push(3)
s.push(6)
s.display()
print(s.pop())
s.display()


## Queue
# : FIFO
# ex) printing