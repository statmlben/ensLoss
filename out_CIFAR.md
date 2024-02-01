# 3 (cat) vs 5 (dog)

#### CIFAR - model: ResNet18 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7452 | 0.7927 | 0.6641 |  0.7528 |
| ('test_acc', 'std')  | 0.002  | 0.0085 | 0.0009 |  0.0028 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0018 |  -6.1156 | less          |
|  6 | Hinge | COTO |   0.0097 |  -3.7773 | less          |
|  9 | EXP   | COTO |   0      | -15.3634 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9982 |  -6.1156 | greater       |
|  6 | Hinge | COTO |   0.9903 |  -3.7773 | greater       |
|  9 | EXP   | COTO |   1      | -15.3634 | greater       |

-- Result --

| (ResNet18) | mean(std) | 0.7452(0.002) | 0.7528(0.0028) | 0.7927(0.0085) |
|          | p_value   | 0.00181        | 0.00974        | ---            |

#### CIFAR - model: ResNet34 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7509 | 0.7857 | 0.6211 |  0.7548 |
| ('test_acc', 'std')  | 0.0065 | 0.0092 | 0.0085 |  0.0056 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0194 |  -3.0295 | less          |
|  6 | Hinge | COTO |   0.0303 |  -2.59   | less          |
|  9 | EXP   | COTO |   0.0002 | -11.2937 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9806 |  -3.0295 | greater       |
|  6 | Hinge | COTO |   0.9697 |  -2.59   | greater       |
|  9 | EXP   | COTO |   0.9998 | -11.2937 | greater       |

-- Result --

| (ResNet34) | mean(std) | 0.7509(0.0065) | 0.7548(0.0056) | 0.7857(0.0092) |
|          | p_value   | 0.0194        | 0.03034        | ---            |

#### CIFAR - model: ResNet50 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7292 | 0.777  | 0.6432 |  0.7405 |
| ('test_acc', 'std')  | 0.0032 | 0.0042 | 0.003  |  0.006  |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -14.1734 | less          |
|  6 | Hinge | COTO |   0.0052 |  -4.5569 | less          |
|  9 | EXP   | COTO |   0      | -33.8202 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -14.1734 | greater       |
|  6 | Hinge | COTO |   0.9948 |  -4.5569 | greater       |
|  9 | EXP   | COTO |   1      | -33.8202 | greater       |

-- Result --

| (ResNet50) | mean(std) | 0.7292(0.0032) | 0.7405(0.006) | 0.777(0.0042) |
|          | p_value   | 7e-05        | 0.00518        | ---            |

#### CIFAR - model: ResNet101 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7075 | 0.7327 | 0.556  |  0.6914 |
| ('test_acc', 'std')  | 0.0071 | 0.0048 | 0.0069 |  0.0029 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0062 |  -4.33   | less          |
|  6 | Hinge | COTO |   0.0022 |  -5.8198 | less          |
|  9 | EXP   | COTO |   0      | -16.6306 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9938 |  -4.33   | greater       |
|  6 | Hinge | COTO |   0.9978 |  -5.8198 | greater       |
|  9 | EXP   | COTO |   1      | -16.6306 | greater       |

-- Result --

| (ResNet101) | mean(std) | 0.7075(0.0071) | 0.6914(0.0029) | 0.7327(0.0048) |
|          | p_value   | 0.00617        | 0.00217        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7699 | 0.8062 | 0.7403 |  0.7762 |
| ('test_acc', 'std')  | 0.005  | 0.0035 | 0.0034 |  0.003  |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0041 |  -4.8688 | less          |
|  6 | Hinge | COTO |   0.0019 |  -6.0202 | less          |
|  9 | EXP   | COTO |   0.0001 | -12.6482 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9959 |  -4.8688 | greater       |
|  6 | Hinge | COTO |   0.9981 |  -6.0202 | greater       |
|  9 | EXP   | COTO |   0.9999 | -12.6482 | greater       |

