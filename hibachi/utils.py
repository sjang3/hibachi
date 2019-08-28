# Copyright 2019 Balaji Veeramani. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility functions for feature selection methods."""
import torch

import random


def project(v, z):
    """Returns the projection of the given vector onto the positive simplex.

    The positive simplex is the set defined by:

        {w : \sum_i w_i = z, w_i >= 0}.

    Implements the formula specified in Figure 2 of Duchi et al. (2008).
    See http://stanford.edu/~jduchi/projects/DuchiShSiCh08.pdf.

    This function uses code sourced from https://github.com/Jianbo-Lab/CCM.

    Arguments:
        v: A one-dimensional tensor.
        z: The desired sum of the components. Must be strictly positive.

    Returns:
        The Euclidean projection of v onto the positive simplex of size z.
    """
    if len(v.shape) != 1:
        raise ValueError("v must be a one-dimensional tensor")
    if z <= 0:
        raise ValueError("z must be a strictly positive scalar")

    v = v.type(torch.FloatTensor)
    n = len(v)

    U = [i for i in range(n)]
    s = 0
    p = 0
    while U:
        k = random.choice(tuple(U))
        G = {j for j in U if v[j - 1] >= v[k - 1]}
        L = {j for j in U if v[j - 1] < v[k - 1]}
        delta_p = len(G)
        delta_s = sum([v[j - 1] for j in G])
        if (s + delta_s) - (p + delta_p) * v[k - 1] < z:
            s = s + delta_s
            p = p + delta_p
            U = L
        else:
            U = G - {k}

    theta = (s - z) / p
    w = torch.tensor([max(v[i - 1] - theta, 0) for i in range(1, n + 1)])
    return w


def center(X):
    """Returns the centered version of the given square matrix.

    The centered square matrix is defined by the following formula:

        X - (1/n) 1 1^T X - (1/n) X 1 1^T + (1/n^2) 1 1^T X 1 1^T.

    This function uses code sourced from https://github.com/Jianbo-Lab/CCM.

    Arguments:
        X: An square tensor.

    Returns:
        The row- and column-centered version of X.
    """
    n = len(X)
    O = torch.ones(n, n)
    return X - (1 / n) * O @ X - (1 / n) * X @ O + (1 / pow(n, 2)) * O @ X @ O
