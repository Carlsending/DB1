# MP3  听歌
# 摩托   moto  可以打电话  听歌
#   苹果手机  apple  可以打电话，听歌 ,玩游戏
class Mp3(object):
    def listen(self):
        print("听歌")
class Moto(Mp3):
    def tel(self):
        print("打电话")
class Apple(Moto):
    def game(self):
        print("玩游戏")

ps = Apple()
ps.game()
ps.tel()
ps.listen()