# # 形成儿童黑话
# vo = input("请输入一个单词：")
# vo.lower()
# # vo_1 = [str(i) for i in vo]

# if vo[0] in ['a', 'e', 'i', 'o', 'u']:
#     vo_2 = vo + 'way'
    
# else:
#     vo_2 = vo[1:-1] + vo[0]+'ay'
# print(vo_2)


x = 1
while x:
    x = int(input("输入是否要继续1/0?"))
    vo = input("请输入一个单词：")
    vo.lower()
    vo_1 = [str(i) for i in vo]
    if vo[0] in ['a', 'e', 'i', 'o', 'u']:
        vo_2 = vo + 'way'
        continue
        
    else:
        vo_2 = vo[1:-1] + vo[0]+'ay'
        print(vo_2)
        continue