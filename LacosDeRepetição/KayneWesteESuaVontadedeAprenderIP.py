'''Problem Statement

Após uma carreira musical de sucesso com muitos shows ao redor do mundo e músicas em alta, Kanye West decide finalmente em seguir seu sonho e carreira que tanto queria em toda sua vida: se mudar para Recife e ser aluno do CIn para aprender IP no GRAD 5!

Após várias tentativas de entrada, o músico e agora novo programador em formação entra no CIn e não vê a hora de começar seus estudos.



Para se sair bem na disciplina, Kanye precisa de sua ajuda, grandioso(a) aluno(a) de IP!

Você precisará informar quais decisões o cantor e futuro programador deve (e não deve) tomar em relações às boas práticas de programação e de estudo da disciplina para que seja um ótimo aluno, assim como você.

As boas práticas levadas em consideração são:

Programar utilizando uma boa IDE —> 3 pontos
Códigos limpos e organizados —> 10 pontos
Nomenclatura objetiva e de fácil identificação de variáveis —> 7 pontos
Assistir às aulas do REDU —> 10 pontos
Comentários significativos —> 5 pontos
Evitar repetições desnecessárias de códigos —> 5 pontos
Tirar dúvidas com os monitores e professores —> 10 pontos
As más práticas levadas em consideração são:

Programar sem utilizar IDE —> -5 pontos
Código bagunçado e mal estruturado —> -6 pontos
Nomenclatura confusa e difícil de identificar variáveis —> - 5 pontos
Não tirar dúvidas com professores e monitores —> -10 pontos
Input

Serão n decisões que gerarão pontos que vão prever o desempenho do ilustre novo aluno na disciplina.

Portanto, a primeira linha de entrada será um número inteiro que vai identificar a quantidade de boas práticas a serem medidas:

n

As seguintes n linhas de entrada serão as práticas de programação (podendo ser boas ou más) levadas em consideração que deixarão Kanye um mestre em IP:

boa_pratica_1

boa_pratica_2

…

boa_pratica_n

Output

Por fim deve-se fazer uma média aritmética da pontuação obtida com as práticas de programação recebidas e apresentar as seguintes mensagens:

OBS: Se a soma das pontuações for negativa, atribuir 0 à pontuação total.

OBS: Se .o número de n linhas for zero, deve-se considerar que a média de Kayne foi zero.

OBS: Se a média for acima de 10, atribuir 10 à media. Faça isso depois de extrair a média aritmética.

Caso a media seja menor que 3, apresentar na tela:

‘É melhor voltar a cantar mesmo!’

Caso a media seja maior ou igual a 3 e menor que 7, apresentar na tela:

‘Vai precisar se esforçar um pouco mais, meu cantor!’

Caso a media seja igual a 7, apresentar na tela:

‘Na conta certa!’

Caso a media seja acima de 7 e menor ou igual a 9, apresentar na tela:

‘Nasceu para programar!’

Caso a media seja acima de 9, apresentar na tela:

‘Já pode ser chamado de Kanye, the dev, West!’ '''

#código
quantidade_de_praticas = int(input())
pontuacao = 0
media = 0

for x in range(quantidade_de_praticas):
    praticas = input('')
    if praticas == 'Programar utilizando uma boa IDE':
        pontuacao += 3
    elif praticas == 'Códigos limpos e organizados':
        pontuacao += 10
    elif praticas == 'Nomenclatura objetiva e de fácil identificação de variáveis':
        pontuacao += 7
    elif praticas == 'Assistir às aulas do REDU':
        pontuacao += 10
    elif praticas == 'Comentários significativos':
        pontuacao += 5
    elif praticas == 'Evitar repetições desnecessárias de códigos':
        pontuacao += 5
    elif praticas == 'Tirar dúvidas com os monitores e professores':
        pontuacao += 10
    elif praticas == 'Programar sem utilizar IDE':
        pontuacao -= 5
    elif praticas == 'Código bagunçado e mal estruturado':
        pontuacao -= 6
    elif praticas == 'Nomenclatura confusa e difícil de identificar variáveis':
        pontuacao -= 5
    elif praticas == 'Não tirar dúvidas com professores e monitores':
        pontuacao -= 10

#media simples
if quantidade_de_praticas != 0:
    media = pontuacao/quantidade_de_praticas

#condicional media
if media < 0 :
    media = 0
elif quantidade_de_praticas == 0 :
    media = 0
elif media > 10:
    media == 10

#condicional de impressao
if media < 3 :
    print('É melhor voltar a cantar mesmo!')
elif media >= 3 and media < 7:
    print('Vai precisar se esforçar um pouco mais, meu cantor!')
elif media == 7 :
    print('Na conta certa!')
elif media > 7 and media <= 9:
    print('Nasceu para programar!')
elif media > 9:
    print('Já pode ser chamado de Kanye, the dev, West!')
    
