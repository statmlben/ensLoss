import numpy as np
import pandas as pd
from torch import einsum
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, models, transforms
# from tab_transformer_pytorch import TabTransformer
from einops import rearrange, repeat

# feedforward and attention

class GEGLU(nn.Module):
    def forward(self, x):
        x, gates = x.chunk(2, dim = -1)
        return x * F.gelu(gates)

def FeedForward(dim, mult = 4, dropout = 0.):
    return nn.Sequential(
        nn.LayerNorm(dim),
        nn.Linear(dim, dim * mult * 2),
        GEGLU(),
        nn.Dropout(dropout),
        nn.Linear(dim * mult, dim)
    )

class Attention(nn.Module):
    def __init__(
        self,
        dim,
        heads = 8,
        dim_head = 64,
        dropout = 0.
    ):
        super().__init__()
        inner_dim = dim_head * heads
        self.heads = heads
        self.scale = dim_head ** -0.5

        self.norm = nn.LayerNorm(dim)

        self.to_qkv = nn.Linear(dim, inner_dim * 3, bias = False)
        self.to_out = nn.Linear(inner_dim, dim, bias = False)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        h = self.heads

        x = self.norm(x)

        q, k, v = self.to_qkv(x).chunk(3, dim = -1)
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h = h), (q, k, v))
        q = q * self.scale

        sim = einsum('b h i d, b h j d -> b h i j', q, k)

        attn = sim.softmax(dim = -1)
        dropped_attn = self.dropout(attn)

        out = einsum('b h i j, b h j d -> b h i d', dropped_attn, v)
        out = rearrange(out, 'b h n d -> b n (h d)', h = h)
        out = self.to_out(out)

        return out, attn

# transformer

class Transformer(nn.Module):
    def __init__(
        self,
        dim,
        depth,
        heads,
        dim_head,
        attn_dropout,
        ff_dropout
    ):
        super().__init__()
        self.layers = nn.ModuleList([])

        for _ in range(depth):
            self.layers.append(nn.ModuleList([
                Attention(dim, heads = heads, dim_head = dim_head, dropout = attn_dropout),
                FeedForward(dim, dropout = ff_dropout),
            ]))

    def forward(self, x, return_attn = False):
        post_softmax_attns = []

        for attn, ff in self.layers:
            attn_out, post_softmax_attn = attn(x)
            post_softmax_attns.append(post_softmax_attn)

            x = attn_out + x
            x = ff(x) + x

        if not return_attn:
            return x

        return x, torch.stack(post_softmax_attns)

# numerical embedder

class NumericalEmbedder(nn.Module):
    def __init__(self, dim, num_numerical_types):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(num_numerical_types, dim))
        self.biases = nn.Parameter(torch.randn(num_numerical_types, dim))

    def forward(self, x):
        x = rearrange(x, 'b n -> b n 1')
        return x * self.weights + self.biases

# main class

class TabMLP(nn.Module):
    def __init__(self, input_shape=12, H=128, D=1):
        super(TabMLP, self).__init__()
        self.H = H
        self.D = D
        self.layer_1 = nn.Linear(input_shape, H) 
        self.layer_2 = nn.Linear(H, H)
        self.layer_3 = nn.Linear(H, H)
        self.layer_out = nn.Linear(H, 1)
        self.relu = nn.ReLU()
        self.batchnorm1 = nn.BatchNorm1d(H)
        self.batchnorm2 = nn.BatchNorm1d(H)
        self.batchnorm3 = nn.BatchNorm1d(H)

    def forward(self, inputs):
        x = self.relu(self.layer_1(inputs))
        x = self.batchnorm1(x)
        if self.D > 1:
            x = self.relu(self.layer_2(x))
            x = self.batchnorm2(x)
        if self.D > 2:
            x = self.relu(self.layer_3(x))
            x = self.batchnorm3(x)
        # x = self.dropout(x)
        x = self.layer_out(x)
        return x

