class Info:
    '''Holds information of Elements and Compounds'''
    
    def __init__(self):
        #Real names (in order): symbol, number, mass, name, amount
        self.data = ['', 0, 0.0, '', 0] 

    def index(self, value):
        '''Returns index value of corresponding real name'''
        try:
            value.isalpha()
        except:
            return value

        types = ['symbol', 'number', 'mass', 'name', 'amount']
        j = 0
        for i in types:
            if i == value:
                return j
            j += 1 
            
    def change(self, index, value):
        '''Changes one of the data values'''
        index = self.index(index)
        self.data[index] = value
        print self.data
        
    def symbol(self):
        return self.data[0]
    def number(self):
        return self.data[1]
    def mass(self):
        return self.data[2]
    def name(self):
        return self.data[3]
    def amount(self):
        return self.data[4]
   
class Element:
    '''A class to hold element information'''

    def __init__(self, symbol):
        self.stat  = Info()
        self.stat.change('symbol', symbol)

    def find(self, value):
        '''Finds element in periodictable.txt, returns element mass'''
        f = open('periodictable.txt', 'r')

        value = self.stat.index(value)
        maxSearch = self.stat.index(value)
        print 'maxSearch: %d' % maxSearch
        j = 0
        for line in f:
            j += 1
            for i in range( maxSearch + 1 ):
                if line.split()[i] == self.stat.symbol():
                    f.close()
                    return line.split()[maxSearch]
        else:
            print 'Could not find element %s! Exiting program' % self.stat.symbol()
            f.close()
            exit(1)

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
            
        if not self.stat.symbol[0].isdigit():
            self.stat.change('amount', 1)
        else:
            self.stat.change('amount', self.stat.symbol[ 0 : j+1 ])

if __name__ == '__main__':    
    j = 0
    compoundList = [ ]
    
    while True:
        
        print 'Input your BALANCED chemical equation (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput == 'help':
            print '\nWelcome to the stoichiometry.py help page!\n'
            print 'The expected input for this program is as follows:'
            print '- R + R... -> P + P...'
            print '* R: Reactants (any order, seperated by the syntax, \' + \'(space plus space)'
            print '* ->: yields symbol, please put a space before and after it'
            print '* P: Products (any order, separated by the syntax, \' +  \'(space plus space)'
            print '\nAny bugs, issues, requests? Put them in the GitHub repo.\n'
        elif userInput == 'quit':
            exit(1)
        else:
            break

    for i in userInput.split():
        
        if i.isalnum():
            compoundList.append( Compound(i) )
            compoundList[compoundList.index(i)].amount()
        else:
            #Exception case ' ', '+', '->'
            pass
        
        j += 1

    #debug
    for i in compoundList:
        
        print i.stat.amount() + 10
