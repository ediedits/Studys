def notacao():
    fator = float(input('Digite o (FATOR)||numero entre 1 e 10: '))
    expo = float(input('Digite o expoente'))
    print('Sua notação cientifica é essa || {}.10^{}'.format(fator, expo))
    resultado = fator * 10 ** expo
    print('Sua notação resolvida fica:{}'.format(resultado))
    globals(fator, expo, resultado)
    return
notacao()
def pluspower():
    print('Vamos Somar 2 potencias abaixo para vc')
    base = int(input('Digite a base: '))
    expoe = int(input('Digite o expoente: '))
    print('({}^{}) + (x^y)'.format(base,expoe))
    base2 = int(input('Digite a base da segunda potencia: '))
    expoe2 = int(input('Digite o expoente da segunda potencia'))
    print('({}^{}) + ({}^{})'.format(base,expoe,base2,expoe2))
    if base == base2:
        res = expoe + expoe2
        print('Seu resultado fica ({}^{})'.format(base,res))
    elif expoe != expoe2:
        res2 = (base ** expoe) + (base2 ** expoe2)
        print('Seu resultado deu {}'.format(res2))
        print('''INFO:não pode fazer essa conta com duas potencias apenas
         podemos resolve-las e somalas :/''')
def timespower():
    base = int(input('Digite a base: '))
    expoe = int(input('Digite o expoente: '))
    print('({}^{}) * (x^y)'.format(base, expoe))
    base2 = int(input('Digite a base da segunda potencia: '))
    expoe2 = int(input('Digite o expoente da segunda potencia'))
    print('({}^{}) * ({}^{})'.format(base, expoe, base2, expoe2))
    if base == base2:
        res = expoe + expoe2
        print('Seu resultado fica ({}^{})'.format(base, res))
    elif expoe != expoe2:
        res2 = (base ** expoe) * (base2 ** expoe2)
        print('Seu resultado deu {}'.format(res2))
        print('''INFO:não pode fazer essa conta com duas potencias apenas
            podemos resolve-las e somalas :/''')
