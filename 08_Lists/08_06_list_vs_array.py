# Differences lists vs array

import numpy as np

my_array = np.array([0,1,2,3,4])
my_list = [1,2,34]

print(my_array/2) # runs the calculation
print(my_list/2) # will throw an error
# TypeError: unsupported operand type(s) for /: 'list' and 'int'