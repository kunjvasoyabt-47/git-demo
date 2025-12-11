try: 
    print("Hello from feature branch!")
    result = 10/0
    print(result)
except ZeroDivisionError: 
    print("Cannot divide by zero")