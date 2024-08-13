'''Em uma emocionante competição de Fórmula 1, o vencedor é determinado pela pontuação acumulada ao longo de várias corridas. A última corrida definirá o resultado final entre os três principais competidores.

Sua missão é anunciar o vencedor com base nas pontuações dos pilotos. Os três principais pilotos são:

Lewis Hamilton
Max Verstappen
Valtteri Bottas

Input

Haverá 6 entradas de números inteiros, correspondendo à pontuação acumulada do piloto na competição e a colocação de cada piloto na última corrida que aconteceu, na seguinte ordem:

Pontuação acumulada de Lewis Hamilton
Colocação de Lewis Hamilton na última corrida
Pontuação acumulada de Max Verstappen
Colocação de Max Verstappen na última corrida
Pontuação acumulada de Valtteri Bottas
Colocação de Valtteri Bottas na última corrida
Caso o piloto esteja entre os 10 primeiros colocados na última corrida, a pontuação acumulada dele é acrescida em 5 pontos.

Em caso de empate na pontuação acumulada, o desempate é feito considerando a ordem alfabética dos nomes dos pilotos.

Output

A saída será uma única linha anunciando o vencedor com base na pontuação acumulada:

"X ganhou a competição com Y pontos!"

Onde X é o nome do piloto vencedor e Y é a sua pontuação acumulada.'''



#código

#lewis
pa_lewis = int(input())
coloq_lewis = int(input())
#max
pa_max = int(input())
coloq_max = int(input())
# valterri
pa_valterri = int(input())
coloq_valterri = int(input())

if coloq_lewis <= 10 :
    pa_lewis += 5

if coloq_max <= 10 :
    pa_max += 5

if coloq_valterri <= 10 : 
    pa_valterri += 5


if (pa_lewis >= pa_max) and (pa_lewis >= pa_valterri):
    print (f'Lewis Hamilton ganhou a competição com {str(pa_lewis)} pontos!')

elif (pa_max >= pa_valterri) and ( pa_max >= pa_lewis) : 
    print(f'Max Verstappen ganhou a competição com {str(pa_max)} pontos!')

elif (pa_valterri >= pa_lewis) and (pa_valterri >= pa_max):
    print(f'Valtteri Bottas ganhou a competição com {str(pa_valterri)} pontos!')