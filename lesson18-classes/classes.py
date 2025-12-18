class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def moves(self):
        print('Moves along...')
        
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")
        
my_car = Vehicle('Toyota', 'Rav 4')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Tesla', 'Model 3')
your_car.get_make_model()
your_car.moves()

#############Inheritance#####################

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')
        
    def modelNo(self):
        print(f'My model number is {self.faa_id}')
        
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')
        
class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessna', 'Skyhawk','N-8732-P')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'Remm12')

cessna.get_make_model()
cessna.modelNo()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

###############Poly-morphism##################
print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()