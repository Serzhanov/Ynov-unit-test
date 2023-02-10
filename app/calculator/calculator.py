class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        # ADDED CODE HERE TO PASS THE TEST
        if y < 0:
            raise ValueError("powering with negative value")

        result = 1
        for i in range(y):
            result *= x
        return result

    def square_root(self, x):
        # ADDED CODE HERE TO PASS THE TEST
        if x < 0:
            raise ValueError("rooting with negative value")
        if x == 0 or x == 1:
            return x
        val = x
        precision = 0.0000001
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2
        return val


def calculate(operation, x, y):
    obj = Calculator()
    if operation == "add":
        result = obj.add(x, y)
    elif operation == "substract":
        result = obj.subtract(x, y)
    elif operation == "multiply":
        result = obj.multiply(x, y)
    elif operation == "divide":
        result = obj.divide(x, y)
    elif operation == "power":
        result = obj.power(x, y)
    elif operation == "square_root":
        result = obj.square_root(x)
    return result


# operation = input(
#     "Enter the operation you would like to perform (add,subtract, multiply, divide, square_root, power): "
# )
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the secod number : "))
# print(calculate(operation, num1, num2))
