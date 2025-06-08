#include "cs50.h"
#include <stdio.h>

int calculateCoins(int change);

int main(void)
{
    int change = 0;

    while (change <= 0)
    {
        change = get_int("Change owed: ");
    }

    int coins = calculateCoins(change);
    printf("%i\n", coins);
}

int calculateCoins(int change)
{
    int coins = 0;
    int currentDenomination = 0;

    if (change / 25 != 0) // 25c
    {
        currentDenomination = change / 25;
        coins += currentDenomination;
        change = change % 25;
    }
    if (change / 10 != 0) // 10c
    {
        currentDenomination = change / 10;
        coins += currentDenomination;
        change = change % 10;
    }
    if (change / 5 != 0) // 5c
    {
        currentDenomination = change / 5;
        coins += currentDenomination;
        change = change % 5;
    }
    if (change > 0)
    {
        coins += change;
    }

    return coins;
}