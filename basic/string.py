# 字符串有4种形式
#   单引号: 可以带转义字符
#   双引号: 也可以带转义字符
#   Note: 在 Python 中，单引号 ' 和双引号 " 功能完全一样，都用来表示字符串。
#        唯一的小区别是：当字符串内包含单引号时，用双引号包裹可以避免转义；
#        反之，包含双引号时用单引号包裹更方便。除此之外，没有性能或类型上的差别。
#   三引号: 长字符串，类似于golang的反引号
#   r开头：原始字符串，可以屏蔽各种转义
# 字符串拼接：
#   +号 和 *号
def str1():
    s1 = 'I\'m a teacher'
    s2 = "I'm a teacher" # 双引号避免单引号的转移
    s3 = "she said: \"I'm a teacher\""
    s4 = r"she said: \"I'm a teacher\"" #原始字符串，屏蔽任意转移字符
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

#str1()

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


#str1()
#str2()
random1()
