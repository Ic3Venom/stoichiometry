/*
** File: stoichiometry.c
** Calculates some basic numbers from an equation and amounts of chemicals
** Created by Julian Meyn, 12.1.2017
*/

#include <stdio.h>
#include <stdlib.h>

#define INPUT_LEN   101
#define CPD_LEN     10

/*
**Struct contains information about an element or a molecule
*/
struct ELEMENT
{
    int     amount;
    int     number;
    char    name[13];
    char    symbol[3];
    float   mass;
};

/*
** COMPOUND is the combination of 2 or more different types of elements
** A compound can contain multiple compounds, stored in linked list CPD_NODE
*/
struct COMPOUND
{
    int     amount;
    float   massTotal;
    struct  ELEMENT elements[CPD_LEN];
};

/*
** Linked list of compounds
*/
struct CPD_NODE
{
    int ID;
    struct COMPOUND compound;
    struct CPD_NODE *next;
};

/*
** Altered code, originally from 'ultimatetypingtest main.c'
*/
int stringToInt(char character)
{
    switch (character)
    {
    case 0:
    case 10:  return -1;
    case '0': return 0;
    case '1': return 1;
    case '2': return 2;
    case '3': return 3;
    case '4': return 4;
    case '5': return 5;
    case '6': return 6;
    case '7': return 7;
    case '8': return 8;
    case '9': return 9;
    case '+': return 11;
    case '-': return 12;
    case ' ': return 13;
    default:  return 10;
    }
}

/*
** Altered exponent function, originally from 'baseconverter main.c'
*/
int exponentiate(short base, short exponent)
{
    int power = 1;

    while(exponent)
    {
        power *= base;
        exponent--;
    }
    return power;
}

/*
** Set an entire array to '\0'
*/
void initializeArray(char array[], int length)
{
    memset(array, '\0', length * sizeof(array[0]));
}

/*
** Finds atomic mass of 'chemical' and multiplies it by 'amount'
*/
float elementFind(char* chemical, int amount)
{
    struct ELEMENT element;
    char fileName[] = "periodictable.txt";
    char *fileMode  = "r";
    FILE *file      = fopen(fileName, fileMode);

    if (file == NULL)
    {
        printf("Unable to find file %s!", fileName);
        exit(2);
    }

    while(fscanf(file, "%d %s %f %s", &(element.number), element.symbol, &(element.mass), element.name) != EOF)
    {
        if (strcmp(element.symbol, chemical) == 0)
        {
            break;
        }
    }

    if ( strcmp(element.symbol, chemical) != 0 )
    {
        printf("Unable to find the element %s in periodictable.txt!", element.name);
        exit(27);
    }

    return element.mass * amount;
}

/*
** UNFINISHED
*/
void compoundRead(char compound[INPUT_LEN])
{
    int i, j, currentChar;
    struct CPD_NODE *root, *conductor;

    root        = (struct CPD_NODE *) malloc( sizeof(struct CPD_NODE) );
    root->next  = 0;
    conductor   = root;
    for(i = 0, j = 0; i < INPUT_LEN; i++)
    {
        currentChar = stringToInt( compound[i] );

        if(currentChar >= 0 /*Occurs when compound has prefix, len(prefix) is stored in j*/
             && currentChar <= 9)
        {
            j++;
        }
        else                /*Occurs when compound has no prefix/prefix ended*/
        {
            break;
        }
    }

    //I despise this entire piece
    if (j == 0)
    {
        conductor->compound.amount = 1;
    }
    else
    {
        i = 0;
    }

    while(j)
    {
        j--;
        currentChar = stringToInt( compound[j] );

        //Here should be a pointer to conductor.compound.amount, but it won't work
        i += (currentChar * exponentiate(10, j) );

        conductor->compound.amount = i; /*This is the problem that stops this project in this language*/
    }
    printf("Amount of compound: %d\n", conductor->compound.amount);
}

/*
** Large block of text from help menu
*/
void help()
{
    printf("\n-----------------------------------<HELP>----------------------------------\n");
    printf("The expected input for this program is as follows:\n");
    printf("\tR + R... -> P + P...\n");
    printf("  * R: Reactants (any order, seperated by the syntax, ' + '(space plus space)\n");
    printf("  * ->: yields symbol, please put a space before and after it\n");
    printf("  * P: Products (any order, separated by the syntax, ' +  '(space plus space)\n");
    printf("Any bugs, issues, requests? Put them in the GitHub repo.");
    printf("\n---------------------------------------------------------------------------\n\n");
}

/*
**Takes input from reader and interprets it, preparing for product creation
*/
void inputRead()
{
    int  i, j, currentChar;
    char input   [INPUT_LEN];
    char compound[CPD_LEN];

    initializeArray(input, INPUT_LEN);
    initializeArray(compound, CPD_LEN);

    //Program UI
    while(1)
    {
        printf("Input your BALANCED chemical equation (type 'help' for help):\n$ ");
        fgets(input, INPUT_LEN, stdin);

        if( strcmp(input, "help") == 0 )
        {
            help();
            continue;
        }

        break;
    }

    for(i = 0, j = 0; i < INPUT_LEN; i++)
    {
        currentChar = stringToInt( input[i] );

        if(currentChar >= 0
             && currentChar <= 10)
        {
            while(1)
            {
                currentChar = stringToInt( input[i + j] );

                if(currentChar >= 0
                   && currentChar <= 10)
                {
                    compound[j] = input[i + j];
                    j++;
                }
                else
                {
                    i += (j - 1);
                    j  = 0;
                    compoundRead(compound);

                    break;
                }
            }
        }
        else
        {
            switch(currentChar)
            {
            case 11:
                break;
            case 12:
                //product production starts here
            case 13:
                initializeArray(compound, CPD_LEN);
                break;
            case -1:
                printf("Done analyzing. If you see this, your input syntax is wrong!");
                exit(0);
            default:
                printf("\nSomething went wrong! Report this with a screenshot at the GitHub issues page");
                exit(-1);
            }
        }
    }
}

/*
** Program start
*/
int main()
{
    inputRead();

    return 0;
}
