#include <stdio.h>
#include <stdlib.h>

struct ELEMENT{
    short   number;
    char    symbol[3];
    float   mass;
    char    name[13];
};

//From 'ultimatetypingtest.cpp'
int stringToInt(char character)
{
    switch (character)
    {
    case 49: return 1;
    case 50: return 2;
    case 51: return 3;
    case 52: return 4;
    case 53: return 5;
    case 54: return 6;
    case 55: return 7;
    case 56: return 8;
    case 57: return 9;
    default: return 0;
    }
}

float elementFind(char* chemical, int amount)
{
    FILE *file;
    struct ELEMENT element;
    char fileName[] = "periodictable.txt";
    char *fileMode = "r";

    file = fopen(fileName, fileMode);

    if (file == NULL)
    {
        printf("Unable to find file %s", fileName);
    }

    while(fscanf(file, "%d %s %f %s", &(element.number), element.symbol, &(element.mass), element.name) != EOF)
    {
        if (strcmp(element.name, chemical) == 0)
        {
            break;
        }
    }

    if (strcmp(element.name, chemical ) != 0)
    {
        printf("Unable to find the element %s in periodictable.txt! Exiting program", element.name);
        exit(-1);
    }

    return element.mass * amount;
}

int main()
{
    char input[100];

    float mass = elementFind("Hydrogen", 2);

    printf("%f", mass);
    return 0;
}
