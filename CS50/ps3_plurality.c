#include "cs50.h"
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
int findMaxVote(void);
void declareWinner(int maxVote);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    int votes[candidate_count];

    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    

    // Display winner of election
    int maxVote = findMaxVote();
    declareWinner(maxVote);
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name,candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
int findMaxVote(void)
{
    int maxVote = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > maxVote)
        {
            maxVote = candidates[i].votes;
        }
    }
    return maxVote;
}


// DECLARE WINNER
void declareWinner(int maxVote)
{
    int winnerCount = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == maxVote)
        {
            winnerCount++;
        }
    }

    if (winnerCount == 1)
    {
        for (int i = 0; i < candidate_count; i++)
        {
            if (candidates[i].votes == maxVote)
        {
            printf("%s wins!\n", candidates[i].name);
            break;
        }
        }
    }
    else if (winnerCount > 1)
    { 
        printf("Tie between: ");
        int mentionedWinners = 0;
        for (int i = 0; i < candidate_count; i++)
        {
            if (candidates[i].votes == maxVote)
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
            printf("%s", candidates[i].name);
            mentionedWinners++;
            }
        }
    printf("!\n");
    }
}