#构造函数
class CC:
    def __init__(self, x, y): # 构造
        print("create CC")
        self.x = x
        self.y = y
    def add(self): # 普通方法
        return self.x + self.y

# 继承重写
class D1(CC):
    def __init__(self, x, y, z): # 重写构造函数
        print("create D1")
        CC.__init__(self, x,y) # Note：实际上这种写法是有问题的，称之为“调用未绑定的父类方法”，可能导致钻石继承问题，下面有详解
        self.z = z
    def add(self): # 普通方法重写
        return CC.add(self) + self.z # 调用父类方法


class D2(CC):
    def __init__(self, x, y, z): # 重写构造函数
        print("create D2")
        CC.__init__(self, x,y)
        self.z = z*2

def func1():
    c = CC(1,2)
    print(c.__dict__)
    print(c.add())
    d = D1(1,2,3)
    print(d.__dict__)
    print(d.add())

#func1()

# 钻石继承问题：上面的子类调用父类方法的写法，会造成钻石继承问题
#    CC
#   /  \
#  D1   D2
#   \  /
#    E1
# 可以看到，下面的函数证明了钻石问题，父类构造被调用了2次！
# 这也很好理解，按照这么朴素的写法，调用2次才是正常的
class E1(D1, D2):
    def __init__(self):
        D1.__init__(self,1, 2, 3)
        D2.__init__(self,4, 5, 6)
#爷爷类CC构造被调用了2次！
def func2():
    e = E1()
    print(e.__dict__)

#func2()

# 如何解决钻石继承的问题？
# 不要直接调用父类构造，而是采用super()的方式，并且无需self
# Note: Python中super()到底是什么？
#   在 Python 中，super() 返回的是一个代理对象（而非父类本身，也非父类的实例对象）。
#   这个代理对象负责将方法调用按照方法解析顺序（MRO, Method Resolution Order）委托给当前类的父类（或兄弟类）。
#   super() 在 Python 3 中可以不传参数，它会自动从上下文获取当前类（__class__）和第一个参数（通常是 self 或 cls）。
#   返回的代理对象允许你调用父类中的方法，并且正确处理多重继承中的钻石形结构（通过协作式多重继承，保证每个父类只被调用一次）。
class CCC:
    def __init__(self):
        print("create CCC")
    def add(self):
        return 10

class D3(CCC):
    def __init__(self): # 重写构造函数
        #CC.__init__(self)
        super().__init__() # 直接super()，无需self
        print("create D3")

class D4(CCC):
    def __init__(self): # 重写构造函数
        #CC.__init__(self, x,y)
        super().__init__() # 直接super()，无需self
        print("create D4")

class E2(D3, D4):
    def __init__(self):
        super().__init__() # 这个super，会同时调用D3和D4的构造函数
        print("create E2")
    def add(self):
        return super().add()

def func3():
    e = E2()
    print(e.add())

#func3()

#MRO：Python解析顺序，多重继承中，解析顺序=>执行顺序
#可以直接通过Class.mro()查看
#这个非常重要，一些Mixin问题，都可以遵循这个原则找到答案
def func4():
    print(E2.mro())

#func4()

#关于Mixin的概念：
#多继承中一个很恶心的特性，要结合MRO来理解
#仔细看下面这段代码，分析为什么出现这个问题
class Displayer:
    def display(self, message):
        print(message)

class LoggerMixin:
    def log(self, message, filename="log.txt"):
        with open(filename, "a") as f:
            f.write(message)
    def display(self, message):
        super().display(message)
        self.log(message)

class MyClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename="mylog.txt")

# 代码分析：
# 1. c.display调用必然是LoggerMixin的display（根据MRO的结果）
# 2. super().display(message)中的super()是谁？因为LoggerMinxin类没有父类，所以第一感觉应该是Object中查找display方法，
#    但是实际上根据MRO的结果，实际上是是取到了Displayer中查找display方法！-- 这就导致终端上打印了一句话
# 3. self.log(message)中的self是谁？这里第一感觉是LoggerMixin对象，实际上应该是MyClass的对象，也就是c实例
# 4. c中的super().log(message, filename="mylog.txt")里面的super是谁？根据MRO，应该是LoggerMixin
# 5. 最终调用的是LoggerMixin中的log方法，不过参数却是mylog.txt!
# HQ：这个确实太绕了，了解即可，实际上这么用就是自己挖坑
def func5():
    print(MyClass.mro())
    c = MyClass()
    c.display("this is a test.\n")

#func5()

#多态和鸭子类型
#Python本身就是一个动态语言，所以只需要满足鸭子，就可以是多态
class Cat:
    def say(self):
        print("i am a cat")

class Book:
    def say(self):
        print("i am a book")

#在Python中，参数甚至不需要是父类的引用，就可以实现多态
def say(x):
    x.say()

def func6():
    a = Cat()
    say(a)
    b = Book()
    say(b)

#func6()

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

def func7():
    c = C(1)
    #print(c.__x) #报错，无法直接访问
    print(c.get_x())
    c.set_x(10)
    print(c.get_x())
    print(c.__dict__) # 利用自省可以发现私有变量的秘密，其实就是改了个名字
    c._C__x = 250  # 变相绕过，Note：Python的name mangling，名字改编技术！
    print(c.get_x())

#func7()

#前面提到了，Python的类，令人惊诧和困惑的动态属性问题，也就是可以随意动态增加成员，本质上就是__dict__
#__dict__的好处是使得程序相当灵活，代价则是牺牲了效率，而__slots__的引入，可以规定仅指定的成员
#这样性能会大幅提升，但是动态属性功能相对得就会被剥夺
#PS：__slots__可以继承，但是子类中不会被固化动态属性，即子类同时拥有__slots__和__dict__
class D:
    __slots__ = ["x", "y"] #只能有x和y
def func8():
    d = D()
    d.x = 1
    d.y = 2
    # d.z = 3 # 动态添加属性，报错！
    # print(d.__dict__) # 报错，没有__dict__了
    print(d.__slots__)

func8()