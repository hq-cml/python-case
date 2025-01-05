# Python的成员变量有点奇怪
# 方法属于类
# 成员变量则遵循copy on write原则
# 初始状态下，所有的对象都共享类变量，直到发生了write
class C:
    x = 1 # 这个变量，既属于类，也属于对象。。。
    def set_x(self, v):
        self.x = v # 这里变更的是对象的x，而非类的
        # x = v 注意这两句的差别，这里是什么也没变更，只变更了x这个局部变量

def func1():
    c1 = C()
    print(c1.x) # 在没有变更前，x既属于对象也属于类
    c1.set_x(10)
    print(c1.x) # 变更后，x分离，属于对象，不再是类的
    print(C.x) # 类的变量不变
    print()
    c2 = C()
    print(c2.x)
    print(C.x)

    #Note：利用内省，可以更清楚的看到对象内部
    print(c1.__dict__) # 分离过
    print(c2.__dict__) # 空对象

# 基于上面的原理，可以有一个特性
# 一个空类，可以当字典用！！！
class M:
    pass

def func2():
    m = M()
    m.x = 1
    m.y = "hello"
    m.z = [1,2,3]
    print(m.__dict__)

#构造函数
class CC:
    def __init__(self, x, y):
        print("create CC")
        self.x = x
        self.y = y

# 继承重写
class D1(CC):
    def __init__(self, x, y, z): # 重写构造函数
        CC.__init__(self, x,y)
        self.z = z

class D2(CC):
    def __init__(self, x, y, z): # 重写构造函数
        CC.__init__(self, x,y)
        self.z = z*2

def func3():
    c = CC(1,2)
    print(c.__dict__)
    d = D1(1,2,3)
    print(d.__dict__)

# 钻石继承问题：上面的写法，会造成钻石继承问题
#    CC
#   /  \
#  D1   D2
#   \  /
#    E1
# 可以看到，下面的函数证明了钻石问题，父类构造被调用了2次！
class E1(D1, D2):
    def __init__(self):
        D1.__init__(self,1, 2, 3)
        D2.__init__(self,4, 5, 6)

def func4():
    e = E1()
    print(e.__dict__)

# 解决钻石继承的方法：不要直接调用父类构造，而是采用super()的方式，并且无需self
class CCC:
    def __init__(self):
        print("create CCC")

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

def func5():
    e = E2()


#MRO：Python解析顺序
#可以直接通过Class.mro()查看
def func6():
    print(E2.mro())

#func1()
#func2()
#func3()
#func4()
#func5()
func6()