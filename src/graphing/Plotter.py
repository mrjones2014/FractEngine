def my_plotter(axes, data_x, data_y, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    axes : Axes
        The axes to draw to

    data_x : array
       The x data

    data_y : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = axes.plot(data_x, data_y, **param_dict)
    return out