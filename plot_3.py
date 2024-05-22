import matplotlib.pyplot as plt
import numpy as np

x = [10, 12.5, 13, 15, 17, 17.5, 19]
y=  [7, 17, 15, 12, 18, 19, 20]
plt.scatter(x, y, label= "Garades", marker= "*")
plt.show()




x = [20, 100, 250, 400, 420, 440, 510]
y=  [120, 300, 700, 1000, 1100, 1500, 2000]
plt.scatter(x, y, label= "pressure & temperature", marker= "*", color= "black")
plt.xlabel("tempercure")
plt.ylabel("pressure")
plt.show()






x = [40, 55, 60, 73, 89, 100, 110]
y=  [500, 710, 750, 890, 1100, 1500, 1600]
plt.scatter(x, y, marker= "*", color= "black")
plt.xlabel("meter")
plt.ylabel("price")




x = [40, 55, 60, 73, 89, 100, 110]
y=  [700, 900, 990, 1200, 1550, 1800, 1900]
plt.scatter(x, y, marker= "*", color= "y")
plt.xlabel("meter")
plt.ylabel("price")




x = [40, 55, 60, 73, 89, 100, 110]
y=  [1000, 1230, 1400, 1900, 2500, 3000, 3700]
plt.scatter(x, y, marker= "*", color= "b")
plt.xlabel("meter")
plt.ylabel("price")
plt.show()