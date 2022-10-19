
# ? unlimited arguments
# ? unlimited positional arguments

# example
def add(n1, n2):
    return n1+n2

# print(add(5, 3))

# now for unlimted


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(5, 3))

# ? kwargs: many keyword Arguments


def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)

# ? creat our own **kwargs


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
