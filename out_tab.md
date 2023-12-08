#### 45023 - D: 3, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.672  | 0.7104 | 0.6732 |  0.6684 |
| ('test_acc', 'std')  | 0.0014 | 0.0016 | 0.0012 |  0.0016 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -25.6073 | less          |
|  6 | Hinge | COTO |        0 | -28.5055 | less          |
|  9 | EXP   | COTO |        0 | -33.794  | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -25.6073 | greater       |
|  6 | Hinge | COTO |        1 | -28.5055 | greater       |
|  9 | EXP   | COTO |        1 | -33.794  | greater       |

-- Result --

| (256, 3) | mean(std) | 0.672(0.0014) | 0.6684(0.0016) | 0.7104(0.0016) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 23512 - D: 3, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.654  | 0.6779 | 0.6569 |  0.6499 |
| ('test_acc', 'std')  | 0.0007 | 0.0006 | 0.0006 |  0.0004 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -29.8654 | less          |
|  6 | Hinge | COTO |        0 | -42.2241 | less          |
|  9 | EXP   | COTO |        0 | -26.478  | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -29.8654 | greater       |
|  6 | Hinge | COTO |        1 | -42.2241 | greater       |
|  9 | EXP   | COTO |        1 | -26.478  | greater       |

-- Result --

| (256, 3) | mean(std) | 0.654(0.0007) | 0.6499(0.0004) | 0.6779(0.0006) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 45025 - D: 3, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |   EXP |   Hinge |
|:---------------------|-------:|-------:|------:|--------:|
| ('test_acc', 'mean') | 0.8728 | 0.8707 | 0.866 |  0.8687 |
| ('test_acc', 'std')  | 0.0016 | 0.0015 | 0.002 |  0.003  |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9203 |  1.4645 | less          |
|  6 | Hinge | COTO |   0.2821 | -0.5869 | less          |
|  9 | EXP   | COTO |   0.0027 | -3.1368 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0797 |  1.4645 | greater       |
|  6 | Hinge | COTO |   0.7179 | -0.5869 | greater       |
|  9 | EXP   | COTO |   0.9973 | -3.1368 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.8728(0.0016) | 0.8687(0.003) | 0.8707(0.0015) |
|          | p_value   | 0.9203        | 0.2821        | ---            |

#### 44128 - D: 5, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9258 | 0.9276 | 0.919  |  0.9197 |
| ('test_acc', 'std')  | 0.0008 | 0.0017 | 0.0038 |  0.005  |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0809 | -1.5239 | less          |
|  6 | Hinge | COTO |   0.0716 | -1.6034 | less          |
|  9 | EXP   | COTO |   0.0276 | -2.2011 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9191 | -1.5239 | greater       |
|  6 | Hinge | COTO |   0.9284 | -1.6034 | greater       |
|  9 | EXP   | COTO |   0.9724 | -2.2011 | greater       |

-- Result --

| (256, 5) | mean(std) | 0.9258(0.0008) | 0.9197(0.005) | 0.9276(0.0017) |
|          | p_value   | 0.08094        | 0.07165        | ---            |

#### 44157 - D: 5, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.5913 | 0.5956 | 0.591  |  0.5914 |
| ('test_acc', 'std')  | 0.0036 | 0.0031 | 0.0028 |  0.0032 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0954 | -1.4149 | less          |
|  6 | Hinge | COTO |   0.0345 | -2.0651 | less          |
|  9 | EXP   | COTO |   0.0653 | -1.6636 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9046 | -1.4149 | greater       |
|  6 | Hinge | COTO |   0.9655 | -2.0651 | greater       |
|  9 | EXP   | COTO |   0.9347 | -1.6636 | greater       |

-- Result --

| (256, 5) | mean(std) | 0.5913(0.0036) | 0.5914(0.0032) | 0.5956(0.0031) |
|          | p_value   | 0.09538        | 0.03446        | ---            |

