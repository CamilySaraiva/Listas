'''Problem Statement

Kanye West para presidente.

No ano de 2020, o rapper norte-americano Kanye West se candidatou à presidência dos Estados Unidos, evento que, posteriormente, se consagrou como um "meme" no meio da cultura pop, uma vez que era evidente que o cantor não tinha chances reais de ganhar. Porém, agora em 2024, ao lançar mais um álbum repleto de hits e tentar promover-se como o maior artista de todos os tempos, ele provocou uma ruptura na realidade como a conhecemos, dando origem ao multiverso. Em um dos universos existentes, Kanye, desta vez, possuía chances reais de se tornar o próximo presidente dos Estados Unidos. Assim, para computar os votos das eleições americanas que estão por vir nesse mundo paralelo, a Casa Branca contratou você, estudante do CIn.

Contudo, o sistema eleitoral nos EUA é diferente do que estamos habituados. Para ser eleito, o fator determinante não é, necessariamente, o número de votos, mas sim o maior número de delegados (se necessário, pode pensar neles como um tipo de pontuação). Cada estado norte-americano, baseado no tamanho da sua população, detém um determinado contingente de delegados, de forma que, quando um candidato conquista a maioria dos votos na região, ele leva para si o voto de todos os respectivos delegados. Ao final do pleito, quem obtiver um número maior de delegados é eleito presidente. A título de curiosidade, caso ainda haja alguma dúvida sobre esse sistema, clique
aqui
para assistir um breve vídeo explicativo de como funcionam as eleições dos EUA.

Input

Inicialmente, você deverá receber duas linhas de entrada, cada uma contendo o nome de um dos principais candidatos às eleições presidenciais.

candidato_1

candidato_2

Em seguida. receberá, por um número indefinido de vezes, o nome de um estado norte-americano (devido ao fenômeno do multiverso, a identificação dos estados e a quantidade deles podem diferir de como os conhecemos), e o número de delegados associados a ele, separados por vírgula e espaço, no seguinte formato:

{estado}, {num_delegados}

Dica: use a função split() para registrar cada informação separadamente

Nas linhas seguintes, serão dados a quantidade de votos populares que cada um dos candidatos recebeu, respectivamente.

votos_candidato1 (int)

votos_candidato2 (int)

Porém, Taylor Swift pode ter inveja do sucesso de Kanye West e tentar boicotar as eleições, roubando as urnas de um determinado estado, o que será indicado pela seguinte entrada (em substituição a algum dos inteiros que representaria a quantidade de votos de um candidato):

Taylor Swift roubou as urnas!

Nesse caso, os votos já computados até o momento no respectivo estado deverão ser anulados, sendo reiniciada a votação logo em seguida. Ou seja, o passo anterior, em que são registrados o número de votos de cada candidato, deve ser imediatamente retomado para o mesmo estado em que houve o roubo das urnas.

OBS.1: O roubo das urnas ocorrerá somente em cenários em que Kanye West está participando da eleição.

OBS.2: A entrada que indica o roubo das urnas pode ser recebida diversas vezes, sendo finalizada a votação do respectivo estado apenas quando os votos de ambos os candidatos forem registrados com sucesso.

O programa deverá continuar recebendo entradas associadas às eleições de um determinado estado (nome e quantidade de delegados), bem como a respectiva sequência de entradas contendo o número de votos dos candidatos e/ou o indicativo de roubo das urnas, até que o programa seja encerrado após a leitura da seguinte entrada:

FIM

OBS.3: Note que a entrada FIM será recebida no momento em que um eventual novo estado seria registrado, ou seja, logo após o fim da votação do estado imediatamente anterior.

Output

Inicialmente, caso nenhum dos dois principais candidatos registrados seja Kanye West, não haverá eleição, sendo encerrado o programa logo após imprimir:

Sem o Ye, sem eleição!


Em relação ao roubo das urnas, para cada vez que Taylor Swift interferir nas eleições, imprima:

A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!


Ao fim da votação em um determinado estado, anuncie o(a) vencedor(a) do pleito:

{vencedor_no_estado} obteve maioria no(a) {estado_x} com {y}% dos votos.

Sendo y o valor inteiro da porcentagem dos votos obtidos pelo(a) candidato(a) vencedor(a) no estado pelo total de votos daquele estado


Ao final das eleições (isto é, tendo sido finalizadas as votações de cada um dos estados), quando todos os votos tiverem sido computados, imprima:

Temos o resultado final! {vencedor} vence a disputa pela presidência, com o apoio de {total_delegados} delegados do colégio eleitoral e {total_votos} votos populares.

ATENÇÃO: O total de votos, nesse caso, diz respeito à soma dos votos populares do candidato vencedor somente nos estados em que ele ganhou as eleições.


Sendo um dos candidatos, caso Kanye West seja o vencedor, também deverá ser mostrado o seu discurso da vitória:

"Everybody wanted to know what I would do if I didn't win... I Guess We'll Never Know."

Por outro lado, se Kanye for derrotado, imprima o seu discurso de consolo:

"Não tem problema, eu obtive o molho!"

Atenção: As aspas que iniciam e terminam as frases dos discursos de Kanye West devem ser incluídas.

Dica: Para evitar conflito entre as aspas dentro do print(), utilize a barra inversa (\) imediatamente antes (à esquerda) de cada aspas simples ou duplas da frase, com exceção das aspas que iniciam e finalizam a string da própria função print().


OBS.4: Sendo extremamente improvável a ocorrência de um empate durante as eleições (estadual ou nacionalmente) em um cenário real, considere que também não haverá qualquer tipo de empate nas eleições nesse universo.'''

