def loop1():
    i = 0
    while True:
        print(i)
        i += 1  # Python没有 ++ ！
        if i == 10 :
            break

# Note: 循环中的else！其他语言没有
#       当循环条件不再为真的时候，才会执行else
#       这个东西的意义是：可以方便的检测到循环退出状态
def loop2():
    i = 0
    while i < 5:
        print("in loop, i=", i)
        i += 1
    else: # else会执行
        print("out loop, i=", i)

# else会执行的例子
def loop3():
    i = 0
    while i < 5:
        print("in loop, i=", i)
        i += 1
        if i == 3:
            break
    else: # else不会执行！因为是break语句导致了循环退出（此时循环条件本身仍然是满足的）
        print("out loop, i=", i)

# for 循环
# Note: range()，将数字转换成可迭代对象
def loop4():
    for i in "abc":
        print(i)
    print("------")
    for i in range(3): # [0, n-1]
        print(i)
    print("------")
    for i in range(5,8): # 开始，结束
        print(i)
    print("------")
    for i in range(5,10, 2): # 开始，结束，步进
        print(i)


# 综合例子，素数分析
def loop5(n=10):
    for i in range(2, n+1):
        for x in range(2, i):
            if i % x == 0:
                print(i, "不是素数")
                break
        else:
            print(i, "是素数")
#loop1()
#loop2()
#loop3()
#loop4()
loop5()