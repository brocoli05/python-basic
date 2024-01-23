def toUpperString(message): # Seneca College
   result = ''

   for char in message:       
      if ord(char) >= 97:
         result += chr(ord(char) - 32)
      else:
         result += char

   return result

# ## Prof's Answer
# def toUpperString(message): # Seneca College
#    count = 0
#    for ch in message: 
#       if ch.isupper():
#          count+= 1
#          if count>=2:
#             return message.upper()
#    return message

print(toUpperString('Seneca College'))


## Prof's Answer 1
# def remove_duplicates(fruits):
#    result = []

#    for fruit in fruits:
#       if fruit not in result:
#          result.append(fruit)

#    return result   # ['Grapes', 'Apple', 'Banana']

## Prof's Answer 2
def remove_duplicates(fruits):
   return list(set(fruits)) # ['Apple', 'Grapes', 'Banana']

print(remove_duplicates(['Grapes', 'Apple', 'Grapes', 'Banana']))


## Prof's Answer
def is_common(first, second):
   for i in first:
      if i in second:
         return True
   
   return False

print(is_common([1, 2, 3], [2, 4, 5])) # True


## Prof's Answer
def second_smallest(lst):
   return sorted(lst)[1]

print(second_smallest([5, 2, 1, 3, 4]))


## Prof's Answer 1
def get_counts(fruits):
   counts = {} # {'name': 4} counts.key()

   for fruit in fruits:
      if fruit not in counts.keys():
         counts[fruit] = 1
      else:
         counts[fruit] += 1

   return counts

## Prof's Answer 2
# from collections import Counter
# def get_counts(fruits):
#    return dict(Counter(fruits))

print(get_counts(['Apple', 'Banana', 'Apple', 'Grapes', 'Apple', 'Banana']))
# {'Apple': 3, 'Banana': 2, 'Grapes': 1}