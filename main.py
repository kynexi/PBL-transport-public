import osmnx as ox
import networkx as nx

place_name = "Chișinău, Moldova"

#Downloading the street network 
G = ox.graph_from_place(place_name, network_type='drive', simplify=True)

# Example high demand coords
high_demand_coords = [
    (47.024910, 28.832919),  # City Center 47°01'29.8"N 28°49'59.0"E
    (47.030472, 28.824115),  # UTM bloc 1
    (47.005323, 28.841467)   # Mall dova
]

# Find nearest nodes in the graph to these coordinates
high_demand_nodes = [ox.distance.nearest_nodes(G, X=lng, Y=lat) for lat, lng in high_demand_coords]

# initialize all edge demand to 1
for u, v, k in G.edges(keys=True):
    G[u][v][k]['demand'] = 1

# Increase demand for edges near high-demand nodes
for node in high_demand_nodes:
    for neighbor in G.neighbors(node):
        for k in G[node][neighbor]:
            G[node][neighbor][k]['demand'] += 10

terminus_node = ox.distance.nearest_nodes(G, X=28.7797, Y=47.0452)  # Statie terminus pentru troleibuz 8
city_center_node = high_demand_nodes[0]

# Create shortest path using inverse of demand (higher demand = lower weight)
for u, v, k, data in G.edges(keys=True, data=True):
    demand = data.get('demand', 1)
    G[u][v][k]['weight'] = 1 / demand

route = nx.shortest_path(G, source=terminus_node, target=city_center_node, weight='weight')
fig, ax = ox.plot_graph_route(G, route, route_linewidth=3, node_size=0, bgcolor='white')

length = sum(G[u][v][0]['length'] for u, v in zip(route[:-1], route[1:]))
total_demand = sum(G[u][v][0]['demand'] for u, v in zip(route[:-1], route[1:]))

print("Route length (m):", length)
print("Total demand covered:", total_demand)
