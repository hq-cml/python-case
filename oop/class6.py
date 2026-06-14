#神奇的type()
class CC:
    def __init__(self, x):
        self.x = x

# python中，万物皆是类
# type是万物支援，一个基础类型或者类，用type()查看，会发现它的类型是"type"
# type自身用type()查看，发现它也是"type"
def func1():
    print("=================")
    print(type(1))
    print(type(int)) #一个基础类型，也可以用type来查看
    print(type("hello"))
    print(type(1) is int)
    print("---------")
    print(type(1)("520")) #想想为什么，类型转换
    print(type(type(1)("520")))
    print(type([])("Hello"))
    print(type(())([1,2,3]))
    print("---------")
    c = CC(1)
    d = type(c)(2) #连对象也能转成类，再用来初始化
    print(d.__dict__)
    print(type(CC)) #一个类，也可以用type来查看
    print(type(type)) # type自身，也是type！！万物之源！
    print("=================")
#func1()

#基于type这个特性
#使用type，可以动态得创造一个类！
#参数：名字、父类、属性和方法（字典形式）、
#     第4个可选：收集参数，涉及到__init_subclass__，拦截类初始化行为
#返回一个新的type对象
def method1(self, name="haha"):
    self.z = name
    print("called method1")

# 创造类C
def CreateC():
    C = type("C", (), {})  # 类名字C，父类空，无属性
    return C

# 创造类D
def CreateD(C):
    # D是类C的子类, 同时，它拥有属性和方法；
    # PS：这里的(C,)表示这是一个元组，所以必须这么写
    return type("D", (C,), {"x":250, "y":520, "meth":method1})

def func2():
    C = CreateC()
    print(type(C))
    c1 = C()
    print(c1)
    D = CreateD(C)
    d = D()
    print(d.x)
    d.meth()
    print(d.z)
    print("-----------------")

#func2()

# 第4个参数：收集参数，涉及到__init_subclass__，拦截类初始化行为
class C1:
    def __init_subclass__(cls, value): # 拦截了子类初始化行为（注意是类的初始化行为，而不是对象初始化行为）
        print("called __init_subclass__") # 注意执行时机
        print("~~~~~~~~~~~~~~~~~~~~~~")
        cls.x = value

# 动态创建D1的时候，会触发C1的__init_subclass__，所以起到了拦截效果
class D1(C1, value=100):
    x = 50 # 这句话将被拦截无效，因为使用了__init_subclass__进行了拦截

def func3():
    d1 = D1()
    print(d1.x)

    # 动态创建类，效果一样
    E = type("E", (C1,), {"x":100}, value=200) # 100将被拦截
    print(E.x)
    print("-----------------")

#func3()

#元类：继承自type的类（略）
#可以理解为它是类和type之间的桥梁！type是元类的父类，其他类又都继承元类
#关系：type -> 元类 -> 类 -> 对象
#object，这个是所有类的父类(但是无论多少层级，类都是一个层次的物种）
#元类 比类高一个层次（包括object，因为object也就是一个类而已）
#type 比元类更高一层次，众神之神

#创建一个元类（继承自type）
#注意这里的__new__和__init__的执行时机：是下面的class CC定义，触发了这里的调用！！
class MetaC(type):
    def __new__(cls, name, bases, attrs):
        print("called __new__ in MetaC")
        print(f"cls={cls}, name={name}, bases={bases}, attrs={attrs}")
        return super().__new__(cls, name, bases, attrs)
    def __init__(cls, name, bases, attrs):
        print("called __init__ in MetaC")
        print(f"cls={cls}, name={name}, bases={bases}, attrs={attrs}")
        super().__init__(name, bases, attrs) # 注意：普通的类__init__，是不需要super().__init__的，这里需要因为是元类

# 注意这里不是继承
# 声明类 CC 时指定元类为 MetaC，即通过 MetaC 来控制（拦截） CC 类的创建过程
# 当 Python 解释器执行到第class CC时，会调用 MetaC.__new__() 和 MetaC.__init__() 来创建类
# 元类比类更高一层，用于在类定义阶段拦截和定制类的行为（如限制类名、属性等）
class CC(metaclass=MetaC):
    def __new__(cls, *args, **kwargs):
        print("called __new__ in CC")
        return super().__new__(cls)
    def __init__(self):
        print("called __init__ in CC")

def func4():
    # 可以看到，元类中的__new__和__init__，在这里已经被被调用了
    print("--------------------------------")
    c = CC()
    print("--------------------------------")
    print(type(c))
    print(type(CC))
    print(type(MetaC))

func4()

#元类，极少使用，通常使用它提供了更高一层级的钩子
#比如，强制规定类名字、类参数等等一系列限制、单例类。。。

#抽象基类（概念和C++一样）
#实现：继承自元类=ABCMeta的类
