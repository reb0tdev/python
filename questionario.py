
while True:
    try:
        nome = input('Qual o seu nome?: ')
        idade = int(input('Qual a sua idade?: '))
        altura = float(input('Qual a sua altura?: '))
        break
    except ValueError:
        print('Dados inválidos, refaça o questionário')
    except NameError:
        print ('Dados inválidos, refaça o questionário')
print(f'Seu nome é {nome}, a sua idade é {idade} e sua altura é {altura}')