"""
Leetcode: Amazon OA Power Grid

Attempts:
Completed:
Acheived Ideal:
Under 30 Mins:

Time Complexity:
Space Complexity:

Pattern:
Technique:

Problems Encountered: Need to brush up on Prim's and Kruskrals Algorithm
Other Solutions:

"""


import heapq as heapq

num = 5
connection = [["A", "B", 1], ["B", "C", 4], [
    "B", "D", 6], ["D", "E", 5], ["C", "E", 1]]


def powerGrid(num, connection):
    edges = []
    # Convert Array into edges
    for c in connection:
        edges.append(Edge(c[2], c[0], c[1]))

    pq = []
    table = {}
    min_cost = float("inf")

    for e in edges:
        if e.begin not in table:
            table[e.begin] = {}
        if e.end not in table:
            table[e.end] = {}
         table[e.from][]
        



    

    
class Edge :
    def __init__(self, begin, end, cost):
        self.begin = begin
        self.end = end
        self.cost = cost
    
    def __lt__(self, b):
        return self.cost < b.cost

    def toArray(self):
        return [self.begin, self.end, self.cost]