-- Result --

| (VGG) | mean(std) | 0.7699(0.005) | 0.7762(0.003) | 0.8062(0.0035) |
|          | p_value   | 0.00411        | 0.00192        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7703 | 0.8001 | 0.7391 |  0.7771 |
| ('test_acc', 'std')  | 0.0025 | 0.0031 | 0.0027 |  0.0024 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0002 | -11.4208 | less          |
|  6 | Hinge | COTO |   0.0036 |  -5.0699 | less          |
|  9 | EXP   | COTO |   0.0001 | -13.4044 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9998 | -11.4208 | greater       |
|  6 | Hinge | COTO |   0.9964 |  -5.0699 | greater       |
|  9 | EXP   | COTO |   0.9999 | -13.4044 | greater       |

-- Result --

| (VGG) | mean(std) | 0.7703(0.0025) | 0.7771(0.0024) | 0.8001(0.0031) |
|          | p_value   | 0.00017        | 0.00357        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7741 | 0.8113 | 0.6915 |  0.7746 |
| ('test_acc', 'std')  | 0.004  | 0.0026 | 0.0039 |  0.0016 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -12.5524 | less          |
|  6 | Hinge | COTO |   0.0001 | -14.4571 | less          |
|  9 | EXP   | COTO |   0      | -19.9567 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -12.5524 | greater       |
|  6 | Hinge | COTO |   0.9999 | -14.4571 | greater       |
|  9 | EXP   | COTO |   1      | -19.9567 | greater       |

-- Result --

| (VGG) | mean(std) | 0.7741(0.004) | 0.7746(0.0016) | 0.8113(0.0026) |
|          | p_value   | 0.00012        | 7e-05        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7679 | 0.8087 | 0.6686 |  0.7687 |
| ('test_acc', 'std')  | 0.0053 | 0.0024 | 0.0062 |  0.0035 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0012 |  -6.8041 | less          |
|  6 | Hinge | COTO |   0      | -16.9814 | less          |
|  9 | EXP   | COTO |   0      | -31.9654 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9988 |  -6.8041 | greater       |
|  6 | Hinge | COTO |   1      | -16.9814 | greater       |
|  9 | EXP   | COTO |   1      | -31.9654 | greater       |

-- Result --

| (VGG) | mean(std) | 0.7679(0.0053) | 0.7687(0.0035) | 0.8087(0.0024) |
|          | p_value   | 0.00122        | 4e-05        | ---            |

#### CIFAR - model: DenseNet121 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8243 | 0.8613 | 0.7431 |  0.8308 |
| ('test_acc', 'std')  | 0.0021 | 0.0021 | 0.0027 |  0.0029 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0003 | -10.0445 | less          |
|  6 | Hinge | COTO |   0.0001 | -14.1844 | less          |
|  9 | EXP   | COTO |   0      | -27.0177 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9997 | -10.0445 | greater       |
|  6 | Hinge | COTO |   0.9999 | -14.1844 | greater       |
|  9 | EXP   | COTO |   1      | -27.0177 | greater       |

-- Result --

| (DenseNet121) | mean(std) | 0.8243(0.0021) | 0.8308(0.0029) | 0.8613(0.0021) |
|          | p_value   | 0.00028        | 7e-05        | ---            |

#### CIFAR - model: DenseNet121 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8299 | 0.8629 | 0.7447 |  0.8288 |
| ('test_acc', 'std')  | 0.0027 | 0.0024 | 0.0025 |  0.0018 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0002 | -10.2571 | less          |
|  6 | Hinge | COTO |   0.0002 | -10.8864 | less          |
|  9 | EXP   | COTO |   0      | -24.8828 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9998 | -10.2571 | greater       |
|  6 | Hinge | COTO |   0.9998 | -10.8864 | greater       |
|  9 | EXP   | COTO |   1      | -24.8828 | greater       |

