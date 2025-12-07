list = ['1','2','3']

# lists or 1d arrays
# accessing elements

print(list[1:2]) #lst[startIndex:endIndex] #endIndex is not included

print(list[::2]) #list[::Step]

# Iterate over lists
for i in list:
    print(i)

# Iterating over Index
for index,element in enumerate(list):
    print(index,element)

# lst comprehension

[x for x in range(10) if x%2==0]

# nested list comprehension
list2= ['2','4','6']

[i+j for i in list for j in list2]