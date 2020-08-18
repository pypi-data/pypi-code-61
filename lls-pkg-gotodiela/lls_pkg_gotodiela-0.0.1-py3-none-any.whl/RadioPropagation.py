"""
# Description: A module related to the radio propagation parameters

Functions::
1. find the reference RSSI, z0
2. find the path loss exponent, alpha
3. find the expected RSSI by the distance between a receiver and transimitter
4. find the best 'alpha' & the best 'reference RSSI'

"""

from math import sqrt,log10
import numpy 

# 1. 
def findRefRSSI(alpha=float, distanceBtwTwoPts=float, measuredRssi=float):
    """Return float, Find the reference RSSI if path loss exponent (alpha), the distance between two points and measured RSSI are known."""
    Z0 = measuredRssi + 10*alpha*(log10(distanceBtwTwoPts))
    return Z0

# 2.
def findAlpha(rssi1=float,rssi2=float,distance1=float,distance2=float):
    """ ... """
    rssi = rssi1-rssi2
    alpha = rssi/(10*(log10(distance2)-log10(distance1)))
    return alpha

# 3.
# input parameters: reference RSSI, path loss exponent, distance between a receiver and a transmitter
def log_Normal_RSSI_With_Distance(alpha=2.5,z0=-33.0,distance=float):
    """Find expected RSSI between two points if the reference RSSI, 
    path loss exponent and the distance between two points are known."""
    z = z0 - ((10.*alpha)*numpy.log10(distance))
    return z

# 4.
# Find the best alpha 
""" Under development... """

