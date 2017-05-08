class Info:
    '''Holds information of Elements and Compounds'''
    
    #TODO: remove (debug)
    def all(self):
        print 'Info<all> (amount %r, name %r, number %r, mass %r, symbol %r)' % (self.amount, self.name, self.number, self.mass, self.symbol)

    def __init__(self):
        #names in order of file): symbol, mass, name, number, amount
        
        self.amount = 0
        self.name   = ''    #Only applies to Element class
        self.number = 0     #Only applies to Element class
        self.mass   = 0.0
        self.symbol = ''

class Element:
    '''A class to hold element information'''

    def amount(self):
        for i in range(len(self.stat.symbol)):
            if not self.stat.symbol[i].isalpha():
                temp = int(self.stat.symbol[i:])
                self.stat.symbol = self.stat.symbol[:i]
                print '  Element<amount>for;if (self.stat.symbol[:i], i, temp)', self.stat.symbol[:i], i, temp
                return temp
        else:   #if self.stat.symbol has no amount attached, defaults to 1
            return 1
    def change(self, i, value):
        if i == 0:
            self.stat.symbol = str(value)
        elif i == 1:
            self.stat.mass   = float(value)
        elif i == 2:
            self.stat.name   = str(value)
        elif i == 3: 
            self.stat.number = int(value)
    
            
    def find(self): #Might revert back to single data return
        '''Finds element in table.bin, returns element mass'''

        with open('table.bin', 'rb') as f:
            for line in f:

                if line.split()[0] == self.stat.symbol: #line.split[0] is symbol location
                    for term in range( len(line.split()) ):
                        self.change(term, line.split()[term])
                        print '    Element<find>with;for;if;for (term, line.split()[term])', term, line.split()[term]
                    
                    break

            else:
                print 'ERROR: unknown element \'%s\'. Exiting program' % self.stat.symbol
                f.close()
                exit(1)

    def __init__(self, symbol, compoundAmount):
        self.stat = Info()
        print 'Element<__init__>start (symbol, compoundAmount)', symbol, compoundAmount

        self.stat.symbol = symbol
        self.stat.amount = compoundAmount * self.amount()

        self.find()
        self.stat.mass = self.stat.mass * self.stat.amount