-- Result --

| (DenseNet121) | mean(std) | 0.8299(0.0027) | 0.8288(0.0018) | 0.8629(0.0024) |
|          | p_value   | 0.00025        | 0.0002        | ---            |

#### CIFAR - model: DenseNet169 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.832  | 0.8612 | 0.7433 |  0.8272 |
| ('test_acc', 'std')  | 0.0029 | 0.0022 | 0.0027 |  0.0032 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -14.3714 | less          |
|  6 | Hinge | COTO |   0      | -15.4323 | less          |
|  9 | EXP   | COTO |   0      | -52.9886 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -14.3714 | greater       |
|  6 | Hinge | COTO |   1      | -15.4323 | greater       |
|  9 | EXP   | COTO |   1      | -52.9886 | greater       |

-- Result --

| (DenseNet169) | mean(std) | 0.832(0.0029) | 0.8272(0.0032) | 0.8612(0.0022) |
|          | p_value   | 7e-05        | 5e-05        | ---            |

#### CIFAR - model: DenseNet201 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8299 | 0.8614 | 0.7432 |  0.832  |
| ('test_acc', 'std')  | 0.0036 | 0.0044 | 0.0037 |  0.0023 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0002 | -11.028  | less          |
|  6 | Hinge | COTO |   0.0002 | -10.7477 | less          |
|  9 | EXP   | COTO |   0      | -17.4681 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9998 | -11.028  | greater       |
|  6 | Hinge | COTO |   0.9998 | -10.7477 | greater       |
|  9 | EXP   | COTO |   1      | -17.4681 | greater       |

-- Result --

| (DenseNet201) | mean(std) | 0.8299(0.0036) | 0.832(0.0023) | 0.8614(0.0044) |
|          | p_value   | 0.00019        | 0.00021        | ---            |

#### CIFAR - model: MobileNet ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.6806 | 0.6995 | 0.5668 |  0.6719 |
| ('test_acc', 'std')  | 0.003  | 0.0042 | 0.0076 |  0.0029 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0067 |  -4.2278 | less          |
|  6 | Hinge | COTO |   0.0023 |  -5.739  | less          |
|  9 | EXP   | COTO |   0      | -20.6115 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9933 |  -4.2278 | greater       |
|  6 | Hinge | COTO |   0.9977 |  -5.739  | greater       |
|  9 | EXP   | COTO |   1      | -20.6115 | greater       |

-- Result --

| (MobileNet) | mean(std) | 0.6806(0.003) | 0.6719(0.0029) | 0.6995(0.0042) |
|          | p_value   | 0.0067        | 0.00228        | ---            |

#### CIFAR - model: MobileNetV2 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7322 | 0.7743 | 0.6268 |  0.7431 |
| ('test_acc', 'std')  | 0.0087 | 0.0036 | 0.009  |  0.0038 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0024 |  -5.6366 | less          |
|  6 | Hinge | COTO |   0.0003 |  -9.851  | less          |
|  9 | EXP   | COTO |   0.0001 | -12.9776 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9976 |  -5.6366 | greater       |
|  6 | Hinge | COTO |   0.9997 |  -9.851  | greater       |
|  9 | EXP   | COTO |   0.9999 | -12.9776 | greater       |

-- Result --

| (MobileNetV2) | mean(std) | 0.7322(0.0087) | 0.7431(0.0038) | 0.7743(0.0036) |
|          | p_value   | 0.00244        | 0.0003        | ---            |


# 1 (automobile) vs 9 (truck)

#### CIFAR - model: MobileNetV2 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8956 | 0.9343 | 0.7613 |  0.8989 |
| ('test_acc', 'std')  | 0.0014 | 0.0017 | 0.0046 |  0.0022 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0      | -19.6854 | less          |
|  6 | Hinge | COTO |   0.0001 | -11.8247 | less          |
|  9 | EXP   | COTO |   0      | -31.4964 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   1      | -19.6854 | greater       |
|  6 | Hinge | COTO |   0.9998 | -11.8247 | greater       |
|  9 | EXP   | COTO |   1      | -31.4964 | greater       |

