def descsen(ws, num):
    if ws in ('senoSeno'):
        mc = int(input(f'Qual a medida do cateto oposto a {num}: '))
        mh = int(input(f'Qual a medida da hipotenusa?: '))
        seno = mc / mh
        return seno
    elif ws in ('Cossenocosseno'):
        mc = int(input(f'Qual a medida do cateto adjacente a {num}: '))
        mh = int(input(f'Qual a medida da hipotenusa?:'))
        cosseno = mc / mh
        return cosseno
 
        

