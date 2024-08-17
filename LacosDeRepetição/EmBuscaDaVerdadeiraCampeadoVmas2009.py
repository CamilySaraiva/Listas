'''Problem Statement

Aldo, um aluno apaixonado por música pop do Centro de Informática da UFPE, teve uma ideia brilhante: realizar um evento para os fãs de divas pop assistirem juntos ao grandioso Video Music Awards de 2009, um verdadeiro clássico da época dourada da música. No entanto, o que era para ser uma noite de celebração tornou-se palco de intensos debates devido ao famoso incidente entre Kanye West e Taylor Swift naquela noite.

Enquanto todos estavam imersos na emoção do evento, uma discussão acalorada aconteceu quando Kanye West interrompeu o discurso de Taylor Swift, declarando que ela não merecia o prêmio de Melhor Vídeo Musical Feminino, e sim a Beyoncé. Esse momento foi o palco de uma das maiores polêmicas da história do VMA.



Aldo percebeu que seus colegas estavam divididos entre os dois lados da questão: alguns defendiam fervorosamente a elegância e talento de Taylor Swift com "You Belong with Me", enquanto outros não conseguiam negar o poder e o impacto de Beyoncé com "Single Ladies".

Para resolver esse impasse, Aldo criou um algoritmo simples, porém eficaz, que permitia aos presentes no evento do Centro de Informática decidirem de uma vez por todas quem merecia o cobiçado prêmio. Mas claro, havia algumas regras:

Cada aluno presente no evento terá a oportunidade de expressar sua opinião.
O algoritmo deve ser imparcial e considerar igualmente todas as opiniões.
O resultado final será baseado na opinião da maioria dos presentes, mas uma reviravolta pode ocorrer.
Se houver um empate, haverá uma rodada de debate onde os alunos podem tentar convencer os outros a mudar de voto.
Após o debate, uma nova votação será realizada e os votos são acumulativos.
Se ainda houver empate após o debate, o organizador (Aldo) terá o voto decisivo.
Input

Inicialmente, você recebera a quantidade de alunos no evento:

quantidade_alunos

Em seguida, você receberá o voto de cada aluno:

"beyonce"

ou

"taylor swift"


Em caso de empate, você receberá de cada aluno na mesma ordem se ele quer mudar de voto ou não após o debate:

"sim"

ou

"nao"

Caso o aluno opte por mudar de voto, você deve receber o novo voto dele após o debate:

novo_voto

Lembrete: os votos que mudarem serão acrescentados aos anteriores


Por fim, se a votação continuar empatada após debate, você receberá o voto decisivo de Aldo:

voto_decisivo

Output

Você precisa imprimir em quem cada aluno votou na primeira votação:

"Aluno {X} votou na Taylor Swift."

ou

"Aluno {X} votou na Beyoncé."

X é o número do aluno que vai de 1 até quantidade_alunos

Após receber todos os votos da primeira seção, imprima a contagem de votos:

"Contagem de votos:"

"Taylor Swift: {qtd_votos_taylor} votos"

"Beyoncé: {qtd_votos_beyonce} votos"


Em caso de empate, você deve imprimir na fase de debate:

"Empate! Iniciando rodada de debate."

"Alunos, agora é a sua chance de convencer os outros a mudar de voto!"

Caso o aluno mude o voto na fase de debate, você deve imprimir:

"Aluno {X} mudou seu voto para Taylor Swift."

ou

"Aluno {X} mudou seu voto para Beyoncé."

Se ocorrer do aluno não mudar o voto após debate, imprima:

"Aluno {X} não mudou seu voto."

Após coletar os novos votos, imprima:

"Nova contagem de votos após o debate:"

"Taylor Swift: {qtd_votos_taylor} votos"

"Beyoncé: {qtd_votos_beyonce} votos"


Se houver uma campeã após a primeira contagem ou após a contagem com os novos votos, imprima as seguintes frases:

"Beyoncé venceu com {qtd_votos_beyonce} votos! Será que Kanye West estava certo?"

ou

"Taylor Swift venceu com {qtd_votos_taylor} votos! Kanye West tá irritado com isso."


Se o empate continuar após o debate, você imprime:

"Aldo, como presidente do evento, tem o voto decisivo."

Por fim, após o voto decisivo, você imprime a campeã:

"Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso."

ou

"Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?"'''

#código

quantidade_alunos = int(input())
voto_beyonce = 0
voto_taylor = 0
contagem_alunos = 0

for i in range(quantidade_alunos):

    voto = input()

    if voto == 'beyonce':
        voto_beyonce += 1
        contagem_alunos += 1
        print(f'Aluno {contagem_alunos} votou na Beyoncé.')
    else:
        voto_taylor += 1
        contagem_alunos += 1
        print(f'Aluno {contagem_alunos} votou na Taylor Swift.')
print('Contagem de votos:')
print(f'Taylor Swift: {voto_taylor} votos')
print(f'Beyoncé: {voto_beyonce} votos')
   

if voto_beyonce == voto_taylor:
    print('Empate! Iniciando rodada de debate.')
    print('Alunos, agora é a sua chance de convencer os outros a mudar de voto!')

    for x in range(1,quantidade_alunos + 1):
        
        mudanca_voto = input()

        #condicional de mudança de voto
        if (mudanca_voto == 'sim') :

            novo_voto = input()

            if (novo_voto == 'taylor swift'):
                voto_taylor += 1
                print(f'Aluno {x} mudou seu voto para Taylor Swift.')
            elif (novo_voto == 'beyonce'):
                voto_beyonce += 1
                print(f'Aluno {x} mudou seu voto para Beyoncé.')

           
        else:
            print(f'Aluno {x} não mudou seu voto.')

    print('Nova contagem de votos após o debate:')
    print(f'Taylor Swift: {voto_taylor} votos')
    print(f'Beyoncé: {voto_beyonce} votos')

#output
if voto_beyonce > voto_taylor:
    print(f'Beyoncé venceu com {voto_beyonce} votos! Será que Kanye West estava certo?')
elif voto_taylor > voto_beyonce:
    print(f'Taylor Swift venceu com {voto_taylor} votos! Kanye West tá irritado com isso.')
else:
    print('Aldo, como presidente do evento, tem o voto decisivo.')
    voto_decisivo = input('')
    if voto_decisivo == 'beyonce':
        print('Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?')
        
    else:
        print('Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.')