-- Result --

| (MobileNetV2) | mean(std) | 0.8956(0.0014) | 0.8989(0.0022) | 0.9343(0.0017) |
|          | p_value   | 2e-05        | 0.00015        | ---            |

#### CIFAR - model: MobileNet ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8317 | 0.8814 | 0.6536 |  0.8335 |
| ('test_acc', 'std')  | 0.0065 | 0.0034 | 0.0073 |  0.0049 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0014 |  -6.5821 | less          |
|  6 | Hinge | COTO |   0.0016 |  -6.3536 | less          |
|  9 | EXP   | COTO |   0      | -23.3992 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9986 |  -6.5821 | greater       |
|  6 | Hinge | COTO |   0.9984 |  -6.3536 | greater       |
|  9 | EXP   | COTO |   1      | -23.3992 | greater       |

-- Result --

| (MobileNet) | mean(std) | 0.8317(0.0065) | 0.8335(0.0049) | 0.8814(0.0034) |
|          | p_value   | 0.00138        | 0.00157        | ---            |

#### CIFAR - model: DenseNet201 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9301 | 0.9573 | 0.8862 |  0.9366 |
| ('test_acc', 'std')  | 0.0019 | 0.0007 | 0.0026 |  0.0026 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0002 | -11.1803 | less          |
|  6 | Hinge | COTO |   0.0005 |  -8.5971 | less          |
|  9 | EXP   | COTO |   0      | -26.6932 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9998 | -11.1803 | greater       |
|  6 | Hinge | COTO |   0.9995 |  -8.5971 | greater       |
|  9 | EXP   | COTO |   1      | -26.6932 | greater       |

-- Result --

| (DenseNet201) | mean(std) | 0.9301(0.0019) | 0.9366(0.0026) | 0.9573(0.0007) |
|          | p_value   | 0.00018        | 0.0005        | ---            |

#### CIFAR - model: DenseNet169 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9291 | 0.9553 | 0.8837 |  0.9352 |
| ('test_acc', 'std')  | 0.0017 | 0.0014 | 0.0023 |  0.0013 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -18.0678 | less          |
|  6 | Hinge | COTO |        0 | -29.6227 | less          |
|  9 | EXP   | COTO |        0 | -39.1883 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -18.0678 | greater       |
|  6 | Hinge | COTO |        1 | -29.6227 | greater       |
|  9 | EXP   | COTO |        1 | -39.1883 | greater       |

-- Result --

| (DenseNet169) | mean(std) | 0.9291(0.0017) | 0.9352(0.0013) | 0.9553(0.0014) |
|          | p_value   | 3e-05        | 0.0        | ---            |

#### CIFAR - model: DenseNet121 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9388 | 0.9578 | 0.8885 |  0.9323 |
| ('test_acc', 'std')  | 0.0015 | 0.0012 | 0.0045 |  0.0024 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0      | -17.7885 | less          |
|  6 | Hinge | COTO |   0.0002 | -10.2677 | less          |
|  9 | EXP   | COTO |   0      | -17.5106 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   1      | -17.7885 | greater       |
|  6 | Hinge | COTO |   0.9998 | -10.2677 | greater       |
|  9 | EXP   | COTO |   1      | -17.5106 | greater       |

-- Result --

| (DenseNet121) | mean(std) | 0.9388(0.0015) | 0.9323(0.0024) | 0.9578(0.0012) |
|          | p_value   | 3e-05        | 0.00025        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9071 | 0.94   | 0.8783 |  0.911  |
| ('test_acc', 'std')  | 0.0024 | 0.0012 | 0.0029 |  0.0021 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -12.3058 | less          |
|  6 | Hinge | COTO |   0      | -22.6295 | less          |
|  9 | EXP   | COTO |   0      | -23.3186 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -12.3058 | greater       |
|  6 | Hinge | COTO |   1      | -22.6295 | greater       |
|  9 | EXP   | COTO |   1      | -23.3186 | greater       |

