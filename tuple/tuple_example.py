# Tuple : Tuples are used to store multiple items in a single variable.

fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)
print(type(fruits))

# length
print(len(fruits))

# print index wise
print(fruits[1])
print(fruits[-1]) # print last value

# range wise print
print(fruits[0:2])

# conditional print
if "banana" in fruits:
    print("Yes, banana is available")

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

buy_fruits_tuple = ("apple","orange","cherry")
fruits_list = list(buy_fruits_tuple)
fruits_list[2] = "graps"
buy_fruits_tuple = tuple(fruits_list)
print(buy_fruits_tuple)


# for loop
for fruit in fruits:
    print(fruit)

# while loop
my_tuple = ("apple", "banana", "cherry")
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i = i + 1