#### 45021 - D: 3, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7191 | 0.7388 | 0.7185 |  0.7126 |
| ('test_acc', 'std')  | 0.001  | 0.0009 | 0.0007 |  0.001  |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -22.2413 | less          |
|  6 | Hinge | COTO |        0 | -27.1072 | less          |
|  9 | EXP   | COTO |        0 | -17.4168 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -22.2413 | greater       |
|  6 | Hinge | COTO |        1 | -27.1072 | greater       |
|  9 | EXP   | COTO |        1 | -17.4168 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.7191(0.001) | 0.7126(0.001) | 0.7388(0.0009) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 45024 - D: 3, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |   BCE |   COTO |    EXP |   Hinge |
|:---------------------|------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.732 | 0.7488 | 0.7252 |  0.7402 |
| ('test_acc', 'std')  | 0.002 | 0.0013 | 0.0017 |  0.0013 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 |  -9.9091 | less          |
|  6 | Hinge | COTO |        0 |  -7.8322 | less          |
|  9 | EXP   | COTO |        0 | -12.3674 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 |  -9.9091 | greater       |
|  6 | Hinge | COTO |        1 |  -7.8322 | greater       |
|  9 | EXP   | COTO |        1 | -12.3674 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.732(0.002) | 0.7402(0.0013) | 0.7488(0.0013) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 44120 - D: 3, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8071 | 0.8121 | 0.8085 |  0.8181 |
| ('test_acc', 'std')  | 0.0044 | 0.0014 | 0.0033 |  0.0023 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.1616 | -1.0242 | less          |
|  6 | Hinge | COTO |   0.9896 |  2.6069 | less          |
|  9 | EXP   | COTO |   0.1212 | -1.2208 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.8384 | -1.0242 | greater       |
|  6 | Hinge | COTO |   0.0104 |  2.6069 | greater       |
|  9 | EXP   | COTO |   0.8788 | -1.2208 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.8071(0.0044) | 0.8181(0.0023) | 0.8121(0.0014) |
|          | p_value   | 0.16156        | 0.98965        | ---            |

#### 44123 - D: 3, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8611 | 0.8734 | 0.86   |  0.8598 |
| ('test_acc', 'std')  | 0.0016 | 0.001  | 0.0009 |  0.0012 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 |  -8.8571 | less          |
|  6 | Hinge | COTO |        0 | -15.5572 | less          |
|  9 | EXP   | COTO |        0 |  -9.9955 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 |  -8.8571 | greater       |
|  6 | Hinge | COTO |        1 | -15.5572 | greater       |
|  9 | EXP   | COTO |        1 |  -9.9955 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.8611(0.0016) | 0.8598(0.0012) | 0.8734(0.001) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 43973 - D: 3, H: 256 ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8688 | 0.8385 | 0.8668 |  0.8685 |
| ('test_acc', 'std')  | 0.0025 | 0.0025 | 0.0019 |  0.0023 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |        1 | 14.3824 | less          |
|  6 | Hinge | COTO |        1 | 11.4517 | less          |
|  9 | EXP   | COTO |        1 | 14.7753 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |        0 | 14.3824 | greater       |
|  6 | Hinge | COTO |        0 | 11.4517 | greater       |
|  9 | EXP   | COTO |        0 | 14.7753 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.8688(0.0025) | 0.8685(0.0023) | 0.8385(0.0025) |
|          | p_value   | 1.0        | 1.0        | ---            |

#### 43973 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8666 | 0.8691 | 0.8662 |  0.8713 |
| ('test_acc', 'std')  | 0.0029 | 0.0025 | 0.0038 |  0.0027 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.1404 | -1.122  | less          |
|  6 | Hinge | COTO |   0.8855 |  1.2578 | less          |
|  9 | EXP   | COTO |   0.2399 | -0.7259 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.8596 | -1.122  | greater       |
|  6 | Hinge | COTO |   0.1145 |  1.2578 | greater       |
|  9 | EXP   | COTO |   0.7601 | -0.7259 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.8666(0.0029) | 0.8713(0.0027) | 0.8691(0.0025) |
|          | p_value   | 0.14036        | 0.88548        | ---            |

#### 44125 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8352 | 0.8445 | 0.8382 |  0.8312 |
| ('test_acc', 'std')  | 0.0011 | 0.0018 | 0.0015 |  0.0014 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0      |  -7.4586 | less          |
|  6 | Hinge | COTO |   0      | -10.7088 | less          |
|  9 | EXP   | COTO |   0.0012 |  -3.6739 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   1      |  -7.4586 | greater       |
|  6 | Hinge | COTO |   1      | -10.7088 | greater       |
|  9 | EXP   | COTO |   0.9988 |  -3.6739 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.8352(0.0011) | 0.8312(0.0014) | 0.8445(0.0018) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 45025 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.854  | 0.8768 | 0.8602 |  0.8576 |
| ('test_acc', 'std')  | 0.0031 | 0.0012 | 0.0027 |  0.002  |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0      | -8.3484 | less          |
|  6 | Hinge | COTO |   0      | -8.1308 | less          |
|  9 | EXP   | COTO |   0.0001 | -4.9347 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   1      | -8.3484 | greater       |
|  6 | Hinge | COTO |   1      | -8.1308 | greater       |
|  9 | EXP   | COTO |   0.9999 | -4.9347 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.854(0.0031) | 0.8576(0.002) | 0.8768(0.0012) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 44120 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8197 | 0.8223 | 0.8019 |  0.8234 |
| ('test_acc', 'std')  | 0.0015 | 0.0008 | 0.0068 |  0.0012 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0514 | -1.745  | less          |
|  6 | Hinge | COTO |   0.8053 |  0.8883 | less          |
|  9 | EXP   | COTO |   0.0051 | -2.9711 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9486 | -1.745  | greater       |
|  6 | Hinge | COTO |   0.1947 |  0.8883 | greater       |
|  9 | EXP   | COTO |   0.9949 | -2.9711 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.8197(0.0015) | 0.8234(0.0012) | 0.8223(0.0008) |
|          | p_value   | 0.05145        | 0.80531        | ---            |

