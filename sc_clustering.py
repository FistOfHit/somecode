# Imports
import sc_common
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


def plot_clusters(x_variable, y_variable, labels, variable_names=['']*2,
                  plot_title=''):
    """
    Plot a bi-variate relationship, coloured by the clustering labels.
    
    Notes
    -----
    Its assumed that clustering has produced labels that are integers from 0 
    upwards, and this pre-processing is not performed here. Additionally, 
    legends are not plotted here due to them just taking up lots of space on 
    the plot for no reason, and implementing a general function with checks
    for that is just pointless.
    
    Parameters
    ----------
    x_variable: numpy array
        Array of x_variable values to plot on x-axis
        
    y_variable:
        Array of y_variable values to plot on y-axis
        
    labels: numpy array
        Array of labels assigned to points for clustering. Assuming the labels 
        are integer values that start at 0.
        
    variable_names: List (default: ['', ''])
        Names of each variable, in this order:
            [x_variable, y_variable]
        
    plot_title: String (default: '')
        Title for the plot
        
    Returns
    -------
    None.
    """
    
    x_variable = sc_common.to_numpy(x_variable)
    y_variable = sc_common.to_numpy(y_variable)
    labels = sc_common.to_numpy(labels)
    
    # Create colour list from labels
    label_colours = [cm.jet(label) for label in np.unique(labels)/np.max(labels)]
    
    # Setup plot
    fig, ax = plt.subplots(figsize = (15, 8))
    plt.title(plot_title)
    plt.xlabel(variable_names[0])
    plt.ylabel(variable_names[1])
    
    # Plot each cluster with its own colour
    for i in range(len(label_colours)):
        
        # Create a mask for this cluster
        mask = (labels == labels[i])
        
        # Extract cluster
        cluster_x = x_variable[mask]
        cluster_y = y_variable[mask]
        
        # Plot with its own colour
        plt.plot(cluster_x, cluster_y, '.', c=label_colours[i])
    
    plt.show()
    
    return


