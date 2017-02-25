class Info:
    '''Holds information of Elements and Compounds'''

    def __init__(self):
        #Real names (in order): symbol, mass, name, number, amount
        self.data = ['', 0.0, '', 0, 0]

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
        for i in range(1, len(self.stat.symbol) ):

            if self.stat.symbol[i].isdecimal():
                temp = self.stat.symbol[i:]
                self.stat.symbol = self.stat.symbol[:i]
                return int(temp)
        else:
            self.stat.symbol = self.stat.symbol[:i+1]
            return 1

    def find(self): #Might revert back to single data return
        '''Finds element in periodictable.txt, returns element mass'''
        with file('periodictable.txt', 'rb') as f:
            for line in f:

                if line.split()[0] == self.stat.symbol[len(str(self.stat.amount)):]: #line.split()[0] is symbol location

                    for term in range( len(line.split()) ):
                        self.stat.data[term] = type(self.stat.data[term])(line.split()[term])

                    break

            else:
                print 'ERROR: unknown element %s. Exiting program' % self.stat.symbol
                f.close()
                exit(1)

    def __init__(self, symbol, compoundAmount):
        self.stat = Info()

        self.stat.symbol = symbol
        self.stat.amount = compoundAmount * self.amount()
        self.find()

class Compound:
    '''A class to hold compounds, which hold class(Element)'''

    def analyze(self):
        '''Determines interior elements and puts them in array(inside)'''
        j = 0
        bracketAmount  = 1
        bracketLocation= () #index slice of what's inside the brackets

        #Finds where the brackets are located and what amount is assigned to them
        for i in range( len(str(self.stat.amount)), len(self.stat.symbol) ):

            if self.stat.symbol[i] == '(':
				bracketLocation = (i,)

            elif self.stat.symbol[i] == ')':
                bracketLocation = bracketLocation + (i-1,)

            	#Checking if there are not enough/too many extra brackets
                if len(bracketLocation) is not 2:
					print 'Missing or too many brackets in userInput.',
					print 'If you believe this is wrong, report this in the GitHub repo.'
					exit(1)

                for j in range( i + 1, len(self.stat.symbol) ):

                    if not self.stat.symbol[j].isdecimal():
                        bracketAmount = int( self.stat.symbol[ bracketLocation[1] + 1:j ] )
                        j = 1

                        break
                else:
                    try:
                        bracketAmount = int( self.stat.symbol[i+1:] )
                    except:
                        bracketAmount = 1

                    j = 1
                    break

        for i in range( len(str(self.stat.amount)), len(self.stat.symbol) ):

            #If i.isupper(): insideAmount.append(self.stat.symbol[slice])
            if self.stat.symbol[i].isupper() and not i == len(str(self.stat.amount)):

                if len( bracketLocation ) > 0:

                    if i >= bracketLocation[0] and i <= bracketLocation[1]:

                        if j < bracketLocation[0]:

                            for k in range(j, i):

                                if k == bracketLocation[0]:
                                    self.inside.append(
                                        Element(
                                            self.stat.symbol[ j:k ],
                                            self.stat.amount ) )
                                    break

                        elif i > bracketLocation[1]:
                            self.inside.append(
                                Element(
                                    self.stat.symbol[ j:bracketLocation[1] - 1 ],
                                    self.stat.symbol * bracketAmount ) )

                        else:
                            self.inside.append(
                                Element(
                                    self.stat.symbol[ j:i ],
                                    self.stat.amount * bracketAmount ) )

                        j = i

        else:
            if len( bracketLocation ) > 0:

                if j <= bracketLocation[1]:
                    self.inside.append(
                        Element(
                            self.stat.symbol[ j:bracketLocation[1]+1 ],
                            self.stat.amount * bracketAmount ) )

            else:
                self.inside.append(
                    Element(
                        self.stat.symbol[ j: ],
                        self.stat.amount ) )

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

    def mass(self):
        self.stat.mass = 0
        for i in self.inside:
            self.stat.mass += i.stat.data[1]

    def __init__(self, symbol):
        self.stat = Info()
        self.stat.symbol = symbol
        self.stat.amount = self.coef()

        self.inside = []
        self.massInput = 0.0

        self.analyze()
        self.mass()

def empirical():
    reactants    = [ ]
    empValSwitch = False
    i = 0

    while True:
        print 'Enter your list of percent amounts of elements (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput == 'help':
            print '\nWelcome to the stoichiometry.py help page!\n'
            print 'The expected input for this program is as follows:'
            print '* MASS SYMBOL, MASS SYMBOL, ...'
            print 'Where \'MASS\' is AT MOST in the thousandths place.'
            print '\nAny bugs, issues, requests? Put them in the GitHub repo.\n'
        elif userInput == 'quit':
            exit(0)
        else:
            break
    #TODO: finish stuff!
    while i < len( userInput.split() ):
        try:
            reactants.append(
                (userInput.split()[i], userInput.split()[i + 1]) )
        except:
            print 'Not enough information to solve the problem.',
            print 'If you believe this is wrong, report this in the GitHub repo.'
            exit(0)

        i += 2
    print reactants


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
    print userInput
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

    #Phase 3: userInput of each componud's mass
    for i in reactants + products:
        print i
        print 'How many grams of %s are in the reaction? (Type \'?\' if value is unknown' % i.stat.symbol

        if userInput == '?':
            continue
        else:
            i.massInput = float( raw_input(">>>") ) #Would like to rename variable

    #debug
    for i in reactants:
        print 'reactants:'
        print '%10f' % i.massInput
        for j in i.inside:
            print 'r:'
            print '%10s' % j.stat.data[0]
            print '%10f' % j.stat.data[1]
            print '%10s' % j.stat.data[2]
            print '%10d' % j.stat.data[3]
    for i in products:
        print i.massInput
        print 'products:'
        for j in i.inside:
            print 'p:'
            print '%10s' % j.stat.data[0]
            print '%10f' % j.stat.data[1]
            print '%10s' % j.stat.data[2]
            print '%10d' % j.stat.data[3]

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
    main()

    exit(0)
