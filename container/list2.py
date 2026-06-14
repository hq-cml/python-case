
# Note:浅拷贝和深拷贝
#      浅拷贝可以很好的解决上面赋值引用的问题，但是，对于嵌套列表就力不从心了
#      深拷贝才是最终完美的解决方案
def list7():
    x = [1,2,3]
    y = x.copy() # 浅拷贝，但是可以解决上面仅赋值引用的问题
    z = x[:]     # 利用切片，也同样是浅拷贝
    print(x is y)
    print(x is z)
    print(y is z)
    x [0] = 2
    print(x)
    print(y)
    print(z)
    print("--------")
    # 潜拷贝的问题：对于嵌套列表存在坑
    x = [[1,2],[3,4]]
    y = x.copy()
    x[0][1] = 8
    print(x)
    print(y)
    # 深拷贝，需要导入copy模块！
    import copy
    x = [[1, 2], [3, 4]]
    z = copy.deepcopy(x) # 深拷贝是一个递归的过程
    x[0][1] = 8
    print(x)
    print(z)

#list7()

# Note：列表推导式（步进优雅，而且效率更高，因为推导式是用C实现的）
# 语法：[expression for target in iterable]
def list8():
    l = [1,2,3]
    y = [i*2 for i in l] # 列表每个元素*2
    print(y)
    print([i for i in range(10)]) # 推导式初始化一个列表
    print([i*10 for i in range(10)])
    print([c*2 for c in "Hello"])
    print([ord(c) for c in "Hello"]) # 每个字符转成unicode编码
    print("-----")
    matrix = [[1,2,3], # 矩阵
              [4,5,6],
              [7,8,9]]
    print([row[1] for row in matrix]) # 推导列表第二列
    print([matrix[i][i] for i in range(len(matrix[0]))]) # 对角线
    # 推导式创建并初始化n维数组
    n = 3
    print([[0] * n for i in range(n)])

#list8()

# Note:推导式高级用法：搭配 if分句(if 分句，用于二次过滤)
# Note:推导式高级用法：推导式的嵌套
def list9():
    print([i for i in range(20) if i % 2==0]) # 仅打印偶数序列
    print([w for w in ["fuck", "bitch", "shit", "bullshit"] if w[0] == 'b']) # 取出b开头的单词
    print("---------")
    matrix = [[1,2,3], # 矩阵
              [4,5,6],
              [7,8,9]]
    print([ c for row in matrix for c in row]) # 利用推导式嵌套，将二维展开成一维，有点烧脑
    print([x+y for x in "abc" for y in "ABC" ]) # 笛卡尔积
    print([[x,y] for x in range(10) if x %2==0 for y in range(10) if y%3==0]) # 嵌套和if相结合

list9()

#list7()
#list8()
#list9()