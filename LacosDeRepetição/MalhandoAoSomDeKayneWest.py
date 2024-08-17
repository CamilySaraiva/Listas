'''Problem Statement

O padre Marcelo Rossi, para terminar seu dia de treino na academia, precisa de músicas que lhe façam ficar motivado e inspirado para puxar pesos, e, infelizmente, o padre cansou de malhar ouvindo sua playlist ”GOSPEL HITS GYM 2023 🏋️‍♀️”. Então, por indicação de alguns amigos começou a ouvir as músicas do cantor Kanye West para ajudar no desenvolvimento do seu shape.


O padre só consegue terminar seu treino se as músicas ouvidas durante o treino lhe motivem a puxar os pesos, por isso, para não perder tempo, Marcelo Rossi chamou você, aluno do CIN, para ajudá-lo nessa saga e acompanhá-lo nesta busca pelo shape sagrado 🙏. Seu desafio será acompanhar o Padre Marcelo em seu treino e verificar se o padre consegue concluí-lo ao som das músicas de Kanye West, ao mesmo tempo que verifica a eficácia das musicas durante seus treinos.


Input

A primeira entrada do seu código será um número inteiro N, que indicará a quantidade de exercícios que serão analisados em cada um dos treinos realizados por padre Marcelo.

quantidade_exercicios

OBS.: A quantidade de exercícios por treino será a mesma para TODOS os treinos e padre Marcelo irá ouvir UMA música por exercício.

Padre Marcelo pode realizar diversos treinos em um só dia. Então, em um dia você irá receber X strings, cada uma ao início de cada treino. Essas strings poderão ser "TREINO DE PERNA DEUS DAI ME FORCAS", "TREINO DE COSTAS FE EM DEUS QUE VAI" ou "TREINO DE PEITO AMEM SENHOR", indicando o tipo de treino que ele irá realizar ou a string "Fim do Treino", indicando o momento de finalizar o dia de treinos.

tipo_treino

Em seguida, para cada treino que padre Marcelo fizer, serão recebidas as N músicas de Kanye West que padre Marcelo está ouvindo naquele treino.

As músicas já passaram por uma análise técnica de especialistas do CIN e já foram classificadas com notas para cada uma delas em relação ao ritmo para academia. 😎

No input, após receber o nome da música, em seguida virá a sua nota.

nome_musica1

nota_musica1

nome_musica2

nota_musica2

...

nome_musicaN

nota_musicaN

OBS.2: Todas as músicas vão ter notas com números inteiros.

OBS.3: Está proibido o uso do break para resolução dessa questão.

Output

Inicialmente, deve ser printado o tipo do treino sendo realizado no momento, da mesma forma que foi recebido no input:

“{tipo_treino}”

Em seguida, para cada um dos exercícios realizados naquele treino, deverá ser exibida a música sendo ouvida naquele exercício junto com a contagem indicando se é a primeira música, segunda, etc, da seguinte forma:

“{contagem_musicas}° música {nome_musica} tocando agora”

Onde {contagem_musicas} será um número inteiro de 1 a N.

Após isso, caso a nota recebida para a música seja igual ou maior do que 7, deve ser printado a seguinte mensagem:

“O padre Marcelo está inspirado, conseguiu finalizar suas séries!”

Caso a nota seja menor do que 7, deve ser printado a seguinte mensagem:

“O padre Marcelo está desanimado, não conseguiu finalizar suas séries”

Por fim, sempre ao final de cada treino deverá ser feita uma verificação da eficácia das N músicas. Caso o número de músicas avaliadas com notas >= 7 seja maior ou igual a metade da quantidade N de músicas, a seguinte mensagem deverá ser exibida:

“ME DEI BEM COM ESSA PLAYLIST, APROVADO”

Caso o número de músicas com notas >= 7 seja menor que a metade da quantidade N de músicas, deve ser exibido a seguinte mensagem:

“NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL”

OBS.4: Para números ímpares, temos que considerar um número maior que a metade deles por exemplo: n = 7 músicas, necessita de 4 músicas que passaram no teste para exibir: "ME DEI BEM COM ESSA PLAYLIST, APROVADO" , enquanto necessita de 3 músicas que passaram no teste exibir: "NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL"'''

#código
quatidade_exercicio = int(input())

# inicializando variaveis
treino = True


while treino:
    tipo_treino = input()

    # se for fim de treino
    if tipo_treino == 'Fim do Treino':
        treino = False

    else:

        print(f'{tipo_treino}')
        # loop musica e nota

        contagem_musica = 0
        eficacia_maior7 = 0
        eficacia_menor7 = 0 

        for i in range(quatidade_exercicio):
            musica = input()
            nota = int(input())
            contagem_musica += 1

            
            print(f'{contagem_musica}° música {musica} tocando agora')

            if nota >= 7:
                eficacia_maior7 += 1
                print('O padre Marcelo está inspirado, conseguiu finalizar suas séries!')
            else:
                eficacia_menor7 += 1
                print('O padre Marcelo está desanimado, não conseguiu finalizar suas séries')

        # eficacia
        if eficacia_maior7 >= eficacia_menor7:
            print('ME DEI BEM COM ESSA PLAYLIST, APROVADO')
        else:
            print('NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL')




