#include "cs50.h"
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
  // GET TEXT
  string textSample = get_string("Enter the text you want to evaluate: \n");

  // DEFINE SENTENCE & WORD
  string word = 
  
  
  int l;
  int s;
  int grade;

  // Declare Grade

  printf("Grade %i", grade);

}

/*
GOAL: This program evaluates readability of a text.asm
/ Prompt user to input text
** Evaluate text based on this formula: 
    index = 0.0588 * L - 0.296 * S - 15.8
      L = average number of letters per 100 words
      S = average number of sentences per 100 words
- Print Grade Level, from Before Grade 1 to Grade 16+


Idea:
** Define word for computer
- Define sentence for computer
- Take sample of 100 words
- Calculate average number of letters in sample
- Calculate average number of sentences in sample


Definitions: 
- A word is surrounded by spaces or punctuation
- A sentence contains at least on word
*/