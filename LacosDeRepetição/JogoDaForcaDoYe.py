'''Problem Statement

O Kanye West estava trabalhando em seus projetos quando de repente surge um enorme interesse em adentrar no mundo da programação!

Com isso, Kanye começa a estudar Python e tem a ideia de criar um jogo da forca com o nome de suas músicas. Mas, devido ao seu trabalho musical, não está tendo tempo suficiente para continuar programando o jogo.

Por isso, Kanye contrata ninguém menos do que você para ajudá-lo a criar o jogo dele!



Kanye deixa bem claro o que você deve fazer no jogo: o usuário deverá receber um número N de músicas famosas do Kanye West. De acordo com o tamanho do nome da música, o usuário possui um número de tentativas igual ao dobro do número de letras da música (sem contar espaços em branco, caso o nome da música possuir mais de uma palavra).

Após isso, o usuário deverá chutar letras até que ele acerte a música misteriosa ou até que a quantidade de chutes acabe.

OBS: inicialmente, você deve atualizar a palavra de modo que a cada letra deverá ter um ‘_’.

Exemplos:
Se a música for STRONGER, inicialmente a resposta do usuário será ________ (8 underlines) caso o usuário erre o chute

Se a música for I WONDER, inicialmente a resposta do usuário será _ ______ (7 underlines totais) caso o usuário erre o chute

Toda vez que o usuário acertar um chute, a letra do chute deverá ser atualizada na sua resposta.

Exemplo:
Se a música era STRONGER e o chute foi O, então a resposta do usuário vai ser atualizada de ________ para ___ O____

Se a música for HEARTLESS e o chute foi S, então a resposta do usuário vai ser atualizada de _________ para _______SS

Ao final do código, deverá ser calculada uma taxa de acertos das músicas acertadas pelo usuário em relação ao total de músicas.

OBS:

Não é permitido usar break no código;
Todos os inputs dos nomes de música virão com as letras maiúsculas, bem como os inputs dos chutes.
Input

A primeira entrada do código deverá ser um número inteiro N que representa o número de músicas que o usuário deve descobrir.

Exemplo:

2

Após isso, serão recebidas N entradas contendo nomes de músicas (strings) do Kanye West.

Exemplos:

FLASHING LIGHTS

STRONGER

A cada entrada de música serão recebidas entradas de chutes, que são letras.

Exemplos:

A

B

Output

A primeira saída deverá ser printada sempre no começo:

Bem vindo ao jogo da forca do ye!

Após isso, cada vez que receber uma entrada de música, printe qual sua ‘posição’ em relação às outras músicas e em relação ao total de músicas:

Caso ela não seja a última música, printe:
Esta é a música {musica_atual} de {numero_de_musicas}.

Caso contrário, printe:
Última música!

Se o usuário chutar uma letra que não está no nome da música, printe:

Eita! Parece que a letra {chute} não está na música secreta!

Caso contrário:

Se o usuário chutou uma letra e ele ainda não havia acertado, printe:
Uhuuuuu! Consegui adivinhar uma letra!

Se o usuário chutou uma letra que ele já havia acertado, printe:
Já tinha colocado essa letra antes, preciso de mais atenção.

Para cada chute, independente de ser um chute certo ou errado, o programa deverá printar a situação atual da resposta do usuário:

Resposta atual: {minha_resposta}

Se o usuário conseguiu acertar a música antes que a quantidade de tentativas chegasse à zero, printe:

Isso! Consegui acertar uma música!

Caso contrário, printe:

Vish, essa tava difícil, a música era {nome_musica}. Espero acertar a próxima!

Após a quantidade de músicas acabarem, o programa deve printar quantas músicas o usuário acertou em relação ao número total de músicas:

Consegui acertar {total_de_pontos} músicas de {numero_de_musicas}!

Logo após, printe de acordo com à taxa de acertos do usuário:

Se a taxa de acertos for inferior ou igual à 50%, printe:
Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!

Se a taxa de acertos for superior à 50% e inferior ou igual à 75%, printe:
Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.

Se a taxa de acertos for superior à 75% e inferior à 100%, printe:
Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.

Se a taxa de acertos for 100%, printe:
Eu sou o próprio Kanye West.'''

#código

quant_musica = int(input())
tentativas = ''
acertos = 0

print('Bem vindo ao jogo da forca do ye!')

for i in range(quant_musica):

    if quant_musica > 1 and i + 1 != quant_musica:
        print(f'Esta é a música {i+1} de {quant_musica}.')

    else:
        print('Última música!')

    # musica
    musica = input('').upper()

    # tentaticas
    chances = (len(musica) - musica.count(' '))*2
    chance_atual = 0
    tentativas = ''

    for i in musica:
        if i != ' ':
            tentativas += '_'
        else:
            tentativas += ' '

    while (tentativas != musica) and (chance_atual != chances):
        chance_atual += 1
        letra = input().upper()
        acerto = False
        str_index = 0

        # ver se acertou a letra
        if tentativas.find(letra) != -1:
            print('Já tinha colocado essa letra antes, preciso de mais atenção.')
        elif letra not in musica:
            print(f'Eita! Parece que a letra {letra} não está na música secreta!')
        else:
            print('Uhuuuuu! Consegui adivinhar uma letra!')

            for i in musica:
                if i == letra:
                    tentativas = tentativas[:str_index] + letra + tentativas[str_index + 1:]
                    acerto = True
                str_index += 1

        print(f'Resposta atual: {tentativas}')

        if tentativas == musica:
            print('Isso! Consegui acertar uma música!')
            acertos += 1
        elif chance_atual == chances:
            print(f'Vish, essa tava difícil, a música era {musica}. Espero acertar a próxima!')

# output Pontuação
print(f"Consegui acertar {acertos} músicas de {quant_musica}!")

if (acertos/quant_musica) * 100 <= 50:
    print('Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!')
elif (acertos/quant_musica) * 100 > 50 and (acertos/quant_musica) * 100 <= 75:
    print('Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.')
elif (acertos/quant_musica) * 100 > 75 and (acertos/quant_musica) * 100 < 100:
    print('Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.')
elif (acertos/quant_musica) * 100 == 100:
    print('Eu sou o próprio Kanye West.')