#código


candidato_1 = input()
candidato_2 = input()

delegados_candit1 = 0
delegados_candit2 = 0
votospop_cadit1 = 0
votospop_cadit2 = 0

if candidato_1 != 'Kanye West' and candidato_2 != 'Kanye West':
    print('Sem o Ye, sem eleição!')
else: 
    while True:
        info_estados = input()
        if info_estados == 'FIM':
            break

        estado, num_delegados = info_estados.split(', ')
        num_delegados = int(num_delegados)

        while True:
            votos_cadit1 = input()
            if votos_cadit1 == 'Taylor Swift roubou as urnas!':
                print('A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!')
                continue
            elif votos_cadit1 == 'FIM':
                break
             
            votos_cadit1 = int(votos_cadit1)

            votos_cadit2 = input()
            if votos_cadit2 == 'Taylor Swift roubou as urnas!':
                print('A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!')
                continue
            elif votos_cadit2 == 'FIM':
                break
            
            votos_cadit2 = int(votos_cadit2)
            break

        if votos_cadit1 == 'FIM' or votos_cadit2 == 'FIM':
            break

        total_votos = votos_cadit1 + votos_cadit2
        porcentagem_candit1 = int((votos_cadit1/total_votos) * 100)
        porcentagem_candit2 = int((votos_cadit2/total_votos) * 100)
        
        if votos_cadit1 > votos_cadit2:
            vencedor_estado = candidato_1
            delegados_candit1 += num_delegados
            votospop_cadit1 += votos_cadit1
            porcentagem_vencedor = porcentagem_candit1
        else:
            vencedor_estado = candidato_2
            delegados_candit2 += num_delegados
            votospop_cadit2 += votos_cadit2
            porcentagem_vencedor = porcentagem_candit2
        
        print(f'{vencedor_estado} obteve maioria no(a) {estado} com {porcentagem_vencedor}% dos votos.')

if delegados_candit1 > delegados_candit2:
    vencedor_fim = candidato_1
    delegados_vencedor = delegados_candit1
    votospop_vencedor = votospop_cadit1
else:
    vencedor_fim = candidato_2
    delegados_vencedor = delegados_candit2
    votospop_vencedor = votospop_cadit2

if 'Kanye West' in [candidato_1, candidato_2]:
    print(f'Temos o resultado final! {vencedor_fim} vence a disputa pela presidência, com o apoio de {delegados_vencedor} delegados do colégio eleitoral e {votospop_vencedor} votos populares.')    

if vencedor_fim == 'Kanye West':
    print('"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know."')
else:
    if 'Kanye West' in [candidato_1, candidato_2]:
        print('"Não tem problema, eu obtive o molho!"')