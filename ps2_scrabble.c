#include <ctype.h>
#include "cs50.h"
#include <math.h>
#include <stdio.h>
#include <string.h>

int computeScore(string word);
int findWinner(int scores[], int playerNumber);
void declareWinner(int scores[], int maxScore, int playerNumber);

int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main (void)
{
  int playerNumber = get_int("How many players? ");

  // GET WORDS
  string words[playerNumber];

  for (int i = 0; i < playerNumber; i++)
  {
    words[i] = get_string("Player %i. Enter a word: ", i + 1);
  }

  //GET SCORE
  int scores[playerNumber];
  for (int i = 0; i < playerNumber; i++)
  {
    scores[i] = computeScore(words[i]);
  }
  

  //PRINT SCORE
  for (int i = 0; i < playerNumber; i++)
  {
    printf("Player %i scores: %i\n", i + 1, scores[i]);
  }
  
  //DECLARE WINNER
  int winningScore = findWinner(scores, playerNumber);
  declareWinner(scores, winningScore, playerNumber);

  return 0;  
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

// FIND WINNER
int findWinner(int scores[], int playerNumber)
{
  int maxScore = scores[0];

  for (int i = 1; i < playerNumber; i++)
  {
    if(scores[i] > maxScore)
    {
      maxScore = scores[i];
    }
  }
  return maxScore;
}

//DECLARE WINNER
void declareWinner(int scores[], int maxScore, int playerNumber)
{
  int winnerCount = 0;

  for (int i = 0; i < playerNumber; i++)
  {
    if (scores[i] == maxScore)
    {
      winnerCount++;
    }
  }

  if (winnerCount == 1)
  {
    for (int i = 0; i < playerNumber; i++)
    {
      if (scores[i] == maxScore)
      {
        printf("Player %i wins!\n", i + 1);
        break;
      }
    }
  }
  else if (winnerCount > 1)
  {
    printf("Tie between: ");
    int mentionedWinners = 0;
    for (int i = 0; i < playerNumber; i++)
    {
      if (scores[i] == maxScore)
      {
        if (mentionedWinners > 0)
        {
          if (mentionedWinners == winnerCount - 1)
          {
            printf(" and ");
          }
          else
          {
            printf(", ");
          }
          
        }
        printf("Player %i", i + 1);
        mentionedWinners++;
      }
    }
    printf("!\n");
  }
}