'''Problem Statement

Kanye West é um artista renomado, conhecido por suas apresentações impactantes e inovadoras. Sua equipe de produção trabalha incansavelmente para garantir que cada show seja uma experiência inesquecível para seus fãs. Como resultado, Kanye deve chegar ao local do show com antecedência suficiente para passar por todos os preparativos necessários, incluindo checagens de som, revisões de palco e outras necessidades técnicas.

Além disso, Kanye é uma figura pública e enfrenta desafios de segurança e logística, diante desses desafios, você deve analisar as três opções de transporte disponíveis para Kanye West, considerando a distância de X km da sua casa até o local do show e fatores externos que podem impactar no tempo da viagem e informar um código de serialização que será utilizado para verificar o transporte e garantir a segurança do cantor.



Opção A - Jato Particular: Kanye será transportado em carros blindados até o aeroporto, viajará de jato particular, e depois seguirá em carros blindados até o destino final.
Trajeto: Local de saída → carro → jato → carro → Local do Show
O tempo total de viagem para essa opção é determinado pela soma dos tempos médio para percorrer x km em cada parte do trajeto mais os possíveis atrasos no trânsito
Considere que o jato particular percorre 80% da distância total
O jato percorre 1089 km em 1 hora e os carros blindados 60 km em 1 hora (sem considerar o trânsito)
Opção B - Seu ônibus personalizado: Kanye pode viajar diretamente ao destino com sua equipe em um ônibus personalizado.
Trajeto: Local de saída → ônibus → Local do Show
O tempo total de viagem para essa opção é determinado pelo tempo médio para percorrer x km de ônibus mais os possíveis atrasos no trânsito
O ônibus percorre 40 km em 1 hora (sem considerar o trânsito)
Opção C - Helicóptero: Kanye pode usar um helicóptero para se transportar diretamente de sua casa ao destino.
Trajeto: Local de saída → Helicóptero → Local do Show → Helicóptero → Local de saída
Local de saída → Helicóptero → Local do Show → Helicóptero → Local de saída
Local de saída → Helicóptero → Local do Show
O tempo total de viagem dessa opção será 5x o tempo médio gasto do local de saída até o show, já que será preciso fazer 3 viagens de idas e 2 de voltas para transportar toda sua equipe e equipamentos
Essa opção não será afetada pelo trânsito
O helicóptero consegue percorrer 60 km em 10 minutos
Para calcular o tempo de atraso no trânsito, considere que:

O tempo de viagem no trânsito aumenta em 36 segundos para cada veículo adicional no trânsito.
Se houver um acidente, o tempo de viagem é aumentado em 20 minutos para usar um atalho.
Para transformar o código de serialização no código válido para verificar a veracidade do veículo, considere que:

O código apenas irá comportar números, e poderá ser de qualquer tamanho.
Caso determinado dígito do código seja par, acrescente na string final de deserialização o dígito sendo analisado e concatenado à string “23”
Caso determinado dígito do código seja impar, acrescente na string final de deserialização o dígito sendo analisado e concatenado à string “78”
Exemplo: Caso o código inválido seja "1234", o código final desserializado será "178223378423".

Algumas considerações finais:

Considere que: Velocidade Média = Distância / Tempo
Para exibir números do tipo float, considere apenas 1 casa decimal.
IMPORTANTE!!: Vocês deverão utilizar a biblioteca decimal do Python com a precisão de 15 casas decimais,
nesse link
você encontra algumas informações sobre para quê serve e como usar essa biblioteca.

OBS: Atentar-se à mensagem no Discord, contém instruções simplificadas para aplicar a biblioteca no contexto da questão.

Input

Você recebe as seguintes entradas:

Um inteiro referente a quantos veículos estão no trânsito atualmente:
quantidade_veiculos

Uma string, podendo ser "sim" ou "nao", informando se houve algum acidente no trânsito:
acidente_info

Um número decimal referente à distância total que deve ser percorrida até o local do show:
distancia_total

Uma string com o código de serialização inválido:
codigo_serializacao

Output

Inicialmente, o programa deverá exibir a seguinte mensagem:

"Análise das opções de transporte até o show!"

Em seguida, deverá ser mostrado em quanto tempo, em minutos, Kayne e sua equipe chegarão ao local do show considerando cada uma das opções:

"Opção {opcao_analisada} - Você chegará ao show em {tempo_necessario} minutos"

Obs.: tempo_necessario é dado com uma casa após a vírgula, para pegar a primeira casa decimal use :.1f

Obs.: opcao_analisada será uma das strings "A", "B" ou "C".

Por fim, o programa deverá revelar o código de serialização transformado:

"---"

"Senha de serialização transformada: {codigo_desserializado}, guarde com segurança!"'''


#código

from decimal import Decimal, getcontext
getcontext().prec = 15

# inputs

quantidade_veiculos = int(input())
acidente_info = input()
distacia_total = Decimal(input())
codigo_serializacao = input()

print('Análise das opções de transporte até o show!')

# opcao A
tempo_jato = (distacia_total * Decimal(0.8) / Decimal(1089)) * Decimal(60)

tempo_carro = ((distacia_total * Decimal(0.2) / Decimal(60)) * Decimal(60))

# tempo total s/ transito e acidente
tempo_total_a = tempo_jato + tempo_carro

# tempo_transito a
tempo_transito_a = (Decimal(quantidade_veiculos * 36) / 60)

# caso houver acidente
if acidente_info == 'sim':
    tempo_transito_a += Decimal(20)

# tempo total da opcao A
tempo_total_a += tempo_transito_a
print(f'Opção A - Você chegará ao show em {tempo_total_a:.1f} minutos')


# opcao B

tempo_onibus = (distacia_total / Decimal(40)) * Decimal(60)

# tempo total onibus s/ acidentes ou transito
tempo_total_b = tempo_onibus

# tempo de transito B
tempo_transito_b = (Decimal(quantidade_veiculos * 36) / 60)

if acidente_info == 'sim':
    tempo_transito_b += Decimal(20)

# tempo total opcao b
tempo_total_b += tempo_transito_b
print(f'Opção B - Você chegará ao show em {tempo_total_b:.1f} minutos')


# OPCAO C
tempo_helicoptero = (distacia_total / Decimal(60)) * Decimal(10)

# tempo total helicoptero considerando 5 viagens
tempo_total_c = tempo_helicoptero * Decimal(5)
print(f'Opção C - Você chegará ao show em {tempo_total_c:.1f} minutos')

# codigo de serialização
codigo_transformado = ''
for digito in codigo_serializacao:
    if int(digito) % 2 == 0:
        codigo_transformado += digito + '23'
    else:
        codigo_transformado += digito + '78'
print('---')
print(f'Senha de serialização transformada: {codigo_transformado}, guarde com segurança!')
