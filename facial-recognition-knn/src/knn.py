import numpy as np
from scipy.io import loadmat
from .helper import l2distance, loaddata, plotfaces

def findknn(xTr, xTe, k):
    """
    Finds the k nearest neighbors of xTe in xTr.

    Input:
    - xTr: nxd input matrix with n row-vectors of dimensionality d
    - xTe: mxd input matrix with m row-vectors of dimensionality d
    - k: number of nearest neighbors to be found

    Output:
    - indices: kxm matrix, where indices(i,j) is the i^th nearest neighbor of xTe(j,:)
    - dists: Euclidean distances to the respective nearest neighbors
    """
    # Compute the distance matrix
    D = l2distance(xTr, xTe)
    # Sort the distances and get indices of k nearest neighbors
    sorted_indices = np.argsort(D, axis=0)
    sorted_distances = np.sort(D, axis=0)
    # Select the top k indices and distances
    indices = sorted_indices[:k, :]
    dists = sorted_distances[:k, :]
    
    return indices, dists

