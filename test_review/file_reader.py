with open ('pi_million_digits.txt') as file_object:
    # contents = file_object.read()
# print(contents.rstrip())
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
# print(pi_string)
# print(len(pi_string))
bir = input("please entry your birthday,in the form mmddy:")
if bir in pi_string:
    print("your birthday in pi")
else:
    print("sorry,but it's not in.")