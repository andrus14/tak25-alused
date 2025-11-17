# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

from math import pi

r = float(input('Sisesta raadius: '))

c = 2 * pi * r

s = pi * r ** 2

print('Ümbermõõt:', c)
print('Pindala:', s)
