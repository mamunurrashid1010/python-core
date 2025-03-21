# python list exercise
student_list = ["kamal","hasan","Noman"]
print(student_list)
print(len(student_list))
print(student_list[1]) 
print(student_list[-1]) # print last element
print(student_list[1:3])

# change list item
student_list[1] = "Arif"
print(student_list)

# conditional
fruits = ["apple","banana","orange"]
if "banana" in fruits:
    print("Yes, banana available")


# Append Items
fruits.append("graps")
print(fruits)

# Insert Items
fruits.insert(1,"watermelon")
print(fruits)

# Extend list
fruits2 = ["mango", "pineapple", "papaya"]
fruits.extend(fruits2)
print(fruits)

# remove item
fruits.remove("papaya")
print(fruits)

# loop list print
for fruit in fruits:
    print(fruit)

# short list
marks = [100, 50, 65, 82, 23]
marks.sort()
print(marks)

# short reverse
marks.sort(reverse = True)
print(marks)
