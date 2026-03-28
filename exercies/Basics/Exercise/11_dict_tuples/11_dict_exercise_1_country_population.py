population = {"china": 143, "india": 136, "usa": 32, "pakistan": 21}


def add():
    country = input("enter the country name to add:")
    country = country.lower()
    if country in population:
        print("counrty already exist in our database\n")
        return
    p = input(f"enter population for {country}")
    p = int(p)
    population[country] = p
    print_all()


def remove():
    country = input("enter name to remove:")
    country = country.lower()
    if country not in population:
        print("country doesn't exist in our database\n")
        return
    del population[country]
    print_all()


def query():
    country = input("enter country name to quary:")
    country = country.lower()
    if country not in population:
        print("country doesn't exist in our database\n")
        return
    print(f"population of {country} is {population[country]}corer")


def print_all():
    for country, p in population.items():
        print(f"{country}==>{p})")


def main():
    op = input("enter operation (add, remove, query, print):")
    if op.lower() == "add":
        add()
    elif op.lower() == "remove":
        remove()
    elif op.lower() == "query":
        query()
    elif op.lower() == "print":
        print_all()


if __name__ == "__main__":
    main()
