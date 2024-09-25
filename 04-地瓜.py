# 烤地瓜规则：
#
# 1.地瓜有自己的状态，默认是生的，地瓜可以进行烧烤
# 2.地瓜有自己烧烤的总时间，由每次烧烤的时间累加得出
# 3.地瓜烧烤时，需要提供本次烧烤的时间
# 4.地瓜烧烤时，地瓜状态随着烧烤总时间的变化而改变：
# [0, 3) 生的、[3, 6) 半生不熟、[6, 8)
# 熟了、>=8 烤糊了
# 5.输出地瓜信息时，可以显示地瓜的状态和烧烤的总时间
class SweetPotato():
    def __init__(self,states,times):
        self.states = states
        self.cooked_time = times
    #烧烤的方法
    def cooked(self,time):
        self.cooked_time += time  #总时间
        if self.cooked_time >= 0 and self.cooked_time < 3:
            self.states = "生的"
        elif self.cooked_time >= 3 and self.cooked_time < 6:
            self.states = "半生不熟"
        elif self.cooked_time >= 6 and self.cooked_time < 8:
            self.states = "熟了"
        elif self.cooked_time >= 8:
            self.states = "糊了"
    def __str__(self):
        return "地瓜的状态：%s  地瓜烧烤的总时间是：%d"%(self.states,self.cooked_time)
one = SweetPotato("生的",0)
one.cooked(2)
print(one)  #调用str方法
one.cooked(2)
print(one)
one.cooked(3)
print(one)
one.cooked(3)
print(one)