import numpy as np

def BC_inv(z, lam=0):
    if lam == 0.:
        return np.exp(z)
    else:
        diff = 1. + lam*z
        return (np.where(diff > 0.0, diff, 0.0))**(1.0/lam)

x = np.random.randn(1000)
z = BC_inv(x, lam=0.0)

import matplotlib.pyplot as plt

plt.hist(z)
plt.show()