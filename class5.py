# property，生成一个内部成员的代理（它是某个对象属性的全方位拦截）
# 下面接触过描述符之后，会进一步加深这个理解
class C:
    def __init__(self):
        self.__x = 250
    def getx(self):
        return self.__x
    def setx(self, v):
        self.__x = v
    def delx(self):
        del self.__x

    #下面这种语法，类似于go的init，会在模块加载时自动执行，非调用触发。。
    print("Hello")
    # 这种方式，实现的是一个类属性！
    val = 10 # 类属性：val也是对象独有的。。。
    #让类属性x，代理了实例属性__x
    x = property(getx, setx, delx)

# property最常见的用法：装饰器！
# 类似于Java里面的lombok
class D:
    def __init__(self):
        self.__x = 250
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, v):
        self.__x = v
    @x.deleter
    def x(self):
        del self.__x

def func1():
    c1 = C()
    c2 = C()
    c1.val = 20
    print(c1.val, c2.val)
    print()

    # 关键是这里，x代理了__x
    print(c1.x)
    c1.x = 502
    print(c1.x, c1.__dict__)
    print()

    # 配合装饰器
    d = D()
    print(d.x)
    d.x = 502
    print(d.x, d.__dict__)
    del d.x
    print(d.__dict__)

#func1()

# 类属性
# 类方法 & 静态方法
# 在C++中类方法和静态方法是一个东西，但是Python里面是两种东西
class D:
    instance = 0 #类属性
    @classmethod
    def GetCount(cls): # 类方法会与类绑定
        print("类方法：目前共有{}个对象".format(cls.instance))
    @staticmethod
    def GetInsCnt(): # 静态方法不与任何东西绑定
        print("静态方法：目前共有{}个对象".format(D.instance))
    def __init__(self):
        D.instance += 1

def func2():
    d1 = D()
    d2 = D()
    D.GetCount()
    d2.GetCount()
    d1.instance = 100 # 并不会覆盖到类属性，只会创建一个实例属性
    d2.GetCount()
    d1.GetInsCnt()
    D.GetInsCnt()

func2()

#描述符：
# 被编写成独立的类，将其实例对象赋值给其他的类属性，最终实现对这个属性的查、改、删的全方位拦截！
# 实现了下面3个魔法方法的就是描述符，这个东西可以用于实现一个自己的property
#__set__/__get__/__delete__
# 描述符：只能用于类属性
#更高级：
#描述符可以用于对象、类的绑定、__slots__等等
#略。。。

#类装饰器
#前面讲过，装饰器实际上是语法糖，利用闭包实现了类似钩子的效果，美其名曰装饰
#一个类，也可以做成装饰器
#略。。。