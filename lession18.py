class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print(f'{self.make} {self.model} Moves along...')


my_car = Vehicle('Tesla', 'Y')
print(my_car.make)
print(my_car.model)
my_car.moves()


your_car = Vehicle('Toyota', 'Rav4')
print(your_car.make)
print(your_car.model)
your_car.moves()


class Truck(Vehicle):
    def __init__(self, make, model, power):
        super().__init__(make, model)
        self.power = power

    def moves(self):
        print(f'Moving round {self.power}')


class Cart(Vehicle):
    pass


my_truck = Truck('Ram', '3', '300')
my_truck.moves()

my_cart = Cart('Golf', 'Big')
my_cart.moves()

print("\n\n")

for v in (my_car, your_car, my_truck, my_cart):
    v.moves()
