def perform_operations(num1 : float, num2 : float, operation : str):
    match operation:
        case '+':
            return num1 + num2 
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1/num2
            else:
                print("Cannot divide by zero")
        case _:
            print("invalid operator")

