HFDA
====

Implementation of Higuchi Fractal Dimension Analysis.

Install
----------

.. code-block:: text

    pip install hfda

Example
-------

.. code-block:: python

    import numpy as np
    import hfda


    N = np.power(2, 15)
    X = np.sin(np.linspace(0, 1000, N))
    k_max = 5

    D = hfda.measure(X, k_max)
