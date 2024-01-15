## function with parameter
# def even_odd(number):
#    if (number%2 == 0):
#       return "Even"
#    return "Odd"

# print(even_odd(6))


# def even_odd(number):
#       return number%2 == 0
   
# print(even_odd(6)) ## True


# def display(name, city):
#       return "{} lives in {}".format(name, city)

# print(display("John", "Toronto")) ## John lives in Toronto
# print(display("John")) ## TypeError: display() missing 1 required positional argument: 'city'


## default value in parameter
# def display(name, city = "Toronto"):
#       return "{} lives in {}".format(name, city)

# print(display("John", "Ottawa")) ## John lives in Ottawa


# def display(name, city = "Toronto"):
#    return {'name': name, 'city': city}

# print(display("John", "Ottawa")) ## {'name': 'John', 'city': 'Ottawa'}


## Python uses pass by reference in functions. 
## Passing a list and changing it inside the function would result in modifying original
# def modifyList(numbers):
#    numbers[0] = 100

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]

# modifyList(numbers)
# print(numbers) # [100, 2, 3, 4, 5]


## Not change the original list
# def modifyList(numbers):
#    new_list = numbers.copy()
#    new_list[0] = 100

# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# modifyList(numbers)
# print(numbers) # [1, 2, 3, 4, 5]


## loop
# def max(numbers):
#    maximum = numbers[0]
#    for number in numbers:
#       if (number > maximum):
#          maximum = number

#    return maximum
# print(max([1,2,3,4,5])) # 5


# def isPalindrome(word):
#    return word == word[::-1] # reverse word

# print(isPalindrome("eye")) # True
# print(isPalindrome("hello")) # False
# # eye madam racecar


## Class --> Object Oriented Programming
# class Vehicle:   
#    def __init__(self, name=None, kms=None): # create data memebers; self is default
#       self.name = name 
#       self.kms = kms

#    def display(self):
#       print("Name: {}, KMs: {}".format(self.name, self.kms))
   
#    ## getters and setters
#    def setName(self, name):
#       self.name = name
   
#    def setKms(self, kms):
#       self.kms = kms

# v1 = Vehicle("Toyota RAV4", 1234)
# v1.display()
# v1.setName("Honda CRV")
# v1.setKms(456)
# v1.display() # Name: Honda CRV, KMs: 456

# # v2 = Vehicle() # TypeError: Vehicle.__init__() missing 2 required positional arguments: 'name' and 'kms'
# # v2.display() # Name: None, KMs: None ==> Default value('None')

# ## Class Inheritance - super()
# class Car(Vehicle):
#    def __init__(self, name=None, kms=None, capacity=None):
#       super().__init__(name, kms) # super: access the parent class
#       self.capacity = capacity

#    def display(self):
#       super().display()
#       print("Capacity:", self.capacity)

# car = Car("Toyota", 1234, 5)
# car.display() # can call display() from Vehicle class


class Numbers:
   def __init__(self, numbers):
      self.numbers = numbers
   
   def display(self):
      print(self.numbers)

   def getMax(self):
      return max(self.numbers)
   
   def getMin(self):
      return min(self.numbers)
   
   def getSum(self):
      return sum(self.numbers)
   
   def getAverage(self):
      return self.getSum()/len(self.numbers)
   
   def isEmpty(self):
      return len(self.numbers) == 0 
   
   def sortList(self):
      return sorted(self.numbers)
   
   def search(self, number):
      return number in self.numbers
   
numbers = Numbers([1,2,8,4,7])
numbers.display()
print("Max:", numbers.getMax()) # Max: 8
print("Min:", numbers.getMin()) # Min: 1
print("Sum:", numbers.getSum()) # Sum: 22
print("Average:", numbers.getAverage()) # Average: 4.4
print("Is Empty:", numbers.isEmpty()) # Is Empty: False
print("Sorted List:", numbers.sortList()) # Sorted List: [1, 2, 4, 7, 8]
print("Search:", numbers.search(3)) # Search: False