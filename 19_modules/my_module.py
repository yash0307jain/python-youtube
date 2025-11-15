# variables
app_name = "Yash App"
version = 1.0


# functions
def greet(name: int) -> str:
    return f"Welcome {name}"


def add(num1: int, num2: int) -> int:
    return num1 + num2


# class
class Calculator:
    def multiply(self, num1: int, num2: int) -> int:
        return num1 * num2
