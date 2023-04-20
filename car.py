class Car:
    '''An attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize all attributes of the car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        ''''Gives a description of the car.'''
        des_name = f'{self.year} {self.model} {self.make}'
        return des_name.title()
    
    def get_milage(self):
        '''Returns the milage of the car'''
        return f'Your {self.get_descriptive_name()} has {self.odometer_reading} miles on it.'
    
    def update_milage(self, milage = 0, increament =0):
        '''Updates the milage of the car, but does not allow milage reversal.'''
        if milage > self.odometer_reading:
            self.odometer_reading = milage
        if increament > 0:
            self.odometer_reading += increament
        elif milage < self.odometer_reading or increament < 0:
            return 'Odometer reading cannot be reversed.'
        
        
    
my_car = Car(make='La Voiture Noire', model='Bugatti', year=2019)
# print(my_car.get_descriptive_name())
# print(f'\n{my_car.get_milage()}')
# my_car.update_milage(1000)
# print(f'\n{my_car.update_milage(100)}')

# print(my_car.get_milage())
# my_car.update_milage(increament= -100)
# print(my_car.get_milage())

class Battery():
    '''To manage all battery properties'''
    def __init__(self, range):
        self.range = range
        
    def get_range(self):
        return self.range

class Electric_car(Car):
    '''Cars with Electric drive-train.'''

    def __init__(self, make, model, year, range):
        super().__init__(make, model, year)
        self.range = range
        self.battery = Battery(range=range)
        
    
    
my_new_car = Electric_car(model='Tesla', make='Model S', year='2022', range=500)

print(my_new_car.battery.get_range())
