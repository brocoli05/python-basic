def calculate_sum(numbers, n):
   ## base case
   if n == 0: # size is zero  # O(1)
      return 0                # O(1)
   else:
      return numbers[n - 1] + calculate_sum(numbers, n - 1) # O(1) + O(n)

numbers = [1,2,3,4,5]
calculate_sum(numbers, len(numbers))

#  0 1 2 3 4
# [1,2,3,4,5]

# sum([1,2,3,4,5], 5)
# 1 + sum([1,2,3,4,5], 0) = 0 = 1
# 2 + sum([1,2,3,4,5], 1) = 1 + 2 = 3
# 3 + sum([1,2,3,4,5], 2) = 3 + 3 = 6
# 4 + sum([1,2,3,4,5], 3) = 6 + 4 = 10
# 5 + sum([1,2,3,4,5], 4) = 10 + 5 = 15

## Lab3 - Part 1:
def linear_search(list, key):
   search_recursion(list, key, index)

def search_recursion(list, key, index):
   pass

## Lab3 - Part 2:
def function3(value, number):
	if (number == 0):                    # O(1)
		return 1                          # O(1)
	elif (number == 1):                  # O(1) 
		return value                      # O(1)
	else:
		half = number // 2                # O(1)
		result = function3(value, half)   # O(logn) ==> number reduced by half
		if (number % 2 == 0):             # O(1)
			return result * result
		else:
			return value * result * result # O(1)
