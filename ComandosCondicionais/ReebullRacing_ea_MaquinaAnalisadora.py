'''Problem Statement

Com o objetivo de fazer uma análise sobre o desempenho de seus pilotos nas competições, a equipe do Red Bull Racing pediu pra você, calouro do Centro de Informática, fazer um programa que imprima um parecer sobre o rendimento do atleta de acordo com os dados recebidos.



Input

Inicialmente, você irá receber o nome do piloto que estará sendo analisado, que pode ser “Max Verstappen” ou “Sergio Perez”:

piloto (string)

Em seguida, será entregue a distância total percorrida nessa prova, em quilômetros:

distancia (float)

Por fim, você receberá o tempo total de prova daquele piloto, em horas:

tempo (float)

Output

Com base nos dados recebidos, você deverá calcular a velocidade média do atleta nessa prova e, a partir daí, imprimir sua análise:

Caso o atleta tenha obtido uma velocidade média maior que 227km/h, imprima:
"{piloto} se deu muito bem na prova de hoje!!"

Caso o atleta tenha como velocidade média nessa prova exatamente 227km/h, imprima:
"{piloto} teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!"

Caso o atleta não tenha obtido nenhum desses resultados, imprima:
"{piloto} não se deu tão bem. É preciso melhorar isso!”

OBS.: {piloto} deve ser substituído por “Max Verstappen” ou “Sergio Perez”, de acordo com o input recebido anteriormente.'''

#código

piloto = str(input())
distancia = float(input())
tempo = float(input())

vel_media = distancia / tempo

if vel_media > 227 :
    print(piloto + " se deu muito bem na prova de hoje!!")
elif vel_media == 227 :
    print(piloto + " teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!")
else :
    print(piloto + ' não se deu tão bem. É preciso melhorar isso!')