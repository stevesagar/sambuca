# Ensure compatibility of Python 2 with Python 3 constructs
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals)
from builtins import *

import sambuca
import sys
from scipy.io import loadmat
from pkg_resources import resource_filename
import timeit


def main():
    '''Simple script for testing the optimisation
    experiments on the forward model.
    '''

    filename = resource_filename(
        sambuca.__name__,
        'tests/data/forwardModelTestValues.mat')
    data = loadmat(filename, squeeze_me=True)

    def forward_model():
        return sambuca.forward_model(
            chl=data['chl'],
            cdom=data['cdom'],
            tr=data['tr'],
            h=data['h'],
            q=data['q'],
            substrate1=data['substrate1'],
            substrate2=data['substrate2'],
            wavelengths=data['wav'],
            awater=data['awater'],
            aphy_star=data['aphy_star'],
            d_wls=data['d_wls'],)

    # warmup
    forward_model()
    forward_model()

    # time it
    iterations = 30000
    t = timeit.Timer(forward_model)
    time = t.timeit(iterations)
    avg = time / iterations * 1000
    print("Forward model, {0} iterations".format(iterations))
    print("Total: {}".format(time))
    print("Avg: {} ms".format(avg))

    return 0


if __name__ == '__main__':
    sys.exit(main())
