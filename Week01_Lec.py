# first = "Seneca"
# last = "College"

# print("hello, world!")
# print(first, last)
# print(f"hello {first}")
# print("hello {} {}".format(first, last))

########################################
# num = 6

# if (num%2 == 0):
#    print("even")
# else:
#    print("odd")

# if (num != 10):
#    print("Not a 6")

########################################
# name = "Seneca"
# campus = "Newnham"

# if name == "Seneca" and campus == "Newnham":
#    print("My campus")
# else:
#    print("Other campus")

# if (name not in "Senece"):
#    print("I dont like it")

########################################
# flag = False

# if (not flag):
#    print("Hello")

########################################
# elif
# marks = 96

# if(marks >= 90):
#    print("A")
# elif(marks >= 80):
#    print("B")
# elif(marks >= 80):
#    print("C")
# else:
#    print("F")   

########################################
# int --> TypeError: not all arguments converted during string formatting
# num = input("Enter a number: ")

# if (int(num)%2 == 0):
#    print("Even")

########################################
# loop - 1) while
# prompt = input("Enter a fruit (press q to quit):")

# while (True):
#    if (prompt == 'q'):
#       break
#    prompt = input("Enter a fruit (press q to quit):")

# loop - 2) for
# for i in range(0, 10, 2): # range(startString, ending, step); increment by 2
#    print(i)

########################################
# Arrays = Lists
   
fruits = ["Apple", "Orange", "Banana"]
# print(fruits)
# print(fruits[0].upper()) # APPLE
# print(fruits[-1]) # Banana

# fruits[0] = "Pine Apple" # modify the value in an array

# fruits.append("Pine Apple") # add new value to the last in an array

# fruits.remove("Apple") # remove the matched value in an array

# fruits.pop() # delete the last one

# fruits.pop(0) # delete the first one

fruits.sort() # sort the value in ascending order

print(fruits)


numbers = [1,7,3,2,6,4,10]

## sort
# print(numbers.sort()) # None --> sort() returns None
# numbers.sort()
# print(numbers)

## for loop
for i in numbers:
   if (i%2 == 0):
      print(i)

## Slicing
print(numbers[0:5]) # [1, 7, 3, 2, 6]
print(numbers[:]) # print all
print(numbers[5:]) # [4, 10]
print(numbers[0:6:2]) # [1, 3, 6] --> increment by 2
print(numbers[1::2]) # [7, 2, 4]
print(numbers[::-1]) # [10, 4, 6, 2, 3, 7, 1] --> reverse order


## Dictionary
students = {
   "name": "John",
   "age": 30
   }
print(students["name"]) # pass the key
print(students["age"])