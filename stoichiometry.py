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
    exit(0)

def inputAnalyze():
    '''Takes equation from user and analyze it'''
    i = 0
    j = 1
    compound = []
    
    print "Input your BALANCED chemical equation (type 'help' for help):"
    userInput = raw_input(">>> ")
    
    while(True):

        currentChar = userInput[i]

        if (currentChar.isdigit()):
            print 'clinton', i
            while(True):
                currentChar = userInput[i + j]

                if (currentChar.isdigit() == False):
                    compound.append(userInput[i + j])
                    j += 1
                else:
                    i += (j - 1)
                    j  = 0
                    compoundAnalyze(compound)

                    break
        else:
            if (i >= (len(userInput) - 1)):
                exit(0)
            
        i += 1
    
if __name__ == '__main__':
    
    inputAnalyze()

    exit
