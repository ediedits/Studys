
fator = float(input('Digite o (FATOR)||numero entre 1 e 10: '))
expo = float(input('Digite o expoente'))
print('Sua notação cientifica é essa || {}.10^{}'.format(fator,expo))
resultado = fator * 10 ** expo
print('Sua notação resolvida fica:{:.2f}'.format(resultado))


