#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Takes a collection of amendment objects and performs various analyses,
e.g. co-authorship, and where the most edited parts are.
"""

__author__ = "Christopher Kittel"
__copyright__ = "Copyright 2015"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Christopher Kittel"
__email__ = "web@christopherkittel.eu"


import networkx
import itertools

def get_coauthors(amendments):
    for amendment in amendments:
        target = [amendment.target]
        coauthors = amendment.author.split(", ")
        yield target, coauthors


def create_coauthor_network(amendments):
    B = networkx.Graph()
    #create bipartite graph
    for target, coauthors in get_coauthors(amendments):
        B.add_nodes_from(target, bipartite=0)
        B.add_nodes_from(coauthors, bipartite=1)
        edges = itertools.product(target, coauthors)
        B.add_edges_from(edges)

    print B.nodes()
    print B.edges()


    return B