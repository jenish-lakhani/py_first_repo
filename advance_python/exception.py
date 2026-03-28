# class Accident(Exception):
# def __init__(self, msg):
# self.msg = msg

# def print_exception(self):
#     print("user define excepiton", self.msg)

# def handle(self):
# print("accident occured. take detour")


# try:
# raise Accident("crash between two cars")
# except Accident as e:
# e.print_exception()
# e.handle()
#


def process_file():
    try:
        f = open("c://Python_AI//funny.txt")
        x = 1 / 0
    except FileNotFoundError as e:
        print("inside except")

    finally:
        print("cleaning up file")
        # if f:
        #     f.close()


process_file()
