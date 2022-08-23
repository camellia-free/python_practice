print("输入quit来停止询问")
while True:
    with open('reason.txt', 'a') as file_object:
        reason = input("please tell me why you like pYThon？")
        if reason == 'quit':
            print("bye~")
            break
        else:
            file_object.write(f"{reason}\n")
        