#### 44123 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8513 | 0.8651 | 0.8498 |  0.8479 |
| ('test_acc', 'std')  | 0.0012 | 0.0013 | 0.004  |  0.0009 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   0      |  -9.2093 | less          |
|  6 | Hinge | COTO |   0      | -20.208  | less          |
|  9 | EXP   | COTO |   0.0013 |  -3.6686 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |   1      |  -9.2093 | greater       |
|  6 | Hinge | COTO |   1      | -20.208  | greater       |
|  9 | EXP   | COTO |   0.9987 |  -3.6686 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.8513(0.0012) | 0.8479(0.0009) | 0.8651(0.0013) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 44128 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9242 | 0.935  | 0.9243 |  0.9237 |
| ('test_acc', 'std')  | 0.0005 | 0.0005 | 0.001  |  0.0007 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -14.3397 | less          |
|  6 | Hinge | COTO |        0 | -13.4468 | less          |
|  9 | EXP   | COTO |        0 |  -9.5809 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -14.3397 | greater       |
|  6 | Hinge | COTO |        1 | -13.4468 | greater       |
|  9 | EXP   | COTO |        1 |  -9.5809 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.9242(0.0005) | 0.9237(0.0007) | 0.935(0.0005) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 23512 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.6562 | 0.6589 | 0.6563 |  0.657  |
| ('test_acc', 'std')  | 0.0009 | 0.0011 | 0.0009 |  0.0007 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0432 | -1.845  | less          |
|  6 | Hinge | COTO |   0.0789 | -1.4923 | less          |
|  9 | EXP   | COTO |   0.0453 | -1.8179 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9568 | -1.845  | greater       |
|  6 | Hinge | COTO |   0.9211 | -1.4923 | greater       |
|  9 | EXP   | COTO |   0.9547 | -1.8179 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.6562(0.0009) | 0.657(0.0007) | 0.6589(0.0011) |
|          | p_value   | 0.04315        | 0.0789        | ---            |

#### 45021 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7238 | 0.7263 | 0.7013 |  0.7211 |
| ('test_acc', 'std')  | 0.0011 | 0.0011 | 0.0065 |  0.0006 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0146 | -2.4289 | less          |
|  6 | Hinge | COTO |   0.0001 | -4.8214 | less          |
|  9 | EXP   | COTO |   0.0008 | -3.8884 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9854 | -2.4289 | greater       |
|  6 | Hinge | COTO |   0.9999 | -4.8214 | greater       |
|  9 | EXP   | COTO |   0.9992 | -3.8884 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.7238(0.0011) | 0.7211(0.0006) | 0.7263(0.0011) |
|          | p_value   | 0.0146        | 0.00014        | ---            |

#### 45021 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7238 | 0.7263 | 0.7013 |  0.7211 |
| ('test_acc', 'std')  | 0.0011 | 0.0011 | 0.0065 |  0.0006 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0146 | -2.4289 | less          |
|  6 | Hinge | COTO |   0.0001 | -4.8214 | less          |
|  9 | EXP   | COTO |   0.0008 | -3.8884 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9854 | -2.4289 | greater       |
|  6 | Hinge | COTO |   0.9999 | -4.8214 | greater       |
|  9 | EXP   | COTO |   0.9992 | -3.8884 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.7238(0.0011) | 0.7211(0.0006) | 0.7263(0.0011) |
|          | p_value   | 0.0146        | 0.00014        | ---            |

#### 45024 - D: 3, H: 256 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7126 | 0.7547 | 0.7116 |  0.7174 |
| ('test_acc', 'std')  | 0.0028 | 0.0023 | 0.0033 |  0.0023 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -14.6815 | less          |
|  6 | Hinge | COTO |        0 | -20.0926 | less          |
|  9 | EXP   | COTO |        0 | -10.7921 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -14.6815 | greater       |
|  6 | Hinge | COTO |        1 | -20.0926 | greater       |
|  9 | EXP   | COTO |        1 | -10.7921 | greater       |

