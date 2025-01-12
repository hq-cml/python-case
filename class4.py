#__getitem__: 用于拦截索引
#__setitem__: 用于拦截索引
class C:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, item):
        print("索引：", item)
        return self.data[item]
    def __setitem__(self, key, value):
        print("设置索引：", value)
        self.data[key] = value

def func1():
    c = C([1,2,3,4,5])
    print(c[0])
    print(c[1:3])
    c[2] = 100
    print(c.data)

func1()