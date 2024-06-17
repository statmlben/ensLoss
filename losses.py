""" Loss functions for Binary Classification"""

# Authors: Ben Dai <bendai@cuhk.edu.hk>
# License: MIT License

import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class ensLoss(nn.Module):
    def __init__(self, dist=torch.distributions.exponential.Exponential(1 / 1.)):
        super(ensLoss, self).__init__()
        self.dist = dist
        self.lam = 0.0
        ## How often should the loss function be updated in SGD, based on `self.period` the number of steps?
        self.period = 10

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
        
        # generate random loss from the inverse Box-Cox transformation
        rd_grad = torch.randn((g_num,))
        rd_grad = - self.BC_inv(rd_grad)
        rd_grad, _ = torch.sort(rd_grad)
        rd_grad = np.maximum(rd_grad, -1.0)
        _, ind_tmp = torch.sort(s_batch)
        g_batch[ind_tmp] = rd_grad

        ## superlinear tail of the loss-derivatives
        pos_ind = s_batch > 1.0
        if len(s_batch[pos_ind]) > 0:
            g_batch[pos_ind] *= (1 / s_batch[pos_ind] ).detach()
        
        g_batch = g_batch.detach() - 1e-6

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

class BinFocal(nn.Module):
    def __init__(self, gamma=2.0, weight=None, reduction='mean'):
        super(BinFocal, self).__init__()
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, output, target):
        loss = sigmoid_focal_loss(inputs=output, 
                                  targets=target, 
                                  gamma=self.gamma, 
                                  reduction=self.reduction)
        return loss    

def sigmoid_focal_loss(
    inputs: torch.Tensor,
    targets: torch.Tensor,
    alpha: float = -1,
    gamma: float = 2,
    reduction: str = "none",
) -> torch.Tensor:
    """
    Loss used in RetinaNet for dense detection: https://arxiv.org/abs/1708.02002.

    Args:
        inputs (Tensor): A float tensor of arbitrary shape.
                The predictions for each example.
        targets (Tensor): A float tensor with the same shape as inputs. Stores the binary
                classification label for each element in inputs
                (0 for the negative class and 1 for the positive class).
        alpha (float): Weighting factor in range (0,1) to balance
                positive vs negative examples or -1 for ignore. Default: ``0.25``.
        gamma (float): Exponent of the modulating factor (1 - p_t) to
                balance easy vs hard examples. Default: ``2``.
        reduction (string): ``'none'`` | ``'mean'`` | ``'sum'``
                ``'none'``: No reduction will be applied to the output.
                ``'mean'``: The output will be averaged.
                ``'sum'``: The output will be summed. Default: ``'none'``.
    Returns:
        Loss tensor with the reduction option applied.
    """
    # Original implementation from https://github.com/facebookresearch/fvcore/blob/master/fvcore/nn/focal_loss.py

    p = torch.sigmoid(inputs)
    ce_loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction="none")
    p_t = p * targets + (1 - p) * (1 - targets)
    loss = ce_loss * ((1 - p_t) ** gamma)

    if alpha >= 0:
        alpha_t = alpha * targets + (1 - alpha) * (1 - targets)
        loss = alpha_t * loss

    # Check reduction option and return loss accordingly
    if reduction == "none":
        pass
    elif reduction == "mean":
        loss = loss.mean()
    elif reduction == "sum":
        loss = loss.sum()
    else:
        raise ValueError(
            f"Invalid Value for arg 'reduction': '{reduction} \n Supported reduction modes: 'none', 'mean', 'sum'"
        )
    return loss

class Hinge(nn.Module):
    def __init__(self, reduction='mean'):
        super(Hinge, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = torch.maximum(1. - score, torch.zeros_like(score))
        if self.reduction == 'mean':
            loss_out = loss.mean()
        elif self.reduction == 'sum':
            loss_out = loss.sum()
        else: 
            raise Exception("Sorry, reduction of loss must be mean or sum") 
        return loss_out

class EXP(nn.Module):
    def __init__(self, reduction='mean'):
        super(EXP, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = torch.exp(-score)
        if self.reduction == 'mean':
            loss_out = loss.mean()
        elif self.reduction == 'sum':
            loss_out = loss.sum()
        else: 
            raise Exception("Sorry, reduction of loss must be mean or sum") 
        return loss_out

class sqrt_Hinge(nn.Module):
    def __init__(self, reduction='mean'):
        super(sqrt_Hinge, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = (score <= 1.0) * (1.0 - score) - 2 * (score > 1.0) * (torch.sqrt(abs(score) - 1))
        # loss = (score <= 1.0) * (1.0 - score) - 0 * (score > 1.0)
        if self.reduction == 'mean':
            loss_out = loss.mean()
        elif self.reduction == 'sum':
            loss_out = loss.sum()
        else:
            raise Exception("Sorry, reduction of loss must be mean or sum") 
        return loss_out

class Inv_Log_Hinge(nn.Module):
    def __init__(self, reduction='mean'):
        super(Inv_Log_Hinge, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = (score <= 1.0) * (1.0 - score) + (score > 1.0) * (torch.e / torch.log(abs(score) + torch.e - 1) - torch.e)
        if self.reduction == 'mean':
            loss_out = loss.mean()
        elif self.reduction == 'sum':
            loss_out = loss.sum()
        else:
            raise Exception("Sorry, reduction of loss must be mean or sum") 
        return loss_out

class Log_Hinge(nn.Module):
    def __init__(self, reduction='mean'):
        super(Log_Hinge, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = (score <= 1.0) * (1.0 - score) - (score > 1.0) * torch.log(abs(score))
        if self.reduction == 'mean':
            loss_out = loss.mean()
        elif self.reduction == 'sum':
            loss_out = loss.sum()
        else:
            raise Exception("Sorry, reduction of loss must be mean or sum") 
        return loss_out

class Exp_Hinge(nn.Module):
    def __init__(self, reduction='mean'):
        super(Exp_Hinge, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = (score <= 1.0) * (1.0 - score) - (score > 1.0) * torch.exp(- (score - 1))
        if self.reduction == 'mean':
            loss_out = loss.mean()
        elif self.reduction == 'sum':
            loss_out = loss.sum()
        else:
            raise Exception("Sorry, reduction of loss must be mean or sum") 
        return loss_out


class Inv_Hinge(nn.Module):
    def __init__(self, reduction='mean'):
        super(Inv_Hinge, self).__init__()
        self.reduction = reduction

    def forward(self, output, target):
        target = 2.*target - 1.
        score = output * target
        loss = (score <= 1.0) * (1.0 - score) + (score > 1.0) * (1 / score - 1)
        if self.reduction == 'mean':
            loss_out = loss.mean()
        elif self.reduction == 'sum':
            loss_out = loss.sum()
        else:
            raise Exception("Sorry, reduction of loss must be mean or sum") 
        return loss_out