from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn import preprocessing
import pandas as pd
from sklearn.metrics import classification_report

## breast cancer
# data = load_breast_cancer()
# X, y = data.data, data.target

## fruit
# df = pd.read_csv('./dataset/citrus.csv')
# y = np.array(df['name'].map({'orange': 1, 'grapefruit': 0}))
# del df['name']
# X = df.values

## H1N1
# df = pd.read_csv('./dataset/H1N1_Flu_Vaccines.csv')
# df = df.dropna(axis=0)
# y = np.array(df['h1n1_vaccine'])

# del_col = ['respondent_id', 'age_group', 'education', 'race', 'sex', 'income_poverty', 
#         'marital_status', 'hhs_geo_region', 'census_msa', 'employment_industry', 
#         'employment_occupation', 'h1n1_vaccine', 'seasonal_vaccine', 'rent_or_own',
#         'employment_status', 'household_children', 'household_adults']
# df.drop(del_col, inplace=True, axis=1)
# X = df.values

# fraud detection bank
df = pd.read_csv('./dataset/fraud_detection_bank_dataset.csv')
df = df.dropna(axis=0)
y = np.array(df['targets'])

df.drop(['Unnamed: 0'], inplace=True, axis=1)
X = df.values

## Wine
# df = pd.read_csv('./dataset/wine.csv')
# y = np.array(df['quality'].map({'bad': 0, 'good': 1}))
# df.drop(['quality'], inplace=True, axis=1)
# X = df.values


# X, y = make_classification(n_samples=1000, n_features=20, flip_y=0.1)
y = 2*y - 1
max_epoch, lr = 1000, 1e-4

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
scaler = preprocessing.StandardScaler()
scaler.fit(X_train)
X_train, X_test = scaler.transform(X_train), scaler.transform(X_test)
X_train, X_test = np.c_[X_train, np.ones(len(X_train))], np.c_[X_test, np.ones(len(X_test))]

d = X_train.shape[1]

def get_batches(X, y, batch_size=32):
    n_samples = X.shape[0]

    # Shuffle at the start of epoch
    indices = np.arange(n_samples)
    np.random.shuffle(indices)

    for start in range(0, n_samples, batch_size):
        end = min(start + batch_size, n_samples)

        batch_idx = indices[start:end]

        yield X[batch_idx], y[batch_idx]

def metrics(beta, X, y):
    n_test = len(X)
    y_pred = X @ beta
    diff = y_pred * y 
    acc = np.mean( 1*(diff > 0) )
    hinge_loss = np.mean(np.maximum(1-diff, 0))
    return acc, hinge_loss

def Acc(beta, X, y):
    n_test = len(X)
    y_pred = X @ beta
    diff = y_pred * y 
    acc = np.mean( 1*(diff > 0) )
    return acc

def sol_beta(mean, var):
    alpha = - mean*(var + mean**2 - mean) / var
    beta = (mean-1)*(var + mean**2 - mean) / var
    return alpha, beta


## B-SGD for SVM
beta_svm = np.ones(d)
for epoch in range(max_epoch):
    batch_tmp = get_batches(X_train, y_train)
    for X_batch, y_batch in batch_tmp:
        s_batch = y_batch[:,np.newaxis] * X_batch @ beta_svm
        beta_svm += - lr * np.mean(y_batch[:,np.newaxis] * X_batch * (-1) * (s_batch <= 1)[:,np.newaxis], 0) # SVM loss
        acc_tmp, hinge_loss_tmp = metrics(beta_svm, X_test, y_test)
    print('Epoch: %d; acc: %.3f; hinge_loss: %.3f' %(epoch, acc_tmp, hinge_loss_tmp))
acc_svm = Acc(beta_svm, X_test, y_test)
print('Max Epoch: %d; acc: %.3f;' %(max_epoch, acc_svm))

