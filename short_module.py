# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph
from cmath import nan
from venv import create
import numpy as np
import sys
from get_locations import get_route_dict,create_mat
from collections import defaultdict



  # mat = [[0 for i in range(20)] for i in range(20)]

#Class to represent a graph
class Graph:
    def __init__(self) -> None:
        self.path_op=list()
        self.graph = create_mat('./data/all_points.json')

    def minDistance(self,dist,queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] <= minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, j):
        if parent[j] == -1 :
            return
        self.printPath(parent , parent[j])
        self.path_op.append(j+1)
    
    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]),end=" ")
            self.printPath(parent,i)
    
    def dijkstra(self, src,dest):
        self.path_op = []
        self.path_op.append(src+1)
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

            

def shortest_path(src,dest):
    a = Graph()
    return  a.dijkstra(src-1,dest-1)
    
# print(shortest_path(1,22))

# g= Graph()
# print(len(create_mat('all_points.json')))
# Print the solution
# details = g.dijkstra(26,4)
# print(details)
