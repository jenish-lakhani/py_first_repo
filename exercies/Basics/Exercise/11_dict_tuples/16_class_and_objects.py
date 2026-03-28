class employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID:{self.id}\nname: {self.name}")


emp = employee(1, "coder")

emp.display()

try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp

# try:
#     emp.display()
# except NameError:
#     print("emp is not defined")
