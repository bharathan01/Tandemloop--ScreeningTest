
#calculator using python language

class Calculator:
    def __init__(self):
        pass

    def add(self,a , b):
        return a + b

    def subtract(self, a , b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self,a, b):
        if b == 0:
            return "Error"
        return a/b


my_calculator = Calculator()


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the type of operation (+, -, *, /): ")

if operation == ' +':
    result = my_calculator.add(a , b)
elif operation == '-':
    result = my_calculator.subtract(a , b)
elif operation == '*':
    result = my_calculator.multiply(a , b)
elif operation == '/':
    result = my_calculator.divide(a , b)
else:
    result = "Invalid"


print(f"Result of {a} {operation} {b} = {result}")
