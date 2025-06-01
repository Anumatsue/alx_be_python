size = int(input("Enter the size of the pattern: "))
symbol = "*"
row = 0
while row < size:
    for i in range(size):
        print(symbol, end = " ")
    print()
    row += 1