class TabMLP5(nn.Module):
    def __init__(self, input_shape=12, H=128):
        super(TabMLP5, self).__init__()
        self.H = H
        self.D = 5
        self.layer_1 = nn.Linear(input_shape, H) 
        self.layer_2 = nn.Linear(H, H)
        self.layer_3 = nn.Linear(H, H)
        self.layer_4 = nn.Linear(H, H)
        self.layer_5 = nn.Linear(H, H)

        self.batchnorm1 = nn.BatchNorm1d(H)
        self.batchnorm2 = nn.BatchNorm1d(H)
        self.batchnorm3 = nn.BatchNorm1d(H)
        self.batchnorm4 = nn.BatchNorm1d(H)
        self.batchnorm5 = nn.BatchNorm1d(H)

        self.layer_out = nn.Linear(H, 1)
        self.relu = nn.ReLU()

    def forward(self, inputs):
        x = self.relu(self.layer_1(inputs))
        x = self.batchnorm1(x)
        x = self.relu(self.layer_2(x))
        x = self.batchnorm2(x)
        x = self.relu(self.layer_3(x))
        x = self.batchnorm3(x)
        x = self.relu(self.layer_4(x))
        x = self.batchnorm4(x)
        x = self.relu(self.layer_5(x))
        x = self.batchnorm5(x)
        x = self.layer_out(x)
        return x

# adapted from "https://github.com/lucidrains/tab-transformer-pytorch/blob/main/tab_transformer_pytorch/ft_transformer.py"
class FTTransformer(nn.Module):
    def __init__(
        self,
        *,
        input_shape,
        dim=512,
        depth=6,
        heads=8,
        categories=tuple(),
        dim_head = 64,
        dim_out = 1,
        num_special_tokens = 2,
        attn_dropout = 0.2,
        ff_dropout = 0.1
    ):
        super().__init__()
        assert all(map(lambda n: n > 0, categories)), 'number of each category must be positive'
        assert len(categories) + input_shape > 0, 'input shape must not be null'

        # categories related calculations

        self.num_categories = len(categories)
        self.num_unique_categories = sum(categories)

        # create category embeddings table

        self.num_special_tokens = num_special_tokens
        total_tokens = self.num_unique_categories + num_special_tokens

        # for automatically offsetting unique category ids to the correct position in the categories embedding table

        if self.num_unique_categories > 0:
            categories_offset = F.pad(torch.tensor(list(categories)), (1, 0), value = num_special_tokens)
            categories_offset = categories_offset.cumsum(dim = -1)[:-1]
            self.register_buffer('categories_offset', categories_offset)

            # categorical embedding

            self.categorical_embeds = nn.Embedding(total_tokens, dim)

        # continuous

        self.input_shape = input_shape

        if self.input_shape > 0:
            self.numerical_embedder = NumericalEmbedder(dim, self.input_shape)

        # cls token

        self.cls_token = nn.Parameter(torch.randn(1, 1, dim))

        # transformer

        self.transformer = Transformer(
            dim = dim,
            depth = depth,
            heads = heads,
            dim_head = dim_head,
            attn_dropout = attn_dropout,
            ff_dropout = ff_dropout
        )

        # to logits

        self.to_logits = nn.Sequential(
            nn.LayerNorm(dim),
            nn.ReLU(),
            nn.Linear(dim, dim_out)
        )

    def forward(self, x_numer, return_attn = False):
    # def forward(self, x_categ, x_numer, return_attn = False):
        # assert x_categ.shape[-1] == self.num_categories, f'you must pass in {self.num_categories} values for your categories input'

        xs = []
        # if self.num_unique_categories > 0:
        #     x_categ = x_categ + self.categories_offset

        #     x_categ = self.categorical_embeds(x_categ)

        #     xs.append(x_categ)

        # # add numerically embedded tokens
        if self.input_shape > 0:
            x_numer = self.numerical_embedder(x_numer)

            xs.append(x_numer)

        # concat categorical and numerical

        x = torch.cat(xs, dim = 1)

        # append cls tokens
        b = x.shape[0]
        cls_tokens = repeat(self.cls_token, '1 1 d -> b 1 d', b = b)
        x = torch.cat((cls_tokens, x), dim = 1)

        # attend

        x, attns = self.transformer(x, return_attn = True)

        # get cls token

        x = x[:, 0]

        # out in the paper is linear(relu(ln(cls)))

        logits = self.to_logits(x)

        if not return_attn:
            return logits

        return logits, attns