-- Result --

| (VGG) | mean(std) | 0.9071(0.0024) | 0.911(0.0021) | 0.94(0.0012) |
|          | p_value   | 0.00013        | 1e-05        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9148 | 0.948  | 0.8697 |  0.9186 |
| ('test_acc', 'std')  | 0.002  | 0.0025 | 0.0027 |  0.0023 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0007 |  -7.907  | less          |
|  6 | Hinge | COTO |   0.0001 | -14.175  | less          |
|  9 | EXP   | COTO |   0      | -22.7433 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9993 |  -7.907  | greater       |
|  6 | Hinge | COTO |   0.9999 | -14.175  | greater       |
|  9 | EXP   | COTO |   1      | -22.7433 | greater       |

-- Result --

| (VGG) | mean(std) | 0.9148(0.002) | 0.9186(0.0023) | 0.948(0.0025) |
|          | p_value   | 0.00069        | 7e-05        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9182 | 0.9469 | 0.8372 |  0.9185 |
| ('test_acc', 'std')  | 0.0022 | 0.0036 | 0.0038 |  0.0029 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0032 |  -5.2254 | less          |
|  6 | Hinge | COTO |   0.0022 |  -5.7936 | less          |
|  9 | EXP   | COTO |   0      | -41.2612 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9968 |  -5.2254 | greater       |
|  6 | Hinge | COTO |   0.9978 |  -5.7936 | greater       |
|  9 | EXP   | COTO |   1      | -41.2612 | greater       |

-- Result --

| (VGG) | mean(std) | 0.9182(0.0022) | 0.9185(0.0029) | 0.9469(0.0036) |
|          | p_value   | 0.0032        | 0.00221        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9143 | 0.9401 | 0.7982 |  0.9159 |
| ('test_acc', 'std')  | 0.0024 | 0.0029 | 0.0035 |  0.0017 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0003 |  -9.8624 | less          |
|  6 | Hinge | COTO |   0.0007 |  -7.8506 | less          |
|  9 | EXP   | COTO |   0      | -43.2144 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9997 |  -9.8624 | greater       |
|  6 | Hinge | COTO |   0.9993 |  -7.8506 | greater       |
|  9 | EXP   | COTO |   1      | -43.2144 | greater       |

-- Result --

| (VGG) | mean(std) | 0.9143(0.0024) | 0.9159(0.0017) | 0.9401(0.0029) |
|          | p_value   | 0.0003        | 0.00071        | ---            |

#### CIFAR - model: ResNet101 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.887  | 0.9361 | 0.6066 |  0.889  |
| ('test_acc', 'std')  | 0.0042 | 0.002  | 0.0108 |  0.0041 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0      | -17.5283 | less          |
|  6 | Hinge | COTO |   0.0002 | -10.274  | less          |
|  9 | EXP   | COTO |   0      | -33.5369 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   1      | -17.5283 | greater       |
|  6 | Hinge | COTO |   0.9998 | -10.274  | greater       |
|  9 | EXP   | COTO |   1      | -33.5369 | greater       |

-- Result --

| (ResNet101) | mean(std) | 0.887(0.0042) | 0.889(0.0041) | 0.9361(0.002) |
|          | p_value   | 3e-05        | 0.00025        | ---            |

#### CIFAR - model: ResNet50 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8874 | 0.9375 | 0.7822 |  0.8886 |
| ('test_acc', 'std')  | 0.0031 | 0.0011 | 0.0036 |  0.003  |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -16.7406 | less          |
|  6 | Hinge | COTO |        0 | -15.2397 | less          |
|  9 | EXP   | COTO |        0 | -39.497  | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -16.7406 | greater       |
|  6 | Hinge | COTO |        1 | -15.2397 | greater       |
|  9 | EXP   | COTO |        1 | -39.497  | greater       |

