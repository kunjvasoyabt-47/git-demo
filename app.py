try: 
    print("Attempting to divide by zero")
    result = 10/0
    print(result)
except ZeroDivisionError: 
    print("Cannot divide by zero")