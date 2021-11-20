'''
Implementar:
- Mensagens de erro
- Não permitir  substituição
'''

import os

l = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def regras():

    print('.'*16)
    print('* TIC-TAC-TOE  *')
    print('.' * 16)
    print('COMO JOGAR:')
    print('** Escolha numeros entre 1 e 9 para selecionar a posição')

    # exemplo

    print()
    print(' 1  |  2   |  3')
    print('_' * 16)
    print(' 4  |  5   |  6')
    print('_' * 16)
    print(' 7  |  8   |  9')
    print()
    start = input('PARA COMEÇAR DIGITE "OK":  ')
    print()

def escolha():

    global xo
    xo = input('Player 1: Escolha "x" ou "o": ')

    if xo == 'x' or xo == 'X':
        print('.' * 16)
        print("Player 1 = x ")
        print("Player 2 = o ")
        print('.' * 16)

    elif xo == 'o' or xo == 'O':
        print('.' * 16)
        print("Player 1 = o ")
        print("Player 2 = x ")
        print('.' * 16)

    else:
        print('escolha apenas "x" ou "o"!!')

def posicaox():

    global n
    n = int(input('x :: ESCOLHA A POSIÇÃO: '))

    l[n] = 'x'

    print()
    print(f' {l[1]}  |  {l[2]}   |  {l[3]}')
    print('_' * 16)
    print(f' {l[4]}  |  {l[5]}   |  {l[6]}')
    print('_' * 16)
    print(f' {l[7]}  |  {l[8]}   |  {l[9]}')


def posicaoo():

    global n
    n = int(input('o :: ESCOLHA A POSIÇÃO: '))

    l[n] = 'o'

    print()
    print(f' {l[1]}  |  {l[2]}   |  {l[3]}')
    print('_' * 16)
    print(f' {l[4]}  |  {l[5]}   |  {l[6]}')
    print('_' * 16)
    print(f' {l[7]}  |  {l[8]}   |  {l[9]}')


def verificax():

    global win_x
    win_x  = 0
    if l[1] == 'x' and l[2] == 'x' and l[3] == 'x' or l[4] == 'x' and l[5] == 'x' and l[6] == 'x' or l[7] == 'x' and l[8] == 'x' and l[9] == 'x' \
    or l[1] == 'x' and l[4] == 'x' and l[7] == 'x' or l[2] == 'x' and l[5] == 'x' and l[8] == 'x' or l[3] == 'x' and l[6] == 'x' and l[9] == 'x' \
    or l[1] == 'x' and l[5] == 'x' and l[9] == 'x' or l[3] == 'x' and l[5] == 'x' and l[7] == 'x':

        win_x = 1
        print('FIM DE JOGO :: "x" É O VENCEDOR!')



def verificao():

    global win_o
    win_o = 0

    if l[1] == 'o' and l[2] == 'o' and l[3] == 'o' or l[4] == 'o' and l[5] == 'o' and l[6] == 'o' or l[7] == 'o' and l[8] == 'o' and l[9] == 'o' \
    or l[1] == 'o' and l[4] == 'o' and l[7] == 'o' or l[2] == 'o' and l[5] == 'o' and l[8] == 'o' or l[3] == 'o' and l[6] == 'o' and l[9] == 'x' \
    or l[1] == 'o' and l[5] == 'o' and l[9] == 'o' or l[3] == 'o' and l[5] == 'o' and l[7] == 'o':

        win_o = 1
        print('FIM DE JOGO :: "o" É O VENCEDOR!')

regras()
escolha()

if xo == 'o' or xo == 'O':

    for i in range(9):
        posicaoo()
        verificao()
        if win_o == 1:
            break
        posicaox()
        verificax()
        if win_x == 1:
            break

elif xo == 'x' or xo == 'X':

    for i in range(9):
        posicaox()
        verificax()
        if win_x == 1:
            break

        posicaoo()
        verificao()
        if win_o == 1:
            break



