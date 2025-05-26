#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool noRepeat(string substitutionKey);

int main(void)
{
  // ASK FOR SUBSITUTION KEY
  string substitutionKey = get_string("Enter the substitution key: \n");

  // VERIFY ONLY LETTERS
  for (int i = 0, length = strlen(substitutionKey); i < length; i++)
  {
    if (!isalpha(substitutionKey[i]))
    {
        printf("Your input has to consist of only letters.\n");
        return 1;
    }
  }

  // VERIFY NUMBER OF LETTERS
  if (strlen(substitutionKey) != 26)
  {
      printf("Your input has to consist of 26 letters.\n");
      return 1;
  }

  // VERIFY NO DUPLICATES
  if (noRepeat(substitutionKey) == false)
  {
      printf("Your input cannot have duplicate letters.\n");
      return 1;
  }

  // ASK FOR TEXT
  string plainText = get_string("Enter your text: \n");

  // LINK PLAIN AND CIPHER ALPHABET
  int shifts[26];
  
  for (int i = 0, length = strlen(substitutionKey); i < length; i++)
  {
    char substitutionCharacter = substitutionKey[i];
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int shiftValue = substitutionCharacter - alphabet[i];
    // LOGIC TEST printf("Shift %c by %i to get %c\n", alphabet[i], shiftValue, substitutionCharacter);
    shifts[i] = shiftValue;
  }
  

  // ENCRYPT AND OUTPUT CIPHERTEXT
  for (int i = 0, length = strlen(plainText); i < length; i++)
  {
    char currentCharacter = plainText[i];

    if (isupper(currentCharacter))
    {
      char encryptedCharacter = currentCharacter + shifts[i];
      printf("%c", encryptedCharacter);
    }
    else if (islower(currentCharacter))
    {
      char encryptedCharacter = currentCharacter + shifts[i];
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

// CHECK FOR DUPLICATES
bool noRepeat(string substitutionKey)
{
  int length = strlen(substitutionKey);
  for (int i = 0; i < length; i++)
  {
    for (int j = i + 1; j < length; j++)
    {
      if (substitutionKey[i] == substitutionKey[j])
      return false;
    }   
  }
  return true;
}