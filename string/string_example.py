# string print
print("Hello World")
print("Python is a popular 'programming language'")
print('It was created by "Guido van Rossum"')

# Assign String to a Variable
name = "My name is Mamunur Rashid"
print('\n'+name)

# Multiline Strings
multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print('\n'+multiline_string)

# string index
first_name = "Mamunur"
print('\n')
print(first_name[0])
print(first_name[1])
print(first_name[-1]) # last index
print('\n')

# string print using loop
for x in "apple":
    print(x)

# sting length
department = "Software development"
print(len(department))

# check string
department = "Software development"
if "Software" in department:
    print("yes, 'Software' is present")

if "python" not in department:
    print("no, 'Python' is not present")

# modify string
father_name = "Hossain"
print("\n")
print(father_name.upper()) # Upper Case
print(father_name.lower()) # Lower Case
print(father_name.capitalize()) # Capital
print(father_name.replace('n','o')) # replace

# splite string : The split() method returns a list where the text between the specified separator becomes the list items.
department =  "Software Development"
print(department.split(' '))

# String Concatenation
first_name = "Mamunur"
last_name = "Rashid"
full_name = first_name + " " + last_name
print(full_name)


# Format String
name = "Mamun"
dummy_text = "My name is " + name
dummy_text1 = f"My name is {name}"
print(dummy_text1)
