import random
import lisbon_metro_graf
import networkx as nx

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    previous_nodes = {vertex: None for vertex in graph}
    distances[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current_vertex)

        for neighbor, details in graph[current_vertex].items():
            weight = details['weight']
            total_distance = distances[current_vertex] + weight
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                previous_nodes[neighbor] = current_vertex

    return distances, previous_nodes

def find_shortest_path(previous_nodes, start, goal):
    path = []
    current_vertex = goal
    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = previous_nodes[current_vertex]
    if path:
        path.insert(0, start)
    return path

# Оновлення для виклику dijkstra для кожної вершини та зберігання шляхів
def all_pairs_shortest_path(graph):
    all_paths = {}
    for start_vertex in graph.keys():
        distances, previous_nodes = dijkstra(graph, start_vertex)
        all_paths[start_vertex] = {}
        for end_vertex in graph.keys():
            path = find_shortest_path(previous_nodes, start_vertex, end_vertex)
            all_paths[start_vertex][end_vertex] = path
    return all_paths

# Приклад графа у вигляді словника
graph = nx.to_dict_of_dicts(lisbon_metro_graf.G)

for node, neighbors in graph.items():
    for neighbor in neighbors:
        graph[node][neighbor]['weight'] = random.randint(1,3) # Додаємо або оновлюємо вагу ребра



shortest_paths = all_pairs_shortest_path(graph)

for start, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від {start}:")
    for end, path in paths.items():
        print(f"до {end}: {path if path else 'недоступний'}")
    print("\n")


