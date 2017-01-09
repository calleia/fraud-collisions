#!/usr/bin/python

import sys

#Search using "Breadth-First Search" algorithm
def searchCollision(graph, start, end):
    if start not in graph:
        return False
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            return True
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return False

#Load collision graph as an adjacency list
def loadGraph(filename):
    with open(filename, "r") as inputFile:
        graph = {}
        for line in inputFile:
            aux = line.strip().split()
            x = aux[0]
            y = aux[1]

            if x not in graph:
                graph[x] = set()
            graph[x].add(y)
        
            if y not in graph:
                graph[y] = set()
            graph[y].add(x)
    return graph

#Add collision between nodes
def addCollision(filename, v1, v2):
    with open(filename, "a") as outputFile:
        aux = v1 + " " + v2 + "\n"
        outputFile.write(aux)
    return


#Main program
FILENAME = "collision-networks.txt"

collisionNets = loadGraph(FILENAME)

#Parse command line arguments
if len(sys.argv) == 3: #Answer if two nodes belong to the same collision network
    print(searchCollision(collisionNets, sys.argv[1], sys.argv[2]))
elif len(sys.argv) == 4 and sys.argv[1] == "--add": #Add new collision between two nodes
    if searchCollision(collisionNets, sys.argv[2], sys.argv[3]) == False:
        addCollision(FILENAME, sys.argv[2], sys.argv[3])
else:
    print("Argument parsing error.")
