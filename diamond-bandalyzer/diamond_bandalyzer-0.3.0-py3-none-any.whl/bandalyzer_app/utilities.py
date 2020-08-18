"""Utility functions and classes used in solving diamond band structure"""

__author__ = "Nikolai Dontschuk and Dan McCloskey"
__copyright__ = "Copyright 2020, Nikolai Dontschuk and Dan McCloskey"
__license__ = "Licensed under the Academic Free License version 3.0"

import numpy as np
from numba import njit
from scipy.interpolate import pchip
from scipy.optimize import brentq
from scipy.integrate import trapz
import re

def ravel_matrix_diag_set(a, val, n=None, k=0):
    """Set the diagonal and off diagonal terms of a matrix a using np.ravel.  Slightly faster to directly implement this,
    and not call this function.  Mostly here to provide the index template for off-diagonals."""
    if n is None:
        n = min(np.shape(a))
    a.ravel()[max(k, -n*k): max(0, (n-k))*n: n+1] = val

# ~10% faster than (np.min, np.max), extrema_fast function is stack exchange code, not subject to our copyright or licence
@njit(fastmath=True)
def extrema_fast(arr):
    n = arr.size
    odd = n % 2
    if not odd:
        n -= 1
    max_val = min_val = arr[0]
    i = 1
    while i < n:
        x = arr[i]
        y = arr[i + 1]
        if x > y:
            x, y = y, x
        min_val = min(x, min_val)
        max_val = max(y, max_val)
        i += 2
    if not odd:
        x = arr[n]
        min_val = min(x, min_val)
        max_val = max(x, max_val)
    return max_val, min_val


def int_float(x):
    f = float(x)
    i = int(f)
    if i == f:
        return i
    return f


def ini_string_to_python(v):
    """This function needs to be updated to deal with strange things in your ini file.
    Currently handles ints, floats, bool, Nonetype and lists only containing floats and ints."""
    if not v:
        return v
    try:
        v = int_float(v)
    except ValueError:
        v = str(v)
        # TODO improve robustness, currently will not handel spaces at beginning and end of string " [ [1,2,] ... ] ] "
        try:
            if v[0] == '[' and v[-1] == ']':
                if v[1] == '[' and v[-2] == ']':
                    removed_brakets = re.split('\]\s*,\s*\[', v[2:-2])
                    v = []
                    for inner_list in removed_brakets:
                        v.append([int_float(x) for x in inner_list.split(',')])
                else:
                    v = [int_float(x) for x in v[1:-1].split(',')]
            if v == 'None' or v == 'none':
                v = None
            if v == 'False' or v == 'false':
                v = False
            if v == 'True' or v == 'true':
                v = True
        except IndexError:
            raise IndexError(f"String '{v}' couldn't be parsed, as v[0], v[1] or v[-2] doesn't exist")
    return v

def solve_meshing_problem(defects, uniformZ, maxDepth, maxPoints):
    # Solves the mathematical problem of optimizing the mesh spacings subject to a constraint
    defectslog = defects + 1 # In case defects has a value of 0 anywhere
    defects = pchip(uniformZ, defects, extrapolate=False)
    defectslog = np.log10(defectslog)
    defectslog = defectslog + 1# In case there are any 0's again
    defectslog = defectslog/max(extrema_fast(defectslog))
    defectslog = pchip(uniformZ, defectslog, extrapolate=False)
    def shoot_to_the_end_findscale(scale, numPts):
        z = 0
        zprev = 0
        # Start with out 'initial guess' dx using the provided value of maxpoints
        dxInit = scale*(maxDepth/(numPts-1))
        for i in range(numPts-1):
            z = zprev + (dxInit/defectslog(zprev))
            if np.isnan(z):
                z = zprev + dxInit
            zprev = z
       # print(z[-1] - maxDepth)
        return z - maxDepth
    def shoot_to_the_end(scale, numPts):
        z = np.zeros(numPts)
        # Start with out 'initial guess' dx using the provided value of maxpoints
        dxInit = scale*(maxDepth/(numPts-1))
        for i in range(numPts-1):
            z[i+1] = z[i] + (dxInit/defectslog(z[i]))
            if np.isnan(z[i+1]):
                z[i+1] = z[i] + dxInit
        return z
    initScale = brentq(shoot_to_the_end_findscale, 1e-5, 100, args=maxPoints, xtol=1e-8)
    #print('initscale = {}'.format(str(initScale)))
    z_mesh = shoot_to_the_end(initScale, maxPoints)
    z_mesh[-1] = maxDepth
    z_downsampled = z_mesh
    diff = np.finfo(float).eps
    scalePoints = 0.9
    lessPoints = int(np.floor(scalePoints*maxPoints))
    while diff < 1e-6: # See how few mesh points we can get away with. Keep decreasing the number by 10 percent each time
        z_mesh = z_downsampled
        lessPoints = int(np.floor(scalePoints*lessPoints))
        initScale = brentq(shoot_to_the_end_findscale, 1e-5, 100, args=lessPoints, xtol=1e-8)
        z_downsampled = shoot_to_the_end(initScale, lessPoints)
        z_downsampled[-1] = maxDepth
        integralupsampled = trapz(defects(z_mesh), z_mesh)
        integraldownsampled = trapz(defects(z_downsampled), z_downsampled)
        diff = np.abs((integraldownsampled - integralupsampled)/integralupsampled)
    #    print(z_mesh)
    z_mesh[-1] = maxDepth
    return z_mesh * 0.1 # convert to cm

class ColourLoop:

    default_colours = ['orange', 'red', 'blue', 'magenta', 'black', 'cyan']

    def __init__(self, custom_colours=None):
        self.colours = custom_colours
        self.position = 0
        if self.colours is None:
            self.colours = self.default_colours

        for colour in self.colours:
            self.check_colour_exsists(colour)

    def __call__(self):
        try:
            colour = self.colours[self.position]
        except IndexError:
            self.position = 0
            colour = self.colours[self.position]
        self.position += 1
        return colour

    def top(self):
        self.position = 0

    def add_colour(self, colour):
        self.check_colour_exsists(colour)
        self.colours.append(colour)

    # TODO: make it so this raises an error if colour given isn't a colour.  For now be careful
    def check_colour_exsists(self, colour):
        pass


