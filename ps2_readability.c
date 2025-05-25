#include "cs50.h"
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
  // GET TEXT
  string textSample = get_string("Enter the text you want to evaluate: \n");

  int charCount = 0;
  int sentCount = 0;
  int wordCount = 0;
  bool inWord = false; 
  bool sentBeginning = false;

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

  printf("WORDCOUNT: %i\n", wordCount);
  printf("CHARACTER COUNT: %i\n", charCount);
  printf("SENTENCE COUNT: %i\n", sentCount);
  
  
  float l;
  float s;

  l = ((float)charCount / wordCount) * 100;
  printf("L ratio: %f\n", l);

  s = ((float)sentCount / wordCount) * 100;
  printf("S ratio: %f\n", s);

  int index = 0.0588 * l - 0.296 * s - 15.8;
  printf("Readability Index: %i\n", index);

  
  int grade;

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