-- Result --

| (ResNet50) | mean(std) | 0.8874(0.0031) | 0.8886(0.003) | 0.9375(0.0011) |
|          | p_value   | 4e-05        | 5e-05        | ---            |

#### CIFAR - model: ResNet34 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9034 | 0.9393 | 0.7785 |  0.9031 |
| ('test_acc', 'std')  | 0.0022 | 0.0017 | 0.011  |  0.0015 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -14.3769 | less          |
|  6 | Hinge | COTO |   0      | -23.6843 | less          |
|  9 | EXP   | COTO |   0.0001 | -13.8046 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -14.3769 | greater       |
|  6 | Hinge | COTO |   1      | -23.6843 | greater       |
|  9 | EXP   | COTO |   0.9999 | -13.8046 | greater       |

-- Result --

| (ResNet34) | mean(std) | 0.9034(0.0022) | 0.9031(0.0015) | 0.9393(0.0017) |
|          | p_value   | 7e-05        | 1e-05        | ---            |


#### CIFAR - model: ResNet18 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8907 | 0.9391 | 0.8399 |  0.8978 |
| ('test_acc', 'std')  | 0.0027 | 0.0019 | 0.0037 |  0.0022 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -37.8192 | less          |
|  6 | Hinge | COTO |        0 | -18.4479 | less          |
|  9 | EXP   | COTO |        0 | -19.3528 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -37.8192 | greater       |
|  6 | Hinge | COTO |        1 | -18.4479 | greater       |
|  9 | EXP   | COTO |        1 | -19.3528 | greater       |

-- Result --

| (ResNet18) | mean(std) | 0.8907(0.0027) | 0.8978(0.0022) | 0.9391(0.0019) |
|          | p_value   | 0.0        | 3e-05        | ---            |

# 2 (bird) vs 4 (deer)
#### CIFAR - model: ResNet18 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.837  | 0.8986 | 0.7719 |  0.8499 |
| ('test_acc', 'std')  | 0.0037 | 0.0035 | 0.0036 |  0.0054 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -13.2897 | less          |
|  6 | Hinge | COTO |   0.0001 | -15.1454 | less          |
|  9 | EXP   | COTO |   0      | -62.9515 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -13.2897 | greater       |
|  6 | Hinge | COTO |   0.9999 | -15.1454 | greater       |
|  9 | EXP   | COTO |   1      | -62.9515 | greater       |

-- Result --

| (ResNet18) | mean(std) | 0.837(0.0037) | 0.8499(0.0054) | 0.8986(0.0035) |
|          | p_value   | 9e-05        | 6e-05        | ---            |

#### CIFAR - model: ResNet34 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8427 | 0.8987 | 0.7438 |  0.85   |
| ('test_acc', 'std')  | 0.0045 | 0.0031 | 0.0039 |  0.0027 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0004 |  -9.1147 | less          |
|  6 | Hinge | COTO |   0      | -29.1612 | less          |
|  9 | EXP   | COTO |   0      | -50.2895 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9996 |  -9.1147 | greater       |
|  6 | Hinge | COTO |   1      | -29.1612 | greater       |
|  9 | EXP   | COTO |   1      | -50.2895 | greater       |

-- Result --

| (ResNet34) | mean(std) | 0.8427(0.0045) | 0.85(0.0027) | 0.8987(0.0031) |
|          | p_value   | 0.0004        | 0.0        | ---            |

