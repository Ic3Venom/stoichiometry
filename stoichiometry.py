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

        j = 0
        for i in ['symbol', 'number', 'mass', 'name', 'amount']:
            if i == value:
                return j
            j += 1 

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

    def find(self, value):
        '''Finds element in periodictable.txt, returns element mass'''
        f = open('periodictable.txt', 'r')

        value = self.stat.index(value)
        maxSearch = self.stat.index(value)
        
        for line in f:
            for i in range( maxSearch + 1 ):
                if line.split()[i] == self.stat.symbol():
                    f.close()
                    return line.split()[maxSearch]
        else:
            print 'Could not find element %s! Exiting program' % self.stat.symbol()
            f.close()
            exit(1)

    def __init__(self, symbol):
        self.stat  = Info()
        self.stat.symbol = symbol

class Compound():
    '''A class to hold compounds, which hold class(Element)'''
    def amount(self):
        j = 0

        for i in range(0, len(self.stat.symbol)):
            currentChar = self.stat.symbol[i + j]
            
            if currentChar.isdigit():
                j += 1
            else:
                break
            
        if not self.stat.symbol[0].isdigit():
            return 1
        else:
            return int( self.stat.symbol[0:j+1] )

    
    def __init__(self, symbol):
        self.stat  = Info()
        self.stat.symbol = symbol
        self.stat.amount = self.amount()

if __name__ == '__main__':
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
        else:
            #Exception case ' ', '+', '->'
            pass

    #debug
    for i in compoundList:
        print i.stat.amount + 10
