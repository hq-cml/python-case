#lambda（一行流：匿名函数）
#lambda可以代替函数，但是它一般是比较简单的逻辑，可以避免函数命名
#def则用于常规的相对复杂一点的地方
#lambda语法：lambda arg1, arg2, ... : expression
#解释：lambda关键字，参数列表，冒号后面是函数体
#等价于: def <lambda> (arg1, arg2, ...):
#           return expression
def func1():
    square = lambda y: y*y
    print(square(5))

    #lambda和map结合(lambda就可以认为是一个函数简写)
    #注意map和filter返回的是一个迭代器，需要list展开
    print(list(map(lambda x: x*x, [1,2,3])))
    print(list(filter(lambda x:x%2==1, range(10))))
#func1()

# 生成器
# 用yield语句，代替return，函数将变成生成器函数！
# 实现的效果类似于闭包（函数退出后内部状态仍然保留），但是比闭包简单
# 是一种特殊的可迭代对象，每次遇到yield，就会生成迭代对象的一个元素
def func2():
    # counter()使用的是yield，
    # 而非return，所以此时counter不再是普通函数，而是生成器函数！
    def counter():
        i = 0
        while i<=3:
            yield i # 生成迭代对象中的一个元素
            i += 1

    # 调用counter()，得到一个迭代器
    it = counter()  # counter()也是一个迭代器
    print(next(it, "over"))
    print(next(it, "over"))
    print(next(it, "over"))
    print(next(it, "over"))
    print(next(it, "over"))
    print(next(it, "over"))

    print("-----------")
    for x in counter(): # counter()就成了一个可迭代对象[0,1,2,3]
        print(x)

#func2()


# 利用生成器来实现斐波那契
# 原理：yield是带记忆功能的return
def func3():
    def fib():
        back1, back2 = 0, 1
        while True:
            yield back1 # 带记忆的return
            back1, back2 = back2, back1+back2
    it = fib()
    # 循环打印前10个fib数
    for i in range (10):
        print(next(it))
#func3()

# Note：生成器对象
# 虽然写法上类似于列表推导式，但是将方括号换成了小括号
# 注意：这不是元组推导式！！！Python没有元组推导式
# 注意这不是元组推导式，而是生成器对象
# 它和列表推导式的区别：生成器一次下一个蛋；列表推导式一次性统一求值
def func4():
    it = (i ** 2 for i in range(10))
    print(type (it))
    for i in it :
        print(i)

#func4()

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