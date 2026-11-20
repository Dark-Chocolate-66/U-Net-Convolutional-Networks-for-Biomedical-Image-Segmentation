"""Scores and losses for binary segmentation 

Shapes: logits / pred / target are tensors of shape (B, 1, H, W).
target holds 0.0 or 1.0. logits are raw scores (before sigmoid).
"""
import torch
import torch.nn.functional as F


def dice_score(pred, target, eps=1e-6):
    pred = pred.flatten(1)
    target = target.flatten(1)
    overlap = (pred * target).sum(dim=1)
    return ((2 * overlap + eps) / (pred.sum(dim=1) + target.sum(dim=1) + eps)).mean()


def iou_score(pred, target, eps=1e-6):
    pred = pred.flatten(1)
    target = target.flatten(1)
    overlap = (pred * target).sum(dim=1)
    union = pred.sum(dim=1) + target.sum(dim=1) - overlap
    return ((overlap + eps) / (union + eps)).mean()


def bce_loss(logits, target):
    return F.binary_cross_entropy_with_logits(logits, target)


def dice_loss(logits, target):
    return 1 - dice_score(torch.sigmoid(logits), target)
