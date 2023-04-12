#PEQUENO JOGUINHO DE ADIVINHAÇÃO

import random #comando para importar a biblioteca ramdom.

numero_secreto = random.randrange(1,101) #classe criada para definir o numero secreto aleatorio e seu range.

numero_de_tentativas = 0 #numero padrão de tentativas.

print('Este é um joguinho simples de advinhação\ndependendo do nivel escolhido você terá:\n20, 10 ou 5 chances para acertar o numero secreto')
print('Agora escolha um nivel')
print('1- fácil, 2- médio, 3- difícil')
nivel= int(input('Digite o nivel desejado: ')) #linha de comando para definir o numero de tentativas ou nivel de dificuldade.

if nivel == 1 :
    numero_de_tentativas = 20
elif nivel == 2 :
    numero_de_tentativas = 10
elif nivel == 3 :
    numero_de_tentativas = 5
else :
    print('digite somente 1, 2 ou 3')
    
for rodada in range(1, numero_de_tentativas, +1): #comando para definir a rodada do jogo e contar o numero de tentativas disponiveis.

    print(f'rodada {rodada} de {numero_de_tentativas}') #mostra o numero da rodada ou quantas chances faltam.

    valor_escolhido_srt = input('Digite um numero entre 1 e 100: ')
    valor = int(valor_escolhido_srt) #comando para converter str em int.

    if valor <1 or valor >100 :
        print('Valor incorreto')
        continue

    acertou = valor == numero_secreto
    maior = valor > numero_secreto
    menor = valor < numero_secreto
    #acertou, maior e menor servem para definir se o valor é correto, maior ou menor. além de reduzir o tamanho da linha de comando.
    
    if acertou :
        print('Parabéns! você acertou o número secreto')
        break
    elif maior :
        print('Infelizmente você não acertou, o número secreto é menor que o número informado')
    elif menor :
        print('Infelizmente você não acertou, o número secreto é maior que o número informado')
        
print(f'o número secreto é {numero_secreto}')
print('Fim de jogo')