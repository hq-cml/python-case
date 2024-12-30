# python中字典和集合的关系，很暧昧
def set1():
    # 类型关系
    print(type({}))
    print(type({"a"}))
    print(type({"a":1}))

    # 集合创建
    s1 = {"a", "b"} # 方法1：花括号
    s2 = {i for i in "abc"} #方法2：推导式
    print(s2, type(s2))
    s3 = set("abc") # 方法3：类型构造器，参数是一个可迭代对象
    print(s3, type(s3))

    # in 和 not in
    print("a" in s1)
    print("c" in s1)

    # 元素仅能遍历，不能随机访问
    for i in s1:
        print(i)

# 集合的应用场景：去重、交集、差集。。。
def set2():
    s1 = set([1,2,3,1,2]) # 去重
    print(s1) #

    # 判断列表元素是否有重复
    l1 = [1,2,3,4,1]
    print(len(l1) == len(set(l1)))

    # 是否毫不相干，不存在交集
    s1 = {1,2,3}
    s2 = {4,5,6}
    s3 = {3,4,5}
    print(s1.isdisjoint(s2))
    print(s1.isdisjoint(s3))

    # 子集和父集判断
    s4 = {2,3}
    print(s4.issubset(s1))
    print(s4.issubset(s2))
    print(s1.issuperset(s4))

    # 交并差
    print(s1.intersection(s3)) # 交集
    print(s1.union(s2)) # 并集
    print(s1.difference(s3)) # 差集

    # 子交并差的符号表示法，必须是两个集合之间
    print(s1 <= {1,2,3}) #子集和超集
    print(s1 < {1,2,3})
    print(s1 >= {1,2,3})
    print(s1 > {1,2,3})
    print(s1 & {1,2}) #交集
    print(s1 | s2) # 并集
    print(s1 - {1}) # 差集


#set1()
set2()