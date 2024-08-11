'''Problem Statement

O mapa do Minecraft é composto de blocos cúbicos em uma relação de igualdade com o sistema métrico, assim, cada aresta dos blocos tem 1 metro. Dessa forma, é possível identificar localidades por triplas de coordenadas X, Y, Z, na qual X representa a longitude, Y representa a elevação em blocos e Z representa a latitude.

Para simplificar a comunicação, é comum se referir a localidades apenas no plano da superfície do mapa, utilizando apenas as coordenadas X e Z, referindo-se ao ponto no X e Z informados e no Y do ponto da superfície.

Para definir distâncias entre duas localidades é utilizada a fórmula de distância euclidiana, na qual o Y das duas coordenadas pode ser omitido para definir apenas a distância nas duas dimensões. A fórmula de distância euclidiana é:

D² = (X1 - X2)² + (Z1 - Z2)²
Para entregar os ferros para as vilas, Tantan precisaria saber quais as distâncias da sua localidade para cada vila, podendo se programar em suas viagens. Nas anotações de Tantan, as vilas estavam associadas as seguintes coordenadas:

Hogsmeade (X: 34, Y: 110, Z: 220)
Kakariko (X: 0, Y: 64, Z: 0)
Solitude (X: 140, Y: 200, Z: 456)
Sua tarefa é, baseado nas coordenadas atuais de Tantan, listar as distâncias para cada uma das vilas.

Input

X - número inteiro
Z - número inteiro
As duas linhas da entrada são compostas por números inteiros X e Z, que indica a coordenada atual de Steve, sem o Y, que pode ser abstraído como informado na descrição.

Obs: Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.

Output

Distancia para Hogsmeade: H
Distancia para Kakariko: K
Distancia para Solitude: S

-H - número de ponto flutuante -K - número de ponto flutuante -S - número de ponto flutuante

As linhas de saída são compostas por um texto seguido, seguido pela distância da coordenada atual de Tantan para a vila correspondente.

Obs: A distância deve ser aproximada em duas casas decimais.'''

#código

import math
coord_x = int(input(''))
coord_z = int(input(''))

H_distancia_x = 34
H_distancia_z = 220
K_distancia_x = 0
K_distancia_z = 0 
S_distancia_x = 140
S_distancia_z = 456

distancia_H = (abs (H_distancia_x - coord_x))**2 + (abs(H_distancia_z - coord_z ))**2 
distancia_final_H = (math.sqrt(distancia_H))
print( f'Distancia para Hogsmeade: {distancia_final_H:.2f}')

distancia_K = (abs (K_distancia_x - coord_x))**2 + (abs(K_distancia_z - coord_z ))**2 
distancia_final_K = (math.sqrt(distancia_K))
print( f'Distancia para Kakariko: {distancia_final_K:.2f}')

distancia_S = (abs (S_distancia_x - coord_x))**2 + (abs(S_distancia_z - coord_z ))**2 
distancia_final_S = (math.sqrt(distancia_S))
print( f'Distancia para Solitude: {distancia_final_S:.2f}')


