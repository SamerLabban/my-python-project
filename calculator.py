class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    print("Addition: ", Calculator.add(1, 2))
    print("Subtraction: ", Calculator.subtract(5, 3))
    print("Multiplication: ", Calculator.multiply(4, 3))
    print("Division: ", Calculator.divide(10, 2))
