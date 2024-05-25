import pandas as pd 
import wandb
api = wandb.Api()

# Project is specified by <entity/project-name>
runs = api.runs("bdai/ensLoss")

df = {'dataset': [], 'model': [], 'trial': [], 'loss': [], 'test_acc': [], 'test_auc': []}
df = pd.DataFrame(df)
for run in runs:
    if 'VGG' in run.name:
        dataset_tmp = run.name.split('-')[0]
        model_tmp = run.name.split('-')[1]
        perf_table = run.logged_artifacts()[2].get('perf_table')
        perf_df = pd.DataFrame(data=perf_table.data, columns=perf_table.columns)
        perf_df.insert(loc=0, column='model', value=model_tmp)
        perf_df.insert(loc=0, column='dataset', value=dataset_tmp)
        df = pd.concat([df, perf_df], ignore_index=True)
