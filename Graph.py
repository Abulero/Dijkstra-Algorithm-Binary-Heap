# ---Author: 
# André Gomes Cecchi
#
# ---Date: 
# 04/02/2020
#
# ---Based on: 
# https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/

from collections import defaultdict
import sys


class Heap:
    def __init__(self, size):
        self.size = size    # Amount of nodes in the heap
        self.nodes = []     # Array of nodes in a binary heap
        self.positions = [] # Array that shows the position in the heap of a node

    # Check if the program finished visiting all of the heap's nodes
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    # Swaps two nodes in the heap array (self.nodes) and in the positions array (self.positions)
    def swap(self, node_a_index, node_b_index):
        temp_node = self.nodes[node_a_index]
        self.nodes[node_a_index] = self.nodes[node_b_index]
        self.nodes[node_b_index] = temp_node

        self.positions[self.nodes[node_a_index][0]] = node_a_index
        self.positions[self.nodes[node_b_index][0]] = node_b_index

    # Returns if a node is in the "valid" portion of the heap. In other words, verifies if that node
    # has not been pushed to the end of the heap by the extract_min method
    def is_in_heap(self, node):
        for i in range(self.size):
            if node == self.nodes[i][0]:
                return True
        return False

    # Method to return the root node (shortest distance from start) and swap it with the last
    # node in the heap, while lowering the heap's size by 1, thus removing the root node from the
    # structure as a way to mark it as "already visited". After swapping the nodes, we need to
    # push the new root node downwards, rearranging the heap and correcting it
    def extract_min(self):
        root = self.nodes[0]

        self.swap(0, self.size - 1)

        self.size -= 1

        self.min_heapify(0)

        return root

    # Method to push a node downwards until it's in its correct place
    def min_heapify(self, index):
        smallest = index

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < self.size and self.nodes[left_child_index][1] < self.nodes[index][1]:
            smallest = left_child_index
        elif right_child_index < self.size and self.nodes[right_child_index][1] < self.nodes[index][1]:
            smallest = right_child_index

        # O(Log V) time complexity
        while smallest != index:
            self.swap(index, smallest)

            self.min_heapify(smallest)

            index = smallest

    # Method to push a node in the heap upwards until it's in its correct place
    def ascend(self, node, distance_from_start):
        index = self.positions[node]
        self.nodes[index][1] = distance_from_start

        parent_index = int((index-1) / 2)

        # O(Log V) time complexity
        while index > 0 and self.nodes[index][1] < self.nodes[parent_index][1]:
            self.swap(index, parent_index)
            index = parent_index

class Graph:
    def __init__(self, **kwargs):
        self.size = kwargs['nodes']
        self.adjacency_list = defaultdict(list) 

    def add_edge(self, **kwargs):
        from_node = kwargs['_from']
        to_node = kwargs['to']
        distance = kwargs['distance']

        # Edge from '_from' to 'to'
        new_edge = [to_node, distance]
        self.adjacency_list[from_node].insert(0, new_edge)

        # Edge from 'to' to '_from'
        new_edge = [from_node, distance]
        self.adjacency_list[to_node].insert(0, new_edge)

    def print_results(self, start, end, distance_from_start):
        print(f'Shortest path from node {start} to node {end}, according to Dijkstra\'s algorithm: {distance_from_start[end]}')

    def dijkstra_solution(self, **kwargs):
        start = kwargs['start']
        end = kwargs['end']
        
        distance_from_start = []

        # Dijkstra Algorithm using a Binary Heap data structure
        # STEP 1: Create a Binary Heap structure to house the graph's nodes
        # STEP 2: Set the Binary Heap's nodes' distances_from_start to maximum value, and the start node's to 0
        # STEP 3: Loop until the Binary Heap is emptied
        # STEP 4: Get the node with the shortest distance from the start in the Binary Heap
        # STEP 5: Check its neighboring nodes' distances from the start node and update their values regarding the
        # currently selected node
        # STEP 6: Exit the loop when the Binary Heap is empty and print the results
        # Time complexity will be analyzed throughout the algorithm using Big O notation, where: 
        # V = numver of vertices and E = number of edges of the graph

        # STEP 1
        min_heap = Heap(self.size)

        # STEP 2
        for vertex in range(self.size): # O(V) time complexity
            distance_from_start.append(sys.maxsize)
            min_heap.nodes.append([vertex, distance_from_start[vertex]])
            min_heap.positions.append(vertex)

        distance_from_start[start] = 0
        min_heap.nodes[start][1] = 0

        # STEP 3
        while not min_heap.is_empty(): # O(V) time complexity
            # STEP 4
            min_node = min_heap.extract_min() # O(Log V) time complexity
            u = min_node[0]
            
            # STEP 5
            for v, distance in self.adjacency_list[u]: # O(E) time complexity
                if min_heap.is_in_heap(v) and distance_from_start[u] + distance < distance_from_start[v]:
                    distance_from_start[v] = distance_from_start[u] + distance
                    min_heap.ascend(v, distance_from_start[v]) # O(Log V) time complexity

        # STEP 6
        self.print_results(start, end, distance_from_start)

        # Time complexity analysis:
        # O(V) + O(V)*(O(Log V) + O(E)*O(Log V))
        # O(V) + O(V)*(O(Log V) + O(E*Log V))
        # O(V) + O(V)*O(E*Log V))
        # O(V + V*E*Log V))
        # O(V*E*Log V)