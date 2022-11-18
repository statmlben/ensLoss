import numpy as np

def compute_mean_var(order=0, n=1):
    idx_range = np.arange(n) + 1
    mean = np.sum( 1./idx_range[n-order-1:] )
    var = np.sum( 1./(idx_range[n-order-1:]**2))
    return mean, var

n_max = 500
df = {'n': [], 'quantile': [], 'mean': [], 'var': []}
for n in range(10, n_max, 20):
    for quantile_tmp in [.1, .3, .5, .7, .9]:
    # for order in range(0, n, int(.2*n)):
        order = int(n*quantile_tmp)
        mean_tmp, var_tmp = compute_mean_var(order=order, n=n)
        df['n'].append(n)
        df['quantile'].append(quantile_tmp)
        df['mean'].append(mean_tmp)
        df['var'].append(var_tmp)

import pandas as pd
df = pd.DataFrame(df)

import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(data=df, x="n", y="mean", hue="quantile", style="quantile")
plt.show()

sns.lineplot(data=df, x="n", y="var", hue="quantile", style="quantile")
plt.show()
