
import os
import os.path

# read a whole file

with open('test.txt', 'r') as f:
    # read the whole file at once
    for line in f:
        print(line.strip())

# write to a file

with open('test.txt', 'w') as f: # open in w to overwrite the file
    f.write('Hello World\n')
    f.write('This is a test\n')

# without overwriting the file

with open('test.txt', 'a') as f: # open in a to append to the file
    f.write('This is a test\n')
    f.write('This is a test\n')

# write to a file

with open('test.txt', 'w') as f: # open in w to overwrite the file
    f.write('Hello World\n')
    f.write('This is a test\n')
# without overwriting the file

with open('test.txt', 'a') as f: # open in a to append to the file
    f.write('This is a test\n')
    f.write('This is a test\n')

# writing and reading a file
# w+ mode

with open('test.txt', 'w+') as f: # open in w+ to overwrite the file and read it
    f.write('Hello World\n')
    f.write('This is a test\n')
    f.seek(0) # move the cursor to the beginning of the file
    for line in f:
        print(line.strip()) # read the whole file at once

os.mkdir('test_dir') # create a directory
items = os.listdir('test_dir') # list the items in the directory
print(items) # print the items in the directory
path = os.path.join('test_dir', 'test.txt') # join the path
print(path) # print the path