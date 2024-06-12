import numpy as np
# f(x)= 3*(x^2)+ (2*x) (-1)

# function value in (-2)
y= ((3*((-2)**2)) + (2*-2) - (1))
print(y)


# The derivative of the function in (-2)
coeff=np.poly1d([3, 2, -1])
derivative= np.polyder(coeff,1)
print(derivative(-2))

# the root of the function
root= np.roots(coeff)
print(root)
