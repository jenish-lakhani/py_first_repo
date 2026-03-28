import time
import multiprocessing

square_num = []


def cal_square(numbers):
    for i in numbers:
        # time.sleep(0.2)
        print("square: ", i * i)
        square_num.append(i * i)

    print(square_num)


# def cal_qube(numbers):
#     for i in numbers:
#         time.sleep(0.2)
#         print("qube: ", i * i * i)


if __name__ == "__main__":
    arr = [2, 3, 4, 6, 7]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    # p2 = multiprocessing.Process(target=cal_qube, args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()
    print(square_num)
