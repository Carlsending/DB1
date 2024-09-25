#狗狗类
class Dog:
    def eat(self):
        print("吃骨头")
    def dark(self):
        print("汪汪")
# 子类 （父类）  只有一个父类，单继承
class Xtq(Dog):
    def fly(self):  #功能 扩展
        print("飞")
# 对象
god = Xtq()
god.eat()
god.dark()   #父类的方法
god.fly()     #自己的方法
