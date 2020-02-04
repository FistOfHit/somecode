# Imports
import collections
import numpy as np
import pandas as pd
import torch


def to_numpy(data):
    """
    Make sure that data entered into any function is compatible shape and type.
    
    Parameters
    ----------
    data: array-like
        Some data form in array like structures, could be:
            Numpy array
            Pandas DataFrame/Series
            Torch Tensor
            List, tuple, deque
    
    Returns
    -------
    variables: Numpy array
        Compatible and usable object which can be passed into any function in 
        this codebase, shaped as a 2D array
    """
    
    # Standardise data type
    acceptable_types = [list, tuple, collections.deque]
    if any(type(data) == obj for obj in acceptable_types):
        variables = np.array(data)
    elif type(data) == pd.Series or type(data) == pd.DataFrame:
        variables = data.to_numpy()
    elif type(data) == torch.Tensor:
        variables = data.numpy()
    elif type(data) != np.ndarray:
        raise TypeError('Input is not an acceptable array-like iterable object')
        return None
        
    # If not 2D, make it 2D
    if len(variables.shape) < 2:
        variables = variables.reshape(1, -1)
        
    return variables
