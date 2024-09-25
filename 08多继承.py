class Granpa:
    def gets(self):
        print("1亿")

class Father(Granpa):
    def gethome(self):
        print("房子")

class Child(Father):
    pass

one = Child()
one.gethome()
one.gets()
