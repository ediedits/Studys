
def notacao():
    fator = float(input('Digite o (FATOR)||numero entre 1 e 10: '))
    expo = float(input('Digite o expoente'))
    print('Sua notação cientifica é essa || {}.10^{}'.format(fator, expo))
    resultado = fator * 10 ** expo
    print('Sua notação resolvida fica:{}'.format(resultado))
    globals(fator, expo, resultado)
    return
def pluspower(base, expoe, base2, expoe2):
    print('Vamos Somar 2 potencias abaixo para vc')
    print('({}^{}) + (x^y)'.format(base,expoe)) 
    print('({}^{}) + ({}^{})'.format(base,expoe,base2,expoe2))
    if base == base2:
        res = expoe + expoe2
        print('Seu resultado fica ({}^{})'.format(base,res))
    elif expoe != expoe2:
        res2 = (base ** expoe) + (base2 ** expoe2)
        print('Seu resultado deu {}'.format(res2))
        print('''INFO:não pode fazer essa conta com duas potencias apenas
         podemos resolve-las e somalas :/''')
    return base, res     
def timespower(base, expoe, base2, expoe2):
    print('({}^{}) * (x^y)'.format(base, expoe))
    print('({}^{}) * ({}^{})'.format(base, expoe, base2, expoe2))
    if base == base2:
        res = expoe + expoe2
        print('Seu resultado fica ({}^{})'.format(base, res))
        return print(f'{base}{res}')
    elif expoe != expoe2:
        res2 = (base ** expoe) * (base2 ** expoe2)
        print('Seu resultado deu {}'.format(res2))
        print('''INFO:não pode fazer essa conta com duas potencias apenas
            podemos resolve-las e somalas :/''')


