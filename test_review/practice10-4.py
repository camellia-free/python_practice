while True:
    name = input("please tell me your name.")
    with open('guest_book.txt', 'a') as file_object:
        print(f"hello {name}")
        file_object.write(f"name,\n")
        # print('\n')