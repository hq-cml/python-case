#这个文件类似于加载钩子，在python 3.3之后非必须
print("__init__.py被调用，__name__=", __name__)

#__init__全局变量，这个全局变量，属于包，而非模块！
x = 250