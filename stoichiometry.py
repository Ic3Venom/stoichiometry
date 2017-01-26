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
        return int(self.data['number'])
    def name(self):
        return int(self.data['name'])
    def symbol(self):
        return int(self.data['symbol'])
    def mass(self):
        return int(self.data['mass'])
    def amount(self):
        return int(self.data['amount'])
    
class Element:
    '''A class to hold element information'''

    def __init__(self, symbol):
        self.stat  = Info()
        self.stat.symbol = symbol

    def elementFind(self):
        '''Finds element in periodictable.txt'''
        f = open('periodictable.txt', 'r')

        for line in f:
            for word in line.split():
                if word == self.stat.symbol:
                    print hi,
                    #continue to find specific things 

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
    
        if not self.stat.symbol[0].isdigit():
            self.stat.change('amount', 1)
        else:
            self.stat.change('amount', self.stat.symbol[ 0 : j+1 ])
        
    def symbol(self):
        print self.stat.symbol


if __name__ == '__main__':    
    j = 0
    compoundList = [ ]
    
    while True:
        
        print 'Input your BALANCED chemical equation (type \'help\' for help):'
        userInput = raw_input(">>> ")

        if userInput == 'help':
            print '-----------------------------------<HELP>-------------------------------------'
            print 'The expected input for this program is as follows:'
            print '\tR + R... -> P + P...'
            print '* R: Reactants (any order, seperated by the syntax, \' + \'(space plus space)'
            print '* ->: yields symbol, please put a space before and after it'
            print '* P: Products (any order, separated by the syntax, \' +  \'(space plus space)'
            print 'Any bugs, issues, requests? Put them in the GitHub repo.'
            print '------------------------------------------------------------------------------\n'

        else:
            break

    for i in userInput.split():
        
        if i[0].isalnum():
            compoundList.append( Compound(i) )
            compoundList[j].amount()
        else:

            pass
        
        j += 1

    #debug
    for i in compoundList:
        
        print i.stat.amount() + 10

    exit
