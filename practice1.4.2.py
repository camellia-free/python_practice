# 统计一句话中字母出现的次数

text = 'Like the castle in its corner in a medieval game, I foresee terrible \
    trouble and I stay here just the same'
my_dict = {}
vo = 'abcdefghijklmnopqrstuvwxyz'
for i in text:
    i = i.lower()
    if i in vo:
        if i in my_dict:
            my_dict[i] += 1
            
        else:
            my_dict[i] = 1
            
print(my_dict)

# 一开始我的结果一直是{i:1}, 这是因为我将my_dict[i]写成了my_dict['i'],不应该加引号，字母从循环中出来后就是字符串的形式，加引号多此一举。