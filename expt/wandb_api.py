import pandas as pd 
import wandb
api = wandb.Api()

# Project is specified by <entity/project-name>
runs = api.runs("bdai/ensLoss")

for run in runs:
    if 'VGG' in run.name:
        perf_table = run.logged_artifacts()[0].get('perf')
        perf_df = pd.DataFrame(data=perf_table.data, columns=perf_table.columns)
        perf_df.insert(loc=0, column='method', value=['BCE', 'EXP', 'Hinge', 'EnsLoss'])

