import matplotlib.pyplot as plt
import numpy as np

x = np.linspace((np.pi)/2, (3*(np.pi))/2, 400)
y= 1-(np.cos(x)**2)
plt.plot(x, y)

plt.show()

