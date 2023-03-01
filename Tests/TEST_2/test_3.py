shopping_list = ['Potatoes']

while True:
    print("Here is the shopping list:")
    for item in shopping_list:
        print(f"- {item}")
    
    choice = input("Do you want to add something (enter 1) or remove something (enter 2) or exit (enter 0): ")
    
    if choice == '1':
        item_to_add = input("What do you want to add: ")
        shopping_list.append(item_to_add)
    elif choice == '2':
        item_to_remove = input("What do you want to remove: ")
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
        else:
            print(f"{item_to_remove} is not in the shopping list.")
    elif choice == '0':
        break
    else:
        print("Invalid choice, please enter 1, 2, or 0.")
        
print("Here is the final shopping list:")
for item in shopping_list:
    print(f"- {item}")
print("Goodbye!")