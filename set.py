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

# 集合的更新、不可变集合
def set3():
    # 集合的更新
    s1 = {1,2,3}
    s1.update({2,3,4})
    print(s1)

    # 不可变集合
    s2 = frozenset([1,2,3])
    #s2.update({2, 3, 4}) # 报错，因为不可变

    # 增加1个元素
    s1.add(5)
    print(s1)

    # 删除一个元素
    s1.remove(5) # 不存在则报错
    print(s1)
    s1.discard(5) # 不存在不报错
    s1.pop() # 随机弹出1个元素
    print(s1)

    # 清空
    s1.clear()

# 可哈希：字典key和set，都必须是可hash的（也就是不可变值）
def set4():
    print(hash(1))
    print(hash(1.0))
    print(hash(1.1))

    #通常来说，仅不可变的变量，才是可hash的
    print(hash("hello"))
    #print(hash([1,2])) 报错，因为[]是可变的
    print(hash((1, 2)))


#set1()
#set2()
#set3()
set4()