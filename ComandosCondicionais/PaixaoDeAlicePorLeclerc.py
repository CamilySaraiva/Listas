'''Problem Statement

Alice é uma nordestina que ama Fórmula 1 e é ainda mais encantada por Charles Leclerc. Ela assiste todas as corridas da temporada e adora fazer comentários com a TV (assim como sua mãe quando assiste novela).

gif do Leclerc

Ela deseja acompanhar a pontuação do seu piloto favorito e comparar com a pontuação do seu maior rival nas pistas, o piloto Max Verstappen

Alice sabe que os 10 primeiros pilotos recebem pontuação de acordo com a lista abaixo:

1º lugar: 25 pontos
2º lugar: 18 pontos
3º lugar: 15 pontos
4º lugar: 12 pontos
5º lugar: 10 pontos
6º lugar: 8 pontos
7º lugar: 6 pontos
8º lugar: 4 pontos
9º lugar: 2 pontos
10º lugar: 1 ponto
O piloto que não chegar entre os 10, não recebe pontuação.

Input

Primeiro, será fornecida a pontuação do piloto favorito de Alice, Charles Leclerc:

pontuacaoCharles

Em seguida, será fornecida a pontuação obtida pelo maior rival de Charles, Max Verstappen:

pontuacaoMax

Output

De acordo com os valores da entrada, você deve imprimir na tela as frases de Alice:

Caso Charles não consiga se classificar entre os 10 primeiros colocados, você deve imprimir somente:
"Oxe! E vai morrer por causa de 25 pontos?”

Caso contrário:
→ Se Charles for o primeiro colocado:

"O meu favorito venceu! Pode torar o aco Verstappen"

→ Se Charles não for o primeiro colocado, mas ainda estiver no pódio:

"Esse Charles eh arretado mesmo"

→ Ou se ele não estiver no pódio, mesmo chegando entre os 5:

"Ele eh desenrolado demais"

→ Independente da colocação (desde que esteja no top10), se Charles Leclerc estiver com até 4 pontos de diferença para mais ou para menos do seu maior rival Max Verstappen, imprima:

“Ta com a molestia, vai perder para Max Verstappen eh”

→ Entretanto, se a diferença for maior que isso e favorecer Charles, imprima:

"Deu o sangue" '''


#código

pontuacaoCharles = int(input())
pontuacaoMax = int(input())
difpoint = abs(pontuacaoMax - pontuacaoCharles)

if (pontuacaoCharles == 0) :
    print('Oxe! E vai morrer por causa de 25 pontos?')
    
elif (pontuacaoCharles == 25) :
    print('O meu favorito venceu! Pode torar o aco Verstappen')

elif (pontuacaoCharles >= 15) and (pontuacaoCharles < 25) :
    print('Esse Charles eh arretado mesmo')

elif ( pontuacaoCharles >= 10) and (pontuacaoCharles <= 12) :
    print('Ele eh desenrolado demais')
    
if (pontuacaoCharles > 0 and difpoint <= 4):
    print('Ta com a molestia, vai perder para Max Verstappen eh')
    
elif (pontuacaoCharles >  pontuacaoMax and difpoint > 4) :
    print('Deu o sangue')



