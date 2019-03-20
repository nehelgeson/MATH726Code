import networkx as nx
import matplotlib.pyplot as plt
import itertools

def draw_spanning_trees(edge_list, pos):
    i = 1
    for edges in edge_list:
        plt.subplot(3, 4, i)
        G = nx.Graph(edges)
        nx.draw(G,pos,node_color='#ccccff', node_size=100)
        i += 1
    
    plt.show()

def is_spanning_tree(edges):
    # given a edge list of length 4, is this a spanning tree?
    # if this edge set connects all nodes, then yes
    if len(edges) != 4: return False

    # visited keeps track of where we've been
    visited = [False for x in range(5)]
    # nodes keeps track of where we are going
    nodes = set()

    # start at node 0
    nodes.add(0)

    # depth first search
    while len(nodes) > 0:
        current = nodes.pop()
        visited[current] = True
        for e in edges:
            if e[0] == current:
                if not visited[e[1]]:
                    nodes.add(e[1])
            elif e[1] == current:
                if not visited[e[0]]:
                    nodes.add(e[0])

    # did DFS visit every node? If no, return False
    for i in visited:
        if not i:
            return False
    return True

def main():
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2)]
    pos = {0: (0, 0), 1: (0.5,0.71), 2: (1, 0), 3: (1, -1), 4: (0, -1)}

    total_trees = 0
    possible_trees = list(itertools.combinations(edges, 4))
    spanning_trees = []
    
    for tree in possible_trees:
        if is_spanning_tree(tree):
            total_trees += 1
            spanning_trees.append(tree)

    print("There are %d unique spanning trees for the house graph" %(total_trees))
    draw_spanning_trees(spanning_trees, pos)

if __name__ == "__main__":
    main()
