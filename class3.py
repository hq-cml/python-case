#多态和鸭子类型
#Python本身就是一个动态语言，所以只需要满足鸭子，就可以是多态
class Cat:
    def say(self):
        print("i am a cat")

class Book:
    def say(self):
        print("i am a book")

#在Python中，参数甚至不需要是父类的引用，都可以实现多态
def say(x):
    x.say()

def func1():
    a = Cat()
    say(a)
    b = Book()
    say(b)

# 私有变量
# Python的哲学是不鼓励私有变量，更高的自由度，所以默认都是共有的
# 双下划线__xxx可以一定程度实现私有的功能，但是也有绕过的办法
class C:
    def __init__(self, x):
        self.__x = x #__x是形式上的私有变量，外部无法直接访问（但是有办法绕过）
    def set_x(self, x):
        self.__x = x
    def get_x(self):
        return self.__x

def func2():
    c = C(1)
    #print(c.__x) #报错，无法直接访问
    print(c.get_x())
    c.set_x(10)
    print(c.get_x())
    print(c.__dict__)
    c._C__x = 250  # 变相绕过
    print(c.get_x())

#__slots__，固化Python类的动态属性功能
#前面提到了，Python的类里面可以动态增加成员，本质上就是__dict__
#__slots__的引入，可以规定仅指定的成员，这样性能会大幅提升，但是动态属性功能相对得就会被剥夺
#PS：__slots__可以继承，但是子类中不会被固化动态属性，即子类同时拥有__slots__和__dict__
class D:
    __slots__ = ["x", "y"] #只能有x和y
def func3():
    d = D()
    d.x = 1
    d.y = 2
    # d.z = 3 报错！
    # print(d.__dict__) # 报错，没有__dict__了
    print(d.__slots__)

#魔法方法:
# 说白了就是钩子，在对象特定阶段自动调用的方法
# 利用这个特性，就可以实现各种拦截效果（类似gin的过滤器）
# __new__(cls,[...])  #此方法在__init__更早之前调用
# __init__(self,[...]) #构造
# __del__(self) #析构


#例子1：篡改成大写
class UpperStr(str): #继承自str类，所以UpperStr也是字符串类型
    def __new__(cls, st): #在__init__之前，篡改了参数
        st = st.upper()
        return super().__new__(cls, st)
    def __del__(self):
        print("拜拜")

#例子2：拦截魔法有非常多，用的时候再查。这里列一些简单的例子
class S(str):
    def __add__(self, other): #本质：s1.__add__(s2)
        return len(self) + len(other)
class S1(str):
    def __iadd__(self, other): #iadd这个会影响到self本身，也就是类似于+=效果
        return len(self) + len(other)
class I():
    def __index__(self): #拦截自身作为索引的时候触发
        print("index被拦截")
        return 3

def func4():
    s = UpperStr("hello")
    print(s)
    del s

    s1 = S("Hello")
    s2 = S("World")
    print(s1+s2)

    s3 = S1("Hello")
    s3+=s2
    print(s3) # s3变成了一个数字

    i = I()
    print("Hello"[i]) #拦截效果

#属性相关的方法
# hasattr, 有个问题，加上下面的魔法方法后，此方法失效？？
# getattr
# setattr
# delattr
#对应魔法方法
# __getattribute__: 拦截getattr
# __getattr__: 当获取的属性不存在的时候自动触发拦截
# __setattr__: 拦截setattr
# __delattr__: 拦截delattr
class X:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # 私有成员
    def __getattribute__(self, item):
        if item == "aaa":
            print("篡改数据")
            return " ha ha ha"
        else:
            return super().__getattribute__(item)
    def __getattr__(self, item):
        print("无法读取，属性{}不存在".format(item))
    def __setattr__(self, key, value):
        print("set 被调用")
        self.__dict__[key] = value # 注意不能写self.key = value，会死循环
    def __delattr__(self, item):
        print("del 被调用")
        del self.__dict__[item]

def func5():
    x = X("张三", 10)
    print(hasattr(x, "name111"))
    print(getattr(x, "name"))
    print(getattr(x, "_X__age")) # 绕开私有变量
    print(setattr(x, "_X__age", 19))
    print(getattr(x, "_X__age"))
    delattr(x, "_X__age")
    print("hasattr----", hasattr(x, "_X__age"))
    print("hasattr----", hasattr(x, "_X__age1"))
    print(getattr(x, "aaa"))
    setattr(x, "aaa", 1)
    print(getattr(x, "aaa"))
    delattr(x, "aaa")


#func1()
#func2()
#func3()
#func4()
func5()