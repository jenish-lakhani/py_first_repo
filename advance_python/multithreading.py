import time
import threading


def cal_square(numbers):
    print("claculating square of numbers")
    for i in numbers:
        time.sleep(0.2)
        print("square:", i * i)


def cal_qube(numbers):
    print("calculating qube of numbers")
    for i in numbers:
        time.sleep(0.2)
        print("qube : ", i * i * i)


arr = [2, 3, 4, 5, 6, 7]
t = time.time()
# cal_square(arr)
# cal_qube(arr)
t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_qube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ", time.time() - t)
print("i am done with all my work now")
