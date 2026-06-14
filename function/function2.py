# 作用域
x = 100 # 全局
def func1():
    print(x)

# 全局作用域，global关键字使得x指向了全局的那个
def func2():
    global x # 注释掉这一行，则x是局部变量，而不是外层的x=100
    x = 100000
    print(x)

# 嵌套函数 & 内部修改外部值
def func3():
    x= 10
    def funcs1():
        nonlocal x # 声明x是非本地，也就是外层x
        x = 20
        print("in funcs1: ", x)
    funcs1()
    print("in func5: ", x)
    # global x # 报错，一个变量不同同时使用global和nonlocal
    # print("global x: ", x)

#func3()

#闭包
def func4():
    x = 100
    def funcs():
        print(x)
    return funcs
# f = func4()
# f()

# 闭包有时候也称为工厂
# 比如这个例子，此时就类似于一个工厂，不同的参数，得到两个不同生产线
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of
# square = power(2)
# cube = power(3)
# print(square(5))
# print(cube(5))

#闭包配合nonlocal（当有写入的时候）
#  如果 inner 内部只是读取 x 和 y（例如 print(x, y)），而不进行赋值，则不需要 nonlocal
#  因为读取时会按 LEGB 规则（Local -> Enclosing -> Global -> Built-in）找到外层变量。
#  一旦涉及赋值（包括 +=、-= 等增强赋值），就必须用 nonlocal（对于嵌套作用域）或 global（对于全局作用域）来声明变量来源。
def foo():
    x = 0
    y = 0
    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"x={x}, y={y}")
    return inner
# oo = foo()
# oo(1,2)
# oo(1,2)
# oo(1,2)

# Note：函数作为参数
def myfunc():
    print("call myfunc...")
def outer(f):
    print("outer begin...")
    f()
    print("outer end...")
#outer(myfunc)

# Note：装饰器：
# Python的语法糖，最终功能有点类似于gin框架的过滤器
# 本质上来说，装饰器就是一个函数，它本身的输入是一个函数，返回的是另一个函数
# 其实就是闭包 + 函数作为参数 两种特性结合的语法糖！

# 例1：最简单装饰器函数
# 入参是待装饰的函数
# 出参是装饰后的函数
# 统计运行时间
def time_calc(f):
    import time
    def call():
        start = time.time()
        f()
        end = time.time()
        print("一共运行了{:.5f}秒".format(end-start))
    return call

# 加载装饰器
# 一旦加载了装饰器，函数就不再是原来的函数了，而是装饰后的函数
@time_calc
def testF():
    import time
    print("开始")
    time.sleep(2)
    print("结束")

# 调用testF()，实际上不再是testF()，而是装饰后的函数，也就是上面内部的那个call()方法
# 非常神奇，在调用testF的同时，自动装载了装饰器，自动执行了time_calc方法，不再需要显式调用！
# 等价于：time_calc(testF)()
#testF()

# 例2：多个装饰器叠加
def add(func):
    def inner():
        x = func()
        return x + 1
    return inner
def cube(func):
    def inner():
        x = func()
        return x * x * x
    return inner
def square(func):
    def inner():
        x = func()
        return x * x
    return inner

@add
@cube
@square
def myFunc():
    return 2

# v = myFunc()
# print(v)
# 等价于：
# def myfunc():
#     return 2
# print(add(cube(square(myfunc)))())

# 例3：装饰器带参数：
#     本质上是多层闭包嵌套，参数通过多套的那一层传递
# 利用functools模块解决装饰器的副作用
import functools
def logger(msg):
    import time
    def time_calc(f):
        #@functools.wraps(f)  # 注意这句，就是关键，可以试着注释掉这句，就能看出区别了
        def call():
            start = time.time()
            f()
            end = time.time()
            print("{}一共运行了{:.5f}秒".format(msg, end - start))
        return call
    return time_calc

@logger(msg="testF1") # 加载装饰器，并附带参数
def testF1():
    import time
    time.sleep(2)

#等价于：logger(msg="testF1")(testF1)()
testF1()
# 装饰器的副作用，testF1.__name__ != testF1
# 这个副作用下需要依靠functools模块来解决
print(testF1.__name__ )
