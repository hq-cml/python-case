# 函数
def func1():
    pass # 占位符，相当于todo

# 参数
def func2():
    def subf1(a, b): # Note：函数嵌套
        print(a,b)

    # 位置参数
    subf1("hello", "world")
    # 关键字参数
    subf1(b = "world", a = "hello")
    # 同时使用，则关键字参数必须放在位置参数后面
    subf1("hello", b = "world")

    # 参数默认值（必须放最后）
    def subf2(a, b="world"):
        print(a, b)
    subf2("hello")

    # Note：/用在参数中，表示左侧仅能是位置参数
    def sub3(a, /, b): # a只能是位置参数
        print(a, b)
    #sub3(a=1, b=2) # 报错
    sub3(1, b=2)

    # Note：*用在参数中，表示右侧仅能是关键字参数
    def sub4(a, *, b):  # b只能是关键字参数
        print(a, b)
    #sub4(a=1, 2) # 报错
    sub4(1, b=2)

    # 不定参数（收集参数）
    def sub5(*args):
        print("有{}个参数".format(len(args)))
        print("第2个参数是：{}".format(args[1]))
        print(args) # Note：直接打印出参数，发现，原来不定参数底层是元组！
        print(type(args))
    sub5("a", "b", "c")

    # 收集参数+普通参数：则必须要配合关键字参数
    def sub6(*args, p1):
        print(args)
        print(p1)
    sub6(1,2,3, p1="a") # 必须如此，否则报错

    # **号，表示参数将被转化为字典，此时必须配合关键字参数
    def sub7(**args):
        print(args)
    sub7(a="1", b="2")

    # 参数解包，类似于golang的...
    # 当一个函数是收集参数的时候，利用*可以将元组解包传入；同理**也是如此
    def sub8(a,b,c):
        print(a,b,c)
    p1 = (1,2,3)
    sub8(*p1) # 此时必须要*进行解包，直接传入p1会报错，类似于golang的...
    p2 = {"a":1, "b":2, "c":3}
    sub7(**p2)
    sub8(**p2)

    # *和**同时有的情况
    help(str.format)


# 返回值
def func3():
    def sub1():
        return 1,2,3
    r = sub1()
    print(r) # Note：多返回值，底层也是元组！
    x, y, z = sub1()
    print(x, y, z) # 也可以直接解包得到返回值

# 作用域
x = 100 # 全局
def func4():
    print(x)

# 嵌套函数 & 内部修改外部值
def func5():
    x= 10
    def funcs1():
        nonlocal x # 声明x是非本地，也就是外层x
        x = 20
        print("in funcs1: ", x)
    funcs1()
    print("in func5: ", x)

#func2()
#func3()
#func4()
func5()