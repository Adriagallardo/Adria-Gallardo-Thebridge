#Random string of number generator with max digits option
    def num_variable(digitos):
        """This function returns a random number in format string with length as parameter."""
        import random
        n = ""
        for i in range(digitos):
            n = n + str(random.randint(1,9))
        return n


import pandas as pd
import numpy as np

def open_file(path_file):
    """
    DOCS # TODO

    Args:
        path_file ([str]): Path where is the file
    """
    # TODO (@gabvaztor) This function must open a file and write something.
    pass


# This file represents your module.
# Write the code...
import pandas as pd
import numpy as np

def mean_visualization():
    """Draw the mean in a plot"""
    return None

def show_list_of_elements(lista):
    # TODO 
    pass


if __name__ == '__main__':
    x = mean_visualization()
    print(x)