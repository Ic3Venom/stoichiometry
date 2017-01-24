class Info:
    '''Holds information of Elements and Compounds'''
    
    def __init__(self):
        self.data = {}
        self.data = self.data.fromkeys(
            ['number','name','symbol','mass','amount'])
        self.data = self.data.fromkeys(self.data.iterkeys(), 0)
    
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
        self.stat.symbol = symbol

    def amount(self):
        currentChar = [ ]
        amount = 0
        j = 0

        for i in range(0, len(self.stat.symbol)):
            
            currentChar = self.stat.symbol[i + j]
            
            if currentChar.isdigit():
                j += 1
            else:
                i = j
                break

        while j >= 0:
            
            currentChar = self.stat.symbol[j]
            self.stat.change('amount', ( self.stat.amount() + (int(currentChar) * pow(10, i-j)) ))

            j -= 1

    def name(self):
        print self.stat.name


if __name__ == '__main__':    
    j = 0
    compoundList = [ ]
    
    while True:
        
        print 'Input your BALANCED chemical equation (type \'help\' for help):'
        userInput = raw_input(">>> ")

        if userInput == 'help':
            help()
        else:
            break

    for i in userInput.split():
        
        if i[0].isalnum():
            compoundList.append( Compound(i) )
            compoundList[j].amount()
        else:
            #insert '+', '->', 'quit', ' ' exceptions here
            pass
        
        j += 1

    for i in compoundList:
        
        print i.stat.amount()

    exit
