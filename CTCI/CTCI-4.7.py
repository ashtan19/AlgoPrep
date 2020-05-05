# CTCI: 4.7 Build Order of Projects (Graph)

# Time Complexity: 
# Space Complexity:
# Solving process:
# Problems Encountered: Problems debugging

# Other Solutions:

class Project: #Vertices of the graph
    def __init__ (self, n) :
        self.name = n
        self.map = {}
        self.neighbours = []
        self.dependencies = 0

    def add_neighbour(self, v) :
        if (v.name not in self.map) :
            self.neighbours.append(v)
            self.map[v.name] = v
            self.dependencies += 1
    
    def incrementDependencies(self) : self.dependencies += 1
    def decrementDependencies ( self ): self.dependencies -= 1
    def getName (self): return self.name
    def getChildren( self) : return self.neighbours
    def getNumDependencies (self): return self.dependencies

class Graph:
    nodes = []
    projectMap = {}

    def getOrAddNode (self, name ):
        if name not in self.projectMap :
            node = Project(name)
            self.nodes.append(node)
            self.projectMap[name] = node
        return self.projectMap[name]

    def addEdge (self, startname, endname) :
        start = self.getOrAddNode(startname)
        end = self.getOrAddNode(endname)
        start.add_neighbour(end)
    
    def getNodes (self) : return self.nodes

def buildGraph ( projects, dependencies) :
    graph = Graph()

    for project in projects:
        graph.getOrAddNode(project)
    
    for dependency in dependencies:
        first, second = dependency
        graph.addEdge(first,second)
    
    return graph

def addNonDependent (order, projects, offset) :
    for project in projects:
        if (project.getNumDependencies() == 0) :
            order[offset] = project
            offset += 1
    
    return offset, order

def orderProjects (projects) :
    order = [None] * len(projects) 
    print(order)
    print(len(order))

    endOfList, order = addNonDependent(order, projects, 0)
    toBeProcessed = 0 
    while (toBeProcessed < len(order)):
        current = order[toBeProcessed]
        print("hello")
        print(order)

        if current == None:
            return None

        children = current.getChildren()
        for child in children :
            child.decrementDependencies()
        
        print(endOfList)

        
        endOfList, order = addNonDependent(order, children, endOfList)
        toBeProcessed += 1
    
    return order

def findBuildOrder ( projects, dependencies):
    graph = buildGraph(projects, dependencies)
    print(graph.projectMap)
    return orderProjects(graph.getNodes())


testProjects = ['a', 'b', 'c', 'd', 'e', 'f']
testdependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

testorder = findBuildOrder(testProjects, testdependencies)
print("zzzz")
print(testorder)
