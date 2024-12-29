#序列：元组、字符串、列表统称
#     前两者是不可变序列，后者是可变序列
# 所以这里统一它们的一些用法

# 乘法和加法
def arr1():
    print([1,2] + [3,4])  # 加法
    print((1,2)*2) # 乘法

# 关于id()
# python中的对象有3个值：类型、值、id
# id就是对象的唯一标识
def arr2():
    a1 = [1,2]
    print(a1, id(a1))
    a1 += [3,4]
    print(a1, id(a1))  # id不变
    t1 = (1,2)
    print(t1, id(t1))
    t1 += (3,4)
    print(t1, id(t1)) # id会变

# in和not in
def arr3():
    print("a" in "abc")
    print("x" in "abc")

# del 可以销毁整个变量，也可以清空序列的一部分
def arr4():
    a = 1
    del a
    #print(a) 直接报错，因为a已经销毁

    s = [1,2,3,4,5]
    del s[1:3] #清空序列的一部分
    print(s)

# 将可迭代对象转化成响应的结构
def arr5():
    print(list("abc")) # 转化为列表
    print(list((1,2,3))) # 转化为列表
    print(tuple("abc")) # 转化为元组
    print(str([1,2,3])) # 注意这里转成字符串，真的是转成了字符串。。。

# 序列作为参数，各种统计类、排序类
def arr6():
    print(min([1,2,3]))
    print(max([1,2,3]))
    print(sum([1,2,3]))
    s = [2,1,7,4,5]
    print(sorted(s)) # 排序，注意和sort的区别，sorted不影响原数组！
    print(s)
    s = ["Aa", "Cc", "B"]
    print(sorted(s)) # 默认维度是字符串大小
    print(sorted(s, key=len)) # sorted还支持key参数，用来指定具体的排序维度！
    s = [1,2,5,8,0]
    rIter = reversed(s) # reversed得到的是一个反向迭代器！
    print(list(rIter))

# 其他
# 判断可迭代对象真假
# zip，拉链函数
# map, 方法映射
# filter，过滤方法，保留真的对象的迭代器
def arr7():
    print(all([1,1,0])) # 全部为真则为真
    print(any([1,1,0])) # 1个为真则为真
    zipped = zip([1,2,3], [4,5,6]) # 返回的是一个迭代器，需要list来
    print(list(zipped))
    maped = map(ord, "Hello") # map是将第一个参数函数，作用到后面的可迭代对象上面，返回迭代器
    print(list(maped)) # 最终得到Hello各个字母的ord值
    maped = map(pow, [2,3], [2,3])
    print(list(maped))
    filtered = filter(str.islower, "Hello World") # 过滤得到所有的小写字母
    print(list(filtered))

# Note: 迭代器和可迭代对象
# 迭代器必然是可迭代对象；前者是一次性的，后者是可重复使用的
def arr8():
    maped = map(ord, "Hello")
    print(list(maped)) # 仅可使用一次
    print(list(maped))
    x = [1,2,3,4,5]
    it = iter(x)
    print(type(x))
    print(type(it))
    # 访问迭代器, next方法
    while True:
        i = next(it, "nothing")# 必须加上默认值，否则会报错
        if i == "nothing":
            print("end")
            break
        else:
            print(i)

    # 访问迭代器
    it = iter(x) # 重置迭代器
    for i in it:
        print(i)

#arr1()
#arr2()
#arr3()
#arr4()
#rr5()
#arr6()
#arr7()
arr8()