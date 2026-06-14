#Note: 列表不要求必须是同一个类型
def list1():
    l = [1,2,3, "hello"] # 不同类型
    for item in l:       # 列表的遍历
        print(item)
    print(l[2])       # 下标访问
    print(l[-1])      # 最后一个元素
    print(l[-2])      # 倒数第2个元素

#Note：切片，和go类似；
#      并且还新增支持step步长
def list2():
    l = [1,2,3,4,5,6,7]
    print(l[1:3])
    print(l[1:])
    print(l[:3])
    print(l[:])
    print(l[::2]) # 步进2
    print(l[::-1]) # 倒序切片（列表），优雅

#list2()

#Note: 列表：增
def list3():
    l1 = [1,2,3]
    l1.append(4) # 这里和Go有区别，append直接就会影响到原来的list
    print(l1)
    l1.extend([1,2,3]) # 批量扩充
    print(l1)
    l1[len(l1):] = [8,8] # 活用切片的方式扩充
    print(l1)
    l1.insert(2, 8) # 8将出现在idx=2的位置
    print(l1)
    l1.remove(8) # 删除元素（只会删除第一个出现的；如果元素不存在，则直接报错！）
    print(l1)
    l1.pop(2) # 删除idx=2的元素，Note: 注意remove和pop的区别
    print(l1)
    l1.clear() # 清空元素=>空列表
    print(l1)

#list3()

#Note: 列表：改
def list4():
    l = [1,1,3,4,5,6]
    print(l)
    l[1] = 2 # 通过下标改元素
    print(l)
    l[3:] = [40, 50] # 利用切片替换，从idx=3开始替换，Note：这种用法相当于将数组从idx=3开始截断了，然后拼接新的！
    print(l)
    l.reverse() # 倒排序（直接影响list本身）
    print(l)
    l.sort() # 正排序（直接影响list本身）
    print(l)
    l.sort(reverse=True) # 倒排序 == reverse()
    print(l)
    l.sort()
    l.insert(2, 3) # 插入
    print(l)
    print(l.count(3)) # 元素计数
    print(l.index(40)) # 查找元素位置（第一次出现）
    print(l.index(3, 3, 5)) # 指定start和end，开始查找
    l2 = l.copy() #列表拷贝（浅拷贝）
    print(l2)
    l3 = l[:]  #列表拷贝（浅拷贝），利用切片
    print(l3)
    l[1] = 88 # 虽然是浅拷贝，但是改变了原来的list，不影响其他list（Note：拷贝的深浅，其实针对的是嵌套列表，也就是二维列表）
    print(l)
    print(l2)
    print(l3)

#list4()

#Note: 列表：加法、乘法、嵌套
def list5():
    l1 = [1,2,3]
    l2 = [4,5]
    print(l1+l2) # 加法：拼接
    print(l1*3) # 乘法：重复
    matrix = [[1,2,3], # 嵌套
              [4,5,6],
              [7,8,9]]
    print(matrix)
    for row in matrix: # 访问循环列表
        for i in row:
            print(i, end=' ') # 规定结尾符，默认是换行
        print()
    print(matrix[1][1])
    print("---------")
    #通过循环创建和初始化一个matrix
    #Note：这里不能写成A = [[0]*3]*3 !，可以用下面的is运算符来分析原因
    A = [0] * 3
    print(A)
    for i in range(3):
        A[i] = [0] * 3
    print(A)

#list5()

# is运算法：同一性运算符，追本溯源，查看变量引用是否一致
def list6():
    a = "hello"
    b = "hello"
    print(a is b) # 对于不可变的字符串，引用一致
    c = [0,0]
    d = [0,0]
    print(c is d) # 对于可变对象list，通常都是不一致的
    x = [1,2,3]
    y = x         # 列表的赋值，只是引用的赋值！
    print(x is y)
    x [0] = 2
    print(x) # 引用赋值，所以同时受影响
    print(y)

#list6()
