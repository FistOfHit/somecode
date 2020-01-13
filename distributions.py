# Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as scistat


def plot_distributions(variables, names=[], optimise_bins=True,
                       return_nan_positions=False):
    """
    Plot the histograms of each predictor variable.
    
    Notes
    -----
    Reasonably generalised function to take in a variable(s), and just plot 
    the histogram hassle free. Useful for quickly and reasonably efficiently 
    inspecting distributions of things. Options for other processes are
    included.
    
    Parameters
    ----------
    variables: List OR Numpy array OR Pandas Dataframe/Series (array-like)
        multi-dimensional array-like object with all values of variable, each
        variable to its own row, and readings/values in columns
        
    names: List (default: [])
        List of variable names for each variable in input arrays
        
    optimise_bins: Bool (default: True)
        Whether or not to automatically determine the optimal bins for 
        histogram, using Freedman-Diaconis rule [1]
        
    return_nan_positions: Bool (default: False)
        Whether or not to return an array with positions of each NaN value
        
    Returns
    -------
    (Optional) nan_positions: Numpy array (shape: same as variables)
        Boolean array with positions of NaN values
        
    References
    ----------
    [1]: Freedman, D., Diaconis, P. On the histogram as a density
    estimator:L 2 theory. Z. Wahrscheinlichkeitstheorie verw Gebiete 57,
    453–476 (1981) doi:10.1007/BF01025868
    """
    
    # Standardise data type
    if type(variables) == list:
        variables = np.array(variables)
    elif type(variables) == pd.Series or type(variables) == pd.DataFrame:
        variables = variables.to_numpy()
    elif type(variables) != np.ndarray:
        raise TypeError('Input is not of type List, Numpy NDArray or Pandas '
                        + 'Series/DataFrame')
        return None
    
    # Determine number of plot to make
    if len(variables.shape) > 1:
        num_variables = variables.shape[1]
    else:
        num_variables = 1
        
    # Check for and alert about NaNs
    if np.sum(np.isnan(variables)) > 1:
        
        print('Variables array contains NaN values. These will be ' +
              'automatically interpolated using the mean of existing ' +
              'values. To get the positions of the NaN values, re-run this ' +
              'function with return_nan_positions = True.')
        
        if return_nan_positions:
            return np.isnan(variables)
    
    # Iterate through each variable and plot distributions
    for i in range(num_variables):
        
        # Fill in NaN values
        values = variables[i, :]
        values[np.isnan(values)] = np.nanmean(values)        
    
        if optimise_bins:
            # Use Freedman-Diaconis rule to calculate optimal number of bins
            # Find optimal bin width
            inter_q_range = scistat.iqr(values)
            bin_width = 2 * inter_q_range * (len(values)**(-1/3))
     
            # Find bounds (min/max) of all data
            bounds = np.percentile(values, q=(0, 100))
        
            # Find number of bins (stabilised if width is too small) and create
            num_bins = int(((bounds[1] - bounds[0]) / (bin_width + 1e-5)) + 1)
            bins = np.linspace(bounds[0], bounds[1], num_bins)
            
            # Create histogram
            density, x_axis = np.histogram(values, density=True, bins=bins)
        
        else:
            # Create histogram
            density, x_axis = np.histogram(values, density=True, bins='auto')
        
        # Initialise plot
        fig, ax = plt.subplots(figsize=(15, 8))
        plt.xlabel('Values')
        plt.ylabel('Frequency density')
        
        # Add a name to plot if applicable
        if len(names) > 0:
            value_name = names[i]
        else:
            value_name = ""
            
        plt.title("Distribution (Histogram) of variable: " + str(i) + "." +
                  str(value_name))
        plt.plot(x_axis[1:], density)
    
    return