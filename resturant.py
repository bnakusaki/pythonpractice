class Resturant:
    def __init__(self, resturant_name, cuisine_type):
        '''Initializing the atributes of Resturant.'''
        self.name = resturant_name
        self.cuisine = cuisine_type

    def describe_resturant(self):
        '''Gives little discription about the resturant.'''
        print(f'This is {self.name}, and they serve {self.cuisine}.')

    def open_resturant(self):
        '''Tells the resturant is open.'''
        print(f'{self.name} is open.')

resturant_1 = Resturant(resturant_name='Las Palmas', cuisine_type='Local dishes')
print(resturant_1.name)
print(resturant_1.cuisine)
resturant_1.describe_resturant()
resturant_1.open_resturant()

print('\n\n')

resturant_2 = Resturant(resturant_name='Golden Tulip', cuisine_type='Foreign dishes')
resturant_3 = Resturant(resturant_name='Chicken Man', cuisine_type='Foreign dishes')

resturant_1.describe_resturant()
resturant_2.describe_resturant()
resturant_3.describe_resturant()

