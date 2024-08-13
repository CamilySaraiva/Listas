'''Problem Statement

Ayrton Senna, renomado piloto brasileiro de Fórmula 1, deixou sua marca em inúmeras pistas ao redor do mundo. Reconhecido por sua intensa dedicação aos treinos, ele exibia um desempenho impressionante - e consistente - em cada circuito que enfrentava.

Dito isso, você irá receber alguns dados e deve desvendar o enigma: em qual pista Senna estava competindo?

Você irá levar em consideração a velocidade máxima dele naquela pista em um certo dia e também as condições climáticas que desafiaram seus talentos naquela corrida.

Foto do Ayrton Senna segurando seu capacete

INFORMAÇÕES:

Sabe-se que o enigma tem somente 03 alternativas de resposta, as pistas de: Mônaco, Ímola ou Spa-Francorchamps.
Em dias ensolarados ou chuvosos, sua velocidade mínima registrada em sua carreira foi de 250km/h e a máxima foi de 260km/h em Mônaco.
Em dias ensolarados ou chuvosos, sua velocidade mínima registrada em sua carreira foi de 261km/h e a máxima foi de 285km/h em Ímola.
Em dias ensolarados ou chuvosos, sua velocidade mínima registrada em sua carreira foi de 286km/h e a máxima foi de 310km/h em Spa-Francorchamps.
Sabe-se que as condições climáticas da corrida podiam ser: Tempo ensolarado, chuvoso ou neblina.
Com o tempo ensolarado, não existem mudanças no padrão de velocidade atingida por ele na pista.
Com o tempo chuvoso, para Senna nada mudava. Ele era o rei da chuva!
Por último, quando havia neblina, a velocidade máxima que Senna atingia na pista na qual corria era equivalente à velocidade máxima da pista imediatamente anterior. Entenda Mônaco como anterior à Ímola e Ímola como anterior à Spa-Francorchamps.
Exemplo: Ao correr no circuito de Ímola com neblina, sua velocidade máxima era igual a de quando corria em Mônaco em um dia sem neblina, ou seja, ao invés de no máximo 285km/h, ele atingia no máximo 260km/h.

OBS.: Quando Senna corria em Mônaco com neblina, sua velocidade máxima era inferior a 250km/h.

Input

Você receberá duas entradas:

velocidade_maxima

Essa entrada corresponde a velocidade máxima dele naquele dia, que pode atingir até 310km/h

tempo

O tempo pode ser uma das três opções: ensolarado, neblina ou chuvoso

Output

Se a resposta encontrada for Mônaco, imprima:
"Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!"

Por sua vez, se a resposta encontrada for Ímola, imprima:
"Senna corria em Ímola, onde infelizmente fez sua última corrida."

Finalmente, se a resposta encontrada for Spa-Francorchamps, imprima:
"Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!"

ATENÇÃO: Cada acento, hífen e espaço importa. Caso erre/esqueça qualquer um desses, a questão não será considerada como certa!'''

#código

velocidade_maxima = int(input())
tempo = str(input())

if (velocidade_maxima >= 250 and velocidade_maxima <= 260) and (tempo == ('ensolarado') or tempo == ('chuvoso')) : 
    print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")

elif (velocidade_maxima >= 261 and velocidade_maxima <= 285) and (tempo == ('ensolarado') or tempo == ('chuvoso')) :
    print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")

elif (velocidade_maxima >= 286 and velocidade_maxima <= 310) and (tempo == ('ensolarado') or tempo == ('chuvoso')) :
    print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")

elif (velocidade_maxima < 250) and (tempo == ('neblina')):
    print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")

elif (velocidade_maxima >= 250 and velocidade_maxima <= 260) and (tempo == ('neblina')):
    print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")

elif  (velocidade_maxima >= 261 and velocidade_maxima <= 285) and (tempo == ('neblina')):
    print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")