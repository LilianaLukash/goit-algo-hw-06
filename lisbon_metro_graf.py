
import os
import pickle
import networkx as nx
import matplotlib.pyplot as plt

# Пути к файлам
stations_file = 'All_stations.pkl'
edges_file = 'All_edges.pkl'


# Функция для сохранения данных в файл в бинарном виде
def save_to_file_binary(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Функция для загрузки данных из файла в бинарном виде
def load_from_file_binary(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


yellow_line = [  "Rato", "Marquês de Pombal", "Picoas", "Saldanha", "Campo Pequeno", "Entre Campos", 
             "Cidade Universitária", "Campo Grande", "Quinta das Conchas", "Lumiar" ]

red_line = ["São Sebastião", "Saldanha", "Alameda", "Olaias", "Bela Vista", "Chelas", "Olivais", "Cabo Ruivo",
             "Oriente" ]

blue_line = ["Praça de Espanha", "São Sebastião", "Parque", "Marquês de Pombal", "Avenida", "Restauradores",
              "Baixa Chiado", "Terreiro do Paço", "Santa Apolónia"]

green_line = ["Cais de sodre", "Baixa Chiado", "Rossio", "Martim Moniz", "Intendente", "Anjos", "Arroios",
               "Alameda", "Areeiro", "Rome", "Alvalade", "Campo Grande", "Telheiras" ]

if not os.path.exists(stations_file) or not os.path.exists(edges_file):

    All_stations = []
    All_eges = []
    list_of_lines = [yellow_line, red_line, blue_line, green_line]
    for line in list_of_lines:
        for index, station in enumerate(line):
            All_stations.append(station)
            if index != 0:
                All_eges.append((line[index-1], station))
    save_to_file_binary(stations_file, All_stations)
    save_to_file_binary(edges_file, All_eges)

else:
    All_stations = load_from_file_binary(stations_file)
    All_eges = load_from_file_binary(edges_file)


# print(All_stations)
# print(All_eges)
    
G = nx.Graph()

G.add_nodes_from(All_stations)
G.add_edges_from(All_eges)

plt.figure(figsize=(8, 6))  # Розмір зображення

def node_color(node):
    if node in blue_line:
        return 'skyblue'
    elif node in green_line:
        return 'lightgreen'
    elif node in red_line:
        return 'red'
    elif node in yellow_line:
        return 'yellow'
    else:
        return 'grey'  

if __name__ == "__main__":
    # Використання функції для створення списку кольорів
    colors = [node_color(node) for node in G.nodes()]

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=700, edge_color='k', linewidths=1, font_size=10)
    plt.show()

    print(f'Number of nodes: { G.number_of_nodes()} Number of edges: { G.number_of_edges()}' )

    print("Ступінь кожної вершини:")
    for node, degree in G.degree():
        print(f"{node}: {degree}")


