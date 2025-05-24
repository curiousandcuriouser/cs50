#include "cs50.h"
#include <stdio.h>

typedef enum { VALID_CARD, INVALID_LENGTH, INVALID_CHECKSUM } CardStatus;

CardStatus validateCardNumber(long card);
int checkLength(long card);
int calculateCheckSum(long card);
int multiplyAndSum(int lastDigit);
void identifyCompany(int numDigits, long start);

int main(void)
{
    long card = 0;
    CardStatus validationResult;

    // GET VALID CARD NUMBER
    do
    {
        card = get_long("Enter your credit card number: ");
        validationResult = validateCardNumber(card);

        if (validationResult == INVALID_LENGTH)
        {
            printf("LENGTH INVALID\n");
        }
        else if (validationResult == INVALID_CHECKSUM)
        {
            printf("NUMBER INVALID\n");
        }
    }
    while (validationResult != VALID_CARD);

    // IDENTIFY COMPANY
    int numDigits = checkLength(card);
    long start = card;
    identifyCompany(numDigits, start);
    return 0;
}

//FUNCTIONS
// VALIDATE CARD DETAILS
CardStatus validateCardNumber(long card)
{
    int numDigits = checkLength(card);

    if (numDigits == 0)
    {
        return INVALID_LENGTH;
    }
    else
    {
        int sumEverySecondDigit = calculateCheckSum(card);
        if (sumEverySecondDigit % 10 != 0)
        {
            return INVALID_CHECKSUM;
        }
    }

    return VALID_CARD;
}

// CHECK IF RIGHT LENGTH
int checkLength(long card)
{
    int length = 0;
    long tempCard = card;

    while (tempCard > 0)
    {
        length++;
        tempCard /= 10;
    }

    if (length != 13 && length != 15 && length != 16)
    {
        return 0;
    }
    return length;
}

// GET CARD NUMBER SUM
int calculateCheckSum(long card)
{
    int sum = 0;
    long tempCard = card;
    bool isSecondDigit = false;
    while (tempCard > 0)
    {
        if (isSecondDigit == true)
        {
            int lastDigit = tempCard % 10;
            int product = multiplyAndSum(lastDigit);
            sum = sum + product;
        }
        else
        {
            int lastDigit = tempCard % 10;
            sum = sum + lastDigit;
        }

        isSecondDigit = !isSecondDigit;
        tempCard /= 10;
    }
    return sum;
};

// ADD SINGLE DIGITS FROM SUM
int multiplyAndSum(int lastDigit)
{
    int multiply = lastDigit * 2;
    int sum = 0;

    while (multiply > 0)
    {
        int lastDigitMultiply = multiply % 10;
        sum = sum + lastDigitMultiply;
        multiply /= 10;
    }
    return sum;
}

// IDENTIFY COMPANY
void identifyCompany(int numDigits, long start)
{
    while (start >= 100)
    {
        start /= 10;
    }

    if (numDigits == 15 && (start == 34 || start == 37))
    {
        printf("AMEX\n");
    }
    else if (numDigits == 16 &&
             (start == 51 || start == 52 || start == 53 || start == 54 || start == 55))
    {
        printf("MASTERCARD\n");
    }
    else if ((numDigits == 16 || numDigits == 13) && ((start / 10) == 4))
    {
        printf("VISA\n");
    }
    else
    {
        printf("COMPANY INVALID\n");
    }
}
