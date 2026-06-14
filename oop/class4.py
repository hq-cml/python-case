# property
# 这个函数能够生成一个内部成员的代理（它是某个对象属性的全方位拦截）
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

    #这里很奇怪，直接在类定义里面写了代码，实际上把这一段放到def上面会更好理解
    #其实这就是定义类属性的代码，类似于go的init，会在模块加载时自动执行，非调用触发。。
    print("Hello，我是类定义代码")
    print("-------------------")
    # 类属性，其实就是类定义代码的方式实现的！
    val = 10 # 类属性：val也是对象独有的。。。

    #定义了一个类属性x，利用property，使得x代理了实例属性__x
    x = property(getx, setx, delx)

def func1():
    c1 = C()
    c2 = C()
    c1.val = 20
    print(c1.val, c2.val)
    print("---------------")

    # Note: 关键是这里，x代理了__x
    # Note: 虽然这个功能用__getattr__, __setattr__, __delattr__也能变相实现，但是非常复杂
    #       并且，property方法的参数是其他的方法，这个最大的魅力在于，本质上它就是装饰器！见下面
    print(c1.x)
    c1.x = 502
    print(c1.x, c1.__dict__)
    print()

#func1()

# property最常见的用法：装饰器！
class D:
    def __init__(self):
        self.__x = 250

    #Note: 本质上就是x = property(x)
    @property
    def x(self):
        return self.__x
    #Note：由于上面的property只传入一个参数，所以这里必须补齐set和del
    #      但是因为x已经被占用，所以用特殊的x.setter和x.deleter代替
    #      先记住这种用法，实际上他和class C是一模一样的
    @x.setter
    def x(self, v):
        self.__x = v
    @x.deleter
    def x(self):
        del self.__x

def func2():
    # 配合装饰器
    d = D()
    print(d.x)
    d.x = 502
    print(d.x, d.__dict__)
    del d.x
    print(d.__dict__)

#func2()

# 类属性
# 类方法 & 静态方法
# 在C++中类方法和静态方法是一个东西，但是Python里面是两种东西，他们都是通过装饰器来实现
# @classmethod：类方法，与类绑定
# @staticmethod：静态方法，不与任何东西绑定
class DD:
    instance = 0 #类属性
    def __init__(self):
        DD.instance += 1 # 注意这里写法，不是self.instance!而是D.instance
    @classmethod
    def GetCount(cls): # 类方法会与类绑定
        print("类方法：目前共有{}个对象".format(cls.instance)) # 注意区别，这里是cls.xx
    @staticmethod
    def GetInsCnt(): # 静态方法不与任何东西绑定
        print("静态方法：目前共有{}个对象".format(DD.instance)) # 注意区别，这里是D.xx


def func3():
    d1 = DD()
    d2 = DD()
    DD.GetCount()
    d2.GetCount()
    print("-----------")
    d1.instance = 100 # 并不会覆盖到类属性，只会创建一个实例属性
    d2.GetCount()
    d1.GetInsCnt() # 静态方法，虽然不绑定任何东西，但是用对象和类名都能调用
    DD.GetInsCnt()
    print("-----------")
    print(d1.instance) # 是对象的
    print(d2.instance) # 还是类的

#func3()

#描述符：
# property和类方法、静态方法的底层实现机制：描述符
# 一个类实现了下面3个魔法方法之一的就是描述符:__set__/__get__/__delete__
# 描述符本身是一个类，它的实例对象赋值给宿主类的某个属性，就可以实现对于该属性的读、写、删除的全方位代理（拦截）
# 注意这个类将被用于定义其他类的属性，所以这3个方法负责拦截的其实是它的宿主类!
# 例子：实现一个类D1，能够达到property的功效
class D1:
    def __get__(self, instance, owner):
        print("__get__")
        print(f"self:{self}")
        print(f"instance:{instance}")
        print(f"owner:{owner}")
        return instance.__x
    def __set__(self, instance, value):
        print("__set__")
        print(f"self:{self}")
        print(f"instance:{instance}")
        print(f"value:{value}")
        instance.__x = value
    def __delete__(self, instance):
        print("__delete__")
        print(f"self:{self}")
        print(f"instance:{instance}")
        del instance.__x
class C1:
    def __init__(self, x=250):
        self.__x = x
    x = D1() # 类似property的功效；描述符仅能用于类属性，不能用于实例属性

def func4():
    c = C1()
    c.x = 100
    print("---------")
    v = c.x
    print(v)
    print("---------")
    del c.x

#func4()

# 有了描述符的基础概念，就可以自己实现property类
# 被编写成独立的类，将其实例对象赋值给其他的类属性
# 最终实现对这个属性的查、改、删的全方位拦截！
# 这个东西可以用于实现一个自己的property
# 注意这里有点抽象，是因为实现了2个版本，一个原始版本，一个装饰器版本
class MyProperty():
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    # 一套原始版本方法
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        self.fset(instance, value)
    def __delete__(self, instance):
        self.fdel(instance)
    # 实现装饰器版本的方法
    def setter(self, fset):
        self.fset = fset
        return self
    def deleter(self, fdel):
        self.fdel = fdel
        return self
    def getter(self, fget):
        self.fget = fget
        return self

# 原始版
class MyC1:
    def __init__(self, x=250):
        self.__x = x
    def getx(self):
        return self.__x
    def setx(self, value):
        self.__x = value
    def delx(self):
        del self.__x
    x = MyProperty(getx, setx, delx)

# 装饰器版，等价于MyC1
class MyC2:
    def __init__(self, x=250):
        self.__x = x
    @MyProperty
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value
    @x.deleter
    def x(self):
        del self.__x

def func5():
    c = MyC1()
    c.x = 100
    print(c.x)
    print(c.__dict__)
    del c.x
    print(c.__dict__)
    print()

    c2 = MyC2()
    c2.x = 100
    print(c2.x)
    print(c2.__dict__)
    del c2.x
    print(c2.__dict__)

func5()


# 描述符
# 还能细分：非数据描述符（仅有__get__）、数据描述符等等
# 这块涉及到拦截的顺序等等，感觉用处不大
# 用时再看。。。。


#更高级：
#描述符可以用于对象、类的绑定、__slots__等等
#略。。。

