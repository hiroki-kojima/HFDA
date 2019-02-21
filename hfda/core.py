import numpy as np


def calc_L(X, k, m):
    """
    Return Lm(k) as the length of the curve.

    """
    N = X.size

    n = np.floor((N-m)/k).astype(np.int64)
    norm = (N-1) / (n*k)

    sum = np.sum(np.abs(np.diff(X[m::k], n=1)))

    Lm = (sum*norm) / k

    return Lm


def calc_L_average(X, k):
    """
    Return <L(k)> as the average value over k sets of Lm(k).

    """
    calc_L_series = np.frompyfunc(lambda m: calc_L(X, k, m), 1, 1)

    L_average = np.average(calc_L_series(np.arange(1, k+1)))

    return L_average


def measure(X, k_max):
    """
    Measure the fractal dimension of the set of points (t, f(t)) forming
    the graph of a function f defined on the unit interval.

    Parameters
    ----------
    X : ndarray
        time series.

    k_max : int
        Maximum interval time that a new series.

    Returns
    -------
    D : float
        Fractal dimension.

    Examples
    --------
    >>> N = np.power(2, 15)
    >>> X = np.sin(np.linspace(0, 1000, N))
    >>> j = 11
    >>> k_max = np.floor(np.power(2, (j-1)/4)).astype(np.int64)
    >>> D = hfda.measure(X, k_max)
    >>> D
    1.0005565919808783

    """
    calc_L_average_series = np.frompyfunc(lambda k: calc_L_average(X, k), 1, 1)

    k = np.arange(1, k_max+1)
    L = calc_L_average_series(k).astype(np.float64)

    D, _ = - np.polyfit(np.log2(k), np.log2(L), 1)

    return D
