#闭包
def func1():
    x = 100
    def funcs():
        print(x)
    return funcs
#f = func1()
#f()

#闭包有时候也称为工厂
def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of
# 此时就类似于一个工厂，不同的参数，得到两个不同生产线
# square = power(2)
# cube = power(3)
# print(square(5))
# print(cube(5))

# 函数作为参数
def myfunc():
    print("call myfunc...")
def outer(f):
    print("outer begin...")
    f()
    print("outer end...")
#outer(myfunc)

# 装饰器：
# 功能类似于gin框架的过滤器
# 本质上其实就是闭包 + 函数作为参数 两种特性结合的语法糖！
import time
# 统计运行时间
def time_calc(f):
    def call():
        start = time.time()
        f()
        end = time.time()
        print("一共运行了{:.5f}秒".format(end-start))
    return call
@time_calc # 加载装饰器
def testF():
    time.sleep(2)
#testF() # 非常神奇，在调用testF的同时，自动装载了装饰器

# 装饰器带参数，本质上是多层闭包
def logger(msg):
    def time_calc(f):
        def call():
            start = time.time()
            f()
            end = time.time()
            print("{}一共运行了{:.5f}秒".format(msg, end - start))
        return call
    return time_calc

@logger(msg="testF1") # 加载装饰器，并附带参数
def testF1():
    time.sleep(2)
testF1()
print(testF1.__name__) # 装饰器的副作用，testF1.__name__ != testF1，这个副作用下一节有方案解决