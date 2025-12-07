## try, except blocks

try:
    a = b
except NameError as e:
    print("NameError:", e)

# Exception class

try:
    result = 1 / 12
    a = b

except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
except Exception as e:
    print("Caught Exception:", e)

# try, except, else and finally

try:
    a = 1 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
else:
    print("No exception occurred, a =", a)
finally:
    print("This block always executes, regardless of exceptions")