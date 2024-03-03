import random
import lisbon_metro_graf
import networkx as nx

def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<20} {:<10} {:<10}".format(vertex, distance, status))
    print("\\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, details in graph[current_vertex].items():
            weight = details['weight']  # Виправлення тут
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances


# Приклад графа у вигляді словника
graph = nx.to_dict_of_dicts(lisbon_metro_graf.G)

for node, neighbors in graph.items():
    for neighbor in neighbors:
        graph[node][neighbor]['weight'] = random.randint(1,3) # Додаємо або оновлюємо вагу ребра

# Виклик функції для вершини A
dijkstra(graph, "Saldanha")