#### CIFAR - model: ResNet50 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8287 | 0.8926 | 0.7277 |  0.8223 |
| ('test_acc', 'std')  | 0.0046 | 0.0038 | 0.0057 |  0.0022 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -14.3519 | less          |
|  6 | Hinge | COTO |   0      | -17.5149 | less          |
|  9 | EXP   | COTO |   0      | -26.1919 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -14.3519 | greater       |
|  6 | Hinge | COTO |   1      | -17.5149 | greater       |
|  9 | EXP   | COTO |   1      | -26.1919 | greater       |

-- Result --

| (ResNet50) | mean(std) | 0.8287(0.0046) | 0.8223(0.0022) | 0.8926(0.0038) |
|          | p_value   | 7e-05        | 3e-05        | ---            |

#### CIFAR - model: ResNet101 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8129 | 0.881  | 0.5983 |  0.8164 |
| ('test_acc', 'std')  | 0.0019 | 0.0039 | 0.0071 |  0.005  |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -15.1846 | less          |
|  6 | Hinge | COTO |        0 | -40.8876 | less          |
|  9 | EXP   | COTO |        0 | -38.4649 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -15.1846 | greater       |
|  6 | Hinge | COTO |        1 | -40.8876 | greater       |
|  9 | EXP   | COTO |        1 | -38.4649 | greater       |

-- Result --

| (ResNet101) | mean(std) | 0.8129(0.0019) | 0.8164(0.005) | 0.881(0.0039) |
|          | p_value   | 5e-05        | 0.0        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8709 | 0.911  | 0.8377 |  0.8774 |
| ('test_acc', 'std')  | 0.0025 | 0.0009 | 0.0036 |  0.0013 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -14.4794 | less          |
|  6 | Hinge | COTO |   0      | -36.5553 | less          |
|  9 | EXP   | COTO |   0      | -16.469  | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -14.4794 | greater       |
|  6 | Hinge | COTO |   1      | -36.5553 | greater       |
|  9 | EXP   | COTO |   1      | -16.469  | greater       |

-- Result --

| (VGG) | mean(std) | 0.8709(0.0025) | 0.8774(0.0013) | 0.911(0.0009) |
|          | p_value   | 7e-05        | 0.0        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8702 | 0.9132 | 0.8037 |  0.8826 |
| ('test_acc', 'std')  | 0.002  | 0.0015 | 0.0048 |  0.0009 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0      | -28.3061 | less          |
|  6 | Hinge | COTO |   0.0001 | -13.2974 | less          |
|  9 | EXP   | COTO |   0      | -20.1193 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   1      | -28.3061 | greater       |
|  6 | Hinge | COTO |   0.9999 | -13.2974 | greater       |
|  9 | EXP   | COTO |   1      | -20.1193 | greater       |

-- Result --

| (VGG) | mean(std) | 0.8702(0.002) | 0.8826(0.0009) | 0.9132(0.0015) |
|          | p_value   | 0.0        | 9e-05        | ---            |

#### CIFAR - model: VGG ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8759 | 0.9085 | 0.7742 |  0.8783 |
| ('test_acc', 'std')  | 0.0026 | 0.0012 | 0.0057 |  0.0034 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0002 | -10.6826 | less          |
|  6 | Hinge | COTO |   0.0008 |  -7.4859 | less          |
|  9 | EXP   | COTO |   0      | -24.3048 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9998 | -10.6826 | greater       |
|  6 | Hinge | COTO |   0.9992 |  -7.4859 | greater       |
|  9 | EXP   | COTO |   1      | -24.3048 | greater       |

-- Result --

| (VGG) | mean(std) | 0.8759(0.0026) | 0.8783(0.0034) | 0.9085(0.0012) |
|          | p_value   | 0.00022        | 0.00085        | ---            |

#### CIFAR - model: DenseNet121 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8984 | 0.9376 | 0.8459 |  0.8991 |
| ('test_acc', 'std')  | 0.0034 | 0.0021 | 0.0016 |  0.0028 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0006 |  -8.3976 | less          |
|  6 | Hinge | COTO |   0      | -17.8214 | less          |
|  9 | EXP   | COTO |   0      | -64.3781 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9994 |  -8.3976 | greater       |
|  6 | Hinge | COTO |   1      | -17.8214 | greater       |
|  9 | EXP   | COTO |   1      | -64.3781 | greater       |

