#Programa utilizando condicionais e tratamento de erros 

while True:
    try:
        idade = int(input('Qual é a sua idade?: '))
        if idade >=18 : print ('Você é um adulto')
        elif idade >=13 : print ('Você é um adolescente')
        else : print ('Você é uma criança')
        break
    except ValueError:
        print ('Digite somente numeros inteiros')