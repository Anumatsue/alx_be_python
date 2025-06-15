"""class outofstock(Exception):
    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."
    
product_inventory = { "apple": 10, "banana":5, "orange": 0, "grapes": 3}

def purchase_item(item, quantity):
    try:
        if product_inventory[item] <= 0:
            raise outofstock(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

item1 = purchase_item("apple", 11)
print(item1)
print(product_inventory)"""
"""def calc_num(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError
    except:
        print(f"Cannot divide by zero")
    else:
        print(f" Your answer is : {x/y}.")
    finally:
        print("Great Arithmetic")

operation = calc_num(5, 0)
print(operation)"""

class ValueTooHighErro(Exception):
    def __init__(self, num1):
        self.num1 = num1
    
def My_Num(num):

    try:
        if num > 100:
            raise ValueTooHighErro
    except:
        print("Number too high")
    else: 
        print("You are on track")
    finally:
        print("Way to go!!!!!")

Result = My_Num(900)
print(My_Num)
 