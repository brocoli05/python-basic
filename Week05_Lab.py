## create the linked list
class LinkedList:
   class Node: ## IMPORTANT! create the new node
      def __init__(self, data, next = None, pre = None):
         self.data  = data
         self.next = next
         self.pre = pre

   def __init__(self):
      self.front = None
      self.back = None

   def push_back(self, data):
      node = self.Node(data, None, self.back)
      # check the edge case
      if self.front is None: # linked list is empty
         self.back = None
      ## different way - check the back first
      # if self.back is None: 
      #    self.front = None
      else:         
         self.back.next = node
      self.back = node
   
   def display(self): ## print the list in reverse order
      current = self.back

      while current is not None:
         print(current.data)
         current = current.pre

   def display_even(self):
      current = self.back

      while current is not None:
         if current.data %2 == 0:
            print(current.data)
         current = current.pre
   
   def get_length(self):
      count = 0
      temp = self.front
      while temp is not None:
         count += 1
         temp = temp.next

      return count

linked_list = LinkedList()
linked_list.push_back(2)
linked_list.push_back(5)
linked_list.push_back(6)
linked_list.push_back(8)
linked_list.push_back(9)

linked_list.display()
