#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            while(fread(&image[i][j], sizeof(3 BYTE), 1, infile) != 0);
            {
            int grayscale = ((RGBTRIPLE.rgbtBlue + RGBTRIPLE.rgbtGreen + RGBTRIPLE.rgbtRed) / 3);
            &image[i][j] = grayscale;
            fwrite(&image[i][j], sizeof(3 BYTE), 1, outfile);
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
