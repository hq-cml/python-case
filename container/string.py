# 字符串大小写、对齐、计数、替换、各类判断、截取
def string1():
    s = "I love you"
    # 大小写转换
    print(s.capitalize()) # 首字母大学
    print(s.casefold()) # 所有字符小写（可以处理各种语言）
    print(s.title()) # 单词首字母大写
    print(s.swapcase()) # 大小写字母翻转
    print(s.upper()) # 所有字符大写
    print(s.lower()) # 所有字符小写（仅英语）
    print()

    # 对齐
    print(s.center(20)) # 字符串居中
    print(s.ljust(20)) # 左对齐
    print(s.rjust(20)) # 右对齐
    print(s.zfill(20)) # 0填充，一般报表常用
    print(s.center(20, "-")) # 指定填充符
    print()

    # 计数
    print(s.count("o")) # 计数
    print(s.find("o"))  # 左侧查找，找不到返回-1
    print(s.rfind("o")) # 右侧查找
    #print(s.index("x")) # 和find类似，区别是：找不到直接报错
    print()

    # 替换
    print(s.replace("you", "her"))
    table = str.maketrans("opqrst", "123457")
    print(s.translate(table)) # 按映射表替换
    print()

    # 判断和检测
    print(s.startswith("I"), s.startswith("H")) # 判断是否指定字符在开始位置
    print(s.endswith("you")) # 判断结束
    print(s.startswith(("I", "You", "Her"))) # 第一参数可以是一个元组，满足1个就是true
    print(s.isupper(), s.upper().isupper()) # 判断是否全是大写
    print(s.islower(), s.lower().islower())
    print("12345".isdecimal()) # 判断是否是数字
    print("12345".isdigit())   # 尺度适中
    print("12345".isnumeric()) # 支持中文
    print()

    # 截取
    print(" aaaa".lstrip())   #左trim
    print("aaabbb".rstrip("b")) #右trim，注意trip和remove是有区别的，前者是元素表，后者则是整个字符串
    print("xxxaaabbbxxx".strip("x")) #两侧trim
    print("www.ba.com".removeprefix("www."))
    print("www.ba.com".removesuffix(".com"))
    print()

#string1()

def string2():
    # 拆分拼接
    print("www.baidu.com".partition(".")) # 切分第一个部分
    print("http://www.baidu.com/abcd.html".rpartition("/"))
    print("www.baidu.com".split(".")) # 切分全部
    print("www.\rbaidu\ncom\r\nshit".splitlines()) # 这个比较牛逼，可以忽略操作系统对于换行的差异
    print(".".join(["www","baidu","com"])) # 拼接，参数是可迭代对象，例如列表或者元组（拼接的性能大于+号）
    print()

#string2()

# 格式化字符串
def string3():
    year = 2024
    str = "study at {} year".format(year)
    print(str)

    # 通过idx选择输出参数
    print("{0} love {1}".format("i", "you"))
    print("{1} love {0}".format("i", "you"))

    # 关键字参数
    print("I am {name}, I love {fav}".format(name="foo", fav="bar"))

    # {}转义
    print("I am {}, {{}} is format string".format("foo"))

    print("------")
    # 高级用法（:冒号左侧是位置符，（只有一个参数可以忽略）
    #        代表format的参数，用来占位）
    print("{:^10}".format(250)) #右对齐，10是宽度
    print("{1:>10}{0:<10}".format(250, 520)) # 右对齐 + 左对齐
    print("{:010}".format(520)) #右对齐，左侧补0
    print("{:+}{:-}".format(520, -250)) #正负号
    print("{:,}".format(1234)) # 千分位分隔符
    print("{:.2f}".format(3.1415926)) # 小数点后，两位小数
    print("{:.2g}".format(3.1415926)) # 小数点前后总共2位数
    print("{:.5}".format("abcdefg")) # 字符串长度保留
    print("{:b}".format(16)) # 二进制
    print("{:c}".format(80)) # unicode
    print("{:d}".format(80)) # 十进制
    print("{:o}".format(16)) # 八进制
    print("{:x}".format(15)) # 16进制
    print("{:#x}".format(15)) # 16进制，井号表示，带一个进制前缀
    print("{:e}".format(3.14)) # 科学计数法
    print("{:E}".format(3.14)) # 科学计数法，小e变大E
    print("{:f}".format(3.14)) # 浮点，默认6位精度
    print("{:g}".format(12345678)) # 默认，小数以f形式输出，大数以科学计数法输出
    print("{:%}".format(0.98)) # 百分号，默认乘以100
    print("{:.2%}".format(0.98)) # 两位精度的百分号
    print("{:.{prec}f}".format(3.1415, prec=3)) # 精度作为参数

#string3()

# f字符串：格式化字符串的语法糖
#  1. 去掉format
#  2. 在双引号前面加上f或者F
#  3. 要填写的动态内容，直接放到{}中冒号的左侧，冒号的右侧则是长度精度之类的信息
def string4():
    print(f"1+2={1+2}")
    print(f"{-520:010}")
    print(f"{12345678:,}")
    print(f"{3.1415:.2f}")

#string1()
#string2()
#string3()
string4()