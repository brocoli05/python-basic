## Time Complexity
def search(numbers, number):
   for i in range(len(numbers)): # i=O(1) range=O(1) len=O(1), loop = n
      if numbers[i] == number:   # O(1) * n
         return True # O(1)
   return False   # O(1)
# Time Complexity = O(1) + O(1) + O(1) + O(n) + O(1) + O(1) = O(n) + O(5)

# Rule 1 = Fastest growing term  => O(n) : assumes that n is the fastest
# Rule 2 = Remove constants => O(n)

print(search([1,2,3,4,5], 3))


## 5 Steps for Analysis
def sum_elements(numbers):
   sum = 0  # O(1)

   for i in range(len(numbers)): # O(1) + O(1) + O(n)
      sum += numbers[i] # O(1) * n = O(n)
   
   return sum # O(1)

# Analysis of Algorithm in 5 steps
# Step 1: Establish your variables: size of numbers in n and T(n)
# Step 2: Count the time complexity
# Step 3: Mathmetical Expression = T(n) = O(1) + O(1) + O(1) + O(n) + O(n) + O(1)
# Step 4: Simplify the equation = O(2n) + O(4) = O(2n) (=> Rule 1) = O(n) (=> Rule 2)
# Step 5: Final Result = T(n) = O(n)


def pairs(numbers): # [1, 2, 3] = (1, 1), (1, 2), (1, 3) (2, 1)
   for i in range(len(numbers)) : # O(1) + O(1) + O(n)
      for j in range(len(numbers)): # O(1)*n + O(1)*n + O(n)*n
         print("({}, {})".format(numbers[i], numbers[j])) # O(1) *n*n

# Step 1: size of numbers is n and T(n)
# Step 2:
# Step 3: T(n) = O(1) + O(1) + O(n) + O(n) + O(n) + O(n^2) + O(n^2)
# Step 4: O(2n^2) + O(3n) + O(2) = O(2n^2) = O(n^2)
# Step 5: T(n) = O(n^2)
