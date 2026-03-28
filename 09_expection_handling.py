x = input("enter a number 1:")
y = input("enter a number 2:")

try:
    z = int(x) / int(y)
# except Exception as e:
#     print("exception occur", e)
#     z = None
# except ZeroDivisionError as e:
#     print("division by zero exception")
#     z = None
except Exception as e:
    print("exception type", type(e).__name__)
    z = None

print("division is", z)
