# 文件操作
import pickle


def func1():
    f = open("a.txt", "w")
    f.writelines("Hello\n")
    f.writelines("World")
    f.close()

def func2():
    f = open("a.txt", "r+")
    for l in f:
        print(l)

#从pathlib中导入Path包
#有很多有用的方法，用时再查
from pathlib import Path

#Note：with管理器，有点类似于golang的defer
def func3():
    with open("a.txt", "w") as f:
        f.write("aaa")
        1/0 # 虽然程序会报错终端，但是仍然可以完成内容保存，因为f.close将有with管理器来负责执行

#Note: 序列化和反序列化
def func4():
    import pickle
    with open("data.pkl", "wb") as f:
        pickle.dump([1,2,3], f)
        pickle.dump({"a":1, "b":2, "c":3}, f)

def func5():
    import pickle
    with open("data.pkl", "rb") as f:
        print(pickle.load(f))
        print(pickle.load(f))

#func1()
#func2()
#func4()
func5()