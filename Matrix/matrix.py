# This is a project for practicing Object Oriented Programming.

class Matrix:
    '''Class for doing basic arithmetic on matrixes.'''
    
    # Initialization
    def __init__(self, size):
        '''Initialize all parameters of the Matrix class.'''
        self.size = size
        self.elements = []
        self.inputs = []
        
    # Matrix Drawer
    def matrix_drawer(self):
        '''Gives a visual output of the state of matrix'''     
        modal_len = 1
        
        # While loop to collect all the values of the elements in the matrix.
        while self.inputs.__len__() < (self.size[0] * self.size[1]): 
            # Logic to find the position of input.
            current_row = self.inputs.__len__() // self.size[1]
            current_column = self.inputs.__len__() % self.size[0]
            
            # Ask user to input element.
            if self.inputs.__len__() < (self.size[0] * self.size[1]):
                valid = False
                while  valid == False:
                    element = input(f'Enter element at a({current_row + 1}, {current_column + 1}) ')
                    try:
                        int(element)
                        valid = True
                    except:
                        print('Input is not valid.')
            self.inputs.append(element)
            
            # Finding the modal length.
            if element.__len__() > modal_len:
                modal_len = element.__len__()
                
            # Updating the elements list
            self.elements.clear()
            self.elements = self.inputs[:]
            neat_elements = []
                       
            # Filling the empty spaces with an 'X'.
            while self.elements.__len__() != (self.size[0] * self.size[1]):
                self.elements.append('X')
                
            # Algorithm to add white spaces to make matrix clean.
            for element in self.elements:
                neat_element = ' ' * (modal_len - len(element)) + element
                neat_elements.append(neat_element)
                
            # Logic to break the matrix list into rows, for proper visualization.
            for column_index in range(self.size[0]):
                section = column_index * self.size[1]
                column = neat_elements[(section):(section + self.size[1])]
                print(column)
                
        return self.inputs