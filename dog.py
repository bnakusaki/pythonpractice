class Dog:
    '''An attempt to model a dog.'''
     
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        '''Commanding a dog to sit.'''
        print(f'{self.name}, sit!')

    def roll_over(self):
        '''Commanding a dog to roll over.'''
        print(f'{self.name} roll over {self.age} times.')

dog_1 = Dog('John', 3)
print(dog_1.name)
print(dog_1.age)
dog_1.sit()
dog_1.roll_over()