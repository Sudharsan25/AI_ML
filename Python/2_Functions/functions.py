addition = lambda x, y: x + y

print(addition(5, 3))

# map and lambda function

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers)) # map takes two arguments: a function and an iterable
# it applies the function to each element of the iterable and returns a map object
print(squared_numbers)

# filter and lambda function

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # filter takes two arguments: a function and an iterable
# it applies the function to each element of the iterable and returns a filter object
print(even_numbers)