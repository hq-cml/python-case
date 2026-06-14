# 浮点数的存储
#     Python和C、Go一样，采用IEEE754标准存储浮点数，所以存在误差
#     Python中浮点数的比较要注意这个问题
def float1():
    print(0.1+0.2)
    if 0.3 == 0.1 + 0.2:
        print("=")
    else:
        print("!=")

# 更明显的例子
def float2():
    i = 0
    while i<1:
        i = i + 0.1
        print(i)

#float2()

# Note: 精确浮点数
# decimal模块
import decimal
def decimal1():
    a = decimal.Decimal("0.1")
    b = decimal.Decimal("0.2")
    print(a+b)
    c = decimal.Decimal("0.3")
    print(a+b==c)

# Note: 地板除法，向下取整数
# Note: divmod()，直接求商和余数
# Note: abs()，绝对值
# Note: int()，转换整数，可以传入字符串、浮点、E记法字符串（科学计数法）
# Note: float()，转浮点数，可以传入字符串、浮点、E记法字符串
# Note: 求幂，两种方法
#       pow(x, y) 或者 x ** y
def div1():
    print(3//2) #地板除法
    print(-3//2) # 注意理解为什么是-2，因为是向下取整
    print(divmod(33,2)) # 直接求商和余数
    print(int('32'))
    print(int(3.14))
    print(float('+1E6')) # 科学计数法
    print(2 ** 10, pow(2, 10))

#float1()
#float2()
#decimal1()
div1()