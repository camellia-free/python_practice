import random
list1 = ['赵', '钱', '孙', '李']
list2 = ['如梦', '雾月', '木星', '子陵']
num_1 = random.randint(0, 3)
num_2 = random.randint(0, 3)
ge_name = "{}{}".format(list1[num_1], list2[num_2])
print(ge_name)