import numpy as np

def accuracy(truth, preds):
    """
    Computes the accuracy of predicted labels.

    Args:
    - truth: An array of true labels.
    - preds: An array of predicted labels.

    Returns:
    - The accuracy as a float.
    """
    truth = np.array(truth).flatten()
    preds = np.array(preds).flatten()
    
    return np.mean(truth == preds)

