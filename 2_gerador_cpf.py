'''
LÓGICA PARA VÁLIDAR CPF:
CPF = 168.995.350-09
----------------------------------------------
1 * 10 = 10                       1 * 11 = 11
6 * 9 = 54                        6 * 10 = 60
8 * 8 = 64                        8 * 9 =  72
9 * 7 = 63                        9 * 8 =  72
9 * 6 = 54                        9 * 7 =  63
5 * 5 = 25                        5 * 6 =  30
3 * 4 = 12                        3 * 5 =  15
5 * 3 = 15                        5 * 4 =  20
0 * 2 = 0                         0 * 3 =  0
                                  0 * 2 =  0
soma = 297                        soma = 345
11 - (297 % 11) = 11              11 - (345 % 11) = 11

11 > 9 = 0                         Se x > 9 = 0 / Se x < 9 = 9
Digito 1 = 0                       Digito 2 = 9

'''

from random import randint

numero = str(randint(100000000, 999999999))
l_cpf = []
l1 = [10,9,8,7,6,5,4,3,2]
novo_l1 = []
novo_l2 = []
string_cpf = []

# transformando numero gerado em uma lista
for n in numero:
    l_cpf.append(n)

# multiplicando o cpf pela sequencia 10-2
for i in range(0,9):
    novo_l1.append(l1[i]*int(l_cpf[i]))

# formula para gerar primeiro digito válido
soma1  = sum(novo_l1)
r1 = 11 - (soma1 % 11)

if r1 > 9:
    dig1 = 0
else:
    dig1 = r1

dig1 = int(dig1)

# inserindo digito na lista l_cpf e add +1 numero a lista l1
l_cpf.append(dig1)
l1.insert(0, 11)

# PARTE 02 DO CALCULO

# multiplicando o cpf pela sequencia 11-2
for i in range(0,10):
    novo_l2.append(l1[i]*int(l_cpf[i]))

# formula para gerar segundo digito válido
soma2  = sum(novo_l2)
r2 = 11 - (soma2 % 11)

if r2 > 9:
    dig2 = 0
else:
    dig2 = r2

l_cpf.append(dig2)

#converter int da lista em str
for i in l_cpf:
    string_cpf.append(str(i))

novo_cpf = ''.join(string_cpf)

print('-'*35)
print(f'CPF ALEATÓRIO: {novo_cpf[0:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:11]}')
print('-'*35)
print()
