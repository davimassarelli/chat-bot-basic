def apresentacao(bot_nome, ano_nascimento):
    print(f'Olá! Meu nome é {bot_nome}.')
    print(f'Eu fui criado em {ano_nascimento}.')


def lembrar_nome():
    print('Por favor, me recorde seu nome.')
    nome = input()
    print(f'Que nome maravilhoso, {nome}!')
    return nome


def adivinha_idade():
    print('Deixe-me adivinhar sua idade.')
    print('Por gentileza, digite o resto da divisão da sua idade por 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    idade = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f'Você tem {idade} anos, acertei?! \nÉ uma ótima idade para começar a programar! Não acha?')


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
    print('''Por que usamos métodos em Python?
          1. Para repetir um teste várias vezes.
          2. Para decompor um programa em várias pequenas subrotinas.
          3. Para determinar o tempo de execução de um programa.
          4. Para interromper a execução de um programa.''')

    num = int(input())
    while num != 2:
        num = int(input('Não é isto. Por favor, tente novamente.\n'))
    else:
        print('Parabéns você acertou, viu como você já está aprendendo programação!\n')


def final(nome):
    print(f'Continue seguindo este caminho {nome}! \n'
          'Acredito que concluí meus procedimentos por aqui, tenha um ótimo dia! ;D \nDESLIGANDO...')


apresentacao('Robotson', '2021')
nome = lembrar_nome()
adivinha_idade()
contagem()
teste()
final(nome)
