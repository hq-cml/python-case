#lambda（一行流：匿名函数）
#lambda可以代替函数，但是它一般是比较简单的逻辑，可以避免函数命名
#def则用于常规的相对复杂一点的地方
def func1():
    square = lambda y: y*y
    print(square(5))

    #lambda和map结合(lambda就可以认为是一个函数简写)
    print(list(map(lambda x: x*x, [1,2,3])))
    print(list(filter(lambda x:x%2==1, range(10))))

# 生成器
# 用yield语句，代替return
# 是一种特殊的可迭代对象，每次遇到yield，就会生成迭代对象的一个元素
def func2():
    def counter():
        i = 0
        while i<=5:
            yield i # 生成迭代对象中的一个元素
            i += 1
    for x in counter(): # counter()就成了一个可迭代对象[0,1,2,3,4,5]
        print(x)

    print()
    it = counter() # counter()也是一个迭代器
    print(next(it))
    print(next(it))
    print(next(it))

# 利用生成器来实现斐波那契
# 原理：yield是带记忆功能的return
def func3():
    def fib():
        back1, back2 = 0, 1
        while True:
            yield back1 # 这里注意理解，没有这句yield则直接死循环了，他就是带记忆的return
            back1, back2 = back2, back1+back2
    it = fib()
    # 循环打印前10个fib数
    for i in range (10):
        print(next(it))

# 生成器对象
# 写法上类似于列表推导式，但是将方括号换成了小括号
# 注意这不是元组推导式，而是生成器对象
# 它和列表推导式的区别：前者一次下一个蛋；后者整体统一求值
def func4():
    it = (i ** 2 for i in range(10))
    for i in it :
        print(i)

# 函数文档，函数第一行的三引号注释，使得函数可以用help查看帮助
# 参数和返回值引导，:和->。注意只是引导，不会强制类型判断
def func5(x:int, y:int)->int:
    """
    功能：乘法
    参数：
    - x 被乘数
    - y 乘数
    返回值：
    - 乘积
    """
    return x * y

# 内省：在程序运行时候，查询一些状态
def func6():
    print(func5.__name__) # 查看函数的名字
    print(func5.__annotations__) # 查看类型注释
    print(func5.__doc__) # 查看文档

# 高阶函数，就是函数作为参数传入另一个函数
import functools
def func7():
    print(functools.reduce(lambda x, y : x * y, [1,2,3,4,5,6,7,8,9,10])) # 累积函数：10的阶乘
    square = functools.partial(pow, exp=2) # 偏函数
    print(square(3))

# 利用functools模块解决装饰器的副作用


# 装饰器带参数，本质上是多层闭包
import time
def logger(msg):
    def time_calc(f):
        @functools.wraps(f) #注意这句，就是关键
        def call():
            start = time.time()
            f()
            end = time.time()
            print("{}一共运行了{:.5f}秒".format(msg, end - start))
        return call
    return time_calc

@logger(msg="testF1")
def testF1():
    time.sleep(2)
testF1()
print(testF1.__name__)

#func1()
#func2()
#func3()
#func4()
#help(func5)
#func6()
#func7()
