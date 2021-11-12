secret = 'amarelo'
digitou = []
chances = 5

while True:
    if chances <= 0:
        print('Você perdeu')
        break;

    letra = input('digite uma letra: ')
    if len(letra) > 1:
        print('digite apenas UMA letra!!')
        continue

    digitou.append(letra)

    if letra in secret:
        print(f'a letra {letra} EXISTE na palavra secreta')
    else:
        print(f'a letra {letra} NÃO EXISTE na palavra secreta')
        digitou.pop()

    secreto_temp = ''

    for letra2 in secret:
        if letra2 in digitou:
            secreto_temp += letra2
        else:
            secreto_temp += '*'

    print(secreto_temp)

    if secreto_temp == secret:
        print(f'Você ganhou!! Palavra: {secreto_temp}')
        break;
    else:
        print(f'a palavra secreta está assim: {secreto_temp}')

    if letra not in secret:
       chances -= 1

    print(f'Você tem {chances} chances')
    print()

