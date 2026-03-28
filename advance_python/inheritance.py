class vehicel:
    def genaral_usage(self):
        print("general use: transporation")


class car(vehicel):
    def __init__(self):
        print("i am a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.genaral_usage()
        print("specific use: commute to work, vaction with family")


class motorCycle(vehicel):
    def __init__(self):
        print("i am a motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.genaral_usage()
        print("specific use: road trip, racing")


c = car()
# c.genaral_usage()
c.specific_usage()

m = motorCycle()
# c.genaral_usage()
c.specific_usage()
