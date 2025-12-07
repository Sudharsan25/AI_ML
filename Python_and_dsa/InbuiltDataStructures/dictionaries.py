#creating an dict

student = {'name':'Susa', 'age':24}

# accessing elements in dict

# method 1

print(student['name'])

# method 2

print(student.get('age'))
print(student.get('grade'))
print(student.get('grade',"Not available"))

# Modifying dictionary elements
# Dictionaries are mutable, which allows you to add, update and delete elements

student['age']=25 # updates value
print(student)

student['last_name'] = "Kumar" # Add a new key: value pair
print(student)

del student['last_name'] # deletes a key: value pair
print(student)

# Dictionary methods

keys = student.keys()
print(keys)

values = student.values()
print(values)

items = student.items()

## shallow copy

student_copy = student ## Assigning this way creates a pointer to the same dict. Which means if you update one the other will also get updated
print(student)
print(student_copy)

student_copy_1 = student.copy() ## Creates a shallow copy

print(student)
print(student_copy_1)

student["name"] = "Susa"

print(student) ## Only this get changed
print(student_copy_1) ## This doesn't change as its a shallow copy

# iterate over dictionaries

for keys in student.keys():
    print(keys)

for values in student.values():
    print(values)

# Iterate over key value pairs

for key, value in student.items():
    print(f'{key}:{value}')

# Dictionary comprehension

squares_even = {x:x**2 for x in range(10) if x%2==0}

# Merge 2 dictionaries into 1

dict_1 = {"a":1, "b":2}
dict_2 = {"b":3, "c":4}

merged_dict = {**dict_1, **dict_2} # similar to spread operator in JS "...[list]" **dict will add any key value pairs in dict to the new merged dictionary

print(merged_dict)