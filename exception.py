#异常的捕获与处理
def func1():
    try:
        import random
        i = random.randint(1, 100)
        if i%4==0:
            1/0
        elif i%4==1:
            "a" + 1
        elif i%4==2:
            raise ValueError("aaa") # 主动抛出一个异常
        elif i%4==3:
            assert 1==0 #断言异常：不满足则会抛出
        else:
            1 + 1
    except ZeroDivisionError as e: # e是取出异常本身，可选
        print("除数==0！", e)
    except (ValueError, TypeError) as e:#一次捕获多个异常
        print("其他错误：", e)
    except:
        print("未知错误")
    else: # 可选，如果未出现任何异常，才会执行，注意，不是finally！
        print("未发现异常")
    finally: # 可选
        print("结束")

func1()