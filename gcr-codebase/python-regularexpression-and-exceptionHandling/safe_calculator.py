try:
    a = 10
    b = 'a'
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero.")
except TypeError:
    print("Error: Invalid input type.")