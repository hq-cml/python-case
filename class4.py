#索引和切片
#__getitem__: 用于拦截索引
#__setitem__: 用于拦截索引
class C:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, item):
        print("索引：", item)
        return self.data[item]
    def __setitem__(self, key, value):
        print("设置索引：", value)
        self.data[key] = value

def func1():
    c = C([1,2,3,4,5])
    print(c[0])
    print(c[1:3])
    c[2] = 100
    print(c.data)

#func1()

#针对for之类的迭代
#针对可迭代对象的魔法方法
#__iter__: 如果一个类定义了一个__iter__，他就是可迭代对象
#__next__: 如果一个类定义了一个__iter__，他就是迭代器
#比如，list是可迭代对象，但它不是迭代器，验证：dir(list)
#所以，当for遍历一个list的时候，到底发生了什么？
#   其实，底层第一步是将list转变成迭代器，然后才能遍历！
def func2():
    x = [1,2,3]
    print(dir(x)) #没有next，说明不是迭代器

    # for
    for i in x:
        print(i, end=" ")
    print()
    # 与for等价
    it = iter(x) #得到迭代器
    while True:
        try:
            v = it.__next__()
        except StopIteration: # 迭代器遍历结束抛出的异常
            break
        print(v, end=" ")
#func2()

#创造一个迭代对象
class Tribble:
    def __init__(self, start, end):
        self.v = start
        self.end = end
    def __iter__(self): #创造一个迭代器，因为自身就是迭代器，所以直接返回
        return self
    def __next__(self):
        if self.v == self.end:
            raise StopIteration
        else:
            ret = self.v * 3
            self.v += 1
            return ret
def func3():
    t = Tribble(1,5)
    # 可迭代对象，直接进行迭代
    for i in t:
        print(i, end=" ")

func3() #体会为什么是这个输出

#其他的一些魔法方法
# 暂且了解
# in & not in: __contains__
# yes or no: __bool__
# <: __lt__
# <=: __le__
# >: __gt__
# >=: __ge__
# ==: __eq__
# !=: __ne__
# 将一个对象当做函数一样调用: __call__，这个特性可以用来替代闭包
# 字符串相关，不怎么常用: __str__和__repr__



#代偿机制：
# 如果直接需要的方法找不到，会尝试其他的方法凑活使用
# __contains__ --->  __iter__/__next__
# __iter__/__next__ --->  __getitem__
# __bool__ --->  __len__