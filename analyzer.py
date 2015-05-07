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


import networkx as nx
import matplotlib.pyplot as plt
import itertools


def get_coauthors(amendments):
    for amendment in amendments:
        target = [amendment.target]
        coauthors = amendment.author.split(", ")
        yield target, coauthors


def create_coauthor_network(amendments):
    """
    Takes amendment objects and creates a bipartite graph,
    with amendment nodes on one side and author nodes on the other.
    """
    B = nx.Graph()
    #create bipartite graph
    for target, coauthors in get_coauthors(amendments):
        B.add_nodes_from(target, bipartite=0)
        B.add_nodes_from(coauthors, bipartite=1)
        edges = itertools.product(target, coauthors)
        B.add_edges_from(edges)

    return B


def get_coauthorships(graph):
    """
    Returns the coauthor-projection of the amendment-author-network.
    Who co-authors with whom?
    """
    bottom_nodes, top_nodes = nx.algorithms.bipartite.sets(graph)
    coauthors = nx.algorithms.bipartite.weighted_projected_graph(graph, bottom_nodes)
    cotargets = nx.algorithms.bipartite.weighted_projected_graph(graph, top_nodes)
    return coauthors


def visualize_graph(graph):
    pos=nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph,pos,node_size=20,node_shape='o',node_color='0.75')
    edgewidth = [ d['weight']/10 for (u,v,d) in graph.edges(data=True)]
    nx.draw_networkx_edges(graph,pos,
                    width=edgewidth,edge_color='b')
    labels = {n:n.decode("latin-1") for n in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=11)

    plt.axis('off')
    #plt.savefig("degree.png", bbox_inches="tight")
    plt.show() 

