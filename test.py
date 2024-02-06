# def running(nums):
#    for i in range(1, len(nums)):    # O(1) + O(1) + O(1) + O(n)
#       nums[i] = nums[i-1] + nums[i] # O(1) + O(1)
#    return nums                      # O(1)

# print(running([3,1,2,10,1]))

# # Step 1: n for nums, T(n) for function time complexity
# # Step 2:
# # Step 3: O(1) + O(1) + O(1) + O(n) + O(n)[O(1) + O(1)] + O(1)
# # Step 4: O(4) + O(n) + O(n) = O(4) + O(2n) = O(2n) = O(n)
# # Step 5: T(n) = O(n)
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
         print(self.stack[::-1])

print("Stack============")
arr = Stack()
arr.push(3)
arr.push(2)
arr.push(6)
arr.display()

print("-------------------")
arr1 = Stack()
arr1.push(5)
arr1.push(3)
arr1.push(4)
arr1.push(2)
arr1.display()
arr1.pop()
arr1.display()
arr1.pop()
arr1.display()
arr1.push(6)
arr1.display()

class Queue:
   def __init__(self):
      self.queue = []
   
   def is_empty(self):
      return len(self.queue) == 0
   
   # Adds an item to the queue
   def enqueue(self, data):
      self.queue.append(data)

   # Removes an item from the queue
   def dequeue(self):
      if self.is_empty():
         print("Queue is empty")
      return self.queue.pop()
   
   def size(self):
      return len(self.queue)
   
   def display(self):
      if self.is_empty():
         print("Queue is empty")
      else:
         print(self.queue)

print("Queue============")
arr2 = Queue()
arr2.enqueue(3)
arr2.enqueue(2)
arr2.enqueue(6)
arr2.display()


from collections import deque

class Deque:
   def __init__(self):
      self.deque = deque()
   
   def is_empty(self):
      return len(self.deque) == 0
   
   # Adds an item to the deque
   def push_front(self, data):
      self.deque.appendleft(data)

   def push_back(self, data):
      self.deque.append(data)

   # Removes an item from the deque
   def pop_front(self):
      if self.is_empty():
         print("Deque is empty")
      return self.deque.popleft()
   
   def pop_back(self):
      if self.is_empty():
         print("Deque is empty")
      return self.deque.pop()

   def size(self):
      return len(self.deque)
   
   def display(self):
      if self.is_empty():
         print("Deque is empty")
      else:
         # print(self.deque)
         print(list(self.deque))

print("Deque============")
arr3 = Deque()
arr3.push_front(2)
arr3.push_back(3)
# arr3.display() # [2, 3]
arr3.push_front(6)
arr3.display()

print("-------------------")
arr4 = Deque()
arr4.push_front(2)
arr4.push_back(3)
# arr4.display() # [2, 3]
arr4.push_back(6)
arr4.display()

print("-------------------")
arr5 = Deque()
arr5.push_front(2)
arr5.push_back(4)
arr5.push_back(3)
arr5.push_back(5)
arr5.display() # [2, 4, 3, 5]
arr5.pop_back()
arr5.display()
arr5.push_front(6)
arr5.display()

print("-------------------")
arr6 = Deque()
arr6.push_front(2)
arr6.push_back(4)
arr6.push_back(3)
arr6.push_back(5)
arr6.display()
arr6.pop_front()
arr6.display()
arr6.push_back(6)
arr6.display()
arr6.pop_front()
arr6.display()
arr6.push_back(7)
arr6.display()