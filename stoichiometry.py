class Info:
    '''Holds information of Elements and Compounds'''

    def __init__(self):
        #Real names (in order): symbol, mass, name, number, amount
        self.data = ['', 0.0, '', 0, 0]

    def change(self, dataTag, value):
        if dataTag in [0, 'symbol']:
            dataTag = 0
        elif dataTag in [1, 'mass']:
            dataTag = 1
        elif dataTag in [2, 'name']:
            dataTag = 2
        elif dataTag in [3, 'number']:
            dataTag = 3
        elif dataTag in [4, 'amount']:
            dataTag = 4
        self.data[dataTag] = value

    def symbol(self):
        return self.data[0]
    def mass(self):
        return self.data[1]
    def name(self):
        return self.data[2]
    def number(self):
        return self.data[3]
    def amount(self):
        return self.data[4]

class Element:
    '''A class to hold element information'''

    def amount(self):
        for i in range(len(self.stat.symbol()) ):
            if not self.stat.symbol()[i].isalpha():
                temp = int(self.stat.symbol()[i:])
                self.stat.change('symbol', self.stat.symbol()[:i])
                print '  Element<amount>for;if (self.stat.symbol()[:i], i, temp)', self.stat.symbol()[:i], i, temp
                return temp
        else:   #if self.stat.symbol has no amount attached, defaults to 1
            return 1

    def find(self): #Might revert back to single data return
        '''Finds element in table.bin, returns element mass'''

        with open('table.bin', 'rb') as f:
            for line in f:

                if line.split()[0] == self.stat.symbol(): #line.split()[0] is symbol location

                    for term in range( len(line.split()) ):
                        self.stat.change(term, type(self.stat.data[term])(line.split()[term]))
                        print '    Element<find>with;for;if;for (term, line.split()[term])', term, type(self.stat.data[term])(line.split()[term])
                    break

            else:
                print 'ERROR: unknown element \'%s\'. Exiting program' % self.stat.symbol()
                f.close()
                exit(1)

    def __init__(self, symbol, compoundAmount):
        self.stat = Info()

        self.stat.change('symbol', symbol)
        self.stat.change('amount', compoundAmount * self.amount())

        self.find()
        self.stat.change('mass', self.stat.mass() * self.stat.amount())

class Compound:
    '''A class to hold compounds, which hold class(Element)'''
    def bracketIndex(self, brackets, i, j):
        for bracket in brackets[1:]:
            print 'Compound<brackets> for;start (bracket, j, bracket[2])', bracket, j, bracket[2]
            if bracket[0] < j and bracket[1] > i:
                print 'Compound<bracketIndex> for;if1;start (i, j, i[2])', bracket, j, bracket[2]
                return bracket[2]
        else:
            return 1
            
    def analyze(self):
        '''Determines interior elements and puts them in array(inside)'''

        j = len( str( self.stat.amount() ) )
        i = len( str( self.stat.amount() ) )
        brackets = [1]
        
        #For1: searches symbol for brackets, and if found, will put more information of them
        for i in range( len( str( self.stat.amount()) ), len(self.stat.symbol())):
            print 'Compound<analyze>for1;start (i, currentChar, brackets):', i, self.stat.symbol()[i], brackets

            if self.stat.symbol()[i] == '(':
                brackets.append([i, 0, 1])

            elif self.stat.symbol()[i] == ')':
                print 'Compound<analyze>for1;if2;start (i, self.stat.symbol()[i])', i, self.stat.symbol()[i]
                
                brackets[brackets[0]][1] = i

                for j in range( i, len(self.stat.symbol()) + 1):
                    if self.stat.symbol()[j].isalpha():
                        print '    Compound<analyze>for1;if2;for1;try;if1 int(self.stat.symbol()[i:j], brackets)', int(self.stat.symbol()[i+1:j-1])
                        brackets[brackets[0]][2] = int(self.stat.symbol()[i+1:j-1])
                        brackets[0] += 1
                        break
                    
                else:
                    if j == len(self.stat.symbol()) and i != len(self.stat.symbol()) -1: #second part used to exclude symbol  without brackets[3]
                        print '    Compound<analyze>for;except<IndexError>;if1 int(self.stat.symbol()[i:j-1])', int(self.stat.symbol()[i+1:j])
                        brackets[brackets[0]][2] = int(self.stat.symbol()[i+1:j])
                        print '    Completed Compound<analyze>(thu:for1;if1;for1;except;if2) end (int(self.stat.symbol()[i+1:j]), brackets):', int(self.stat.symbol()[i+1:j]), brackets
                        break
                    
        i = self.stat.amount() #resetting value of i
        
        while i < (len(self.stat.symbol()) + 1):
            print 'Compound<analyze>while1;start (j, i, currentChar, brackets, self.skipIndex(brackets, i)):', j, i, self.stat.symbol()[i], brackets, self.skipIndex(brackets, i)
            
            if self.stat.symbol()[i].isupper(): #P4
                print 'Compound<analyze>while1;if (i, j, self.bracketIndex(brackets, i, j)):', i, j, self.bracketIndex(brackets, i, j)
                self.inside.append(
                    Element(
                        self.stat.symbol()[j:i],
                        self.stat.amount() * self.bracketIndex(brackets, i, j) ) )
                j = i

            elif self.stat.symbol()[i] == '(':  #P1
                if j != i: #If not first char after total amount is '(', append another compound
                    print 'Compound<analyze>while1;elif1;if1 (self.stat.symbol()[j:i], j, i, self.bracketIndex(brackets, i, j))', self.stat.symbol()[j:i], j, i, self.bracketIndex(brackets, i, j)
                    self.inside.append(
                        Element(
                            self.stat.symbol()[j:i],
                            self.stat.amount() * self.bracketIndex(brackets, i, j) ) )
                    j = i + 2

                if not len(brackets) == 0:
                    print 'Too many brackets in userInput. Exiting program',
                    print 'If you believe this is wrong, report this in the GitHub repo.'
                    exit(1)

            elif self.stat.symbol()[i] == ')':  #P1
                if not len(brackets) == 1:
                    print 'Missing brackets in userInput. Exiting program',
                    print 'If you believe this is wrong, report this in the GitHub repo.'
                    exit(1)
                    
                else:
                    print 'Compound<analyze>while1;try;if3;else;start (self.bracketIndex(brackets, i, j), i, j)', self.bracketIndex(brackets, i, j), i, j
                    self.inside.append(
                        Element(
                            self.stat.symbol()[j:i],
                            self.stat.amount * brackets[2] * self.bracketIndex(brackets, i, j) ) )
                    
                    i += len( str( self.bracketIndex(brackets, i, j))) + 1
                    continue
                
            i += 1

        else:
            print 'Compound<analyze>while1;except<IndexError>;start'
            self.inside.append(
                Element(
                    self.stat.symbol()[j:],
                    self.stat.amount() ) )

    def coef(self):
        #if Compound has no coefficient, amount defaults to 1
        if not self.stat.symbol()[0].isdigit():
            self.stat.change('symbol', '1' + self.stat.symbol())
            return 1

        for i in range( len( self.stat.symbol())):
            if not self.stat.symbol()[i].isdigit():
                temp = self.stat.symbol()[:i]
                print 'Compound<coef>for;if (temp, self.stat.symbol)', temp, self.stat.symbol()
                self.stat.change('symbol', self.stat.symbol[i:])
                return temp

    def mass(self):
        for i in self.inside:
            self.stat.change('mass', self.stat.mass() + i.stat.mass())

    def __init__(self, symbol):
        self.stat = Info()
        self.inside = []
        self.massInput = 0.0 #Will be used later

        self.stat.change('symbol', symbol)
        self.stat.change('amount', self.coef())

        self.analyze()
        self.mass()

