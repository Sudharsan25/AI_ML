# sets are used tp store unique elements
# they are unordered and unindexed

# creating a set
my_set = {1, 2, 3, 4, 5}
print(type(my_set))  # Output: {1, 2, 3, 4, 5}

# creating an empty set

empty_set = set()
print(type(empty_set))

# sets ignore duplicates
my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set)

# adding elements to a set

my_set.add(6)

# removing elements from a set

my_set.remove(10)  # raises KeyError if the element is not found
my_set.discard(10)  # does not raise an error if the element is not found
popped_element = my_set.pop() # FIFO
print(popped_element)
# Clearing a set

my_set.clear()

# mathematical operation

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

# Set membership test

my_set = {1, 2, 3, 4, 5}
print(1 in my_set)  # Output: True
### difference between intersection and intersection_update

print(set1)
set1.intersection_update(set2)  # modifies set1 in place
print(set1)

set1 = {1,2,3,4,5,6}

# Difference in sets

difference = set1.difference(set2)  # returns a new set with elements in set1 but not in set2
print(difference)

# symmetric difference

set1.symmetric_difference(set2) # return the unique elements in each sets (removes intersection elements)

# set methods

set1 = {1,2,3,4,5}

set2 = {3,4,5}

print(set1.issubset(set2))
print(set1.issuperset(set2))