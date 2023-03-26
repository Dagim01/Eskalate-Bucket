class ArthimeticClass:
    def add(x, y):
        # adding two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        return x + y
    def subtract(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        return x - y
        # subtracting two numbers
    def multiply(x, y):
        # multiplying two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        return x * y
    def divide(x, y):
        # dividing two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        if y==0:
            raise ZeroDivisionError("Denominator should be different from 0")
        return x / y