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

}

/*
/ Ask user to int
  / Int must be only one and positive
  / If user submits more than one or none, print error message and return 1
  If user does not submit decimal digit, print Usage: ./caesar key and return 1
2. Then ask for input plaintext: space space and ask for a string
3. Then output ciphertext: space
4. Return 0 after successful execution


General:
- Mustr preserve case
- If not a letter, maintain
- 

*/