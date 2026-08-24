import random

def read_matrix(nome_arquivo, num_vertices):
    matrix = [[0] * num_vertices for i in range(num_vertices)]
    with open(nome_arquivo, 'r') as f:
        for line in f:
            i, j = map(int, line.strip().split(','))
            matrix[i][j] = 1
            matrix[j][i] = 1
    return matrix

#contar o número de vértices em uma matriz de adjacência        
def count_vertices(nome_arquivo):
    maior_vertice = -1
    with open(nome_arquivo, 'r') as f:
        for line in f:
            i, j = map(int, line.strip().split(','))
            maior_vertice = max(maior_vertice, i, j)
    return maior_vertice + 1
    

def rand_label(matrix):
    n = len(matrix)
    n_labels = n // 2
    labels = []
    for i in range(n):
        labels.append(random.randint(0, n_labels))
    return labels
        
def rand_vertices(vertices):
    n = len(vertices)
    rand_list = []
    for i in range(n):
        rand_list.append(i)
    random.shuffle(rand_list)
    return rand_list

# retorna vizinhos do elemento "i" da matriz "matrix"
def get_neighbors(i, matrix):
    n = len(matrix)
    neighbors = []
    for j in range(n):
            if matrix[i][j] == 1:
                neighbors.append(j)
    return neighbors

import random

def label_mode(labels):
    label_dict = {}

    # conta rótulos e soma resultado em dict
    for label in labels:
        label_dict[label] = label_dict.get(label, 0) + 1

    max_count = 0
    mode_label = None

    # procura o rótulo mais frequente (moda)
    for label, count in label_dict.items():
        if count > max_count:
            max_count = count
            mode_label = label
        elif count == max_count:

            # em caso empate a escolha é aleatória 
            if random.randint(0, 1):
                mode_label = label

    return mode_label


def label_propagation(matrix, max_iterations):
    vertices = len(matrix)
    labels = rand_label(matrix)

    iteration = 0
    changed = True

    while iteration < max_iterations and changed:
        changed = False
        order_vertices = rand_vertices(list(range(vertices)))
        for i in order_vertices:
            neighbors = get_neighbors(i, matrix)

            if len(neighbors) > 0:
                neighbor_labels = []

                # coleta o rótulo de cada vizinho
                for neighbor in neighbors:
                    neighbor_labels.append(labels[neighbor])

                # verifica nova moda de rótulos
                new_label = label_mode(neighbor_labels)

                if not new_label == labels[i]:
                    labels[i] = new_label
                    changed = True
        iteration += 1

    return labels

def print_matrix(matrix, labels):
    n = len(matrix)

    row_width = len(f"{n - 1}({max(labels)}) |")

    # Cabeçalho
    print(" " * (row_width), end="")

    for j in range(n):
        print(f"{j:>2}", end=" ")

    print()

    print(" " * row_width + "-" * (3 * n))

    # Matriz
    for i in range(n):
        if labels[i] > 9:
            print(f"{i:>{len(str(n - 1))}}({labels[i]}) |", end=" ")
        else:
            print(f"{i:>{len(str(n - 1))}}({labels[i]})  |", end=" ")
        for j in range(n):
            print(f"{matrix[i][j]:>1}", end="  ")

        print()
    print()

def run(path):
    matrix = read_matrix(path, count_vertices(path))
    labels = label_propagation(matrix, 100)
    print_matrix(matrix, labels)


run("rede1_duas_comunidades.csv")
run("rede2.csv")
run("zachary.csv")



        
            

