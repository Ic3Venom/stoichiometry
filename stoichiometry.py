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
        self.stat.amount = amount * self.amount()

class Compound():
    '''A class to hold compounds, which hold class(Element)'''

    def analyze(self):
        '''Determines interior elements and compounds and puts them in array(inside)'''
        j = 0
        
        for i in range( len( str(self.stat.amount) ), len(self.stat.symbol) ):
            print 'i: %d, %s' % (i, self.stat.symbol[i])

            #if: i is a bracket, then then find subscript of bracket or find more brackets
            '''if self.stat.symbol[i] == '(':
                bracketCount  = 0
                bracketAmount = 0
                
                while True:
                    if self.stat.symbol[i + j] == '(':
                        bracketCount += 1
                    elif self.stat.symbol[i + j] == ')':
                        bracketCount -= 1
                    if bracaketCount == 0:
                        k = j
                        while True:
                            j += 1 
                            if not self.stat.symbol[i + j].isdecimal():
                                self.inside.append(
                                    Element(
                                        self.stat.symbol[k: k + j],
                                        self.stat.amount * self.stat.symbol[i + j: k + j)


                while True:                    
                    self.stat.symbol[j] != ')'
                    j += 1

                    if j > len( self.stat.symbol ):
                        print 'ERROR: unable to end parenthesis \')\'. Exiting program'
                        exit(1)'''

            
            if self.stat.symbol[i].isupper() and not j == 0:
                self.inside.append(
                    Element(
                        self.stat.symbol[len(str.stat.symbol) - i: j + 1],
                        self.stat.amount) )

            #if: i is decimal, continue until Capital Letter or end of Compound
            if self.stat.symbol[i].isdecimal():
                while True:

                    if j > len( self.stat.symbol ):
                        pass

            '''self.elements.append(
                Element(
                    self.stat.symbol[j: i],
                    self.stat.amount)'''

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
        self.stat = Info()
        self.stat.symbol = symbol
        self.stat.amount = self.coef()

        self.inside = []
        self.analyze()
 
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
