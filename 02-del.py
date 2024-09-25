# del 删除对象的时候，自动调用该方法
class Game(object):
    def __init__(self):
        self.name ="悟空"
    # 删除对象的时候，自动调用该方法
    def __del__(self):
        # print("%状态不好，血量不足"%)
        print("%s状态不好，血量不足"%self.name)

one = Game()
del one #del 删除对象