-- Result --

| (DenseNet121) | mean(std) | 0.8984(0.0034) | 0.8991(0.0028) | 0.9376(0.0021) |
|          | p_value   | 0.00055        | 3e-05        | ---            |

#### CIFAR - model: DenseNet169 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8964 | 0.9341 | 0.8419 |  0.9035 |
| ('test_acc', 'std')  | 0.0023 | 0.0011 | 0.0037 |  0.0025 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0      | -17.7176 | less          |
|  6 | Hinge | COTO |   0.0004 |  -9.0492 | less          |
|  9 | EXP   | COTO |   0      | -21.8748 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   1      | -17.7176 | greater       |
|  6 | Hinge | COTO |   0.9996 |  -9.0492 | greater       |
|  9 | EXP   | COTO |   1      | -21.8748 | greater       |

-- Result --

| (DenseNet169) | mean(std) | 0.8964(0.0023) | 0.9035(0.0025) | 0.9341(0.0011) |
|          | p_value   | 3e-05        | 0.00041        | ---            |

#### CIFAR - model: DenseNet201 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8928 | 0.9325 | 0.8383 |  0.8975 |
| ('test_acc', 'std')  | 0.0027 | 0.0033 | 0.0029 |  0.0022 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0      | -19.6606 | less          |
|  6 | Hinge | COTO |   0.0002 | -10.5408 | less          |
|  9 | EXP   | COTO |   0      | -16.2328 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   1      | -19.6606 | greater       |
|  6 | Hinge | COTO |   0.9998 | -10.5408 | greater       |
|  9 | EXP   | COTO |   1      | -16.2328 | greater       |

-- Result --

| (DenseNet201) | mean(std) | 0.8928(0.0027) | 0.8975(0.0022) | 0.9325(0.0033) |
|          | p_value   | 2e-05        | 0.00023        | ---            |

#### CIFAR - model: MobileNet ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7691 | 0.8162 | 0.6331 |  0.7663 |
| ('test_acc', 'std')  | 0.0059 | 0.003  | 0.0056 |  0.0055 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.0006 |  -8.0922 | less          |
|  6 | Hinge | COTO |   0.0016 |  -6.3214 | less          |
|  9 | EXP   | COTO |   0      | -49.8012 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0.9994 |  -8.0922 | greater       |
|  6 | Hinge | COTO |   0.9984 |  -6.3214 | greater       |
|  9 | EXP   | COTO |   1      | -49.8012 | greater       |

-- Result --

| (MobileNet) | mean(std) | 0.7691(0.0059) | 0.7663(0.0055) | 0.8162(0.003) |
|          | p_value   | 0.00063        | 0.0016        | ---            |

#### CIFAR - model: MobileNetV2 ####


 Step Size: {'lr': 0.001, 'type': 'SGD', 'lr_scheduler': 'CosineAnnealingLR', 'args': {'T_max': 200}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8349 | 0.882  | 0.7251 |  0.8319 |
| ('test_acc', 'std')  | 0.0019 | 0.0029 | 0.0096 |  0.0028 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -20.3936 | less          |
|  6 | Hinge | COTO |        0 | -30.4526 | less          |
|  9 | EXP   | COTO |        0 | -15.4782 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -20.3936 | greater       |
|  6 | Hinge | COTO |        1 | -30.4526 | greater       |
|  9 | EXP   | COTO |        1 | -15.4782 | greater       |

-- Result --

| (MobileNetV2) | mean(std) | 0.8349(0.0019) | 0.8319(0.0028) | 0.882(0.0029) |
|          | p_value   | 2e-05        | 0.0        | ---            |