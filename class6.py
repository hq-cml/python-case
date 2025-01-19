#神奇的type()
class C:
    def __init__(self, x):
        self.x = x

def func1():
    print(type(1))
    print(type(1)("520")) #想想为什么
    print(type(type(1)("520")))
    print(type([])("Hello"))
    print(type(())([1,2,3]))
    c = C(1)
    d = type(c)(2) #连对象也能转成类，再用来初始化
    print(d.__dict__)
    print(type(C)) #一个类，也可以用type来查看
    print(type(type)) # type自身，也是type！！万物之源！

#使用type，可以创造一个类！
#参数：4个：名字、父类、属性和方法、收集参数(可选)；返回一个新的type对象
#手机参数，涉及到__init_subclass__，这里略
def method1(self, name="hq"):
    self.z = name
    print("called method1")

def func2():
    C = type("C", (), {}) #类名字C，父类空，无属性
    print(type(C))
    c1 = C()
    print(c1)
    D = type("D", (C,), {"x":250, "y":520, "meth":method1}) #D是类C的子类, 同时，它拥有属性和方法
    d = D()
    print(d.x)
    d.meth()
    print(d.z)

#元类：继承自type的类（略）
#可以理解为它是类和type之间的桥梁
#object 所有类的父类(但是无论多少层级，类都是一个层次的物种）
#元类 比类高一个层次（包括object，因为它也就是一个类而已）
#type 比元类更高一层次，众神之神

#元类，极少使用，通常使用它提供了更高一层级的钩子
#比如，强制规定类名字、类参数等等一系列限制、单例类。。。

#抽象基类（概念和C++一样）
#实现：继承自元类=ABCMeta的类

#func1()
func2()