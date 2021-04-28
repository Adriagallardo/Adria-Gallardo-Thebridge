import sys, os

ruta= __file__
print(ruta)

for i in range(3):
 ruta= os.path.dirname(ruta)
 print(ruta)

sys.path
sys.path.append(ruta)

import a.x as x
import b.y as y


def f1z():
    print("f1z")
    y.f1z

def f2z():
    print("f2z")
    x.f2x()

z = 3
z_z = 33
