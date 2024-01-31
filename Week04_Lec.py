## Simple sorting - bubble sort, selection sort ------------------------------------------
def bubble_sort(numbers):
   for i in range(len(numbers)):
      for j in range(len(numbers) - i - 1): # -1: no need to compare the last element
         if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
   return numbers      

# Time complexity: O(n^2) ==> considering it is getting important (cost of cloud service)
numbers = [2,5,1,4,6,9,10,8,3]
print(numbers)
print('bubble sort:', bubble_sort(numbers))


def selection_sort(numbers):
   for i in range(len(numbers)):
      smallest = i
      for j in range(i + 1, len(numbers)):
         if numbers[j] < numbers[smallest]:
            smallest = j

      if i != smallest:
         numbers[i], numbers[smallest] = numbers[smallest], numbers[i] # one line swapping

   return numbers

# Time complexity: O(n^2)
numbers = [2,5,1,4,6,9,10,8,3]
print(numbers)
print('selection sort:', selection_sort(numbers))


## Merge Sort ----------------------------------------------------------------------
def merge_sort(numbers):
   # step 1: split
   size = len(numbers)

   if size < 2: # simple case: no need to sort
      return 
   
   mid = size // 2 # split the array

   left = numbers[0:mid] # starting from index 0 to index mid
   right = numbers[mid:] # starting from index mid to the last element

   merge_sort(left) # split
   merge_sort(right) # split

   merge(numbers, left, right)

# Time Complexity: O(nlogn) -- n: merge, logn: split, calling merge function again

def merge(numbers, left, right):
   size = len(numbers)
   size_left = len(left)
   size_right = len(right)

   i = j = k = 0

   while (i < size_left and j < size_right): # not out of bounds
      if left[i] <= right[j]:
         numbers[k] = left[i]
         i += 1
      else:
         numbers[k] = right[j]
         j += 1
      k += 1

   while (i < size_left):  # leftover in the left array
      numbers[k] = left[i]
      k += 1
      i += 1

   while (j < size_right):  # leftover in the right array
      numbers[k] = right[j]
      k += 1
      j += 1

numbers = [2,5,11,4,6,9,10,8,3]
print(numbers)
merge_sort(numbers)
print('merge sort:', numbers)


## Quick Sort ----------------------------------------------------------------------
# pivot - greater than: right, less than: left
def partition(numbers, start, end):
   pivot = numbers[end] # set pivot as the last element
   i = start - 1  # pivot index for the greater element

   for j in range(start, end):
      if numbers[j] < pivot:
         i += 1
         numbers[i], numbers[j] = numbers[j], numbers[i] # swap

   i += 1
   numbers[i], numbers[end] = numbers[end], numbers[i] # swap

   return i

def quick_sort(numbers, start, end):
   if start < end:   # only if size of array more than 1
      pivotIndex = partition(numbers, start, end) 
      quick_sort(numbers, start, pivotIndex - 1)
      quick_sort(numbers, pivotIndex + 1, end)

# Time Complexity: O(nlogn), O(n^2) -- worst case depending on pivot

numbers = [5,8,6,2]
# numbers = [2,5,1,4,16,9,10,8,3]
print(numbers)
quick_sort(numbers, 0, len(numbers) - 1)
print('quick sort:', numbers)