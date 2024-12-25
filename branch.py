# 分支例子
def branch1():
    s = input("input a num:")
    n = int(s)
    if n<10:
        print("n < 10")
    elif n<20:
        print("n < 20")
    elif 30 <= n < 50:    # Note：还能这么写！
        print("30 <= n < 50")
    else:
        print("n >= 50")

# 高级写法，条件表达式
# Note：小括号可以组装多行代码，则无需再用\结尾
def branch2():
    s = input("input a num:")
    n = int(s)
    print("n < 10") if n < 10 else print("n >= 10") #4行变成1行
    # 更高级组合
    # 小括号可以组装多行代码
    level = (
        "perfect" if n > 90 else
        "good" if 75 < n <= 90 else
        "middle" if 60 < n <= 70
        else "bad"
    )
    print(level)

# 条件表达式应用，求min
def branch3():
    a = 3
    b = 5
    small = a if a < b else b # 优雅
    print("small=", small)


#branch1()
branch2()
#branch3()