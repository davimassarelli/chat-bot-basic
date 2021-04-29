def apresentacao(bot_nome, ano_nascimento):
    print(f'Olá! Meu nome é {bot_nome}.')
    print(f'Eu fui criado em {ano_nascimento}.')


def lembrar_nome():
    print('Por favor, me recorde seu nome.')
    nome = input()
    print(f'Que nome maravilhoso, {nome}!')


def adivinha_idade():
    print('Deixe-me adivinhar sua idade.')
    print('Por gentileza, digite o resto da divisão da sua idade por 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    idade = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f'Você tem {idade} anos, acertei?! \n É um bom momento para começar a programar! não acha?')


def contagem():
    print('Agora eu vou te provar que consigo contar até o número que você quiser.\n'
          'Por favor, digite um número qualquer.')

    num = int(input())
    atual = 0
    while atual <= num:
        print(atual, '!')
        atual += 1


def teste():
    print('Agora vamos testar seu conhecimento em programação. Pronto?')
    print('''Por que usarmos métodos?
          1. Para repetir um teste várias vezes.
          2. Para decompor um programa em várias pequenas subrotinas.
          3. Para determinar o tempo de execução de um programa.
          4. Para interromper a execução de um programa.''')
    num = int(input())
    while num != 2:
        print('Por favor, tente novamente.')
    else:
        print('Concluído, tenha um ótimo dia!')


def final():
    print('Parabéns, você passou nos testes e eu concluí meus procedimentos tenha um ótimo dia! \nDESLIGANDO...')


apresentacao('Robotson', '2021')  # change it as you need
lembrar_nome()
adivinha_idade()
contagem()
teste()
final()
