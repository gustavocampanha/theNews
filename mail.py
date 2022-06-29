from random import randint
from time import sleep

def interface():

    print('-='*60)
    sleep(0.1)
    print('\033[32m{:^120}\033[m'.format('Bem Vindo ao Criador de E-Mails'))
    sleep(0.1)

    mails = list()

    senha = 'senha123.'

    nomes = [
            'betina',
            'valentina',
            'olivia',
            'martina',
            'alice',
            'laura',
            'manuela',
            'sophia',
            'isabella',
            'madalena',
            'luiza',
            'julia',
            'greta',
            'marialuiza',
            'cecilia',
            'eloa',
            'giovanna',
            'beatriz',
            'helena',
            'sara',
            'zoe',
            'iris',
            'maya',
            'jade',
            'emilia',
            'leonor',
            'alba',
            'louise',
            'eva',
            'naomi',
            'olga',
            'ayla',
            'mariaalice',
            'heloisa',
            'mariaclara',
            'mariacecilia',
            'maite',
            'eliza',
            'lorena',
            'livia',
            'antonella',
            'kayra',
            'zaya',
            'rayka',
            'ava',
            'vicky',
            'harper',
            'emma',
            'kesia',
            'liz',
            'charlotte',
            'gael',
            'miguel',
            'arthur',
            'valentim',
            'ben',
            'davi',
            'lorenzo',
            'noah',
            'heitor',
            'theo',
            'joaomiguel',
            'bento',
            'isaac',
            'anthony',
            'rayan',
            'pedrohenrique',
            'gabriel',
            'pedro',
            'benjamim',
            'matheus',
            'santiago',
            'henrique',
            'nicolas',
            'joaquim',
            'samuel',
            'afonso',
            'rafael',
            'guilherme',
            'enzo',
            'murilo',
            'teo',
            'luan',
            'levi',
            'george',
            'hugo',
            'anton',
            'francisco',
            'elias',
            'bernardo',
            'simao',
            'oscar',
            'benicio',
            'caleb',
            'ethan',
            'rael',
            'zion',
            'otto',
            'ravi',
            'kalel',
            'yuri',
            'vicente'
        ]

    sobrenomes = [
            'almeida',
            'alves',
            'andrade',
            'barbosa',
            'barros',
            'batista',
            'borges',
            'campos',
            'cardoso',
            'carvalho',
            'castro',
            'costa',
            'dias',
            'duarte',
            'freitas',
            'fernandes',
            'ferreira',
            'garcia',
            'gomes',
            'goncalves',
            'lima',
            'lopes',
            'machado',
            'marques',
            'martins',
            'medeiros',
            'melo',
            'mendes',
            'miranda',
            'monteiro',
            'moraes',
            'moreira',
            'moura',
            'nascimento',
            'nunes',
            'oliveira',
            'pereira',
            'ramos',
            'reis',
            'ribeiro',
            'rocha',
            'santana',
            'santos',
            'silva',
            'soares',
            'souza',
            'teixeira',
            'vieira',
        ]

    while True:
            sleep(0.2)
            print('-='*60)
            sleep(0.2)
            print("""
        [ 1 ] Criar E-Mail
        [ 2 ] Sair
                """)
            sleep(0.2)
            print('-='*60)
            sleep(0.2)

            escolha = input('\nEscolha sua opção: ').strip() 

            if escolha == '1':

                quant = int(input('Quantidade de emails: '))

                for a in range(0, quant):

                    a = randint(0, len(nomes)-1)
                    b = randint(0, len(sobrenomes)-1)
                    m = str(randint(0,9))
                    y = str(randint(0,9))

                    mail = nomes[a]+m+y+sobrenomes[b]+m+y

                    conta = [mail, senha]

                    mails.append(conta)

                break

            elif escolha == '2':
                break

            else:

                sleep(0.2)
                print("\n\033[31mPor favor, escolha uma opção válida!\033[m")

    return mails