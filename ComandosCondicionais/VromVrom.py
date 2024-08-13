'''Problem Statement

A estreia de Charli XCX como pilota profissional na corrida da empresa Atlantic Records&Races está repleta de nervosismo e expectativa. Sendo sua primeira vez nas pistas em um ambiente profissional, a pressão é ainda maior para que ela demonstre suas habilidades no volante.

gif questao 2.gif

No entanto, uma ideia paira sobre a cabeça de Charli: Um ponto no ouvido! Um detalhe que poderia auxiliá-la durante a corrida. Nesse momento crucial, ela busca orientação para tomar as decisões certas e alcançar o melhor desempenho possível. É aí que entra a sua função, a orientar estrategicamente em cada movimento para enfrentar os desafios da pista.

Conforme a corrida se desenrola, você, como o guia de Charli, precisa interpretar suas falas e sinais para tomar as decisões ideais. A cada curva, reta e momento de ultrapassagem, sua orientação precisa ser rápida e precisa, levando em conta não apenas a habilidade de condução de Charli, mas também a presença de outros competidores e as condições da pista.


Input

Você receberá 2 inputs, que correspondem às frases que Charli poderá falar durante a corrida.

frase_01

frase_02

Elas podem ser:

"TÔ EM ÚLTIMO!"
"Esse cara não sai da minha frente..."
"Tem uma curva vindo aí, me ajuda!"
"MEU PNEU FUROU SOCORRO!"
OBS.: Caso a frase recebida seja "Tem uma curva vindo aí, me ajuda!", você receberá logo em seguida mais um input, que pode corresponder à direção da curva ("DIREITA", "ESQUERDA" ou qualquer outra mensagem que irá lhe deixar confuso). Um exemplo disso seria:

"Tem uma curva vindo aí, me ajuda!"

"DIREITA"

"MEU PNEU FUROU SOCORRO!"

Com base nessas frases, você deverá fornecer mensagens de orientação para Charli, ajudando-a a tomar decisões estratégicas e enfrentar os obstáculos da corrida.

ATENÇÃO: Você deve armazenar os inputs em variáveis e printar os outputs correspondentes na mesma ordem em que os inputs foram recebidos.

Output

Caso você receba a mensagem "TÔ EM ÚLTIMO!", deverá printar:
"PISA FUNDO"

Caso receba a mensagem “Esse cara não sai da minha frente...”, deverá printar:
"Ultrapassa ele agora!"

Caso receba a mensagem "Tem uma curva vindo aí, me ajuda!", deverá printar:
"FREIA AGORA E ME DIZ PARA QUE LADO É"

Para esse caso, você deve imprimir um segundo output relativo ao input extra recebido.

Caso a curva seja para direita, você deverá printar:

"ENTÃO VIRA LOGO!"

Caso a curva seja para esquerda, você deverá printar:

"É SÓ VIRAR!"

Caso ela não informe nem “DIREITA” e nem “ESQUERDA”, você deverá printar:

"Assim não tem como te ajudar, amiga"

Caso receba a mensagem “MEU PNEU FUROU SOCORRO!”, deverá printar:
"Amiga, calma! Tem um pit stop na tua frente…"

Caso a mensagem recebida não seja nenhuma das 4 informadas, deverá printar:
Eita, não entendi nada…

Ao fim, você deverá printar a mensagem abaixo para desejar uma boa corrida a Charli

"LET'S RIDE!" '''

#código

frase_1 = input()

if (frase_1 == 'Tem uma curva vindo aí, me ajuda!'):
    print('FREIA AGORA E ME DIZ PARA QUE LADO É')
    direcao = input()
    if (direcao == 'DIREITA' ):
        print('ENTÃO VIRA LOGO!')
    elif (direcao == 'ESQUERDA'):
        print('É SÓ VIRAR!')
    else:
        print('Assim não tem como te ajudar, amiga')
elif (frase_1 == 'TÔ EM ÚLTIMO!') : 
    print('PISA FUNDO')
elif (frase_1 == 'Esse cara não sai da minha frente...'):
    print('Ultrapassa ele agora!')
elif (frase_1 == 'MEU PNEU FUROU SOCORRO!'):
    print('Amiga, calma! Tem um pit stop na tua frente…')
else :
     print('Eita, não entendi nada…')

frase_2 = input()

if (frase_2 == 'TÔ EM ÚLTIMO!'):
     print('PISA FUNDO')
elif (frase_2 == 'Esse cara não sai da minha frente...'):
    print('Ultrapassa ele agora!')
elif (frase_2 == 'MEU PNEU FUROU SOCORRO!'):
    print('Amiga, calma! Tem um pit stop na tua frente…')
    
elif  (frase_2 == 'Tem uma curva vindo aí, me ajuda!'):
    print('FREIA AGORA E ME DIZ PARA QUE LADO É')
    direcao = input()
    if (direcao == 'DIREITA' ):
        print('ENTÃO VIRA LOGO!')
    elif (direcao == 'ESQUERDA'):
        print('É SÓ VIRAR!')
    else:
        print('Assim não tem como te ajudar, amiga')
else :
     print('Eita, não entendi nada…')

print("LET'S RIDE!")