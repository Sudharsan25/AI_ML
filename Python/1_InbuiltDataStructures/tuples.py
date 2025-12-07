# Tuples
# ordered and immutable

empty_tuple = ()
print(type(empty_tuple))

# can store dissimilar elements

mixed_tuple= (1,"Nim",True)

for i in mixed_tuple:
    print(type(i))

numbers = (1,2,3,4,5)

# Tuple operations

new_tuple = mixed_tuple + numbers

new_tuple = new_tuple * 3

new_tuple

# Tuple methods
print(numbers.count(1))
print(numbers.index(3))

# Packing and Unpacking tuple

packed_tuple = 1,2,"Heloo"
print(packed_tuple)

a, b, c = packed_tuple

first, *middle, last = numbers

print(a,b,c)
print(first, middle, last)