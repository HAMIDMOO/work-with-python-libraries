import numpy as np

array1= np.array([[1, 2, 5], [2, 9, 7]])
array2= np.array([[5, 5, 3], [5, 6, 7]])
print(np.stack((array1, array2), axis=0))