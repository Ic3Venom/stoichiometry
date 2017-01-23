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
    currentChar = []
    j      = 0
    amount = 0

    for i in range(0, len(compound)):
        
        currentChar = compound[i + j]
        
        if currentChar.isdigit():
            j += 1
        else:
            break
        
    while j >= 0:
        currentChar = compound[j]

        amount += ( int(currentChar) * pow(10, j) ) #DOES NOT WORK

        j -= 1

    print amount
    return

if __name__ == '__main__':
        
    i = 0
    compound = []
    
    while True:
        print 'Input your BALANCED chemical equation (type \'help\' for help):'
        userInput = raw_input(">>> ")

        if userInput == 'help':
            help()
        else:
            break
    
    compound = userInput.split()

    for i in compound:
        if i[0].isalnum():
            compoundAnalyze( i )
        else:
            #insert '+', '->', 'quit', ' ' exceptions here
            pass

    exit
