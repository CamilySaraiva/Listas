'''Problem Statement

Em uma realidade alternativa em que Ayrton Senna ainda está vivo, os carros da Fórmula 1 são mais do que máquinas de alta velocidade, eles são verdadeiros laboratórios de tecnologia. Equipados com sistemas embutidos em Python, esses automóveis estão prontos para desafiar os limites do possível.

Agora, imagine-se como um dos principais engenheiros de software de Ayrton Senna, navegando nesse mundo onde a tecnologia e a paixão pelo automobilismo se entrelaçam. Senna, confiante em sua habilidade técnica, pede sua ajuda para consertar a calculadora em seu carro. Parece simples, certo? Mas há um pequeno detalhe: você só tem três linhas de código para resolver esse problema.

É como se estivéssemos nos boxes de uma corrida, onde cada segundo conta, e você precisa agir com rapidez e precisão. A pressão está alta, mas a emoção é palpável. Você está prestes a embarcar em uma jornada de engenhosidade e criatividade, onde cada linha de código é uma curva a ser superada, e a vitória está na ponta dos seus dedos.

Prepare-se para desafiar a lógica e aprimorar suas habilidades de programação enquanto trabalha para criar um programa que faça todas as operações básicas de uma calculadora comum, as quais são soma ( + ), subtração ( - ), multiplicação ( * ) e divisão ( / ). Esta é a sua chance de provar que, mesmo em uma realidade alternativa onde Ayrton Senna ainda existe, sua capacidade de resolver problemas é digna de pódio. 🏆


Input

O seu programa receberá três valores:
O primeiro valor será um inteiro x:

x (int)

O segundo valor será um caractere: podendo ser: +, -, * ou /, representando cada um uma funcionalidade da calculadora, entretanto há a possiblidade desse caractere não ser um operador válido para o código;

operador (string)

O terceiro valor será um inteiro y:

y (int)

Output

O output será um valor inteiro caso a operação seja válida, ou seja, caso o valor do operador for +, -, * ou /. Tal output é o resultado da operação entre os outros inputs. Podemos defini-lo apenas como um inteiro z:

resultado = z (int)

Entretanto, caso a operação não seja válida o resultado obrigatoriamente será a frase:

Erro: operador não reconhecido.

Dicas:
Para a resolução dessa questão é necessário saber atribuir valores à multiplas variáveis ao mesmo tempo, portanto deixo este endereço como auxílio:
https://www.w3schools.com/python/python_variables_multiple.asp

Além disso, é necessário ter conhecimento sobre expressões condicionais e, como antes, deixo este endereço como fonte de auxílio:
https://www.w3schools.com/python/python_conditions.asp

Observações:
Em caso de operação de divisão ( / ), o inteiro y nunca será zero e você deverá utilizar o operador // para obter o resultado da divisão inteira.

Além disso, é obrigatório que o código contenha no máximo três linhas e é terminantemente proibido o uso de qualquer biblioteca externa ou outros assuntos além de condicionais e operadores lógicos.'''

#código

valor1, operador, valor2 = int(input()), input(), int(input())
print(valor1 + valor2 if operador == '+' else valor1 - valor2 if operador == '-' else valor1 * valor2 if operador == '*' else valor1 // valor2 if operador == '/' and valor2 != 0 else 'Erro: operador não reconhecido.')
