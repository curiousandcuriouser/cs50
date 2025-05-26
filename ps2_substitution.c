#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool noRepeat(string substitutionKey);
string makeKeyUppercase(string substitutionKey);

////////////////////////////////////////////////////////////////////

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

  // INITIALIZE LENGTH OF KEY
  int substitutionKeyLength = strlen(substitutionKey);

  // MAKE KEY UPPERCASE
  makeKeyUppercase(substitutionKey);

  // ASK FOR TEXT
  string plainText = get_string("Enter your text: \n");

  // ENCRYPT AND OUTPUT CIPHERTEXT
  for (int i = 0, length = strlen(plainText); i < length; i++)
  {
    char currentCharacter = plainText[i];

    if (isupper(currentCharacter))
    {
      char encryptedCharacter = substitutionKey[plainText[i] - 'A'];
      printf("%c", encryptedCharacter);
    }
    else if (islower(currentCharacter))
    {
      char encryptedCharacter = tolower(substitutionKey[plainText[i] - 'a']);
      //currentCharacter + shifts[i] - 'a';
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

////////////////////////////////////////////////////////////////////

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

string makeKeyUppercase(string substitutionKey)
{
  int substitutionKeyLength = strlen(substitutionKey);

  for (int i = 0; i < substitutionKeyLength; i++)
  {
    substitutionKey[i] = toupper(substitutionKey[i]);
  }
  return substitutionKey;
}