class Compound:
    '''A class to hold compounds, which hold class(Element)'''
     
    def bracketAmount(self, brackets, i, j):
        for bracket in brackets[1:]:
            if bracket[0] < j and bracket[1] > i:
                return bracket[2]
        else:
            return 1
            
    def analyze(self):
        '''Determines interior elements and puts them in array(inside)'''

        brackets = [1] #Initially starts with the first index where bracket indices will be stored
        print 'Compound<analyze>start (self.stat.symbol)', self.stat.symbol
        
        #For1: searches symbol for brackets, and if found, will put more information of them
        for i in range(len(self.stat.symbol)):
            print 'Compound<analyze>for1;start (i, currentChar, brackets):', i, self.stat.symbol[i], brackets

            if self.stat.symbol[i] == '(':
                brackets.append([i, 0, 1])

            elif self.stat.symbol[i] == ')':
                print 'Compound<analyze>for1;if2;start (i, self.stat.symbol[i])', i, self.stat.symbol[i]
                
                brackets[brackets[0]][1] = i
                for j in range( i, len(self.stat.symbol)):
                    print 'Compound<analyze>for1;if2;for1;start (i, j, self.stat.symbol()[j])', i, j, self.stat.symbol[j]
                    if self.stat.symbol[j].isalpha():
                        print '    Compound<analyze>for1;if2;for1;try;if1 int(self.stat.symbol[i:j], brackets)', int(self.stat.symbol[i+1:j-1])
                        brackets[brackets[0]][2] = int(self.stat.symbol[i+1:j-1])
                        brackets[0] += 1
                        break
                    
                else:
                    print '    Compound<analyze>for1;if2;for1;end int(self.stat.symbol[i:j-1])', int(self.stat.symbol[j:])
                    brackets[brackets[0]][2] = int(self.stat.symbol[j:])
                    print '    Completed Compound<analyze>(thu:for1;if1;for1;except;if2);end (int(self.stat.symbol[i+1:j]), brackets):', int(self.stat.symbol[j:]), brackets
                    break

        print '  Completed Compound<analyze>for1 (brackets)', brackets
        #Checks if first char in self.stat.symbol is capitalized or is '('
        if self.stat.symbol[0].isupper():
            i = j = 1
        elif self.stat.symbol[0] == '(':
            i = j = 0
        else: 
            print 'Impossible character \'%s\'. Exiting program.' % self.stat.symbol[0]
            exit(1)
        brackets[0] = 1
        skip = 1
        
        while i < len(self.stat.symbol) and j <= len(self.stat.symbol):
            print 'Compound<analyze>while1;start (j, i, currentChar, brackets):', j, i, self.stat.symbol[i], brackets
              
            if self.stat.symbol[i] == '(' and skip == 1:
                j += 1
                
            elif self.stat.symbol[i].isupper() and skip == 1:
                skip = None

            elif self.stat.symbol[i].isupper(): #P4
                print 'Componud<analyze>while1;if3 (j, i, self.stat.symbol[j:i])', j, i, self.stat.symbol[j:i]
                self.inside.append(         #CRASH OCCURS HERE ( when input = '(NH4)')
                    Element(
                        self.stat.symbol[j:i],
                        self.stat.amount * brackets[brackets[0]][2] ) )
                j = i
                print 'Compound<analyze>while1;if1 (j, i, self.stat.symbol[j:], self.stat.symbol[:i])', j, i, self.stat.symbol[j:], self.stat.symbol[:i]

            elif self.stat.symbol[i] in ['(', ')']:  #P1
                print 'Compound<analyze>while1;if3;start (i, j, brackets)', i, j, brackets
                self.inside.append(
                    Element(
                        self.stat.symbol[j:i],
                        self.stat.amount * brackets[brackets[0]][2] ) )
                j += len(str(self.stat.symbol[j:i]))
                
                if self.stat.symbol[i] == ')':                    
                    i += len(str(self.inside[-1].stat.symbol))
                    brackets[0] += 1
            
            i += 1

        else:
            print 'Compound<analyze>while1;except<IndexError>;start (i, j)', i, j
            if self.stat.symbol[j:].isalnum():                
                self.inside.append(
                    Element(
                        self.stat.symbol[j:],
                        self.stat.amount ) )

    def coef(self):
        #if Compound has no coefficient, amount defaults to 1
        if not self.stat.symbol[0].isdigit():
            return 1

        for i in range( len( self.stat.symbol)):
            if not self.stat.symbol[i].isdigit():
                temp = self.stat.symbol[:i]
                print 'Compound<coef>for;if (temp, self.stat.symbol())', temp, self.stat.symbol
                self.stat.symbol = self.stat.symbol[i:]
                return temp

    def mass(self):
        for i in self.inside:
            print '(i.stat.mass, type(i.stat.mass))', i.stat.mass, type(i.stat.mass), i.stat.symbol, i.stat.amount
            print 'BEFORE CRASH', i.stat.mass, type(i.stat.mass), type(self.stat.mass)
            self.stat.mass += i.stat.mass #Symbol strings are corrupting i.stat.mass, got 'NitrogenNitrogen'

    def __init__(self, symbol):
        self.stat = Info()
        
        self.inside = []
        self.massInput = 0.0 #Will be used later

        self.stat.symbol = symbol
        self.stat.amount = self.coef()

        self.analyze()
        print 'Everything: symbol, mass, name, number, amount', self.stat.symbol, self.stat.mass, self.stat.name, self.stat.number, self.stat.amount
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
        print "Limiting for2;start (i)", i
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
        
        else:
            print 'Unknown value "%s".' % userInput

if __name__ == '__main__':
    test = Compound( raw_input("Compound: ") ) #TODO: remove
    print test.stat.all()
    
    #main() *need to work on Compound.analyze() more before I can work on main()

    exit(0)
