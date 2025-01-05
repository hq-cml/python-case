#类定义
class Turtle:
    head = 1
    eyss = 2
    def sleep(self): #注意这个self是必须的！！，它就是对象本身的指针
        print("Zzz...")
    def eat(self):
        print("eat...")

class Turtle2:
    head = 10
    eyes = 20

#类继承
class B(Turtle):
    pass

#继承 & 覆盖
class C(Turtle):
    def sleep(self):
        print("......zzz")

# 多重继承，一个类有2个及2个以上父类
# 覆盖权重是左>右，除非左侧找不到
class D(Turtle, Turtle2):
    pass

class Cat:
    def sleep(self):
        print("cat sleep...")

# 组合
class Animal():
    c = Cat()
    t = Turtle()
    def sleep(self):
        self.c.sleep()
        self.t.sleep()

def func1():
    t = Turtle() #创建对象
    t.sleep()
    b = B()
    b.sleep()
    c = C()
    c.sleep()

    # 判断对象是否是某个类的实例化: isinstance
    print(isinstance(b, B))
    print(isinstance(b, Turtle))

    # 判断继承关系
    print(issubclass(B, Turtle))

def func2():
    # 多重继承
    d = D()
    print(d.head) # head成员使用的是左侧，因为优先级左>右

    # 组合
    a = Animal()
    a.sleep()

#func1()
func2()