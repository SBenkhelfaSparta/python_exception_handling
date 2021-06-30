# Zero division error: We can create an mathematical error by dividing by zero
# print(1 / 0)

# Type error:
# num = 9
# if num > 'Hello':
#     print(num)

# We will create a file with required permission and see what error/exception are observable

# First Iteration
# file = open("order.txt")  # `open()` takes a string arg with file name
# print(file)

# Task

from pack import p_exceptions
pex = p_exceptions.PExceptions()
pex.exce(input("Please enter what items you would like to add: ")) #seperate items by commas