basket = {"orange", "apple", "mango", "apple", "orange"}
# print(type(basket))
# print(basket)

a = set()
a.add(1)
a.add(2)
# print(a)

a = {}
# print(type(a))
a = {"something"}
# print(type(a))

numbers = [1, 2, 3, 4, 2, 3, 4]
unique_numbers = set(numbers)
# print(unique_numbers)
unique_numbers.add(5)
# print(unique_numbers)

fs = frozenset(numbers)
# print(fs)

x = {"a", "b", "c"}
# print("a" in x)
# print("g" in x)

# for i in x:
#     print(i)

y = {"a", "g", "h"}
# print(x)
# print(y)

# print(x.union(y))
# print(x | y)  # also union

# print(x.intersection(y))
# print(x & y)  # also intersection

# print(x.difference(y))
# print(x - y)  # bad kari nakhe

# print(x < y)  # subset 6 ke nai e check kare
# print(y < x)

x = {"h", "g"}

print(x < y)
print(y < x)
