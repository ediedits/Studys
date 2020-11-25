n1 = int(input("""Digite o primeiro numero 
 x    x
__ = __

 x    x
"""))
n2 = int(input(f"""Digite o segundo numero
{n1}  x
__ = __

 x    x
"""))
n3 = int(input(f"""Digite o segundo numero
{n1}   {n2}
__  =   __

 x       x
 """))
n4 = int(input(f"""Digite o segundo numero
{n1}   {n2}
__  =   __

{n3}    x
 """))
comp1 = n1 * n4
comp2 = n2 * n3
if comp1 == comp2:
    print('Sua razão é proporcional!!')
else:
    print('Sua razão não é proporcional!!')


