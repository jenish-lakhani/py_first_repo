# import random

# choices = ["rock", "paper", "scissors"]


# while True:
#     computer = random.choice(choices)
#     user = input("enter your choice (rock,pepar,scissors").lower()
#     print(f"computer choice is {computer}")

#     if user == computer:
#         print("tie")
#     elif user == "rock" and computer == "scissors":
#         print("youy win")
#         break
#     elif user == "paper" and computer == "rock":
#         print("you win")
#         break
#     elif user == "scissors" and computer == "paper":
#         print("you win")
#         break
#     else:
#         print("you lose")


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list1 = [n for n in list if n % 2 != 0]
# list2 = [n for n in list if n % 2 == 0]
# print(list1)
# print(list2)

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# letters = ["a", "b", "c", "d", "e", "f"]
# letters.pop(2)
# print(letters)

# x = {"a": 1, "b": 2}
# x.update(b=3, c=4)
# x.pop("b")
# print(list(x.keys()))

# lt = [1, 2, 3, 4, 5, 3, 2, 4, 1]
# print(list(set(lt)))


# def func(x, y=[]):
#     y.append(x)
#     return y
# print(func(1))
# print(func(2))

# nums = [1, 3, 5, 7]
# nums.append(sum(nums))
# nums.pop(1)
# print(len(nums))


n = 5
for i in range(n):
    for j in range(i):
        print(j, end=" ")

text = "Python"
print(text[0] + text[-1])

x = [1, 2, 3]
print(x * 2)

lis = [5, 1, 2, 2, 3, 4, 3, 2, 6]
d = dict.fromkeys(lis)  # remove duplicate but maintain   the order
print(list(d))
