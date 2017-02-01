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

    def amount(self):
        for i in range( len(self.stat.symbol) ):
            pass
            
    
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
            print 'ERROR: unknown element %s. Exiting program' % self.stat.symbol()
            f.close()
            exit(1)

    def __init__(self, symbol, totalAmount):
        self.stat = Info()
        self.stat.symbol = symbol
        self.stat.amount = totalAmount #* self.amount()

class Compound:
    '''A class to hold compounds, which hold class(Element)'''

    def analyze(self):
        '''Determines interior elements and compounds and puts them in array(inside)'''
        j = 0
        brackets = 0

        for i in range( len(str(self.stat.amount)), len(self.stat.symbol) ):
            '''
                NaNO3
                -----
                0 1 Capital letter, continue
                1 2 Lower case, continue
                2 1 Capital letter, end previous
                3 1 Capital letter, end previous
                4 2 Number, multiply to current
                5 0 End of Compound


                Mg(NO3)2
                --------
                0 1 Capital letter, continue
                1 2 Lower case letter, continue
                2 0 Parenthesis, end previous, find end parenthesis
                2 0 1 Capital letter, ignore
                2 0 2 Capital letter, ignore
                2 0 3 End parenthesis, now find amount assigned
                2 0 4 Number, continue
                2 0 4 Not a number, end number, add value to array
                3 1 Capital letter, end previous
                4 1 Capital letter, end previous, mult previous by end parenthesis
                5 2 Number, continue
                6 0 Parenthesis, end previous, mult previous by value/end parenthesis
                7 0 Number, already known, skip
                8 0 End of Compound


                NaNa

                0:1
                2:3
            '''

            #NEED TO FIX THIS
            if self.stat.symbol[i].isupper() and not i == len(str(self.stat.amount)):
                self.inside.append(
                    Element(
                        self.stat.symbol[ j + self.stat.amount:i ],
                        self.stat.amount * brackets) )
                j = i

            if self.stat.symbol[i] == '(':

                for k in range( i, len(self.stat.symbol) ):
                    if self.stat.symbol[i] == ')':
                        brackets = k
                        break

                for k in range( i + brackets, len(self.stat.symbol) ):

                    try:
                        int( self.stat.symbol[k] ).isdecimal()
                        brackets = int( self.stat.symbol[ i+brackets:k ] )
                    except:
                        brackets = 1
                        
            if i == len(self.stat.symbol) - 1:
                self.inside.append(
                    Element(
                        self.stat.symbol[ j:i+1 ],
                        self.stat.amount) )
        
    def coef(self):
        for i in range( len(self.stat.symbol) ):
            currentChar = self.stat.symbol[i]

            if not currentChar.isdigit():
                break

        #if Compound has no coefficent, amount defaults to 1
        if not self.stat.symbol[0].isdigit():
            change = '1' + self.stat.symbol
            self.stat.symbol = change
            return 1
        else:
            return int( self.stat.symbol[0:i] )
        
    def elementLen(self):
        j = 0
        for i in self.stat.symbol:
            if i.isupper():
                j += 1

        return j

    def __init__(self, symbol):
        self.stat = Info()
        self.stat.symbol = symbol
        self.stat.amount = self.coef()

        self.inside = []
        self.insideAmounts = []
        self.analyze()

        for i in self.inside:
            print 'hi', i.stat.symbol, i.stat.amount
 
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
        if i[0].isalnum():
            compoundList.append( Compound(i) )
        else:
            if i not in [' ', '+', '->']:
                print 'gg'
            #Exception case ' ', '+', '->'
            pass
