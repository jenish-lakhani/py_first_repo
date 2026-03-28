def calculate_triangle_area(base, height):
    print("__name__: ", __name__)
    return 1 / 2 * (base * height)


def calculate_square_area(length):
    return length * length


if __name__ == "__main__":
    print("i am in module.py")
    a = calculate_triangle_area(10, 20)
    print("triangle area: ", a)
