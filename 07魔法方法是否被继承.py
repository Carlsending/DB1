class Dog:
    def __init__(self,names,legs):
        self.name =names
        self.leg = legs
    def __str__(self):
        return "名字:%s %d 条腿"%(self.name,self.leg)

# 定义一个哮天犬  Xtq类继承了父类 Dog
class Xtq(Dog):
    def name1(self):
        print("旺财")

#  哮天犬对象
one = Xtq("哮天犬",4)
print(one)
one.name1()