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
  bool sentBeginning = true;

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
          sentBeginning = false;
        }
        else if (sentBeginning == true && wordCount <=100)
        {
          sentCount++;
        }
    }
  }

  printf("WORDCOUNT: %i\n", wordCount);
  printf("CHARACTER COUNT: %i\n", charCount);
  
  
  int l;
  int s;

  l = charCount / wordCount;
  printf("L ratio: %i\n", l);

  s = sentCount / wordCount;
  printf("S ratio: %i\n", s);



return 0;
  
  int grade;

  // DECLARE GRADE

  printf("Grade %i", grade);

}


/*
GOAL: This program evaluates readability of a text.asm
/ Prompt user to input text
** Evaluate text based on this formula: 
    index = 0.0588 * L - 0.296 * S - 15.8
    / L = average number of letters per 100 words
    / S = average number of sentences per 100 words
- Print Grade Level, from Before Grade 1 to Grade 16+

 // EDGE CASE: If text has less than 100 words?


Idea:
/ Define word for computer
/ Define sentence for computer
/ Take sample of 100 words
/ Calculate average number of letters in sample
/ Calculate average number of sentences in sample


Definitions: 
- A word is surrounded by spaces or punctuation
- A sentence contains at least on word
*/