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

        print len(str(self.stat.amount)), len(self.stat.symbol)
        for i in range( len(str(self.stat.amount)), len(self.stat.symbol) ):
            print 'i: %d, %s' % (i, self.stat.symbol[i])
            if self.stat.symbol[i].isalnum() or self.stat.symbol[i] == '(' or self.stat.symbol[i] == ')':
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
                '''
                
                if self.stat.symbol[i].isalpha() and j == 0:
                    print 'Inside if statement 1; i: %d, %s, %d' % (i, self.stat.symbol[i], self.stat.amount)
                    self.inside.append(
                        Element(
                            self.stat.symbol[ i-j:i ],
                            self.stat.amount * brackets) )
    
                if self.stat.symbol[i] == '(':
                    print 'Inside if statement 2; i: %d, %s' % (i, self.stat.symbol[i])
                    for k in range( i, len(self.stat.symbol) ):
                        print 'Inside if statement 2.1; i: %d, %s' % (i, self.stat.symbol[k])
                        if self.stat.symbol[i] == ')':
                            brackets = k
                            break

                    for k in range( i + brackets, len(self.stat.symbol) ):
                        print 'Inside if statement 2.2; i: %d, %s' % (i, self.stat.symbol[k])

                        try:
                            int( self.stat.symbol[k] ).isdecimal()
                            brackets = self.stat.symbol[i + brackets:k] 
                        except:
                            brackets = 1
                        
                '''self.elements.append(
                    Element(
                        self.stat.symbol[j: i],
                        self.stat.amount)'''
            else:
                print 'ERROR: unknown character %c. Exiting program.'% self.stat.symbol[i]
        print brackets, self.stat.symbol,self.stat.amount
        
    def coef(self):
        for i in range( len(self.stat.symbol) ):
            currentChar = self.stat.symbol[i]

            if not currentChar.isdigit():
                break

        #if Compound has no coefficent, amount defaults to 1
        if not self.stat.symbol[0].isdigit():
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
        print 'hello?'
        self.stat = Info()
        print 'Info() complete'
        self.stat.symbol = symbol
        print 'symbol complete'
        self.stat.amount = self.coef()
        print 'coef() complete'

        self.inside = []
        self.insideAmounts = []
        self.analyze()
        print 'analyze complete'
 
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
        print i
        if i[0].isalnum():
            compoundList.append( Compound(i) )
            print i
        else:
            #Exception case ' ', '+', '->'
            pass
