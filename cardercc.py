import random

while 100:

    vermelho = '\033[1;31m'
    azul = '\033[1;34m'
    verde = '\033[1;32m'
    branco = '\033[1;30m'
    fechar = '\033[m'

    print(branco)
    print('''           v2                             

 ▄████▄   ▄▄▄       ██▀███  ▓█████▄ ▓█████  ██▀███   ▄████▄   ▄████▄  
▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒▒██▀ ▀█  ▒██▀ ▀█  
▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌▒███   ▓██ ░▄█ ▒▒▓█    ▄ ▒▓█    ▄ 
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒
▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ░▒████▒░██▓ ▒██▒▒ ▓███▀ ░▒ ▓███▀ ░
░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░░ ░▒ ▒  ░░ ░▒ ▒  ░
  ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░  ░  ▒     ░  ▒   
░          ░   ▒     ░░   ░  ░ ░  ░    ░     ░░   ░ ░        ░        
░ ░            ░  ░   ░        ░       ░  ░   ░     ░ ░      ░ ░      
░                            ░                      ░        ░        

 Coded  By: Koppy404
 Instagram: koppyyy_               
''')
    print(fechar)
    print(vermelho)
    print('''MENU CARDER:
[1] GERAR BINs
[2] GERAR CPFs
[3] FAZER CC
[4] O QUE ESSE BOTÃO FAZ?
[5] SAIR 
''')
    print(fechar)
    print(branco)
    pergunta = int(input('Opção: '))
    print(fechar)
    print(azul)
    if pergunta == 1:
        print('VOCÊ ESCOLHEU GERADOR DE BINS!')
        print(fechar)
        print(vermelho)
        print('''BINS DE QUANTOS DIGITOS?
[1] 6 DIG
[2] 5 DIG
        ''')
        print(fechar)
        print(branco)
        bin = int(input('ESCOLHA SUA OPÇÃO!:'))

        print(azul)
        if bin == 1:
          print('VOCÊ ESCOLHEU BINs DE 6 DIGITOS / VISA')
          print(fechar)

          print(verde)
          binvisa = random.randint(1, 9999)
          binvisa2 = random.randint(1, 9999)
          binvisa3 = random.randint(1, 9999)
          binvisa4 = random.randint(1, 9999)
          binvisa5 = random.randint(1, 9999)
          binvisa6 = random.randint(1, 9999)
          binvisa7 = random.randint(1, 9999)
          binvisa8 = random.randint(1, 9999)
          binvisa9 = random.randint(1, 9999)
          binvisa10 = random.randint(1, 9999)
          taxa = ['65%','70%','75%','76%','77%','78%','83%','84%','87%','90%','91%']
          txx = random.choice(taxa)
          print('45', binvisa, 'xxxxxxx')
          print('45', binvisa2, 'xxxxxxx')
          print('45', binvisa3, 'xxxxxxx')
          print('45', binvisa4, 'xxxxxxx')
          print('45', binvisa5, 'xxxxxxx')
          print('45', binvisa6, 'xxxxxxx')
          print('45', binvisa7, 'xxxxxxx')
          print('45', binvisa8, 'xxxxxxx')
          print('45', binvisa9, 'xxxxxxx')
          print('45', binvisa10, 'xxxxxxx')
          print('TAXA DE SUCESSO :',txx)
          print(fechar)

        print(azul)
        if bin == 2:
            print('VOCÊ ESCOLHEU BINs DE 5 DIGITOS / VISA')
            print(fechar)
            print(verde)
            binvisax = random.randint(1, 999)
            binvisax2 = random.randint(1, 999)
            binvisax3 = random.randint(1, 999)
            binvisax4 = random.randint(1, 999)
            binvisax5 = random.randint(1, 999)
            binvisax6 = random.randint(1, 999)
            binvisax7 = random.randint(1, 999)
            binvisax8 = random.randint(1, 999)
            binvisax9 = random.randint(1, 999)
            binvisax10 = random.randint(1, 999)
            binvisax11 = random.randint(1, 999)
            binvisax12 = random.randint(1, 999)
            binvisax13 = random.randint(1, 999)
            binvisax14 = random.randint(1, 999)
            binvisax15 = random.randint(1, 999)
            binvisax16 = random.randint(1, 999)
            binvisax17 = random.randint(1, 999)
            binvisax18 = random.randint(1, 999)
            binvisax19 = random.randint(1, 999)
            binvisax20 = random.randint(1, 999)
            taxa2 = ['65%', '70%', '75%', '76%', '77%', '78%', '83%', '84%', '87%', '90%', '91%']
            txx2 = random.choice(taxa2)
            print('45', binvisax, 'xxxxxxxxxxx')
            print('45', binvisax2, 'xxxxxxxxxxx')
            print('45', binvisax3, 'xxxxxxxxxxx')
            print('45', binvisax4, 'xxxxxxxxxxx')
            print('45', binvisax5, 'xxxxxxxxxxx')
            print('45', binvisax6, 'xxxxxxxxxxx')
            print('45', binvisax7, 'xxxxxxxxxxx')
            print('45', binvisax8, 'xxxxxxxxxxx')
            print('45', binvisax9, 'xxxxxxxxxxx')
            print('45', binvisax10, 'xxxxxxxxxxx')
            print('45', binvisax11, 'xxxxxxxxxxx')
            print('45', binvisax12, 'xxxxxxxxxxx')
            print('45', binvisax13, 'xxxxxxxxxxx')
            print('45', binvisax14, 'xxxxxxxxxxx')
            print('45', binvisax15, 'xxxxxxxxxxx')
            print('45', binvisax16, 'xxxxxxxxxxx')
            print('45', binvisax17, 'xxxxxxxxxxx')
            print('45', binvisax18, 'xxxxxxxxxxx')
            print('45', binvisax19, 'xxxxxxxxxxx')
            print('45', binvisax20, 'xxxxxxxxxxx')
            print('TAXA DE SUCESSO :', txx2)
            print(fechar)

    if pergunta == 2:
        print('VOCÊ ESCOLHEU GERAR CPFs')
        print(verde)
        cpf = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf2 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf3 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf4 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf5 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf6 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf7 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf8 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf9 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf10 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf11 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf12 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf13 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf14 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf15 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf16 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        cpf17 = ''.join(map(str, [random.randint(0, 9) for i in range(0, 9)]))
        print(cpf)
        print(cpf2)
        print(cpf3)
        print(cpf4)
        print(cpf5)
        print(cpf6)
        print(cpf7)
        print(cpf8)
        print(cpf9)
        print(cpf10)
        print(cpf11)
        print(cpf12)
        print(cpf13)
        print(cpf14)
        print(cpf15)
        print(cpf16)
        print(cpf17)
        print(fechar)


    if pergunta == 3:
        print(azul)
        print('VOCÊ ESCOLHEU FAZER CCs\033[1;31m (BETA)\033[m')
        print(fechar)

        nome = ['Carla' , 'João' , 'Júlia' , 'Douglas',  'Maria' ,
              'Luís' , 'Fernanda' 'José' , 'Sibely',  'Márcio',
        'Brenda' , 'Mário' , 'Andreza' , 'Breno' , 'Sandra'
        , 'Osvaldo' ,'Lisandra','Gabriel','Gabriele','Gustavo'
        ,'Vitória', 'Artison', 'Rayna', 'Edgar', 'Sabrina',
        'Tiago', 'Paola', 'Higor', 'Beatriz', 'Hericles',
        'Karina', 'Pablo', 'Cristiane', 'Andre', 'Jacimara',
        'Cleber', 'Joyce', 'Blenda', 'Brenda' ,  'Jhulian' ,
        'Flavia' ,  'Almir', 'Lucas' ,'Stefany' ,  'Vitor' ,
        'Kessia', 'Vailso', 'Edson' , 'Raynara' ,  'Italo'  ,
        'Tulio' ,  'Ana' ,  'Luisa', 'Ramon' , 'Kethelen' , 'Tamires' , 'Jordânia' , 'Liriele' ,  'Clarisse' , 'Phelipe' , 'Wilians' , 'William' , 'wilson ', 'Ayla', 'Fabiana', 'Marcela', 'Pedro', 'Nicolas', 'Jorge', 'Juliana', 'Henrique', 'Rosangela', 'Fabricio', 'Guilerme', 'Bruno', 'Marcos', 'Glaudim', 'Fernando', 'Brian', 'Rafael', 'Mateus', 'Patrick', 'Sandra', 'Milena', 'Andre', 'Solange', 'Sandy', 'Valdete', 'Valdevir', 'Cristiano', 'Junior', 'Adrian',
        'Sam', 'Dean', 'Vanda', 'Luana', 'Elton', 'Raul', 'Israel']

        titu = random.choice(nome)
        sobre = random.choice(nome)
        endname = random.choice(nome)
        print(titu,sobre,endname)
       #REFORMAR NOMES / NOMES GERADOS ERRADOS


'''Titular: Laureana Acosta Brayer
CC: 5390830320852996
CVV:
Bandeira: MasterCard
Validade: 05/2023'''

