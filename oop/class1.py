#类定义
#self,指向对象的指针！
class Turtle:
    head = 1 #属性，属于对象
    eyes = 2
    def sleep(self): #注意这个self是必须的！！它就是对象本身的指针
        print("Turtle zzz...")
    def eat(self):
        print("eat...")

# 另一个类
class Turtle2:
    head = 10
    eyes = 20

#类继承
class B(Turtle):
    pass

#继承 & 覆盖
class C(Turtle):
    eyes = 4 # 覆盖
    def sleep(self):
        print("C ......zzz")

#python中，一切接对象
def func0():
    print(type(1))
    print(type([1,2]))
    print(type((1,2)))
    print(type({1}))
    print(type({"a":1}))

#func0()

# 类的创建
def func1():
    t1 = Turtle()  # 创建对象
    t2 = Turtle()  # 创建对象
    print(t1.eyes)
    t1.legs = 4  # 对象可以动态创建一个属性！
    print(dir(t1))
    print(dir(t2))  # 少了一个动态创建的legs

#func1()

# 类的继承
def func2():
    t = Turtle() #创建对象
    t.sleep()
    b = B()
    b.sleep()
    print(b.eyes)
    c = C()
    print(c.eyes)
    c.sleep()
    print("--------")
    # 判断对象是否是某个类的实例化: isinstance
    print(isinstance(b, B))
    print(isinstance(b, Turtle))
    print(isinstance(t, B))

    # 判断继承关系
    print(issubclass(B, Turtle))

#func2()

# 多重继承，一个类有2个及2个以上父类
# 覆盖权重是左>右，除非左侧找不到
class D(Turtle, Turtle2):
    pass

class Cat:
    def sleep(self):
        print("cat sleep...")

# 组合：就是两个成员分别是另外两个类的对象
class Animal():
    c = Cat()
    t = Turtle()
    def sleep(self):
        self.c.sleep() # 注意这个用法，这个self是必须的，没有则会报错！
        self.t.sleep() # 原因是因为self表示对象，如果没有self，则t.sleep()将无法找到，下一章有详解

# 多重继承 & 组合
def func3():
    # 多重继承
    d = D()
    print(d.head) # head成员使用的是左侧，因为优先级左>右

    # 组合
    a = Animal()
    a.sleep()

#func3()

# Python的成员变量有点奇特
# 方法属于类，这个好理解；
# 成员变量则即属于类，也属于对象，遵循copy on write原则；
# 初始状态下，所有的对象都共享类变量，直到发生了write
class CC:
    x = 1 # 这个变量，初始既属于类，也属于对象。。。
    def set_x(self, v):
        self.x = v # 这里变更的是对象的x，而非类的，因为self
        #x = v #注意这两句的差别，这个x只是一个局部变量，所以这里只变更了x这个局部变量，其他什么也没变更

def func4():
    c1 = CC()
    print(c1.x) # 在没有变更前，x既属于对象也属于类
    c1.set_x(10) # Note：本质上这行相当于 C.set_x(c1)，注意理解
    print(c1.x) # 变更后，x分离，属于对象，不再是类的
    print(CC.x) # Note：直接用类名，也能引用变量！
    print("-----------")

    c2 = CC() # 新的对象，无任何影响
    print(c2.x)
    print(CC.x)
    print()

    CC.x = 88 # 直接通过类修改变量，则全都变了（非常不建议这样的操作）
    c3 = CC()
    print(c3.x)
    c3.set_x(99) # 再次修改局部，触发COW;
    print(c3.x)
    print(CC.x)
    print(c2.x) # 注意这里，c2没有派生过，所以它的x值是类的，而不是对象的，所以也跟着变
    print(c1.x) # 注意这里，c1派生过，所以它的x值是对象的，所以不会受影响

    print()
    #Note：利用内省，可以更清楚的看到对象内部（只能看到对象实例的，类的变量看不到）
    print(c1.__dict__) # 分离过，多出一个x
    print(c2.__dict__) # 空对象
    print(c3.__dict__) # 分离过
    print(dir(c3)) # dir和__dir__的区别

#func4()

# 基于上面的原理，可以有一个特性
# 一个空类，可以当字典用！！！（自省）
# Note：一个非常反直觉的认知：在Python中类和对象，都可以通过自省来观察，它们其实都可以看做字典，都可以动态插入成员属性！
class M: # 空类
    pass

def func5():
    m = M()
    m.x = 1   # 反直觉：对象可以动态增加属性，属于对象
    m.y = "hello"
    m.z = [1,2,3]
    print(m.__dict__)
    print("-----")

    M.x = 10000 # 反直觉：类可以动态增加属性，属于类
    M.abc = "8888" # 类可以动态增加属性，属于类，但是对象也能访问
    print(M.__dict__) # 类自省
    print(m.__dict__) # 对象自省
    print(m.abc)  # 对象也能访问到类的属性（但是自省是看不到的）

func5()
