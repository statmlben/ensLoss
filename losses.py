import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim

class COTO(nn.Module):
    def __init__(self, dist=torch.distributions.exponential.Exponential(1 / 1.)):
        super(COTO, self).__init__()
        self.dist = dist

    def forward(self, output, target):
        target = 2.*target - 1.
        batch_size_tmp = len(target)
        s_batch = torch.zeros(batch_size_tmp+1)
        s_batch[:-1] = output.flatten()*target.flatten()

        ## generate random gradient
        g_batch = torch.zeros(batch_size_tmp+1)
        rd_grad = - self.dist.sample((batch_size_tmp+1,)).flatten()
        rd_grad, _ = torch.sort(rd_grad)
        _, ind_tmp = torch.sort(s_batch)
        g_batch[ind_tmp] = rd_grad

        ## generate log gradient
        # exp_batch = (-1.0/(1.0+torch.exp(torch.rand(1)*(s_batch - torch.rand(1))))).detach()
        # log_batch = -(torch.exp(-torch.rand(1)*s_batch)).detach()
        # g_batch = exp_batch

        ## standarize the scale of a random loss; Grad(0) = -1
        g_batch = g_batch / abs(g_batch[-1])

        ## refine grad by heavy tail
        exp_batch = - torch.exp(-s_batch)
        g_batch = torch.where(s_batch > 1.0, torch.maximum(exp_batch, g_batch), g_batch)

        g_batch = g_batch.detach()
        ## final gradient
        loss = g_batch[:-1] * s_batch[:-1]
        loss = loss.mean()
        # print(g_batch)
        return loss

class BCELoss(nn.Module):
    def __init__(self, weight=None, reduction='mean'):
        super(BCELoss, self).__init__()
        self.BCE = nn.BCEWithLogitsLoss(weight=weight, reduction=reduction)

    def forward(self, output, target):
        loss = self.BCE(output, target)
        return loss

class Hinge(nn.Module):
    def __init__(self, reduction='mean'):
        super(Hinge, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = torch.maximum(1. - score, torch.zeros_like(score))
        return loss.mean()

class EXP(nn.Module):
    def __init__(self, reduction='mean'):
        super(EXP, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = torch.exp(-score)
        return loss.mean()