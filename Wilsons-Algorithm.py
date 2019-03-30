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
visited[cur_node] = True
num_visited = 1

steps_per_node = [] * n # mark how long it took us to get from node to node
steps_this_node = 0 # tracker of how long it has been since we saw a new node

while num_visited < n: # break once we have seen every node at least once
    while visited[cur_node]:
        cur_node = int(random()*n)
    walk = [cur_node]
    neighbors = [x for x in G[cur_node]] # G[cur_node] gives an iterable which is hard to get a random element from, instead just make it a list
    next_node = neighbors[int(random()*len(neighbors))] # choose random element of neighbors
    steps_this_node = 1
    
    while not visited[next_node]: # loop until we connect back to our tree  
        walk.append(next_node) # add the random walk to a list called walk
        cur_node = next_node
        neighbors = [x for x in G[cur_node]]
        next_node = neighbors[int(random()*len(neighbors))]
        steps_this_node += 1

        while next_node in walk: # don't allow looping back on ourselves, if this happens, restart at the point we looped back to
            if (walk.index(next_node) == 0): # looping back to the start node is problematic as it deletes the entire list
                walk = [walk[0]] # in this case, restart at the beginning node
            else:
                walk = walk[:walk.index(next_node)] # else cut the entire loop off of the walk
            neighbors = [x for x in G[walk[-1]]]
            next_node = neighbors[int(random()*len(neighbors))]
            steps_this_node += 1
        
    
    walk.append(next_node) # go ahead and add the final node in the spanning tree to the walk, makes it easier later for adding to spanning tree
    cur_node = walk[0]
    visited[cur_node] = True
    num_visited += len(walk)-1

    for i in range(1, len(walk)): # go back through the walk and add it to the spanning tree graph
        next_node = walk[i]
        visited[next_node] = True
        S.add_edge(cur_node, next_node)
        cur_node = next_node

    cur_node = int(random()*n) # current position in the random walk 
    neighbors = [x for x in G[cur_node]] # G[cur_node] gives an iterable which is hard to get a random element from, instead just make it a list

    avg_per_node = steps_this_node / (len(walk)-1)
    steps_per_node.extend([avg_per_node] * (len(walk)-1))
    

nx.draw(S, node_size = 20) # visualize generated spanning tree
plt.show()

print(steps_per_node) # show how the running time is higher at the beginning of the algorithm
print("Total average random walk steps per node added was %.1f" % (sum(steps_per_node) / len(steps_per_node)))
