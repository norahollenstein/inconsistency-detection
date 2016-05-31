#!/usr/bin/env python

from __future__ import division
import math, sys


__author__ = 'Nora Hollenstein'
__date__ = "20150719"


# Ranking methods for the detection of inconsistency candidates in the annotation of supersense labels


def discrepancy_ranking(ss_freq):
    """
    Discrepancy ranking for supersense labels
    based on Equation (2) from Hollenstein et al. (2016)

    :param ss_freq: Frequency index of all supersense-annotated words, tab-separated input format

    :return: ranked_ss

    """

    super = []

    for ss in ss_freq:
        ss = ss.strip().split("\t")
        if int(ss[1]) >= 2: #test if word has been annotated ambiguously (i.e. with at least 2 supersense labels)
            n = int(ss[4])
            m = int(ss[-1])
            weight = ((n - m) * int(ss[2]))/int(ss[1])
            ss.append(weight)

            super.append(ss)

    ranked_ss = sorted(super, key = lambda x:x[-1], reverse=True)

    return ranked_ss


def entropy_ranking(ss_freq):
    """
    Entropy ranking for supersense labels
    based on Equation (3) from Hollenstein et al. (2016)

    :param ss_freq: Frequency index of all supersense-annotated words

    :return: ranked_ss
    """

    super = []

    for ss in ss_freq:
        ss = ss.strip().split("\t")
        sum = 0
        if int(ss[1]) >= 2:
            for elem in ss[3:]:
                try:
                    elem = int(elem)
                    prob = elem / int(ss[2])
                    ent = prob * math.log(prob, 2)
                    sum += ent
                except ValueError:
                    pass

            entropy = - sum
            ss.append(entropy)
            super.append(ss)

    ranked_ss = sorted(super, key = lambda x:x[-1])

    return ranked_ss


def main():
    input = open(sys.argv[1], 'r').readlines()
    #discrepancy_ranking(input)
    #entropy_ranking(input)

if __name__ == "__main__":
    main()