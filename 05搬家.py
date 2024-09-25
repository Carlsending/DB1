class Item(object):
    def __init__(self,type,area):
        self.type = type
        self.area =area
    def __str__(self):
        return "家具的类型%s 家具的占用面积%0.1f"%(self.type,self.area)
#
bed  = Item("双人床",4.9)
print(bed)
safa  = Item("沙发",6.7)
print(safa)


class Home(object):
    def __init__(self,address,areas):
        self.address =address  #地址
        self.area = areas   # 房屋的总面积
        self.free_area = areas  # 房屋的剩余面积
     # 添加家具
    def add_item(self,itemarea):
        if self.free_area-itemarea>=0:
            print("添加成功")
            self.free_area -= itemarea   # 剩余的面积
        else:
            print("添加失败")

    def __str__(self):
       return "房屋的地址%s 房屋的面积%.1f,房屋的剩余面积%.1f"%(self.address,self.area,self.free_area)
bed  = Item("双人床",4.9)  # 家具对象
safa = Item("沙发",10)    #家具对象
print(bed)  #bed.area
print(safa)
home = Home("201房",60)   #房屋对象
# 对象的方法  对象.方法()
home.add_item(bed.area)
home.add_item(safa.area)
print(home)
