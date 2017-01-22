class Info:
    '''Holds information of Elements and Compounds'''
    
    def __init__(self):
        self.data = {}
        self.data = self.data.fromkeys(
            ['number','name','symbol','mass','amount'])
    
    def change(self, key, value):
        '''Changes one of the data values'''
        for i in self.data:
            if i == key:
                self.data[key] = value
                return self.data[key]
    
    def number(self):
        return self.data['number']
    def name(self):
        return self.data['name']
    def symbol(self):
        return self.data['symbol']
    def mass(self):
        return self.data['mass']
    def amount(self):
        return self.data['amount']
    
class Element:
    '''A class to hold element information'''

    def __init__(self, symbol):
        self.stat  = Info()

    def elementFind(self):
        '''Finds element in periodictable.txt'''
        f = open('periodictable.txt', 'r')

        for line in f:
            for word in line.split():
                print word,

        f.close()

class Compound():
    '''A class to hold compounds, which hold class(Element)'''
    
    def __init__(self, symbol):
        self.stat  = Info()

    
def compoundAnalyze(compound):
    print compound
    
    ''' Was from inputAnalyze, until I remembered about '.split()'
        while i < len(userInput):

        currentChar = userInput[i]
        
        if ( currentChar.isalnum() ):
            for j in range(0, len(userInput) + 1):
                
                try:
                    currentChar = userInput[i + j]
                except IndexError:
                    currentChar = '\0'
                
                if ( currentChar.isalnum() ):
                    compound.append( currentChar )
                else:
                    compoundAnalyze( compound )

                    i += j
                    j  = 0
                    compound = []
                    
                    break
        else:
            #insert '+', '->', 'quit', ' ' exceptions here
            i += 1
            pass
    '''
    return

if __name__ == '__main__':
        
    i = 0
    compound = []
    
    print 'Input your BALANCED chemical equation (type \'help\' for help):'
    userInput = raw_input(">>> ")

    compound = userInput.split()

    for i in compound:
        if i[0].isalnum():
            compoundAnalyze( i )    

    exit
