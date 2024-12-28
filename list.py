#Note: 列表不要求必须是同一个类型
def list1():
    l = [1,2,3, "hello"] # 不同类型
    for item in l:       # 列表的遍历
        print(item)
    print(l[2])       # 下标访问
    print(l[-1])      # 最后一个元素
    print(l[-2])      # 倒数第2个元素

#Note：切片，和go类似；
#      并且还新增支持step
def list2():
    l = [1,2,3,4,5,6,7]
    print(l[1:3])
    print(l[1:])
    print(l[:3])
    print(l[:])
    print(l[::2]) # 步进2
    print(l[::-1]) # 倒序切片（列表），优雅

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
    l1.pop(2) # 删除idx=2的元素
    print(l1)
    l1.clear() # 自我销毁=>空列表
    print(l1)

#Note: 列表：改
def list4():
    l = [1,1,3,4,5,6]
    print(l)
    l[1] = 2 # 通过下标改元素
    print(l)
    l[3:] = [40, 50] # 利用切片替换，从idx=3开始替换
    print(l)
    l.reverse() # 倒排序（直接影响list本身）
    print(l)
    l.sort() # 正排序（直接影响list本身）
    print(l)
    l.sort(reverse=True) # 倒排序 == reverse()
    print(l)
    l.sort()
    l.insert(2, 3)
    print(l)
    print(l.count(3)) # 元素计数
    print(l.index(40)) # 查找元素位置（第一次出现）
    print(l.index(3, 3, 5)) # 指定start和end，开始查找
    l2 = l.copy() #列表拷贝（浅拷贝）
    print(l2)
    l3 = l[:]  #列表拷贝（浅拷贝），利用切片
    print(l3)

#list1()
#list2()
#list3()
list4()