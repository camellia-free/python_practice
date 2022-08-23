"""以列表的形式加载一个文本文件

参数：
文本文件的名字
异常： 若没有找到文件，则报告IOError类型的需错误
返回值：一个包含文本文件中所有单词小写形式的列表。
要求导入的模块sys
"""

import sys
def load(file):
    # 打开文本文件，并以列表的形式返回文件内容对应的小写字母
    try:
        with open(file) as in_file:
            
            load_txt = in_file.read().strip().split('\n')
            load_txt = [x.lower() for x in load_txt]
            return load_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program".format(e, file),
              file=sys.stderr)
        sys.exit(1)
            



    