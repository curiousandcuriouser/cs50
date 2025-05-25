#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
  // ASK FOR SUBSITUTION KEY
  string substitutionKey = get_string("Enter the substitution key: \n");

  // VERIFY SUBSTITUTION KEY
  for (int i = 0, length = strlen(substitutionKey); i < length; i++)
  {
    if (!isalpha(substitutionKey[i]))
    {
        printf("Your input has to consist of only letters.\n");
        return 1;
    }
  }

  if (strlen(substitutionKey) < 26)
    {
        printf("Your input has to consist of 26 letters.\n");
        return 1;
    }

  // ASK FOR TEXT
  string plaintext = get_string("Enter your text: \n");

  // ENCRYPT AND OUTPUT CIPHERTEXT
  
}

/*
1. Ask for substitution key
  If no or too many CLA, print error message and return 1
  If invalid, print error message and return 1
2. Ask for plaintext with get_string
3. Output ciphertext
4. Print new line and return 0

General:
- Key should be case-insensitive
- Preserve text case
*/