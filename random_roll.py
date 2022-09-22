import tkinter
win = tkinter.Tk()
# 进入消息循环
win.title("点名册")  # 该语句定义窗口名称，但要放在main.loop语句前
win.geometry('320x160+650+240') # 定义窗口出现的位置，320x160是窗口尺寸大小，而650+240是位置

win.mainloop()

# print(win.title)