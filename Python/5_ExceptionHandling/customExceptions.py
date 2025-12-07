# custom exception

# This code defines a custom exception class `dobException` that inherits from a base class `CustomError`.
# The script prompts the user for their birth year and calculates their age.
# Depending on the age, it raises the `dobException` with appropriate messages if the user is not an adult or not born yet.

class CustomError(Exception):
    """Base class for custom exceptions in this module."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.code = 500
    def __str__(self):
        return f"CustomError: {self.message} (code: {self.code})"

class dobException(CustomError):
    pass

year = int(input("Enter your birth year: "))

try:
    age = 2025 - year
    if age < 0:
        raise dobException("You are not born yet!")
    elif age > 18:
        print("You are an adult.")

    elif age == 18:
        print("You are 18 years old.")
    else:
        raise dobException("You are not an adult yet!")

except dobException as e:
    print(e)