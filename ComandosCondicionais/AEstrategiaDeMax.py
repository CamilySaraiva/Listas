'''Problem Statement

Na Fórmula 1, a estratégia é fundamental para a vitória. Em um esporte que cada segundo conta, tudo influencia no resultado final, desde a escolha dos pneus ao tipo de abordagem que o piloto irá adotar. O piloto Max Verstappen, maior nome da geração atual de F1, está para fazer mais uma corrida e sua equipe está precisando de ajuda para definir a estratégia de prova de Max. Por isso, eles pediram que você, aluno do CIn, desenvolva um programa que analise as condições pré-corrida e determine a estratégia que Max deverá seguir para esta prova.

Input

Inicialmente, você receberá quatro inputs:

(str) condicoes_metereologicas

Essa entrada terá três possibilidades: ensolarado, nublado e chuvoso.

Caso o clima esteja chuvoso, seu programa deve imediatamente captar mais um input:

pista_molhada.

OBS: Esse input será recebido em forma de string ("True" ou "False"), mas deve ser convertido em booleano para armazenar o valor verdadeiro ou falso.

(str) temperatura_pista

A temperatura da pista pode variar entre: alta, moderada e baixa.

(str) desempenho_treinos

O desempenho de Max nos treinos para a corrida será bom ou ruim.

(int) posicao_largada

Diz a posição que Max irá largar entre os 20 pilotos.

Output

Primeiramente, deve ser printado o seguinte:
“Estratégia de prova de Max Verstappen!”

Em seguida, o seu programa deverá analisar as possibilidades e dizer qual estratégia Max deve seguir.

Com relação ao clima e a temperatura da pista:
Se o clima estiver ensolarado e a temperatura da pista for alta:
“Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!”

Se o clima estiver ensolarado e a temperatura da pista não for alta:
“Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.”

Se o clima estiver nublado e com temperatura alta:
“Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!”

Se o clima estiver nublado e com a temperatura da pista baixa ou moderada:
“Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!”

Se o clima estiver chuvoso e com pista molhada:
“Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.”

Se o clima estiver chuvoso e sem pista molhada:
“Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!”

Já para a abordagem de Max durante a corrida:
Se ele largar em primeiro e seu desempenho nos treinos for bom:
“Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.”

Caso ele largue em primeiro, mas seu desempenho no treino tenha sido ruim:
“Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.”

Caso ele não saia em primeiro, mas esteja entre os 12 primeiros:
“Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.”

Por fim, se Max estiver largando atrás dos 12 primeiros:
“Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.”'''

#código

condicoes_metereologicas = input()
if condicoes_metereologicas == 'chuvoso':
    pista_molhada = (input())
    if pista_molhada == 'False':
        pista_molhada = False
    else:
        pista_molhada = True

temperatura_pista = str(input())
desempenho_treinos = str(input())
posicao_largada = int(input())

print ('Estratégia de prova de Max Verstappen!')

#condicional clima e temperatura
if condicoes_metereologicas == 'ensolarado' and temperatura_pista == 'alta':
    print('Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!')
elif condicoes_metereologicas == 'ensolarado' and (temperatura_pista == 'moderada' or temperatura_pista == 'baixa'):
    print('Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.')
elif condicoes_metereologicas == 'nublado' and temperatura_pista == 'alta':
    print('Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!')
elif condicoes_metereologicas == 'nublado' and (temperatura_pista == 'moderada' or temperatura_pista == 'baixa'):
    print('Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!')
elif condicoes_metereologicas == 'chuvoso' :
    if pista_molhada == True :
        print('Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.')
    else :
        print('Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!')
#abordagem durante a corrida

if posicao_largada == 1 and desempenho_treinos == 'bom' :
    print('Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.')
elif posicao_largada == 1 and desempenho_treinos == 'ruim':
    print('Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.')
elif posicao_largada > 1 and posicao_largada <= 12 :
    print('Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
else :
    print('Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.')