'''Problem Statement

Kanye West é reconhecido como um dos artistas mais influentes da música contemporânea, com uma carreira que abrange mais de duas décadas. Com uma vasta discografia que abrange uma ampla gama de gêneros, desde o hip-hop até o gospel, sua presença nas plataformas de streaming é marcante, com milhões de ouvintes mensais, superando a casa dos 70M no Spotify.

Com o fim do primeiro trimestre do ano, sua plataforma preferida resolveu fazer uma retrospectiva sobre as streams dos fãs de Kanye West.

Input

Primeiramente você receberá a informação do nome do ouvinte e da quantidade de músicas que ele ouviu

nome_ouvinte

quantidade_musicas

Após isso, a partir da quantidade de músicas, você receberá a informação do nome da música e da quantidade de vezes que aquela música foi ouvida

musica

quantidade_streams

Output

A partir disso, deverá ser analisada qual a música que mais foi ouvida, menos foi ouvida e a quantidade de streams delas.

Caso o ouvinte não ouviu nenhuma música do Kanye, deverá imprimir:
“{nome_ouvinte} é team Taylor e não ouviu Kanye West”

Caso o ouvinte tenha ouvido apenas uma música:
“A única música que {nome_ouvinte} ouviu foi {musica} com {numero_de_ streams} streams”

Caso o ouvinte tenha ouvido mais de uma música:
“A música que {nome_ouvinte} mais ouviu foi {musica} com {numero_de_streams} streams”

”A música que {nome_ouvinte} menos ouviu foi {musica} com {numero_de_streams} streams'

OBS1: Caso duas ou mais músicas tenham a mesma quantidade de streams, deverá ser considerada a primeira múscia recebida
OBS2: Caso todas as músicas tenham a mesma quantidade de streams, não deverá ser printado a música menos ouvida (pois ela também é a mais ouvida). Então, apenas deverá ser printadoa música com mais streams. '''

#código
nome_ouvinte = str(input())
quantidade_musicas = int(input())

# Inicialização de variáveis
musicaMaior = ''
musicaMenor = ''
maiorStream = 0
menorStream = -1 

# Se o ouvinte não escutou Kanye
if quantidade_musicas == 0:
    print(f'{nome_ouvinte} é team Taylor e não ouviu Kanye West')
else:
    for i in range(quantidade_musicas):
        musica = str(input())
        quantidade_stream = int(input())

        if quantidade_stream > maiorStream:
            musicaMaior = musica
            maiorStream = quantidade_stream

        if menorStream == -1 or quantidade_stream < menorStream:
            musicaMenor = musica
            menorStream = quantidade_stream

    if quantidade_musicas == 1:
        print(f'A única música que {nome_ouvinte} ouviu foi {musicaMaior} com {maiorStream} streams')
    else:
        if maiorStream != menorStream:
            print(f'A música que {nome_ouvinte} mais ouviu foi {musicaMaior} com {maiorStream} streams')
            print(f'A música que {nome_ouvinte} menos ouviu foi {musicaMenor} com {menorStream} streams')
        else:
            print(f'A música que {nome_ouvinte} mais ouviu foi {musicaMaior} com {maiorStream} streams')
