import random

'''
def num_vertices(matrix):
    n = len(matrix)
    vertices = 0
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] == 1:
                vertices += 1
    return vertices
'''

def rand_label(matrix):
    max_label = len(matrix)/2
    labels = []
    for i in range(len(matrix)):
        labels[i] = i % max_label

def rand_vertices(vertices):
    n = len(vertices)
    rand_list = []
    while len(rand) < n:
        rand = random.rand(0, )

def label_propagation(matrix, max_iterations):
    vertices = len(matrix)
    label = rand_label(matrix)

    iteration = 0
    changed = True

    while iteration < max_iterations and changed:
        changed = False


