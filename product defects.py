#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'largestArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY samples as parameter.
#

def largestArea(samples):
    # Write your code here
    rows = len(samples) # no. de linhas em samples[][]
    columns = len(samples[0]) # no. de colunas em samples[][]
 
    matrix = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            if i==0 or j==0:
                temp += samples[i][j],
                print("Temp IF: ", temp)
            else:
                temp += 0,
                print("Temp else: ", temp)
        matrix += temp,
        print("matrix em rows: ", temp)
    print("matrix fora laço: ", temp)
    # aqui defini a primeira linha e a primeira coluna de samples iguais à matriz de entrada, outras entradas são definidas como 0
 
    # Atualiza outras entradas
    for i in range(1, rows):
        for j in range(1, columns):
            if (samples[i][j] == 1):
                matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
                print("matris no 2 for if: ", matrix)
            else:
                matrix[i][j] = 0
                print("matris no 2 for else: ", matrix)
        print("\n")

    # Encontre a entrada máxima e índices de entrada máxima em samples[][]
    max_of_matrix = matrix[0][0]
    max_rows = 0
    max_columns = 0
    for i in range(rows):
        for j in range(columns):
            if (max_of_matrix < matrix[i][j]):
                max_of_matrix = matrix[i][j]
                max_rows = i
                max_columns = j

    return max_of_matrix
 

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    '''samples_rows = int(input().strip())
    samples_columns = int(input().strip())'''

    samples = []

    '''for _ in range(samples_rows):
        samples.append(list(map(int, input().rstrip().split())))'''
    
    samples = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]

    
    result = largestArea(samples)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
'''
Complexidade de tempo: O(m*n) onde m é o número de linhas e n é o número de colunas na matriz dada.
Solução otimizada: Para calcular uma entrada em qualquer posição da matriz, precisamos apenas da linha atual e da linha anterior.

Algoritmo:
Seja uma matriz binária a ideia do algoritmo é construir uma matriz de tamanho auxiliar matrix[][] 
na qual cada entrada matrix[i][j] representa o tamanho da submatriz quadrada com todos os 1s incluindo samples[i][j] 
onde samples[i][j] é a entrada mais à direita e mais embaixo na submatriz.

1) Construa uma matriz de soma matrix[R][C] para o dado samples[R][C].
      a) Copie a primeira linha e as primeiras colunas como é de samples[][] para matrix[][]
      b) Para outras entradas, use as seguintes expressões para construir matrix[][]
          Se samples[i][j] é 1 então
             matrix[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
          Senão /*Se samples[i][j] for 0*/
             matrix[i][j] = 0
2) Encontre a entrada máxima em matrix[R][C]
3) Usando o valor e as coordenadas de entrada máxima em S[i], imprima ubmatriz de samples[][]

Para o dado samples[R][C] no exemplo acima, matrix[R][C] construído seria:
   0  1  1  0  1
   1  1  0  1  0
   0  1  1  1  0
   1  1  2  2  0
   1  2  2  3  1
   0  0  0  0  0
O valor da entrada máxima na matriz acima é 3 e as coordenadas da entrada são (4, 3). Usando o valor máximo e suas coordenadas, podemos descobrir a submatriz necessária.
'''