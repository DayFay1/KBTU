to_do_list = []
while True:
    print("Here is the list:")
    for item in to_do_list:
        print("- " + item)
    
    new_item = input("What do you want to add (type 'nothing' to exit): ")
    if new_item.lower() == "nothing":
        print("Here is the final list:")
        for item in to_do_list:
            print("- " + item)
        print("Goodbye!")
        break
    else:
        to_do_list.append(new_item)

