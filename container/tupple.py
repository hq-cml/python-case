#元组
# 和list类似，但是不可变；所以list相关的读取的方法，元组都可以；
# 但是写入的方法就不支持
# 元组的意义：
#   多重赋值，函数多参，多返回值
def tupple1():
    x = 1,2,3 # 多重赋值，本质上就是元组，实际上元组甚至都不需要()
    print(x)
    t = (1,2,3)
    print(t)
    # t[2] = 3 # 会报错，因为元素不可变
    print(t[1])
    print(t[::-1]) # 倒序
    tt = ((1,2),(3,4)) # 嵌套元组
    print(tt)
    print([i*2 for i in t]) # 推导式

#tupple1()

# 元组的解包：一个元组赋值对应数量的多个变量（元组和list都适应）
def tupple2():
    t = (1,2,3)
    x, y, z  = t # 解包
    print(x, y, z)
    x, y = 10, 20 # Note: 本质上Python的多重赋值就是用的元组
    print(x, y)

tupple2()