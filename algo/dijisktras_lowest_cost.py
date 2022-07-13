#using hash(dictionary)

#implement the graph
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

#implement the costs
infinity = float('inf')

costs ={}
costs['a'] = 6 # cost from start to point a = 6
costs['b'] = 2 # cost from start to point b = 2
costs['fin'] = infinity


#implement the parents
parents ={}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

#array to store processed node
processed = []
parent_nodes =[]


#function that finds the lowest cost in the cost graph
def find_lowest_cost(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    parent_nodes.append(parents[node])
    processed.append(node)
    node = find_lowest_cost(costs)
        

print('total cost', cost)
print(parent_nodes)
print(processed)
