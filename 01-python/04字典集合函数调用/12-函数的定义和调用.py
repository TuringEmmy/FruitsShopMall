# 定义函数的格式
# def 函数名(参数[可选]):
#     # 功能代码的实现
print("我要定义函数了")
# 定义函数，不会执行函数里面的代码
def show_info():
    # 函数里面叫做功能实现的代码
    name = input("请输入您的姓名:")
    age = input("请输入您的年龄:")

    print("姓名:%s 年龄:%s" % (name, age))

# 调用函数会执行函数里面的代码
show_info()
