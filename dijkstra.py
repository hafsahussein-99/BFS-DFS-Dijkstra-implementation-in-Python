import heapq

def dijkstra(graph, start):
    # Initial distances to all nodes are infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min-heap priority queue
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Skip if we already found a shorter path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example weighted graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 3)],
    'D': []
}

print("\nDijkstra’s Shortest Paths from A:")
dist = dijkstra(graph, 'A')
print(dist)
