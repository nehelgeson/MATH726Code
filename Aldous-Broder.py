"""Aldous-Broder.py: A python demonstration of the Aldous-Broder algorithm for generating a random spanning tree."""
__author__      = "Nathan Helgeson"

import networkx as nx
import matplotlib.pyplot as plt
from random import random

n = 100 # number of nodes for G
m = 200 # number of edges for G
G = nx.gnm_random_graph(n, m) # G a random graph with n nodes and m edges (could be disconnected)
S = nx.Graph() # spanning tree for G

num_graph_draws = 1
# this could potentially be very expensive, but this is an easy way to
# get a connected random graph
while (not nx.is_connected(G)):
    num_graph_draws += 1
    G = nx.gnm_random_graph(n, m)

print("Graph was drawn %d times before a connected graph was found" % (num_graph_draws))

# show the graph we are finding a spanning tree for
nx.draw(G, node_size = 20)
plt.show()

visited = [False] * n # marks which nodes we have been to so far
cur_node = int(random()*n) # current position in the random walk
next_node = None # next position in the random walk
visited[cur_node] = True
num_visited = 1

steps_per_node = [0] * n # mark how long it took us to get from node to node
steps_this_node = 0 # tracker of how long it has been since we saw a new node

while num_visited < n: # break once we have seen every node at least once
    steps_this_node += 1
    neighbors = [x for x in G[cur_node]] # G[cur_node] gives an iterable which is hard to get a random element from, instead just make it a list
    next_node = neighbors[int(random()*len(neighbors))] # choose random element of neighbors
    if not visited[next_node]: # if this is a new node
        visited[next_node] = True
        steps_per_node[num_visited] = steps_this_node
        steps_this_node = 0
        num_visited += 1
        S.add_edge(cur_node, next_node) # add edge to spanning tree (nodes are automatically added)
    cur_node = next_node # step forward in random walk

nx.draw(S, node_size = 20) # visualize generated spanning tree
plt.show()

print(steps_per_node) # show how the running time increases towards the end of the algorithm
