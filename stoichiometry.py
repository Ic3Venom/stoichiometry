import compounds

def empirical():
    storage = [ ]

    while True:
        print 'Enter your list of percent amounts of elements (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput == 'help':
            print 'stoichiometry.py/emperical() help:'
            print '  The expected input for this program is as follows:'
            print '    MASS SYMBOL, MASS SYMBOL, ...'
            print '  * Where \'MASS\' is AT MOST in the thousandths place.'
            print '  Any bugs, issues, requests? Put them in the GitHub repo.\n'
            
        elif userInput == 'quit':
            exit(0)
        
        else:
            break

    #TODO: finish stuff!
    for i in userInput.split(','):
        try:
            storage.append(
                (compounds.Compound(
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
            print '* R: Reactants (any order, separated by the syntax, \' + \'(space plus space)'
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
                products.append( compounds.Compound(i) )
                switch = False

            else:
                reactants.append( compounds.Compound(i) )

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
            print '\nstoichiometry.py help:'
            print '  For empirical/molecular formula, type \'empirical\' or \'molecular\''
            print '  For limiting reactant solver, type \'limiting\''
            print '  Any bugs, issues, requests? Report them in the GitHub repo.\n'

        elif userInput.lower() == 'quit':
            exit(0)

        elif userInput.lower() in ['empirical', 'emp', 'molecular', 'mol']:
            empirical()
            break

        elif userInput.lower() in ['limiting', 'lim']:
            limiting()
            break
        
        else:
            print 'Unrecognized command "%s".' % userInput

if __name__ == '__main__':
    
    main()

    exit(0)
