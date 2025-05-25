#include "cs50.h"
#include <stdio.h>

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

  // MAKE CIPHERTEXT
  char uppercaseLetters[26] = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90}; // A - Z

  char lowercaseLetters[26] = {97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}; // a - z

  for (int i = 0, length = strlen(plaintext); i < length; i++)
    if (plaintext[i] >= 65 && plaintext[i] <= 90)
    {
      plaintext[i] += key;
    }
    else if (plaintext[i] >= 97 && plaintext[i] <= 122)
    {
      plaintext[i] += key;
    }
    else
    {

    }


  // OUTPUT CIPHERTEXT

  
  return 0;
}

/*
/ Ask user to int
  / Int must be only one and positive
  / If user submits more than one or none, print error message and return 1
  If user does not submit decimal digit, print Usage: ./caesar key and return 1
/ Then ask for input plaintext: space space and ask for a string
3. Then output ciphertext: space
/ Return 0 after successful execution


General:
- Mustr preserve case
- If not a letter, maintain
- 

*/