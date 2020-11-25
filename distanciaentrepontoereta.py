from operacaos import pluspower
import math
from time import sleep
print('Lembre-se')
sleep(1)
print('ax + by + c = 0')
a = float(input('Digite o A:'))
b = float(input('Digite o b:'))
c = float(input('Digite o c:'))
xp = float(input('Digite o primeiro valor do P:'))
yp = float(input('Digite o segundo valor do p:'))
formdowsoma = math.sqrt(a**2 + 4 ** 2)
formup = a * xp
formup2 = b * yp
formupfinal = formup - formup2 + c
print(f'O resultado deu {formupfinal}sobre {formdowsoma}')



