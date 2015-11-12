"""
This module allows for the creation of various signals.
"""

import numpy as np

def get_the_saw():
    """
    Synthetic example. Returns a saw tooth wave.
    """
    return np.fromiter( (x%100 for x in range(1,5000)) , int )

def collatz_sequence(seq, col):
    """
    Helper for Collatz fn. immediately below.
    """
    seq.append(col)
    if col == 1:
        return seq
    col = col/2 if (col % 2 == 0)  else col*3+1
    return collatz_sequence(seq, col)


def get_the_collatz(start=63728127):
    """
    Synthetic exampe. Returns consecutive intermediate values
    generated by following a particular path of the Collatz conjecture
    """
    seq = []
    seq = collatz_sequence(seq, start)
    return np.asarray(seq)

