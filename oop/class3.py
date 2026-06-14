#魔法方法: 拦截的艺术！！！！！！
# 遍布于类全生命周期各个阶段的钩子，在对象特定阶段自动调用的方法
# 利用这个特性，就可以实现各种拦截效果（类似gin的过滤器）

# __new__(cls,[...])  #此方法用于创建一个类的对象，在__init__更早之前调用
# __init__(self,[...]) #此方法用于初始化已经创建的对象实例
# __del__(self) #析构

#__new__和__init__核心对比
# 特性           __new__                                    __init__
# 角色           构造器：创建并返回一个新实例                    初始化器：设置实例的初始状态
# 调用时机        先调用，在实例创建之前                         后调用，在实例创建之后
# 第一个参数       cls（类本身）                               self（已创建的实例）
# 返回值          必须返回一个实例对象（通常是 cls 的实例）       必须返回 None（不应返回其他值）
# 是否是类方法     是（隐式静态方法，但可以接受 cls）             是实例方法
# 常见使用场景     控制实例创建（单例、不可变类型子类等）          常规的实例属性初始化
#
# 说明：
# 日常编程中，99% 的情况只写 __init__，__new__ 只在需要深度控制对象创建时才使用。
class Person:
    def __new__(cls, name):
        print("1. __new__ called")
        instance = super().__new__(cls)   # 真正创建实例
        return instance                   # 必须返回实例，可以试试没有这句，一切都将崩塌

    def __init__(self, name):
        print("2. __init__ called")
        self.name = name                  # 不需要返回值，因为他这是初始化一个已存在的对象
def func1():
    p = Person("Alice")
    print(p.name)

#func1()

# 利用__new__实现单例
class Singleton:
    _instance = None
    # 注销掉这个__new__方法，再看结果
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance   # 总是返回同一个实例
    def __init__(self):
        self._instance = 1
        print("Singleton __init__ called")

def func2():
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2) # True，如果将上面的__new__注释掉，就会是False。体会

#func2()

#例子1：篡改成大写
#UpperStr继承自str类，所以UpperStr也是字符串类型
class UpperStr(str):
    def __new__(cls, st): #在__init__之前，篡改了参数
        st = st.upper()
        return super().__new__(cls, st)
    def __del__(self): # 对象销毁的时候调用
        print("拜拜")

#例子2：拦截魔法有非常多，用的时候再查。这里列一些简单的例子
class S(str):
    def __add__(self, other): #本质：s1.__add__(s2)
        return len(self) + len(other)
class S1(str):
    def __iadd__(self, other): #增强：iadd这个会影响到self本身，也就是类似于+=效果
        return len(self) + len(other)
class I():
    def __index__(self): #拦截自身作为索引的时候触发
        print("index被拦截")
        return 3

def func3():
    s = UpperStr("hello")
    print(s)
    del s
    print("---------")

    s1 = S("Hello")
    s2 = S("World")
    print(s1+s2)

    s3 = S1("Hello")
    s3+=s2
    print(s3) # s3变成了一个数字
    print(type(s3))
    print("---------")

    i = I()
    print("Hello"[i]) #拦截效果

#func3()

#属性相关的方法
# hasattr, 有个问题，加上下面的魔法方法后，此方法失效？？
# getattr
# setattr
# delattr
#对应魔法方法如下：
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
        #return super().__getattr__(self, item)
        raise AttributeError # 抛出异常，会自动转换成false，不能写上面这句，因为object没有__getattr__方法
    def __setattr__(self, key, value):
        print(f"set 被调用, key=>{key}, val=>{value}")
        #self.__dict__[key] = value # 注意不能写self.key = value，会死循环
        return super().__setattr__(key, value)
    def __delattr__(self, item):
        print(f"del 被调用, item=>{item}")
        #del self.__dict__[item]
        return super().__delattr__(item)

def func4():
    x = X("张三", 10)
    print("-------------")
    print(hasattr(x, "name111"))
    print(getattr(x, "name"))
    print(getattr(x, "_X__age")) # 绕开私有变量
    print("-------------")
    setattr(x, "_X__age", 19)
    print(getattr(x, "_X__age"))
    print("-------------")
    delattr(x, "_X__age")
    print("hasattr----", hasattr(x, "_X__age"))

#func4()

#索引和切片
#__getitem__: 用于拦截索引
#__setitem__: 用于拦截索引
class C:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, item):
        print("索引：", item)
        return self.data[item]
    def __setitem__(self, key, value):
        print(f"设置索引：{key}=>{value}")
        self.data[key] = value

def func5():
    c = C([1,2,3,4,5])
    print(c[0])
    print(c[1:3]) # 索引不一定是一个数，也可能是一个切片
    c[2] = 100
    print(c.data)

func5()

#针对for之类的迭代
#针对可迭代对象的魔法方法
#__iter__: 如果一个类定义了一个__iter__，他就是可迭代对象
#__next__: 如果一个类定义了一个__next__，他就是迭代器
#比如，list是可迭代对象，但它不是迭代器，验证：dir(list)
#所以，当for遍历一个list的时候，到底发生了什么？
#   其实，底层第一步是将list转变成迭代器，然后才能遍历！
def func6():
    x = [1,2,3]
    print(dir(x)) #没有next，说明不是迭代器
    print("----------")

    # for
    for i in x:
        print(i, end=" ")
    print()
    print("----------")

    # 与for等价
    it = iter(x) #得到迭代器
    while True:
        try:
            v = it.__next__()
        except StopIteration: # 迭代器遍历结束抛出的异常
            print("break")
            break
        print(v, end=" ")
#func6()

#创造一个迭代对象
class Tribble:
    def __init__(self, start, end):
        self.v = start
        self.end = end
    def __iter__(self): #创造一个迭代对象，因为自身就是迭代对象，所以直接返回
        return self
    def __next__(self): #迭代器
        if self.v == self.end:
            raise StopIteration
        else:
            ret = self.v * 3
            self.v += 1
            return ret
def func7():
    t = Tribble(1,5)
    # 可迭代对象，直接进行迭代
    for i in t:
        print(i, end=" ")

#func7() #体会为什么是这个输出

#其他的一些魔法方法
# 暂且了解
# in & not in: 对应 __contains__
# yes or no: 对应 __bool__


#代偿机制：
# 如果直接需要的方法找不到，会尝试其他的方法凑活使用
# __contains__ --->  __iter__/__next__
# __iter__/__next__ --->  __getitem__
# __bool__ --->  __len__

# <: __lt__
# <=: __le__
# >: __gt__
# >=: __ge__
# ==: __eq__
# !=: __ne__

# 将一个对象当做函数一样调用: __call__，这个特性可以用来替代闭包
class ID1:
    def __call__(self, *args, **kwargs):
        print("shit")

class ID2:
    def __call__(self, *args, **kwargs):
        print(f"位置参数：{args}, 关键字参数：{kwargs}")
def func8():
    c = ID1()
    c() # 将对象当成函数调用
    d = ID2()
    d(1,2, x=100, y=100)

#func8()


# 字符串相关，不怎么常用: __str__和__repr__
# eval是repr的反函数，用时再理解
