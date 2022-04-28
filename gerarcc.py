import random
##666; Koppy404
print('Powered By: Koppy404')
print ('IG: koppy999_')
s = True
n = False
list = [2018, 2019, 2020, 2021, 2022, 2023]
nume = random.randrange(1, 9999999999999999)
cvv = random.randint(3, 999)
data1 = random.randrange(1, 31)
data2 = random.randrange(1, 12)
data3 = random.choice(list)
cpf = random.randrange(1, 99999999999)

bi = str(input('Você deseja inserir sua BIN ? s ou n?: '))

if bi == 's':
    nume2 = random.randrange(1, 9999999999)
    bin = int(input('Digite sua BIN de 6 digitos : '))
    print('Número do cartão', bin, nume2)
    print('Cvv do cartão:',cvv)
    print('Data do cartão:', data1, data2, data3)
    print('CPF cadastrado no cartão:', cpf)
else:
    print('Número do cartão:',nume)
    print('CvV do cartão:',cvv)
    print('Data:',data1,data2,data3)
    print('CPF cadastrado no cartão:',cpf)
