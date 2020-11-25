def linha():
    print('-------------------------------------------------------------------')
    return
linha()
print('''Olá Vamos hoje resolver para vc uma questão de raiz se vc não
conhece tal operação matematica digite (info) para resolver digite (resolver)''')
linha()
answe = str(input('Digite oq deseja aqui: '))
if answe == 'info':
    linha()
    print('Olá vc optou saber oq signifa resolver uma raiz')
    linha()
    print('sendo a um numero inteiro acima de zero identifique-o como quiser')
    linha()
    print(' ²√a  sendo um exemplo como ²√25')
    linha()
    print(' sendo ² = índice || √ = radical || a = radicando ')
    linha()
    print('resolvendo a questão anterior ²√25 seria o 5')
    linha()
    print('Porque 5² = 25')
    linha()
    print('o índice é o numero que dado a potencia tem que dar o valor do radicando')
    linha()
    print('²√25 || x² = 25 ')
    linha()

elif answe == 'resolver':
    print('Olá vc está na area de resolver')
    print('para tirar duvidas: ')
    print('² = índice || √ = radical || a = radicando')
    radican = float(input('Digite o radicando: '))
    indic = int(input('Digite o índice: '))
    res = radican ** (1/indic)
    print('O resultado da operação é {}'.format(res))


