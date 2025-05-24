#include <ctype.h>
#include "cs50.h"
#include <math.h>
#include <stdio.h>
#include <string.h>

int computeScore(string word);
void declareWinner(int score1, int score2);
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main (void)
{
  // GET WORDS
  string word1 = get_string("Player 1. Enter a word: ");
  string word2 = get_string("Player 2. Enter a word: ");

  //GET SCORE
  int score1 =  computeScore(word1);
  int score2 =  computeScore(word2);

  //PRINT SCORE
  printf("Player 1 Score: %i\n", score1);
  printf("Player 2 Score: %i\n", score2);
  
  //DECLARE WINNER
  declareWinner(score1, score2);
  
}

// COMPUTE SCORE
int computeScore(string word)
{
  int score = 0;
  // COMPARE WORD SCORES
  for(int i = 0, length = strlen(word); i < length; i++)
  {
    if (isupper(word[i]))
    {
      score += points[word[i] - 'A'];
    }
    else if (islower(word[i]))
    {
      score += points[word[i] - 'a'];
    } else
    {
      score+= 0;
    }
  } 
  return score;
}

// DECLARE WINNER
void declareWinner(int score1, int score2)
{
  if (score1 > score2)
  {
    printf("Player 1 wins!\n");
  }
  else if (score2 > score1)
  {
    printf("Player 2 wins!\n");
  }
  else
  {
    printf("Tie\n");
  }
}