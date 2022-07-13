from numpy import Inf

#create wour graph using an adjency list representation
#each 'node' in our list should be a node name and a distance


"""
    node neigbour     weight/cost
    0 -> 1 with weight 1

    1 -> 0 with weight 1
    1 -> 2 with weight 2
    1 -> 3 with weight 3

    2 -> 1 with weight 2
    2 -> 3 with weight 1
    2 -> 4 with weight 5

    3 -> 1 with weight 3
    3 -> 2 with weight 1
    3 -> 4 with weight 1

    4 -> 2 with weight 5
    4 -> 3 with weight 1
"""
graph = {
    0: [(1,1)],
    1: [(0,1), (2,2), (3,3)],
    2: [(1,2), (3,1), (4,5)],
    3: [(1,3), (2,1), (4,1)],
    4: [(2,5), (3,1)]    
}

friends_network = {
    'seyi':[('gbemi', 1)],
    'gbemi':[('seyi', 1), ('funmi', 2)]
}

friendNetwork = {}
friendNetwork['Seyi'] ={}
friendNetwork['Seyi']['Gbemi'] = 1
friendNetwork['Gbemi'] ={}
friendNetwork['Gbemi']['Seyi'] = 1
friendNetwork['Gbemi']['Funmi'] = 2



#create a list of distances initialized to infinty
def naive_dijkstras(graph, root):
    n = len(graph)
    
    #initialize distance list as all inifinities
    dist = [Inf for _ in range(n)]
    
    #set the distance for the root to be 0
    dist[root] = 0
    
    #we create a list of visited nodes, all initialized to False
    #initialize list of visited nodes
    visited = [False for _ in range(n)]
    
    #loop thru all the nodes
    for _ in range(n):
        #'start'our node as -1 (so we dont have a start/next node yet)
        u = -1
        #lopp thru all the nodes to check for visitiation status
        for i in range(n):
            #if the node 'i' hasnt been visited and
            #we havent processed it or the distance we have for it is less
            #than the distance we have to the  'start' node
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        #all the nodes have been visited or we cant reach this node
        if dist[u] == Inf:
            break
        
        #set the node as visited
        visited[u] =True
        
        #compare the distance to each node from the 'start' node
        #to the distance we currently have on file for it
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
    print("nodes ")
    return dist


# print(naive_dijkstras(graph,1))
#parent nei       cost
# 1 -> 0 is weight 1
# 1 -> 2 is weight 2
# 2 -> 3 is weight 1
# 3 -> 4 is weight 1


#Using Lazy Dijkstras algo
import heapq

def lazy_dijkstras(graph, root):
    n = len(graph)
    #set up 'inf' distance
    dist = [Inf for _ in range(n)]
    #set up root distance
    dist[root] = 0
    #set up visited node list
    visited = [False for _ in range(n)]
    
    #set up priority queue
    pq = [(0, root)]
    
    #while there are nodes to process
    while len(pq) > 0:
        #get the root, discard current distance
        _, u = heapq.heappop(pq)
        
        
        
print(friendNetwork)
print(friends_network)
