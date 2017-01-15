#include <stdio.h>
#include <stdlib.h>

#define INPUT_LEN   51
#define CPD_LEN     5

//Struct contains information about an element or a molecule
struct ELEMENT{
    int     amount;
    int     number;
    char    name[13];
    char    symbol[3];
    float   mass;
};

//COMPOUND is the combination of 2 or more different types of elements
//A compound can contain multiple compounds, stored in linked list CPD_NODE
struct COMPOUND{
    int     amount;
    float   massTotal;
    struct  ELEMENT elements[CPD_LEN];
};

struct CPD_NODE{
    struct COMPOUND;
    struct CPD_NODE *next;
} *root, *cpd1;

//Altered code, originally from 'ultimatetypingtest.cpp'
int stringToInt(char character)
{
    switch (character)
    {
    case '1': return 1;
    case '2': return 2;
    case '3': return 3;
    case '4': return 4;
    case '5': return 5;
    case '6': return 6;
    case '7': return 7;
    case '8': return 8;
    case '9': return 9;
    case '+': return 10;
    case '-': return 11;
    case ' ': return 12;
    default: return 0;
    }
}

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

void compoundRead(char chemical[CPD_LEN])
{

}

//Seems justified to separate this large amount of text into a separate function
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

void inputRead()
{
    int  j, i;
    char input[INPUT_LEN];

    while(1)
    {
        printf("Input your BALANCED chemical equation (type 'help' for help):\n$ ");
        scanf("%s", input);

        if( strcmp(input, "help") == 0 )
        {
            help();
            continue;
        }

        break;
    }

    /*
    Linked list is just a concept, not implemented correctly, so this is incomplete

    root = (struct node *) malloc( sizeof(struct node) );
        root -> next = 0;

    */

    for(i = 0, j = 0; i < INPUT_LEN; i++)
    {

    }

}

int main()
{
    inputRead();

    return 0;
}
