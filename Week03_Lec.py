## Searching and Sorting
# linear, binary search


## Recursion: reduce the number of lines of code

## Factorial #########################################################
# 4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! = 4 * 3 * 2 * 1 * 0!
# n! = n * (n-1)!

# def factorial(n):
#    if (n <= 1):
#       return 1
#    else:
#       return n * factorial(n - 1)

# print(factorial(0))

## Time Complexity
# f(4) = 4 * f(3) = O(1)
# f(3) = 3 * f(2) = O(1)
# f(2) = 2 * f(1) = O(1)
# f(1) = 1 * f(0) = O(1)
# f(0) = 1        = O(1) ==> T(4) = O(5), T(n) = O(n+1) = O(n)

# whenever function calls always going to be O(1)
# func call = O(1)

## Fibonacci #########################################################
# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13 
def fib(n):
   if n <= 1:
      return n
   else:
      return fib(n-1) + fib(n-2)
   
print(fib(0), fib(1), fib(2), fib(3), fib(7))

# f(4) = f(3) + f(2) = f(2) + f(1) + f(1) + f(0) = f(1) + f(0) + f(1) + f(1) + f(0)
# ==> f(1) + f(0) : -2
# L0 = 1 = 2^0
# L1 = 2 = 2^1
# L2 = 4 = 2^2
# L3 = 8 = 2^3

# T(4) = O(2^2 - 2)
# T(n) = O(2^n - 2) = O(2^n)

## Linear Search #########################################################
def linear_search(numbers, number):
   for i in numbers:
      if numbers[i] == number:
         return i 
   return -1

print(linear_search([1,2,3,4,5], 3))
# print(linear_search([1,2,3,4,5], 7))

## Binary Search #########################################################
#              10    2 1 8 9 4 10 90
# 1) Sort            1 2 4 8 9 10 90
# 2) head and tail: 1 and 90
# 3) mid = 7/2 = 3: 8
# 4) 
   # if n[mid] == num
   #    return True
   # elif num > n[mid]:
   #    head = mid + 1
   # else:
   #    tail = mid - 1

def binary_search(numbers, number):
   numbers.sort() # ignore this
   found = False  # O(1)

   head = 0       # O(1)
   tail = len(numbers) - 1  # O(1)

   while(head <= tail):     # O(log n) -- reduce half
      mid = (head + tail) // 2 # O(1)
      # //: remove decimal part
      if numbers[mid] == number: # O(1)
         found = True            # O(1)
         break # O(1)            # O(1)
      elif number > numbers[mid]:   # O(1)
         head = mid + 1             # O(1)
      else:          
         tail = mid - 1             # O(1)

   return found                     # O(1)

print(binary_search([2,1,8,9,4,10,90], 90))
# T(n) = O(1) + O(1) + O(1) + O(log n){O(1) + O(1) + O(1) + O(1) + O(1) + O(1) + O(1)} + O(1)
# T(n) = O(4) + O(log n){O(7)} = O(log n({O(7)})) = O(log n)
