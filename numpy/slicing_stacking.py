import numpy as np

a = np.array([6, 7, 8, 9])
print(a[0:2])  # print 6, 7

print(a[2:])  # print 8,9
print(a[-1])  # last element 9
print(a[-2])  # last second element
print(a[-2:])  # print 8,9


b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[1, 2])  # print 6
print(b[2, 0])  # print 7
print(b[-1])  # print last row
print(b[-1, 0:2])  # print the first tow element of last row
print(b[:, 1:3])  # colum 1 and 2 print karse


c = np.array([[101, "Mira"], [102, "Abdul"], [103, "Andrea"]])
d = np.array(
    [
        [101, 250.50, "2023-08-01"],
        [102, 150.00, "2023-08-02"],
        [103, 300.00, "2023-08-01"],
    ]
)

print(np.hstack((c, d)))  # banne ne bhega karse horizontaly , combine arry
# 2 be round bracket no matlab ke aapde aane tupple ma fervyu 6

e = np.array([[104, "Venkat"], [105, "John"], [106, "Lathy"]])

print(np.vstack((c, e)))  # add karse verticaly


transaction = np.array(
    [
        [101, "Mohan", 250.50, "2023-08-01"],
        [102, "Bob", 150.00, "2023-08-02"],
        [103, "Fatima", 300.75, "2023-08-01"],
        [104, "Davida", 400.50, "2023-08-03"],
        [105, "Aryan", 330.1, "2023-08-04"],
    ]
)

print(np.hsplit(transaction, [3]))  # spllite kari dese 3 column thi
a, b = np.hsplit(transaction, [2])
print(a)  # a ma pelo bhag aavse array no
print(b)  # b ma bijo bhag aavse array no

x, y = np.vsplit(transaction, [4])  # splite karse 4 row  thi vertically
print(x)
print(y)


monthaly_sales = np.array([30, 33, 35, 28, 42])

result = monthaly_sales < 32
print(result)

print(monthaly_sales[result])

print(monthaly_sales.max())  # max aapse

index = np.argmax(monthaly_sales)  # index return karse
print(index)

print(monthaly_sales[index])  # actule value provide kare

# transaction[:]  this mean give me all rows
print(
    transaction[:, 2]
)  # all rows and give me 2 column  , it will print only second colimn value

print(transaction[:, 2].astype(float))  # float ma convert kare

t_index = np.argmax(transaction[:, 2].astype(float))
print(t_index)

print(transaction[t_index])  # aakhi max vali index print thase

print(transaction[transaction[:, 0] == "102"])  # 102 vali row print thase
