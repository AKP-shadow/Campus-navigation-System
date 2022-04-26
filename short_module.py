# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph
from cmath import nan
from venv import create
import numpy as np
import sys

from collections import defaultdict

def get_markers():
    markers = dict()
    with open("markers.csv","r") as file:
        a = file.readlines()
        for landmark in a:
            print
            marker_unorg = landmark.split(',')
            markers[marker_unorg[0]] = int(marker_unorg[1])
    return markers

def create_mat():
  # mat = [[0 for i in range(20)] for i in range(20)]
    with open("map_1.csv","r") as file:
        mat = np.genfromtxt(file,delimiter=",")
    return mat
#Class to represent a graph
class Graph:
    def __init__(self) -> None:
        self.path_op=list()
        self.graph = create_mat()

    def minDistance(self,dist,queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, j):
        if parent[j] == -1 :
            return
        self.printPath(parent , parent[j])
        self.path_op.append(j)
    
    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]),end=" ")
            self.printPath(parent,i)
    
    def dijkstra(self, src,dest):
        self.path_op = []
        self.path_op.append(src)
        row = len(self.graph)
        col = len(self.graph[0])
        
        dist = [float("Inf")] * row
        parent = [-1] * row

		# Distance of source vertex
		# from itself is always 0
        dist[src] = 0
	
		# Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)
			
		#Find shortest path for all vertices
        while queue:

			# Pick the minimum dist vertex
			# from the set of vertices
			# still in queue
            u = self.minDistance(dist,queue)

			# remove min element	
            queue.remove(u)

			# Update dist value and parent
			# index of the adjacent vertices of
			# the picked vertex. Consider only
			# those vertices which are still in
			# queue
            for i in range(col):
				# '''Update dist[i] only if it is in queue, there is
				# an edge from u to i, and total weight of path from
				# src to i through u is smaller than current value of
				# dist[i]'''
                if self.graph[u][i] and i in queue:
                    if dist[u] + self.graph[u][i] < dist[i]:
                        dist[i] = dist[u] + self.graph[u][i]
                        parent[i] = u
        return self.metrics(parent,dest,dist)

		# print the constructed distance array
    def metrics(self,parent,dest,dist):
        self.printPath(parent,dest)
        # print(dist[dest])
        met =dict()
        met["dist"] = dist[dest]
        met["path"] = self.path_op
        return met

            


g= Graph()

# Print the solution
details = g.dijkstra(26,4)
print(details)


