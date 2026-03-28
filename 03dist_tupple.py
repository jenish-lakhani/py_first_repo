d = {"tom": 7851236542, "rob": 7851236543, "joe": 7851236544}
print(d)
print(d["tom"])
d["sumit"] = 7851236545
print(d)
del d["sumit"]
print(d)

# for key in d:
#     print("key = ", key, "value = ", d[key])

# for k, v in d.items():
# print("key = ", k, "value = ", v)

# print("tom" in d)
# print("samir" in d)

d.clear()
print(d)

point = (5, 9)
print(point[0])
print(point[1])
