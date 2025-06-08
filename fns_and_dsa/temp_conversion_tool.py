FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius
user_temp = float(input("Enter the temperature to convert: "))
scale = input("Is this temperature in celsius or fahrenheit? (C/F): ")
if scale == "C":
    result = convert_to_fahrenheit(user_temp)
    print(f"{user_temp}\u00B0C is {result}\u00B0F")
elif scale == "F":
    result = convert_to_celsius(user_temp)
    print(f"{user_temp}\u00B0F is {result}\u00B0C")
else:
    print("Invalid input")
