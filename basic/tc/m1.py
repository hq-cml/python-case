def func1():
    print("模块m1, 方法func1")

#要访问包的全局变量，要导入整个包
def func2():
    from basic import tc
    print(tc.x) # 注意这个x，它不是下面的x，是__init__.py文件的x

#模块的全局变量
x = 123

print("模块名：", __name__)
if __name__ == "__main__":
    print("如果被导入，不该执行")

#Note：模块中的：__all__
# 这种用法是规定了可以被from xx import *用法的可见性
# 对于模块来说，如果没有定义__all__，那么from xx import *语法将导入模块中的所有东西
#__all__ = ["func2"] # 这句话如果去掉注释，module.py将报错