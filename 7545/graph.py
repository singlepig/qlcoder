#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author        : singlepig
# Email         : gys.nanjing@gmail.com
# Description   : about graph


if __name__ == '__main__':
    import networkx as nx
    # import matplotlib.pyplot as plt

    G = nx.Graph()
    f = open("./144047638844506.txt")
    for line in f:
        name1, name2 = line.strip().split(" ")
        G.add_edge(name1, name2)
    cc = nx.connected_components(G)
    print(len(list(cc)))
    # nx.draw(G)
    # plt.show()
    ND = G.degree()
    maxDegree = 0
    maxNode = 0
    for node, degree in ND.items():
        # degree = int(degree)
        if maxDegree < int(degree):
            maxNode, maxDegree = node, int(degree)
    print("the max degree is {}, on node {}".format(maxDegree, maxNode))
