# 装饰器装饰一个类
# 本质上：将一个类作为装饰器函数的参数
# 注意对比，函数装饰器装饰一个函数，类装饰器装饰一个类，本质区别就是参数的不同
def report(cls):
    def oncall(* args, ** kwargs):
        print("开始初始化，加塞逻辑")
        ins = cls(* args, ** kwargs)
        print("初始化完成，加塞逻辑")
        return ins
    return oncall

@report # 等价于: C = report(C)
class C:
    pass

class D:
    pass

def func1():
    print(type(C))  # 注意，C不再是类了，被装饰之后，成了一个function
    c = C() # 此时，C()相当于调用了一个函数，但是这个函数的返回值是类实例，所以看起来还是和类初始化一样
    print(type(D)) # 对比
    print(type(c)) # 但是c仍然是一个类实例

#func1()

#同样的，一个类，也可以做成装饰器，来装饰一个函数！
#本质上：是将函数作为参数传入一个类的构造函数中
#注意，被装饰过的函数，会变成一个类实例，所以要调用它，需要__call__方法
class Counter:
    def __init__(self, func): #注意：__init__ 方法在装饰器应用的那一刻被调用，也就是在函数 f 定义时，而不是在调用 f() 时。
        self.func = func
        self.count = 0
        print("__init__被调用")
    def __call__(self, * args, ** kwargs): # __call__方法负责拦截调用，当一个对象实例被当做函数一样加上小括号的时候，就是一次调用，并返回结果
        self.count += 1
        print("调用了{}，当前计数为{}".format(self.func.__name__, self.count))
        return self.func(* args, ** kwargs)

# 实现一个计数器：
# 等价于: f = Counter(f)
# 此时的f，本质上是一个类实例，所以f()会触发__call__方法调用
# 此时就已经在调用__init__了
@Counter
def f(x):
    print(x)

def func2():
    print("---------")
    print(type(f))
    f(1)
    f("a")
    f([1,2,3])

func2()