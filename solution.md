Proposed Solution:

Input:

Bus stations (number and location), streets, travel demand of each bus stations (assigned to the directed edges(OUT of bus station and IN to bus station)), population density (for travel demand), schedule(orar).

Steps:

Work from the endpoints (statiile terminus) to the city center (or any other high demand destination), progressively choosing an adjacent edge with the highest demand, until destination. then pick a route back to the end point, choosing the same edges in the opposite direction, or if it is not possible pick the highest demand nodes that still get to the end point(or the most efficient way back, no matter the demand).

After running through one edge, the algorithm picks a different edge (highest demanding).

Go through every end point( statie terminus). Have at least one bus route running from each end point. Have at least one route run through each very high demand nodes (universities, malls, city center etc.). Make sure there is another supply for high population density regions (out to high demand nodes).

Must allocate a fair amount of trolleybuses. Based on the current schedule, account the buses based on peak / off-peak times.

Must also have some long routes running from terminus - that get from distinct city sectors, running through the city center. Connecting high demand sectors with other high demand sectors.

Output:

Optimized network of trolleybuses and buses.
