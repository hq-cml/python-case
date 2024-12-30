# dict 创建
def dict1():
    m0 = {} # 创建0,空字典
    print(type(m0))
    m1 = {"a":1, "b":2, "c":3} # 创建1
    m2 = dict(a=1, b=2, c=3) # 创建2，注意，key不能有引号
    m3 = dict([("a", 1),("b", 2),("c", 3)]) # 创建3，利用元组
    m4 = dict(zip(("a", "b", "c"), (1,2,3))) # 创建4，利用zip
    print(m1== m2==m3==m4)
    print(m4)
    m5 = dict.fromkeys(("a", "b", "c"), 101) # 创建5：给出keys，相同的值
    print(m5)

    # 删除key
    m5.pop("b") #删除1 如果不存在，则会报错
    print(m5)
    del m5["a"] #删除2
    print(m5)
    m5.clear() # 清空dict
    print(m5)

    # 改
    m5["a"] = 1
    m5.update({"b":2, "c":3}) # update批量更新key
    print(m5)

# 查
def dict2():
    m1 = {"a": 1, "b": 2, "c": 3}
    print(m1["a"]) # 这种方法如果Key不存在，则会报错！
    print(m1.get("a", "not exsist"))
    print(m1.get("A", "not exsist")) # get方法则可以提供默认值
    #setdefault，有则无效，无则更新
    print(m1.setdefault("a", 10))
    print(m1.setdefault("d", 10))
    print(m1)

    #视图对象
    keys = m1.keys()
    values = m1.values()
    items = m1.items()
    print(keys)
    print(values)
    print(items)
    m1.pop("d")  # 一旦dict发生改变，则视图对象也会发生改变
    print(keys)
    print(values)
    print(items)

    #copy，浅拷贝
    m2 = m1.copy()
    m2["a"] = 100
    print(m1)
    print(m2)

    # 长度
    print(len(m1))

    # 存在性
    print("a" in m1)
    print("x" in m1)

    # 获取Key列表，value列表
    print(list(m1.keys()))
    print(list(m1.values()))
    print(list(reversed(m1.values()))) #对值进行翻转，感觉没啥意义

    # 将字典转换为迭代器
    it = iter(m1)  # 重置迭代器
    for i in it:
        print(i)

# 推导式
def dict3():
    m1 = {"a": 1, "b": 2, "c": 3}
    m2 = {v:k for k,v in m1.items()} # 键值对调换
    print(m2)
    m3 = {v:k for k,v in m1.items() if v % 2 == 1} # 推导式 + 过滤条件
    print(m3)
    m4 = {c:ord(c) for c in "Hello"} # 字符串编码
    print(m4)
    m5 = {k:v for k in ["a", "b", "c"] for v in [1,2,3]} # 推导式嵌套
    print(m5) # 仔细看这个结果，想想为什么会是这样!

#dict1()
#dict2()
dict3()