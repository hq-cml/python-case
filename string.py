# Note：字符串有3种形式
#  单引号: 可以带转义字符
#  双引号: 也可以带转义字符
#  三引号: 长字符串，类似于golang的反引号
# Note：原始字符串
#  r开头，可以屏蔽各种转义
# Note: +号 和 *号
#  字符串拼接
def str1():
    s1 = 'I\'m a teacher'
    s2 = "I'm a teacher"
    s3 = "she said: \"I'm a teacher\""
    s4 = r"she said: \"I'm a teacher\""
    s5 = """
        面朝大海
        春暖花开
    """
    s6 = s5 * 3
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)

# Note: input()
#  捕获终端输入
def str2():
    name = input("""who are you?
input:""")
    print(name)

# Note: 随机数
#  random模块，需要提前导入
import random
def random1():
    i = random.randint(1,10)
    print(i)

# Note 逻辑运算符
#      and or not
#      短路原则
def bool1():
    print(3 and 4)
    print(3 or 4)
    print(not 3)

#str1()
#str2()
#random1()
bool1()