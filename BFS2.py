from collections import deque

# graph
graph = {
    'Delhi': ['Jaipur', 'Chennai'],
    'Jaipur': ['Delhi', 'Mumbai'],
    'Chennai': ['Delhi', 'Mumbai'],
    'Mumbai': ['Jaipur', 'Chennai'],
    'Bhubaneswar': ['Kolkata', 'Hyderabad'],
    'Kolkata': ['Bhubaneswar', 'Hyderabad'],
    'Hyderabad': ['Bhubaneswar', 'Kolkata']
}


def bfs(start, target):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None

# Example usage
start_node = 'Delhi'
target_node = 'Kolkata'
path = bfs(start_node, target_node)
if path:
    print(" -> ".join(path))
else:
    print(f"No path exists from {start_node} to {target_node}.")

