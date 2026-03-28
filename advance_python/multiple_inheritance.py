class father:
    # def gardening(self):
    #     print("i enjoy the gardning")
    def skills(self):
        print("gardening, programming")


class mother:
    # def cooking(self):
    #     print("i enjoying the cooking")
    def skills(self):
        print("cooking, art")


class child(father, mother):
    # def sports(self):
    #     print("i enjoy the sports")

    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("sports")


c = child()
# c.gardening()
# c.cooking()
# c.sports()
c.skills()
