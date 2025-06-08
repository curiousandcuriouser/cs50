#include "cs50.h"
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
  // INITIALIZE VARIABLE
  int charCount = 0;
  int sentCount = 0;
  int wordCount = 0;
  bool inWord = false; 
  bool sentBeginning = false;
  float l;
  float s;

  // GET TEXT
  string textSample = get_string("Enter the text you want to evaluate: \n");

  // COUNT CHARACTERS & SENTENCES IN FIRST 100 WORDS
  for (int i = 0, length = strlen(textSample); i < length; i++)
  {
    if ((!isspace(textSample[i]) && (!inWord)))
    {
      inWord = true;
      wordCount++;
    } 
    else if ((isspace(textSample[i]) && (inWord)))
    {
      inWord = false;
    }

    if (wordCount <= 100 && ((!isspace(textSample[i]))))
    {
        charCount++;

        if (textSample[i] == '!' || textSample[i] == '?' || textSample[i] == '.')
        {
          sentCount++;
          sentBeginning = true;
        }
    }
  }

  // PRINT METRICS
  printf("WORDCOUNT: %i\n", wordCount);
  printf("CHARACTER COUNT: %i\n", charCount);
  printf("SENTENCE COUNT: %i\n", sentCount);
  
  // CALCULATE RATIO
  l = ((float)charCount / wordCount) * 100;
  printf("L ratio: %f\n", l);

  s = ((float)sentCount / wordCount) * 100;
  printf("S ratio: %f\n", s);

  // CALCULATE INDEX
  int index = 0.0588 * l - 0.296 * s - 15.8;

  // DECLARE GRADE
  if (index < 1)
  {
    printf("Before Grade 1\n");
  }
  else if (index > 16)
  {
    printf("Grade 16+\n");
  }
  else
  {
    printf("Grade %i\n", index);
  }
  return 0;
}

/*
TO DO:
1. Refactor
2. Figure out examples 2 & 3 issues
*/