## B-SGD for Logistic Regression
beta_log = np.ones(d)
for epoch in range(max_epoch):
    batch_tmp = get_batches(X_train, y_train)
    for X_batch, y_batch in batch_tmp:
        s_batch = y_batch[:,np.newaxis] * X_batch @ beta_log
        beta_log += lr * np.mean( (1. / (1. + np.exp(s_batch)))[:,np.newaxis] * y_batch[:,np.newaxis] * X_batch, 0) # logistic loss
        acc_tmp, hinge_loss_tmp = metrics(beta_log, X_test, y_test)
    print('Epoch: %d; acc: %.3f; hinge_loss: %.3f' %(epoch, acc_tmp, hinge_loss_tmp))
acc_log = Acc(beta_log, X_test, y_test)
print('Max Epoch: %d; acc: %.3f;' %(max_epoch, acc_log))

## B-SGD for Random Logistic Regression
# beta_log = np.ones(d)
# for epoch in range(max_epoch):
#     batch_tmp = get_batches(X_train, y_train)
#     for X_batch, y_batch in batch_tmp:
#         lam = np.random.uniform(0,2)
#         s_batch = y_batch[:,np.newaxis] * X_batch @ beta_log
#         beta_log += lr * np.mean( (1. / (1. + np.exp(lam*s_batch)))[:,np.newaxis] * y_batch[:,np.newaxis] * X_batch, 0) # logistic loss
#         acc_tmp, hinge_loss_tmp = metrics(beta_log, X_test, y_test)
#     print('Epoch: %d; acc: %.3f; hinge_loss: %.3f' %(epoch, acc_tmp, hinge_loss_tmp))
# acc_log, hinge_loss_log = metrics(beta_log, X_test, y_test)
# print('Max Epoch: %d; acc: %.3f; hinge_loss: %.3f' %(max_epoch, acc_log, hinge_loss_log))


## B-SGD for Random surrogate loss
beta_rd = np.ones(d)
for epoch in range(max_epoch):
    batch_tmp = get_batches(X_train, y_train)
    for X_batch, y_batch in batch_tmp:
        batch_size = len(X_batch)
        s_batch = np.zeros(batch_size+1)
        g_batch = np.zeros(batch_size+1)
        rd_grad = np.zeros(batch_size+1)

        s_batch[:-1] = y_batch[:,np.newaxis] * X_batch @ beta_rd
        grad_svm = 1*(s_batch<=1)
        # alpha, beta = sol_beta(mean=grad_svm.mean(), var=(grad_svm.std())**2)
        # rd_grad[s_batch>0.] = - np.random.beta(.5,.5,len(s_batch[s_batch>0.])) / 2
        # rd_grad[s_batch<=0.] = -1/2 - np.random.uniform(.5, .5, len(s_batch[s_batch<=0.]))/2

        # rd_grad = -abs(np.random.randn(len(s_batch)))
        # rd_grad = -np.random.uniform(0,1,len(s_batch))
        # rd_grad = -abs(np.random.laplace(0,1,batch_size+1))
        rd_grad = - np.random.exponential(1, batch_size+1)
        # rd_grad = - np.random.beta(alpha, beta, batch_size+1)
        rd_grad.sort()
        ind_tmp = np.argsort(s_batch)
        g_batch[ind_tmp] = rd_grad
        g_batch = g_batch[:-1] / abs(g_batch[-1])
        # g_batch = g_batch[:-1]
        beta_rd += - lr * np.mean( g_batch[:,np.newaxis] * y_batch[:,np.newaxis] * X_batch, 0) # random loss
        acc_tmp, hinge_loss_tmp = metrics(beta_rd, X_test, y_test)
    print('Epoch: %d; acc: %.3f; hinge_loss: %.3f' %(epoch, acc_tmp, hinge_loss_tmp))
acc_rd = Acc(beta_rd, X_test, y_test)
print('Max Epoch: %d; acc: %.3f' %(max_epoch, acc_rd))


print('SVM: Max Epoch: %d; acc: %.3f;' %(max_epoch, acc_svm))
print('Logistic: Max Epoch: %d; acc: %.3f;' %(max_epoch, acc_log))
print('eLOTO: Max Epoch: %d; acc: %.3f' %(max_epoch, acc_rd))
