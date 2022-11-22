from typing import List

import numpy as np
import torch
import torch.nn as nn
from torch.nn import Module
from torch.utils.data import DataLoader, TensorDataset


class MLPModel(nn.Module):
    """
    A simple feed-forward network with one input/output unit, two hidden layers and tanh activation.

    Attributes
    ----------
    hidden_sizes : int
        Number of hidden units per hidden layer
    """

    def __init__(self, hidden_sizes: List[int]):
        raise NotImplementedError

    def forward(self, x):
        raise NotImplementedError

    def predict(self, x):
        raise NotImplementedError

    def fit(self, data, targets, batch_size=5, learning_rate=5e-3, max_epochs=300):
        raise NotImplementedError


class PolynomialModel:
    def __init__(self, order: int):
        raise NotImplementedError

    def predict(self, x):
        """Compute the network output for a given input and return the result as numpy array.

        Parameters
        ----------
        x : float or numpy.array or torch.Tensor
            The model input

        Returns
        ----------
        numpy.array
            The model output
        """
        raise NotImplementedError

    def fit(self, data, targets):
        """Fit coefficients of the polynomial model on the given data.

        Parameters
        ----------
        data : numpy.array
            The input training samples
        targets : numpy.array
            The output training samples
        Returns
        ----------
        list
            The training set MSE score
        """
        raise NotImplementedError


class RBFModel:
    def __init__(self, order: int, lengthscale: float = 10.):
        raise NotImplementedError

    def predict(self, x):
        raise NotImplementedError

    def fit(self, data, targets):
        raise NotImplementedError
