import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

def loaddata(filename):
    """
    Load data from a .mat file.
    
    Args:
        filename: The path to the .mat file to load.
        
    Returns:
        A tuple of training and testing data: (xTr, yTr, xTe, yTe)
    """
    data = loadmat(filename)
    return data['xTr'], data['yTr'], data['xTe'], data['yTe']

def plotfaces(images):
    """
    Plot a series of face images.
    
    Args:
        images: A numpy array of images to plot.
    """
    fig, axes = plt.subplots(1, len(images), figsize=(11, 8))
    for i, ax in enumerate(axes):
        ax.imshow(images[i].reshape(28, 28), cmap='gray')  # Assuming images are 28x28
        ax.axis('off')
    plt.show()

def l2distance(X, Z=None):
    """
    Compute the L2 distance between two sets of points.
    
    Args:
        X: A set of points.
        Z: Another set of points. If None, compute the distance within X.
        
    Returns:
        A matrix of distances.
    """
    if Z is None:
        Z = X
    D = np.sqrt(((X[:, :, None] - Z[:, :, None].T) ** 2).sum(1))
    return D
