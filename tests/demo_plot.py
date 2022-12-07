import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(1024)
sns.set()
df = {'z': [], 'y': [], 'loss': []}
n_trials = 5
n = 100

z_points = np.random.randn(n+1)
z_points = np.sort(z_points)

for i in range(n_trials):
    slopes = np.add.accumulate(np.random.random(size=n))
    # slopes = np.append(0,slopes)
    slopes -= max(slopes)
    slopes /= abs(np.random.randn())

    y_incr = np.ediff1d(z_points)*slopes
    y_points = np.add.accumulate(y_incr)
    y_points -= min(y_points)
    y_points /= abs(max(y_points)*np.random.randn())
    df['z'].extend(list(z_points[1:]))
    df['y'].extend(list(y_points))
    df['loss'].extend([i]*n)

df=pd.DataFrame(df)

sns.relplot(
    data=df, x='z', y="y",
    col="loss", hue="loss", style="loss", kind="line")

plt.show()