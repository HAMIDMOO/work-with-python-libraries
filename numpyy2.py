import numpy as np

array1= np.array([[2, 4, 2], [2, 1, 2], [2, 1, -2]])
array2= np.array([15, -5, 0])

solution = np.linalg.solve(array1, array2)
print(solution)



