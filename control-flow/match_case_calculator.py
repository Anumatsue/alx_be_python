num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+,-,*,/): ")
#result_1 = num1 + num2
#result_2 = num1 - num2
#result_3 = num1 * num2
#result_4 = num1/num2

match (operation):
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"The result is {num1 / num2}")
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")