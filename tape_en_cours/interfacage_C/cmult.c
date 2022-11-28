#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cmult.h"

#define DEBUG 1
float cmult(int int_param, float float_param)
{
    float return_value = int_param * float_param;
    return return_value;
}

void square_numpy(float *in, float *out, int len)
// on créer un tableau 1d en numpy et l'utiliser en C
{
    for (int i = 0; i < len; i++)
    {
        out[i] = in[i] * in[i];
    }
}

float *demo_2d_array(int N, int M)
// on peut passer une taille et récupérer un tableau 2d numpy
{
    float *arr;
    arr = (float *)malloc(N * M * sizeof(float));
    memset(arr, 0xFF, N * M * sizeof(float));

    for (int x = 0; x < N; x++)
    {
        for (int y = 0; y < M; y++)
        {
            arr[(x * M) + y] = x + y;
        }
    }

    return arr;
}