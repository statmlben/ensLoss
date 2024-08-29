import pandas as pd 
import wandb
import seaborn as sns
import matplotlib.pyplot as plt

api = wandb.Api()

pd.options.display.float_format = '{:.4f}'.format

# Project is specified by <entity/project-name>
runs = api.runs("bdai/ensLoss")

def find_record(runs, condition=['CIFAR']):
    
    df = {'dataset': [], 'model': [], 'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
    df = pd.DataFrame(df)

    test_df = {'dataset': [], 'model': [], 'A': [], 'B': [], 'pvalue': [], 'stat': [], 'alternative': []}
    test_df = pd.DataFrame(test_df)

    for run in runs:
        # if 'VGG' in run.name:
        if all(q in run.name for q in condition):
            dataset_tmp = run.name.split('-')[0]
            model_tmp = run.name.split('-')[1]
            perf_table = run.logged_artifacts()[2].get('perf_table')
            pless_table = run.logged_artifacts()[3].get('p_less')
            pgreater_table = run.logged_artifacts()[4].get('p_greater')

            perf_df = pd.DataFrame(data=perf_table.data, columns=perf_table.columns)
            pless_df = pd.DataFrame(data=pless_table.data, columns=pless_table.columns)
            pgreater_df = pd.DataFrame(data=pgreater_table.data, columns=pgreater_table.columns)

            perf_df.insert(loc=0, column='model', value=model_tmp)
            perf_df.insert(loc=0, column='dataset', value=dataset_tmp)
            pless_df.insert(loc=0, column='model', value=model_tmp)
            pless_df.insert(loc=0, column='dataset', value=dataset_tmp)
            pgreater_df.insert(loc=0, column='model', value=model_tmp)
            pgreater_df.insert(loc=0, column='dataset', value=dataset_tmp)

            df = pd.concat([df, perf_df], ignore_index=True)
            test_df = pd.concat([test_df, pless_df], ignore_index=True)
            test_df = pd.concat([test_df, pgreater_df], ignore_index=True)
    return df, test_df

def sum_perf(df):
    return df.groupby(['dataset', 'model', 'loss'], as_index=False)[['test_acc', 'test_auc']].agg(['mean', 'std'])

## Image Performance
df, test_df = find_record(runs, condition=['CIFAR35', 'VGG'])
perf = sum_perf(df)

plot_df = df.groupby(['dataset', 'model', 'loss'], as_index=False)['test_acc'].mean()
plot_df = plot_df.pivot(index="dataset", columns="loss", values="test_acc")
plot_df = plot_df.reset_index()
plot_df = plot_df.sort_values("Hinge", ascending=False)

# Plot the total crashes
sns.set_theme("paper", style='white')
f, ax = plt.subplots(figsize=(15, 6))
alpha = 0.55

sns.set_color_codes("pastel")
sns.barplot(y="ensLoss", x="dataset", data=plot_df,
            label="ensLoss", color="b", alpha=alpha)

sns.barplot(y="Hinge", x="dataset", data=plot_df,
            label="Hinge", color="g", alpha=alpha)
# sns.set_color_codes("bright")

ax = sns.barplot(y="BCE", x="dataset", data=plot_df,
            label="BCE", color="orange", alpha=alpha)
ax.set_alpha(alpha)

ax = sns.barplot(y="EXP", x="dataset", data=plot_df,
            label="EXP", color="red", alpha=alpha)
ax.set_alpha(alpha)

ax.legend(ncol=4, loc="upper right", frameon=True)
ax.set(ylim=(0.6, 1), xlabel="",
       ylabel="Test Accuracy")
sns.despine(left=True, bottom=True)
plt.xticks(rotation=80)
plt.tight_layout()
plt.savefig('perf_list.png')


## Test results
sig_test_df = test_df[test_df['pvalue']<.05]
sig_test_df.groupby(['model', 'A', 'B', 'alternative'])['pvalue'].size()


## PATH
path_df = {'model': [], 'loss': [], 'epoch': [], 'train_acc': [], 'test_acc': []}
path_df = pd.DataFrame(path_df)

sns.set_theme("paper", style='white', rc={'figure.figsize':(11.7,8.27)})
for run in runs:
    if 'CIFAR35' in run.name:
        dataset_tmp = run.name.split('-')[0]
        model_tmp = run.name.split('-')[1]
        path_table = run.logged_artifacts()[1].get('path')
        df_tmp = pd.DataFrame(data=path_table.data, columns=path_table.columns)
        df_tmp.insert(loc=0, column='model', value=model_tmp)
        path_df = pd.concat([path_df, df_tmp], ignore_index=True)

path_plt = sns.relplot(data=path_df.query("epoch % 10 == 0 & model in ['VGG16', 'ResNet34', 'MobileNetV2']"), 
                        x="epoch", y="test_acc",
                        col="model", hue="loss", style="loss",
                        kind="line", markers=True, dashes=False,
                        facet_kws={'sharey': False, 'sharex': True}
                    )
sns.move_legend(path_plt, "center right")
plt.tight_layout()
plt.savefig('CIFAR35.pdf')
