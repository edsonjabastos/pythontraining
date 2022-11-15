from art import logo

print(logo)

# Operations
def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


while True:
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    use_last_answer = input(
        f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.: "
    )
    if use_last_answer == "y":
        operation_symbol = input("Pick another operation: ")
        num3 = int(input("What's the next number?: "))
        second_answer = calculation_function(first_answer, num3)
        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
