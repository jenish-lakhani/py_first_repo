def total_exp(exp):
    total = 0
    for i in exp:
        total += i
    return total


tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

tom_total = total_exp(tom_exp_list)
joe_total = total_exp(joe_exp_list)

print("Tom's total exp is ", tom_total)
# print("Joe's total exp is ", str(joe_total))
print("Joe's total exp is " + str(joe_total))


total = 0


def sum(a, b):
    # total = 0
    print("a = ", a)
    print("b = ", b)
    total = a + b
    print("total inside the function = ", total)
    return total


n = sum(10, 20)
print("total outside the function = ", total)


def sum1(a, b=0):
    print("a = ", a)
    print("b = ", b)
    total = a + b
    return total


n = sum1(10)
print(n)
