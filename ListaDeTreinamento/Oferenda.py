'''Após ficarem impressionados com a mecânica do jogo, Arthur, Luiz e Pedro resolveram continuar jogando. Como Tantan estava muito mais avançado em recursos, eles convidaram Tantan para morar em suas vilas e fizeram ofertas de diamantes para tornar o convite mais interessante. Arthur ofereceu 10 diamantes, Luiz ofereceu 30 e Pedro 100.

Tantan estava precisando de diamantes, porém, sendo um garoto muito humilde, falou que iria aceitar a menor oferta possível que suprisse sua necessidade.

Sua tarefa é fazer um programa que ajude Tantan a decidir com quem ir morar.

Input

D - número natural (1 <= D)
A linha única de entrada é composta pela quantidade de diamantes que Tantan necessita.
Obs: Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.

Output

P - string

A linha única de saída é composta pelo nome de quem fez a oferta que foi aceita por Tantan, ou pela string "Nenhum", no caso em que nenhuma oferta supria a quantidade de diamantes necessária.'''

#código

diamante_tantan = int(input())
dima_arthur = int(10)
dima_luiz = int(30)
dima_pedro = int(100)

if diamante_tantan <= 10 :
    print('Arthur')

elif diamante_tantan > 10 and diamante_tantan <= 30 :
    print('Luiz')

elif diamante_tantan > 30 and diamante_tantan <= 100 :
    print('Pedro')
else:
    print('Nenhum')