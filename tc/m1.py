def func1():
    print("模块m1, 方法func1")

#包内部，要访问包全局变量，要导入整个包
def func2():
    import tc
    print(tc.x)

x = 123

print("模块名：", __name__)
if __name__ == "__main__":
    print("如果被导入，不该执行")