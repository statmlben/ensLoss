import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.pyplot import figure

figure(figsize=(16, 12), dpi=100)

df = pd.read_csv('./test_loss_sim.csv')

df.replace("log_Hinge", "Log_Hinge", inplace=True)
df.replace("log_inv_Hinge", "Inv_Log_Hinge", inplace=True)

sns.lineplot(
    data=df[df['epoch'] % 5 == 1], x="epoch", y="train_loss",
    # col="loss", 
    hue="loss", style="loss",
    hue_order=['Hinge', 'Exp_Hinge', 'Inv_Hinge', 'Inv_Log_Hinge', 'Log_Hinge'],
    markers=True, dashes=False
)

plt.tight_layout()
plt.show()
