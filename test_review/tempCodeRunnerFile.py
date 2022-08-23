from curses.ascii import isdigit


from _curses import*
num = input("please:")
a = ''
for i in num:
    if str.isdigit(i):
        a += i
    else:
        break
print(a)