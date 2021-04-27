import sys, os

ruta= __file__
print(ruta)

for i in range(2):
 ruta = os.path.dirname(ruta)
 print(ruta)

sys.path
sys.path.append(ruta)

import b.c.z as z


def f1x():
    print("f1x")


def f2x():
    print("f2x")
    z.f2z()

x = 1
x_x = 11
