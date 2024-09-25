# def show():
#     pass
#     a = "hello"
#     return a
# print(show())  #None

class Dog(object):
    #输出对象的事后，自动调用str的魔法方法
    # pass
    def __str__(self):
        return "描述信息"    #结果返回给    对象

wc = Dog()
print(wc)     #默认对象地址  <__main__.Dog object at 0x7fd9f8139af0>