import lisbon_metro_graf

def DFS(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))

def BFS(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))

dfs_path = DFS(lisbon_metro_graf.G, "Saldanha", "Baixa Chiado")
bfs_path = BFS(lisbon_metro_graf.G, "Saldanha", "Baixa Chiado")
print("DFS path:", dfs_path)
print("BFS path:", bfs_path)
print('''DFS і BFS знайшли різні шляхи, тому що вони використовують різні стратегії для обходу графа. 
      DFS занурюється настільки глибоко, наскільки це можливо, перш ніж відступати, 
      що призвело до знаходження шляху, який довший за найкоротший.
      BFS, з іншого боку, використовує стратегію обходу найближчих вершин спочатку,
      що гарантує знаходження найкоротшого шляху в невзваженому графі, як і вийшло.''')