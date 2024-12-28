#元组
# 和list类似，但是不可变
# 元组的意义：
#   多重赋值，函数多参
def tupple1():
    t = (1,2,3)
    print(t)
    # t[2] = 3 # 会报错，因为元素不可变
    print(t[1])
    print(t[::-1]) # 倒序
    tt = ((1,2),(3,4))
    print(tt) # 嵌套元组
    print([i*2 for i in t]) # 推导式


tupple1()