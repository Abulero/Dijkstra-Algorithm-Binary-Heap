# ---Author: 
# André Gomes Cecchi
#
# ---Date: 
# 04/02/2020
#
# ---Objective: 
# Solve weighted graphs using Dijkstra's Algorithm
#
# ---Guide:
# -Instantiate the Graph class with "nodes" number of nodes
# -Use add_edge to build your graph's edges
# -Call dijkstra_solution to print the shortest path from "start" to "end" according to Dijkstra's Algorithm


from Graph import Graph
from collections import defaultdict 


if __name__ == '__main__':
    graph = Graph(nodes=6)

    graph.add_edge(_from=0, to=1, distance=5)
    graph.add_edge(_from=0, to=2, distance=4)
    graph.add_edge(_from=1, to=2, distance=4)
    graph.add_edge(_from=1, to=4, distance=7)
    graph.add_edge(_from=1, to=3, distance=1)
    graph.add_edge(_from=2, to=4, distance=8)
    graph.add_edge(_from=2, to=5, distance=10)
    graph.add_edge(_from=3, to=4, distance=1)
    graph.add_edge(_from=4, to=5, distance=2)

    graph.dijkstra_solution(start=0, end=5)