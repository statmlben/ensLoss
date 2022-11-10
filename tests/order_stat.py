import numpy as np

def compute_mean_var(order=0, n=1):
    idx_range = np.arange(n) + 1
    mean = np.sum( 1./idx_range[n-order-1:] )
    var = np.sum( 1./(idx_range[n-order-1:]**2))
    return mean, var

n_max = 1000
df = {'n': [], 'order': [], 'mean': [], 'var': []}
for n in range(5, n_max, 20):
    for order in range(0, n, int(.2*n)):
        mean_tmp, var_tmp = compute_mean_var(order=order, n=n)
        df['n'].append(n)
        df['order'].append(order/n)
        df['mean'].append(mean_tmp)
        df['var'].append(var_tmp)

import pandas as pd
df = pd.DataFrame(df)

import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(data=df, x="n", y="mean", hue="order", style="order")
plt.show()

sns.lineplot(data=df, x="n", y="var", hue="order", style="order")
plt.show()
