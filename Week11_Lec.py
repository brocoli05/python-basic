class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

## Time complexity: O(logn)
class BinarySearchTree:
   def __init__(self):
      self.root = None

   def insert_node(self, value):
      node = Node(value) # left = None, value = 11, right = None

      if self.root is None:
         self.root = node
      else:
         current = self.root
         parent = None # or self.root

         while True:
            parent = current
            if value < current.value:
               current = current.left
               if current is None: # empty, available to insert node
                  parent.left = node
                  return
            else:
               current = current.right
               if current is None: # empty, available to insert node
                  parent.right = node
                  return 
   
   def print_nodes(self):
      stack = []
      current = self.root

      while current or stack: # current or stack is not empty
         if current: # push
            stack.append(current)
            current = current.left
         else: # pop
            current = stack.pop()
            print(current.value) 
            current = current.right # move to the right after printing node

   def search(self, value):
      current = self.root

      while current and current.value != value:
         if value < current.value:
            current = current.left
         else:
            current = current.right

      return current

   # def remove(self, value):
   #    if self.root is None:
   #       return
      
   #    current  = self.root
   #    if value < current.value:
   #       self.remove(current.left, value)
   #    elif value > current.value:
   #       self.remove(current.right, value)
   #    else:
   #       # case 1) no child
   #       if current.left is None and current.right is None:
   #          current = None
   #       # case 2) 1 child
   #       elif current.left is None:
   #          temp = current
   #          current = current.left
   #          del temp

   #       elif current.right is None:
   #          temp = current
   #          current = current.right
   #          del temp
   #       # case 3) 2 children
   #       else:
   #          temp = min(current.right)
   #          current.value = temp.value
   #          current.right = self.remove(current.right, temp.value)

   #    return current
   def remove(self, value):
        self.root = self.remove_node(self.root, value)

   def remove_node(self, current, value):
      if current is None:
         return current

      if value < current.value:
         current.left = self.remove_node(current.left, value)
      elif value > current.value:
         current.right = self.remove_node(current.right, value)
      else:
         # Case 1: No child or only one child
         if current.left is None:
               return current.right
         elif current.right is None:
               return current.left
         
         # Case 2: Node to be removed has two children
         # Find the minimum value node in the right subtree
         min_right_subtree = self.min_value_node(current.right)
         # Replace current node's value with that of the minimum value node
         current.value = min_right_subtree.value
         # Delete the minimum value node from the right subtree
         current.right = self.remove_node(current.right, min_right_subtree.value)

      return current

   def  min_value_node(self, node):
      current = node
      while current.left is not None:
         current = current.left
      return current





tree = BinarySearchTree()
tree.insert_node(5)
tree.insert_node(10)
tree.insert_node(2)
tree.insert_node(11)
tree.insert_node(1)
tree.insert_node(3)
tree.insert_node(20)
tree.insert_node(15)
tree.insert_node(90)

tree.print_nodes()

print("Found" if tree.search(2) != None else "Not Found")
print("Found" if tree.search(21) != None else "Not Found")

# tree.remove(90)
tree.remove(20)
tree.print_nodes()