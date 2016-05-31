#!/usr/bin/env python

from __future__ import division
import math, sys


__author__ = "Nora Hollenstein"
__date__ = "20150719"

# Ranking methods for the detection of inconsistency candidates in the annotation of multiword expressions


def discrepancy_ranking(mwe_freq):
    """
    Discrepancy ranking for multiword expressions
    based on Equation (1) from Hollenstein et al. (2016)

    :param mwe_freq: Frequency index of all MWEs (annotated and non-annotated occurrence counts)

    :return: ranked_mwes
    """

    mwes = []

    for mwe in mwe_freq:
        mwe = mwe.strip().split("\t")
        if not int(mwe[3]) == 0:
            weight = abs(int(mwe[2])-int(mwe[3]))*int(mwe[2])
            mwe.append(weight)

            mwes.append(mwe)

    ranked_mwes = sorted(mwes, key = lambda x:x[4], reverse=True)

    return ranked_mwes

def entropy_ranking(mwe_freq):
    """
    Entropy ranking for multiword expressions
    based on Equation (3) from Hollenstein et al. (2016)

    :param mwe_freq: Frequency index of all MWEs (annotated and non-annotated occurrence counts)

    :return: ranked_mwes
    """

    mwes = []

    for mwe in mwe_freq:
        mwe = mwe.strip().split("\t")
        if not int(mwe[3]) == 0:
            p1 = int(mwe[2])/(int(mwe[2])+int(mwe[3]))
            p2 = int(mwe[3])/(int(mwe[2])+int(mwe[3]))
            entropy = -(p1*math.log(p1,2) + p2*math.log(p2,2))
            mwe.append(entropy)

            mwes.append(mwe)

    ranked_mwes = sorted(mwes, key = lambda x:x[4])

    return ranked_mwes


def main():
    input = open(sys.argv[1], 'r').readlines()
    #discrepancy_ranking(input)
    #entropy_ranking(input)


if __name__ == "__main__":
    main()