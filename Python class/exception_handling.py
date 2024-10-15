# exception is an event detected during code execution and affects the flow of the program. So,
# any peice of code that could lead to an exception can be treated as done below

try:
    numerator = int(input("Enter the number to be divided: "))
    denominator = int(input("divide by: "))
    result = numerator / denominator
except ZeroDivisionError as error_message:
    print(error_message)
    print("You can't divide by zero.")
    # variable can be added to display the error type
except ValueError as error_message:
    print(error_message)
    print("Numbers only please")
except Exception as error_message:
    print(error_message)
    print("Something's not right!")
else:
    print(result)
