import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim

class COTO(nn.Module):
    def __init__(self, dist=torch.distributions.exponential.Exponential(1 / 1.)):
        super(COTO, self).__init__()
        self.dist = dist
        self.lam = 0.0

    def BC_inv(self, z):
        if self.lam == 0.:
            return torch.exp(z)
        else:
            diff = 1. + self.lam*z
            return (torch.where(diff > 0.0, diff, 0.0))**(1.0/self.lam)

    def forward(self, output, target):
        target = 2.*target - 1.
        batch_size_tmp = len(target)
        s_batch = torch.zeros(batch_size_tmp+1)
        s_batch[:-1] = output.flatten()*target.flatten()

        ## generate random gradient
        g_num = batch_size_tmp + 1
        g_batch = torch.zeros(g_num)
        
        # sample from dist
        # rd_grad = - self.dist.sample((g_num,)).flatten()
        
        # generate random loss from Box-Cox transformation
        rd_grad = torch.randn((g_num,))
        rd_grad = - self.BC_inv(rd_grad)
        rd_grad, _ = torch.sort(rd_grad)
        rd_grad = np.maximum(rd_grad, -1.0)
        _, ind_tmp = torch.sort(s_batch)
        g_batch[ind_tmp] = rd_grad

        ## refine decay of the gradient sequence
        pos_ind = s_batch > 1.0
        if len(s_batch[pos_ind]) > 0:
            g_batch[pos_ind] *= (1 / s_batch[pos_ind]).detach()

        ## genrate gradient via inverse Box-Cox transformation (fair performance)
        # g_batch = - self.BC_inv(-s_batch)
        
        ## standarize the scale of a random loss; Grad(0) = -1
        g_batch = g_batch.detach() - 1e-6
        # g_batch = g_batch / abs(g_batch[-1])

        ## refine grad by heavy tail (almost no change)
        # exp_batch = - torch.exp(-s_batch)
        # g_batch = torch.where(s_batch > 1.0, torch.maximum(exp_batch, g_batch), g_batch)

        ## final gradient
        loss = g_batch[:-1] * s_batch[:-1]
        loss = loss.mean()
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