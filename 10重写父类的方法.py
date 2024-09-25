# 定义要给Animal动物类，吃肉的方法，喝的方法，睡觉的方法
# 定义要给子类 狗Dog 继承了动物类的方法 ，没有问题
# 定义一个子类Rabbit 兔子 继承了动物类， 但是吃的方法，要改一下，不能吃肉，要吃草
class Animal(object):
    def eat(self):
        print("吃肉")
    def sleep(self):
        print("睡觉")
class Dog(Animal):
    pass
class Rabbit(Animal):   # 父类的方法，不适合子类用， 子类的方法名，和父类的方法名一样
    def eat(self):   # 重写了Animal 中的eat() 方法
        print("吃草")

tz = Rabbit()
tz.eat()
tz.sleep()