def empirical():
    storage = [ ]

    while True:
        print 'Enter your list of percent amounts of elements (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput == 'help':
            print '\nWelcome to the stoichiometry.py help page!'
            print '* The expected input for this program is as follows:'
            print '\tMASS SYMBOL, MASS SYMBOL, ...'
            print '* Where \'MASS\' is AT MOST in the thousandths place.'
            print '\nAny bugs, issues, requests? Put them in the GitHub repo.\n'
        elif userInput == 'quit':
            exit(0)
        else:
            break

    #TODO: finish stuff!
    for i in userInput.split(','):
        try:
            storage.append(
                (Compound(
                    i.split()[0] ),
                int( i.split()[1] )) )

        except:
            print 'Incorrect syntax in userInput. Exiting program.',
            print 'If you believe this is wrong, report this in the GitHub repo.'
            exit(0)

def limiting():
    reactants = [ ]
    products  = [ ]
    switch    = False

    #Phase 1: read input and check for commands
    while True:
        print 'Enter your BALANCED chemical equation (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput == 'help':
            print '\nWelcome to the stoichiometry.py help page!\n'
            print 'The expected input for this program is as follows:'
            print '\tR + R... -> P + P...'
            print '* R: Reactants (any order, seperated by the syntax, \' + \'(space plus space)'
            print '* ->: yields symbol, please put a space before and after it'
            print '* P: Products (any order, separated by the syntax, \' +  \'(space plus space)'
            print '\nAny bugs, issues, requests? Put them in the GitHub repo.\n'
        elif userInput == 'quit':
            exit(0)
        else:
            break

    #Phase 2: read input and put compounds into list(reactants) or list(products)
    for i in userInput.split():

        if i == '->':
            if switch is True:
                print 'Repeated syntax %s in userInput.' % i,
                print 'If you believe this is wrong, report this in the GitHub repo.'
                exit(1)

            switch = True
            continue

        for j in i:
            if j.isalnum() or j in [')', '(']:
                continue
            elif j == '+':
                break
            else:
                print 'Unknown character %c in userInput.' % j,
                print 'If you believe this is wrong, report this in the GitHub repo.'
                exit(1)
        else:
            if switch is True:
                products.append( Compound(i) )
                switch = False

            else:
                reactants.append( Compound(i) )

    #Phase 3: userInput of each compound's mass
    for i in reactants + products:
        print i
        print 'How many grams of %s are in the reaction? (Type \'?\' if value is unknown' % i.stat.symbol

        if userInput == '?':
            continue

        else:
            i.massInput = float( raw_input(">>>") ) #Would like to rename variable

def main():
    #Phase 1: read input and check for commands
    while True:
        print 'What mode of stoichiometry would you like to do? (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput.lower() == 'help':
            print '\nWelcome to the stoichiometry.py help page!\n'
            print 'For empirical/molecular formula, type \'empirical\' or \'molecular\''
            print 'For limiting reactant solver, type \'limiting\''
            print '\nAny bugs, issues, requests? Put them in the GitHub repo.\n'

        elif userInput.lower() == 'quit':
            exit(0)

        elif userInput.lower() in ['empirical', 'emp', 'molecular', 'mol']:
            empirical()
            break

        elif userInput.lower() in ['limiting', 'lim']:
            limiting()
            break

if __name__ == '__main__':
    test = Compound( raw_input("Compound: ") )
    print test.stat.data

    #main() *need to work on Compound.analyze() more

    exit(0)
