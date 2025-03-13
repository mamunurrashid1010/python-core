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