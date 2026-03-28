import statistics

stocks = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}


def print_all():
    for stock, price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"{stock}==>{price_list}==>avg:", round(avg, 2))


def add():
    s = input("enter the stock ticker to add:")
    p = input("enter price if this stock:")
    p = int(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    print_all()


def main():
    op = input("enter operation(print, add :")
    if op.lower() == "print":
        print_all()
    elif op.lower() == "add":
        add()
    else:
        print("invalid operation", op)


if __name__ == "__main__":
    main()
