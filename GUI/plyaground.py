def add(*args):
    sum = 0
    for num in args:
        sum+=num
    return(sum)

print(add(1,2,3,4))

def calculate(n, **kwargs):
    sum = 0
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)

calculate(2, add=5, mul = 10)

class Car:

    def __init__(self, **kw):
        self.year = kw.get("year")
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(year=2022, make = "Ford", model="Escape")

print(f"{my_car.year} {my_car.make} {my_car.model}")


