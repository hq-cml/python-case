# python常用示例

### 构建venv

#### windows:
基于pycharm自动创建.venv
#### linux:
共享文件夹无法建立软链，所以需要在系统其他目录创建venv
* py -m venv /data/python_venv/python-case/venv
* source /data/python_venv/python-case/venv/bin/activate

### 循序渐进
基础：basic
1. string: 基础字符串、STD I/O、随机数
2. number: 浮点数的比较误差问题、精确浮点decimal包、数字类型转换、求商、求余、幂运算等
3. bool：逻辑运算符：and/or/not，短路原则、空值False问题
4. branch，条件分支、***条件表达式***
5. loop，循环：while、***循环中的else***、for、range
6. file：文件读写、文件路径相关、***with管理器***、***序列化&反序列化***
7. module、tc/m1：***模块和包***、***模块上传PyPI***

容器：container
1. list1，列表（数组）：类似于go的slice、CRUD、数组的加法和乘法、嵌套（多维数组）
2. list2，深浅拷贝、copy模块深拷贝、***列表推导式***
3. tupple，元组 
4. string，字符串高级操作：大小写转换、对齐、计数、替换、各类判断、截取、切割、***格式化和f子字符串***
5. sequence，序列：***id()方法、is运算符***、***可迭代对象&迭代器***、zip、map、filter
6. dict，字典：CURD、***字典推导式***
7. set，集合：无val的的dict、无序性、不重复、子交并补

函数：function
1. function1：pass、函数嵌套、未知参数、关键字参数、参数默默认值、***收集参数（不定参）***、、***字典参数（配合关键字）***
2. function2：***作用域***、***闭包***、***装饰器***
3. function3：***lambda***、***生成器yield***、***生成器对象***、***函数文档***、***参数引导***、***内省***
4. exception：***try/except/finally***、***raise***、***else***

类和对象：oop
1. class1：定义、继承、覆盖、组合、***dir查看一个对象***、***isinstance***、***issubclass***、***成员的归属问题***、***__dict__内省***、
2. class2：***构造函数***、***钻石基础问题***、***super()***、***MRO顺序***、***MixIn问题***、***鸭子类型***、***私有变量 & 名字改编***、
3. class3：***魔术方法（拦截的艺术）***、***__new__&__init__***、***增删改查__attr__***、***__iter__&__next__***、***__call__***
4. class4: ***property***、***属性描述符***、***__get__***、***__set__***、***__delete__***
5. class5: ***装饰器***、***函数装饰一个类***、***类装饰一个函数***
6. class6: ***type***、***type动态创造一个类***、***元类***

