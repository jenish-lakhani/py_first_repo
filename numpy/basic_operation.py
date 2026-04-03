import numpy as np

rev_q1 = np.array([10, 12, 9])
# print(rev_q1.ndim)  # daimantion batave ketal nu 6

rev = np.array([[10, 12, 9], [15, 11, 13]])
# print(rev.ndim)

# print(rev[1, 2])
# print(rev[0, 1])

rev[1, 0] = 14
# print(rev)

# print(rev.dtype)  # datatype batave

rev = np.array(
    [[10, 12, 9], [15, 11, 13]], dtype=np.float64
)  # you can explicitly difinetype
print(rev.dtype)
print(rev.nbytes)
print(rev.itemsize)  # item , size ocupyd by each of the element
print(rev.size)  # ketla element 6 e batave
print(rev.shape)  # total number of rows and column

print(np.sort(rev))  # sorting karva mate
print(np.sort(rev, axis=None))  # badha asending order ma batavse
print(np.zeros((2, 3)))  # empty numpy array banave
print(np.ones((2, 3)))  # same as 0 but it put 1
print(np.arange(20, 30, 2))  # pstart, stop, step , print only even element
print(
    np.linspace(10, 20, 5)
)  # element are lienaryly space , 5 means that will print 5 element with equal distance
print(rev.flatten())  # print a flate array
print(rev.reshape(3, 2))  # reshape the array , 3 rows and 2 colm
print(rev.min())  # min element return kare
print(rev.max())  # max element return kare
print(rev.sum(axis=1))  # sum kari aapse array no , ek j axis pr result aapse
print(rev.sum(axis=0))  # its take a verticaly sum

for row in rev:
    print("row ->", row)

b = np.array([1, 4, 16])
print(np.sqrt(b))  # square root batavse
print(np.square(b))  # square karse
print(np.std(b))  # it will find the standerd davesion of all those number
