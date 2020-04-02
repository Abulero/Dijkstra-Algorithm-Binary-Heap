# DijkstraAlgorithmPython

Simple implementation of a Dijkstra algorithm in Python.

# Notes

I consciously decided not to approach the problem with an adjency list or matrix so that the code can be more intuitive and easy to understand, although being less performatic.

# How to use

Instantiate the Graph class.

```python
graph = Graph(nodes=6)
```

To build your graph, call the add_node method to create each individual node and its edges. The "neighbors" argument of the add_node method takes a dictionary in which the keys are the node names and values are the distance from the node you are creating and that neighbor.

```python
graph.add_edge(_from=0, to=1, distance=5)
graph.add_edge(_from=0, to=2, distance=4)
graph.add_edge(_from=1, to=2, distance=4)
graph.add_edge(_from=1, to=4, distance=7)
graph.add_edge(_from=1, to=3, distance=1)
graph.add_edge(_from=2, to=4, distance=8)
graph.add_edge(_from=2, to=5, distance=10)
graph.add_edge(_from=3, to=4, distance=1)
graph.add_edge(_from=4, to=5, distance=2)
```

To solve the graph you built, simply call the dijkstra_solution method. The "start" argument is the desired starting node and the "end" argument is the end node. The program shall then print out the minimum distance and path, according to Dijkstra's Algorithm.

```python
graph.dijkstra_solution(start=0, end=5)
```

# Time Complexity

The algorithm involves, in total, 5 loops.  
Below we have all of them and their time complexity, where V = number of vertices and E = number of edges in the graph:

```python
# O(V)
for vertex in range(self.size)
```

```python
# O(V)
while not min_heap.is_empty()
```

```python
# O(E)
for v, distance in self.adjacency_list[u]
```

```python
# O(Log V)
while index > 0 and self.nodes[index][1] < self.nodes[parent_index][1]
```


```python
# O(Log V)
while smallest != index
```

Altogether we have:

```python
for vertex in range(self.size): # O(V) time complexity
    distance_from_start.append(sys.maxsize)
    min_heap.nodes.append([vertex, distance_from_start[vertex], False])
    min_heap.positions.append(vertex)

distance_from_start[start] = 0
min_heap.nodes[start][1] = 0

while not min_heap.is_empty(): # O(V) time complexity
    min_node = min_heap.extract_min() # O(Log V) time complexity
    u = min_node[0]
            
    for v, distance in self.adjacency_list[u]: # O(E) time complexity
        if not min_heap.already_visited(v) and distance_from_start[u] + distance < distance_from_start[v]:
            distance_from_start[v] = distance_from_start[u] + distance
            min_heap.ascend(v, distance_from_start[v]) # O(Log V) time complexity
```

Which brings us to:

O(V) + O(V)*(O(Log V) + O(E)*O(Log V))  
O(V) + O(V)*(O(Log V) + O(E*Log V))  
O(V) + O(V)*O(E*Log V))  
O(V + V*E*Log V))  
O(V*E*Log V)

Therefore, the overall time complexity of the algorithm is of O(V*E*Log V)