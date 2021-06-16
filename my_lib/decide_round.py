from decimal import localcontext, Decimal, ROUND_HALF_DOWN, ROUND_HALF_UP
import numpy as np

def round_down(data, column):
    "This function forces numbers of a column in a dataset to round half down"
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_DOWN
        for i in range(1, 15, 2):
            n = Decimal(i) / 2
            print(n, '=>', n.to_integral_value())

    a = data[column].to_numpy().tolist()
    e = []
    for num in a:
        n = Decimal(num)
        n_fin = n.to_integral_value()
        i = int(n_fin)
        e.append(i)
    print("Mostreo de datos de columna:", np.array(e))

    data[column] = np.array(e)

    
    return data

def round_up(data, column):
    "This function forces numbers of a column in a dataset to round half up"
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        for i in range(1, 15, 2):
            n = Decimal(i) / 2
            print(n, '=>', n.to_integral_value())

    a = data[column].to_numpy().tolist()
    e = []
    for num in a:
        n = Decimal(num)
        n_fin = n.to_integral_value()
        i = int(n_fin)
        e.append(i)
    print("Mostreo de datos de columna:", np.array(e))

    data[column] = np.array(e)

    
    return data