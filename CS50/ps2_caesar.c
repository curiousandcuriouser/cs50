#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
  // ASK FOR KEY
  int key = get_int("Enter key: ");

  // VERIFY KEY
  if (key < 0)
  {
    printf("Usage: ./caesar key\n");
    return 1;
  }

  // ASK FOR TEXT
  string plaintext = get_string("Enter your text:  ");

  // MAKE & OUTPUT CIPHERTEXT
  for (int i = 0, length = strlen(plaintext); i < length; i++)
  {
    char currentCharacter = plaintext[i];

    if (isupper(currentCharacter))
    {
      char encryptedCharacter = ((currentCharacter - 'A') + key) % 26 + 'A';
      printf("%c", encryptedCharacter);
    }
    else if (islower(currentCharacter))
    {
      char encryptedCharacter = ((currentCharacter - 'a') + key) % 26 + 'a';
      printf("%c", encryptedCharacter);
    }
    else
    {
      printf("%c", currentCharacter);
    }
  }
  printf("\n");

  
  return 0;
}

/*
TODO:
1. Make reverse
*/