#
def string1():
    s = "I love you"
    # 大小写
    print(s.capitalize()) # 首字母大学
    print(s.casefold()) # 所有字符小写
    print(s.title()) # 单词首字母大写
    print(s.swapcase()) # 大小写字母翻转
    print(s.upper()) # 所有字符大写
    print(s.lower()) # 所有字符小写
    print()
    # 对齐
    print(s.center(20)) # 居中
    print(s.ljust(20)) # 左对齐
    print(s.rjust(20)) # 右对齐
    print(s.zfill(20)) # 0填充，一般报表常用
    print(s.center(20, "-")) # 指定填充符
    print()
    # 计数
    print(s.count("o")) # 计数
    print(s.find("o"))  # 左侧查找
    print(s.rfind("o")) # 右侧查找
    #print(s.index("x")) # 找不到直接报错
    print()
    # 替换
    print(s.replace("you", "her"))
    print(s.translate(str.maketrans("opqrst", "123457"))) # 按映射表替换
    print()
    # 判断和检测
    print(s.startswith("I"), s.startswith("H")) # 判断开始
    print(s.endswith("you")) # 判断结束
    print(s.startswith(("I", "You", "Her"))) # 第一参数可以是一个元组，满足1个就是true
    print(s.isupper(), s.upper().isupper()) # 判断是否全是大写
    print(s.islower(), s.lower().islower())
    print("12345".isdecimal()) # 判断是否是数字
    print("12345".isdigit())   # 尺度适中
    print("12345".isnumeric()) # 支持中文
    print()
    print()
    print()
    print()
    print()

string1()