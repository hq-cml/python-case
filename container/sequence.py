#序列：
#   在python中，序列是列表、元组、字符串等的统称
#   其中列表是可变序列，其他两者是不可变序列，
# 所以这里统一它们的一些用法：
#   1. 都可以通过索引来获取指定元素
#   2. 索引开始位是0
#   3. 都可以通过切片来获取范围
#   4. 很多运算符都是通用的

# 乘法和加法
def seq1():
    print([1,2] + [3,4])  # 加法
    print((1,2)*2) # 乘法

#seq1()

# 关于id()
# Note：python中的对象有3个值：类型、值、id
# id就是对象的唯一标识
# is运算符：本质上就是看两个对象的id是否一致
def seq2():
    a1 = [1,2]
    print(a1, id(a1))
    a1 += [3,4]
    print(a1, id(a1))  # id不变！
    t1 = (1,2)
    print(t1, id(t1))
    t1 += (3,4)
    print(t1, id(t1)) # id会变（因为元组是不可变的）
    print(a1 is t1) # is运算符

#seq2()

# in和not in，是否包含或者不包含
def seq3():
    print("a" in "abc")
    print("x" in "abc")

# del 可以销毁整个变量，也可以清空序列的指定部分
# clear 清空一个序列（但是变量本身没有销毁）
def seq4():
    a = 1
    del a
    #print(a) 直接报错，因为a已经销毁

    s = [1,2,3,4,5]
    del s[1:3] #清空序列的一部分，本质上利用了切片
    print(s)
    s.clear()
    print("---", s)
#seq4()

# 将可迭代对象转化成相应的结构
def seq5():
    print(list("abc")) # 转化为列表
    print(list((1,2,3))) # 转化为列表
    print(tuple("abc")) # 转化为元组
    print("---")
    s = str([1,2,3])
    print(type(s))
    print(s) # 注意这里转成字符串，'[1,2,3]', 真的是转成了字符串。。。
    print(len(s)) # 太令人费解了

#seq5()

# 序列作为参数，各种统计类、排序类
def seq6():
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
    rIter = reversed(s) # reversed得到的是一个反向迭代器！（迭代器本质上也是一种可迭代对象）
    print(list(rIter))
#seq6()

# 其他
# 判断可迭代对象真假
# zip，拉链函数，依次配对
# map, 方法映射，将第一个参数函数，作用到后面的可迭代对象上面，返回迭代器
# filter，过滤方法，保留真的对象的迭代器
def seq7():
    print(all([1,1,0])) # 全部为真则为真
    print(any([1,1,0])) # 1个为真则为真
    zipped = zip([1,2,3], [4,5,6]) # 依次两两配对，返回的是一个迭代器，需要list来展开
    print(type(zipped))
    print(list(zipped))
    print("------")
    maped = map(ord, "Hello") # map是将第一个参数函数，作用到后面的可迭代对象上面，返回迭代器
    print(type(maped)) #<class 'map'>，这里注意不要混了，pyhon中map是迭代器，不是golang中的map
    print(list(maped)) # 最终得到Hello各个字母的ord值
    maped = map(pow, [2,3], [2,3]) # pow(2,2), pow(3,3)
    print(list(maped))
    filtered = filter(str.islower, "Hello World") # 过滤得到所有的小写字母
    print(type(filtered))
    print(list(filtered))
seq7()

# 迭代器的意义：
#    迭代器是“懒加载”的遍历工具，它不一次性把所有元素都准备好，而是每次问它要下一个，
#    它才计算/取出下一个。这比直接迭代可迭代对象（如列表）更节省内存，也能处理无穷序列。
#    迭代器其实分很多种：<class 'map'>、<class 'filter'>、<class 'list_iterator'>、、<class 'zip'>
# Note: 迭代器和可迭代对象
#    迭代器必然是可迭代对象，反之不然，区别如下：
#    迭代器是一次性的；迭代对象可重复使用的
def seq8():
    maped = map(ord, "Hello")
    print(list(maped)) # 仅可使用一次
    print(list(maped)) # 为空
    print("----")
    x = [1,2,3,4,5]
    it = iter(x) # iter将x变成可迭代器
    print(type(x))
    print(type(it))
    # 访问迭代器, next方法
    while True:
        i = next(it, "nothing") # 必须加上默认值，否则会报错
        if i == "nothing":
            print("end")
            break
        else:
            print(i)
    print("----")
    # 访问迭代器
    it = iter(x) # 重置迭代器
    for i in it:
        print(i)
    print("----")
    # 直接迭代也可以
    for i in x:
        print(i)
#seq1()
#seq2()
#seq3()
#seq4()
#seq5()
#seq6()
#seq7()
#seq8()