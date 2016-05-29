# file: numpy_pi.py
"""Calculating pi with Monte Carlo Method and NumPy.
"""

from __future__ import print_function

import numpy                                                   #1


def pi_numpy(total):                                           #2
    """Compute pi.
    """
    x = numpy.random.rand(total)                               #3
    y = numpy.random.rand(total)                               #4
    dist = numpy.sqrt(x * x + y * y)                           #5
    count_inside = len(dist[dist < 1])                         #6
    return 4.0 * count_inside / total

if __name__ == '__main__':

    def test():
        """Time the execution.
        """
        import timeit
        start = timeit.default_timer()
        pi_numpy(int(1e6))
        print('run time', timeit.default_timer() - start)
    test()