-- Result --

| (256, 3) | mean(std) | 0.7126(0.0028) | 0.7174(0.0023) | 0.7547(0.0023) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 44123 - model: FTTransformer ####


 Step Size: {'lr': 1e-05, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8584 | 0.8708 | 0.8595 |  0.8723 |
| ('test_acc', 'std')  | 0.0014 | 0.0013 | 0.0014 |  0.0014 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |    0     | -8.6573 | less          |
|  6 | Hinge | COTO |    0.883 |  1.2436 | less          |
|  9 | EXP   | COTO |    0     | -7.1699 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |    1     | -8.6573 | greater       |
|  6 | Hinge | COTO |    0.117 |  1.2436 | greater       |
|  9 | EXP   | COTO |    1     | -7.1699 | greater       |

#### 44123 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8483 | 0.8534 | 0.8441 |  0.851  |
| ('test_acc', 'std')  | 0.0016 | 0.001  | 0.0034 |  0.0013 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0017 | -3.5093 | less          |
|  6 | Hinge | COTO |   0.0398 | -1.8909 | less          |
|  9 | EXP   | COTO |   0.0046 | -3.0176 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9983 | -3.5093 | greater       |
|  6 | Hinge | COTO |   0.9602 | -1.8909 | greater       |
|  9 | EXP   | COTO |   0.9954 | -3.0176 | greater       |

#### 44120 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8186 | 0.8247 | 0.8038 |  0.8211 |
| ('test_acc', 'std')  | 0.0016 | 0.0009 | 0.0065 |  0.0016 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.001  | -3.7965 | less          |
|  6 | Hinge | COTO |   0.0122 | -2.5228 | less          |
|  9 | EXP   | COTO |   0.0036 | -3.1389 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.999  | -3.7965 | greater       |
|  6 | Hinge | COTO |   0.9878 | -2.5228 | greater       |
|  9 | EXP   | COTO |   0.9964 | -3.1389 | greater       |

#### 43973 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8692 | 0.8682 | 0.8671 |  0.8719 |
| ('test_acc', 'std')  | 0.0025 | 0.0023 | 0.0034 |  0.0018 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.655  |  0.4072 | less          |
|  6 | Hinge | COTO |   0.9455 |  1.7118 | less          |
|  9 | EXP   | COTO |   0.3881 | -0.2898 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.345  |  0.4072 | greater       |
|  6 | Hinge | COTO |   0.0545 |  1.7118 | greater       |
|  9 | EXP   | COTO |   0.6119 | -0.2898 | greater       |

-- Result --

| (TabMLP5) | mean(std) | 0.8692(0.0025) | 0.8719(0.0018) | 0.8682(0.0023) |
|          | p_value   | 0.65501        | 0.9455        | ---            |

#### 44128 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.9214 | 0.9295 | 0.913  |  0.9223 |
| ('test_acc', 'std')  | 0.0007 | 0.0006 | 0.0068 |  0.0006 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0      | -8.8057 | less          |
|  6 | Hinge | COTO |   0      | -8.4062 | less          |
|  9 | EXP   | COTO |   0.0149 | -2.4168 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   1      | -8.8057 | greater       |
|  6 | Hinge | COTO |   1      | -8.4062 | greater       |
|  9 | EXP   | COTO |   0.9851 | -2.4168 | greater       |

-- Result --

| (TabMLP5) | mean(std) | 0.9214(0.0007) | 0.9223(0.0006) | 0.9295(0.0006) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 44125 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8317 | 0.8372 | 0.8373 |  0.827  |
| ('test_acc', 'std')  | 0.0015 | 0.001  | 0.0014 |  0.0016 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0034 | -3.1691 | less          |
|  6 | Hinge | COTO |   0      | -6.1006 | less          |
|  9 | EXP   | COTO |   0.5296 |  0.0756 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9966 | -3.1691 | greater       |
|  6 | Hinge | COTO |   1      | -6.1006 | greater       |
|  9 | EXP   | COTO |   0.4704 |  0.0756 | greater       |

-- Result --

| (TabMLP5) | mean(std) | 0.8317(0.0015) | 0.827(0.0016) | 0.8372(0.001) |
|          | p_value   | 0.00341        | 1e-05        | ---            |

#### 23512 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.6575 | 0.6675 | 0.6504 |  0.6582 |
| ('test_acc', 'std')  | 0.0007 | 0.0008 | 0.0016 |  0.0008 |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -12.7881 | less          |
|  6 | Hinge | COTO |        0 |  -7.6316 | less          |
|  9 | EXP   | COTO |        0 |  -9.7752 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -12.7881 | greater       |
|  6 | Hinge | COTO |        1 |  -7.6316 | greater       |
|  9 | EXP   | COTO |        1 |  -9.7752 | greater       |

-- Result --

| (TabMLP5) | mean(std) | 0.6575(0.0007) | 0.6582(0.0008) | 0.6675(0.0008) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 44157 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.5936 | 0.591  | 0.5656 |  0.5946 |
| ('test_acc', 'std')  | 0.0023 | 0.0021 | 0.0056 |  0.0026 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.8763 |  1.207  | less          |
|  6 | Hinge | COTO |   0.9005 |  1.3482 | less          |
|  9 | EXP   | COTO |   0.001  | -3.765  | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.1237 |  1.207  | greater       |
|  6 | Hinge | COTO |   0.0995 |  1.3482 | greater       |
|  9 | EXP   | COTO |   0.999  | -3.765  | greater       |

-- Result --

| (TabMLP5) | mean(std) | 0.5936(0.0023) | 0.5946(0.0026) | 0.591(0.0021) |
|          | p_value   | 0.87628        | 0.9005        | ---            |

#### 45021 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.7239 | 0.7302 | 0.7051 |  0.7259 |
| ('test_acc', 'std')  | 0.0011 | 0.0009 | 0.0038 |  0.0009 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.001  | -3.7668 | less          |
|  6 | Hinge | COTO |   0.0019 | -3.4544 | less          |
|  9 | EXP   | COTO |   0      | -6.5019 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.999  | -3.7668 | greater       |
|  6 | Hinge | COTO |   0.9981 | -3.4544 | greater       |
|  9 | EXP   | COTO |   1      | -6.5019 | greater       |

-- Result --

| (TabMLP5) | mean(std) | 0.7239(0.0011) | 0.7259(0.0009) | 0.7302(0.0009) |
|          | p_value   | 0.00104        | 0.00194        | ---            |

#### 45024 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.6914 | 0.7279 | 0.7032 |  0.6972 |
| ('test_acc', 'std')  | 0.0029 | 0.003  | 0.0036 |  0.003  |

-- Testing --

|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        0 | -12.5702 | less          |
|  6 | Hinge | COTO |        0 |  -9.0008 | less          |
|  9 | EXP   | COTO |        0 |  -8.5578 | less          |
|    | A     | B    |   pvalue |     stat | alternative   |
|---:|:------|:-----|---------:|---------:|:--------------|
|  3 | BCE   | COTO |        1 | -12.5702 | greater       |
|  6 | Hinge | COTO |        1 |  -9.0008 | greater       |
|  9 | EXP   | COTO |        1 |  -8.5578 | greater       |

-- Result --

| (TabMLP5) | mean(std) | 0.6914(0.0029) | 0.6972(0.003) | 0.7279(0.003) |
|          | p_value   | 0.0        | 0.0        | ---            |

#### 45025 - model: TabMLP5 ####


 Step Size: {'lr': 0.0001, 'type': 'Adam', 'lr_scheduler': 'ConstantLR', 'args': {'factor': 0.3333333333333333, 'total_iters': 1}} 


-- Performance --

|                      |    BCE |   COTO |    EXP |   Hinge |
|:---------------------|-------:|-------:|-------:|--------:|
| ('test_acc', 'mean') | 0.8533 | 0.8655 | 0.8515 |  0.8524 |
| ('test_acc', 'std')  | 0.0022 | 0.0022 | 0.0058 |  0.0031 |

-- Testing --

|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.0001 | -5.0457 | less          |
|  6 | Hinge | COTO |   0.0027 | -3.2948 | less          |
|  9 | EXP   | COTO |   0.0153 | -2.4042 | less          |
|    | A     | B    |   pvalue |    stat | alternative   |
|---:|:------|:-----|---------:|--------:|:--------------|
|  3 | BCE   | COTO |   0.9999 | -5.0457 | greater       |
|  6 | Hinge | COTO |   0.9973 | -3.2948 | greater       |
|  9 | EXP   | COTO |   0.9847 | -2.4042 | greater       |

-- Result --

| (TabMLP5) | mean(std) | 0.8533(0.0022) | 0.8524(0.0031) | 0.8655(0.0022) |
|          | p_value   | 9e-05        | 0.00266        | ---            |
