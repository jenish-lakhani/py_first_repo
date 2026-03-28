class human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tenis")
        elif self.occupation == "actor":
            print(self.name, "shoots a flim")
        else:
            print(self.name, "is a programmer")

    def speaks(self):
        print(self.name, "says how are you")


tom = human("tom cruise", "actor")
tom.do_work()
tom.speaks()

maria = human("maria sharapova", "tennis player")
maria.do_work()
maria.speaks()

jenish = human("jenish", "programmer")
jenish.do_work()
jenish.speaks()
