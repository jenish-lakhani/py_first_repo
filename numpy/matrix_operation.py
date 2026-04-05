import numpy as np

q1 = np.array([[200, 220, 250], [150, 180, 210], [300, 330, 360]])

q2 = np.array([[209, 231, 259], [155, 192, 222], [310, 340, 375]])

print(q1 + q2)
print(q2 - q1)
print((q2 - q1) * 100 / q1)  # show as into a % groth show in % persentage

prices = np.array([[10, 12, 11], [8, 9, 10], [15, 16, 17]])

q1_revenue = q1 * prices
print(q1_revenue)

q1_discount = q1_revenue * 0.2
print(q1_discount)  # discount of 20%

net_revenue = q1_revenue - q1_discount
print(net_revenue)

print(np.sum(q1_discount))  # total discount
print(np.sum(net_revenue))  # total net


features = np.array([[2000, 3], [1800, 2]])
weights = np.array([150, 50000])

print(2000 * 150 + 3 * 50000)  # total of first home price
print(np.dot(features, weights))  # total of home

c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print(np.cross(c, d))
