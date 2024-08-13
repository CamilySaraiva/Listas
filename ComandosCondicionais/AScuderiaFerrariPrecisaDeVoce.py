'''Problem Statement

No mundo do automobilismo, especificamente na Fórmula 1, a Ferrari é uma equipe com uma história longa e muitas vitórias. No entanto, na temporada de 2024, a Ferrari está enfrentando dificuldades para superar a equipe da Red Bull e assumir a liderança no campeonato.


Por isso, a Scuderia precisa de você, estudante do Cin, para aumentar sua competitividade em relação às outras equipes! Para isso, a Ferrari precisa que você desenvolva um programa capaz de analisar as performances da equipe, levando em consideração algumas estratégias usadas pela Scuderia, dentre elas o clima, a dificuldade da pista, a quantidade de voltas e o tipo dos pneus:

1. Cada tipo de pneu tem uma durabilidade (duro = 90, médio = 70, macio = 50 e chuva = 50).
2. Se um pneu de chuva for usado em clima de sol, independentemente da dificuldade, o programa deve multiplicar o número de voltas por 15 e subtrair da durabilidade (o mesmo se aplica a pneus que não são de chuva usados em clima de chuva).
3. Se o clima for de sol, a dificuldade for baixa ou média e o tipo de pneu for macio ou medio, deve-se multiplicar o número de voltas por 2 e subtrair da durabilidade.
4. Se o clima for de sol, a dificuldade for alta e os pneus forem macios, deve-se multiplicar o número de voltas por 3 e subtrair da durabilidade.
5. Se o clima for de sol, a dificuldade for alta e os pneus forem duros, deve-se apenas subtrair o número de voltas da durabilidade.
6. Se o clima for de chuva, a dificuldade for baixa e os pneus apropriados para o clima, deve-se apenas subtrair o número de voltas da durabilidade. No caso da dificuldade ser media, multiplica-se por 2 e subtrai e finalmente, se for alta multiplica-se por 3 e subtrai.


Input

Inicialmente, o seu programa deve receber 4 variáveis:
O primeiro valor será um número inteiro voltas que representa a quantidade de voltas dadas pelo carro da Ferrari.

(int) voltas

O segundo valor é uma string (str) clima que dita o clima da pista

(str) clima

Os possíveis climas são:

chuva
sol
O terceiro valor é uma string (str) dificuldade, a qual tem relação com as adversidades da pista

(str) dificuldade

As possíveis dificuldades são:

baixa
média
alta
Finalmente, o ultimo valor é uma string (str) tipo_pneu que determina os pneus usados pela Ferrari durante a corrida.

(str) tipo_pneu

Os tipos de pneus são:

macio
médio
duro
chuva


Output

Por último, o seu programa deve printar as seguinte mensagem caso a durabilidade dos pneus seja maior ou igual a 20:

A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de (desgaste).

OBS: O print deve incluir o valor da variável desgaste.

Caso a durabilidade seja inferior a 20 a seguinte mensagem deve ser produzida:

"Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de (desgaste) e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.”'''

#código
voltas = int(input())
clima = str(input())
dificuldade = str(input())
tipo_pneu = str(input())
desgaste = 0
durabilidade = 0

# condicinal de durabilidade
if tipo_pneu == 'duro':
    durabilidade = 90
elif tipo_pneu == 'médio':
    durabilidade = 70
elif tipo_pneu == 'macio':
    durabilidade = 50
elif tipo_pneu == 'chuva':
    durabilidade = 50

# condicional para calcular desgaste
# 2
if clima == 'sol' and tipo_pneu == 'chuva':
    desgaste = durabilidade - (voltas*15)
elif clima == 'chuva' and tipo_pneu != 'chuva':
    desgaste = durabilidade - (voltas*15)

# 3
elif clima == 'sol' and (dificuldade == 'baixa' or dificuldade == 'média') and (tipo_pneu == 'macio' or tipo_pneu == 'médio'):
    desgaste = durabilidade - (voltas*2)
# 4
elif clima == 'sol' and dificuldade == 'alta' and tipo_pneu == 'macio':
    desgaste = durabilidade - (voltas*3)
# 5
elif clima == 'sol' and dificuldade == 'alta' and tipo_pneu == 'duro':
    desgaste = durabilidade - voltas
# 6
elif clima == 'chuva' and dificuldade == 'baixa' and tipo_pneu == 'chuva':
    desgaste = durabilidade - voltas
elif clima == 'chuva' and dificuldade == 'média' and tipo_pneu == 'chuva':
    desgaste = durabilidade - (voltas*2)
elif clima == 'chuva' and dificuldade == 'alta' and tipo_pneu == 'chuva':
    desgaste = durabilidade - (voltas*3)

# output
if desgaste >= 20:
    print(f'A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {desgaste}.')
else:
    print(f'Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {desgaste} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.')
