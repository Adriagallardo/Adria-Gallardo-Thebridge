import sys, os

ruta= __file__
print(ruta)

for i in range(2):
 ruta= os.path.dirname(ruta)
 print(ruta)

sys.path.append(ruta)

import a.x as x

def f1y():
    print("f1y")
    x.f1x()
    

def f2y():
    print("f2y")
    y.f2y()
    

y = 2
y_y = 22
