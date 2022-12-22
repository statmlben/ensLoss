import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import argparse
import scipy.stats

def path_plot(filename, D, H, train_verbose=True):
    sns.set(rc={'figure.figsize':(12, 9)})
    sns.set_theme(style='white')

    csv_path= filename+'/path_D'+str(D)+'_H'+str(H)+'_Batch256.csv'
    # ci_level = 1 - 2*(1 - scipy.stats.norm.cdf(1.96/np.sqrt(15)))

    df = pd.read_csv(csv_path)
    df = df.drop(['train_loss'], axis=1)
    df.columns = ['loss', 'epoch', 'train_acc', 'test_acc']
    
    if train_verbose:
        g = sns.lineplot(data=df, x="epoch", y="test_acc", hue="loss", label='TEST Acc', errorbar=('se', 1./np.sqrt(15)))
        g = sns.lineplot(data=df, x="epoch", y="train_acc", hue="loss", ax=g, linestyle='--', label='TRAIN Acc', errorbar=('se', 1./np.sqrt(15)))
        
        handles, labels = g.get_legend_handles_labels()
        ## Line style legend
        order = [0,6]
        plt.gca().add_artist(plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order], title='type', loc='lower right'))
        
        ## color legend
        order = [3,4,5]
        plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc='upper right', title='method') 
    else:
        g = sns.lineplot(data=df, x="epoch", y="test_acc", hue="loss", errorbar=('se', 1./np.sqrt(15)))

    plt.ylabel('Acc')
    plt.title('{}_{}({})'.format(filename,D,H))
    plt.tight_layout()
    plt.show()
    plt.savefig(csv_path[:-4]+'.png')
    return plt

if __name__=='__main__':
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='eLOTO plot')
    parser.add_argument('-D', '--depth', default=1, type=int,
                        help='depth of the neural network')
    parser.add_argument('-H', '--width', default=128, type=int,
                           help='width of the neural network')
    parser.add_argument('-f', '--filename', default='sylva_prior', type=str,
                           help='filename of the dataset')
    args = parser.parse_args()

    H, D = args.width, args.depth
    filename = args.filename
    
    plt_tmp = path_plot(filename, D, H)
