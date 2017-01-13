#include <stdio.h>
#include <stdlib.h>

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

int main()
{
    char input[100];

    scanf("%s", input);
    printf("%s", input);

    return 0;
}
