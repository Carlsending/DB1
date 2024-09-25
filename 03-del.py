# del 删除对象的时候，自动调用该方法
class Game:
    def __init__(self):
        self.name ="悟空"
    # 删除对象的时候，自动调用该方法
    def __del__(self):
        # print("%状态不好，血量不足"%)
        print("%s状态不好，血量不足"%self.name)

print("*"*40)   #整个文件执行完成后，输出

def fun():
    one = Game()  #调用完函数，one 局部变量 生存周期 就是在函数内部
fun()
print("*"*40) 