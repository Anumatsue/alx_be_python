
def display_menu():
    print("SHopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("Enter Item to be removed: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found")
        elif choice == '3':
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item} ")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

main()