class Fish:

    def __init__(self):
        ''' Constructor for this class. '''
        # Create fish species
        self.members = ['Salmon', 'Carp', 'Cat_Fish']
        
    
    def printMembers(self):
        print('Printing members of the fish class')
        for member in self.members:
            print('\t%s ' % member)
