""" António Ramos N101193"""

from os import write
from itertools import combinations, permutations
import time
import random

random.seed(101193) #define seed with my number of student
text_file = "output_graph.txt"
adj_file = "adj_matrix.txt"

#function to generate the coordinates for x and y 
def generate_coordinate(min=1, max=9):
    x = random.randint(min, max)
    y = random.randint(min, max)
    if x == y:
       x, y = generate_coordinate(min, max)
    return x, y

def generate_edges(id, vertices, percentage):
    adj_matrix = [[0 for i in range(len(vertices))] for j in range(len(vertices))]
    size_graph = len(vertices)

    # because 2 is 
    if id == 2: 
        for i in range(size_graph):
            for j in range(size_graph):
                if vertices[i] != vertices[j]: 
                    adj_matrix[i][j] = 1
                else:
                    adj_matrix[i][j] = 0
    else:
        number_edges = round(size_graph * (percentage/100))

        number_of_alt = 0 # operations to change random vertice to fill the percentage of edges
        if number_edges != 0:
            for i in range(size_graph):
                for j in range(size_graph):
                    if number_of_alt <= number_edges:
                        vert_i = random.choice(vertices[i])
                        vert_j = random.choice(vertices[j])
                        number_of_alt += 1
                        adj_matrix[vert_i][vert_j] = 1
    


                
    return adj_matrix
   
#function to generate the vertices    
def generate_vertices(n_vertices):
    vertices = []
   
    for i in range(n_vertices):
        vertices.append(generate_coordinate())

    return vertices

#function to create a new file when the application runs
def create_file():
    file = open(text_file, "w")  
    file.write("id: {(x, y): n_edges}\n")
    file.close()

#function to write information of graph on the file
def write_file(id, graph):
    file = open(text_file, "a")  
    file.write(str(id) + ": " + str(graph) + "\n\n")
    file.close() 

#function to write the percentage of edges on file before writing graph    
def write_percentage(text, percentage):
    file = open(text, "a")
    file.write("\nPercentage of egdes " + str(percentage) + "% \n")
    file.close()

def create_file_adj():
    file_adj = open(adj_file, "w")
    file_adj.write("id: adj matrix")
    file_adj.close()

def write_adj_matrix(id, graph):
    file = open("adj_matrix.txt", "a")  
    file.write(str(id) + ":\n")
 
    for i in range(len(graph)):
        for j in range(len(graph)):
            file.write(str(graph[i][j]) + "\t")
        file.write("\n")
    file.write("\t\n")
    file.close() 

def main():
    count_operations = 0
    graph = {}
    percentage_egdes = [25, 50, 75, 100]
    min_vertices = 10
    max_vertices = 20
    create_file() # create "output_graph.txt" every time that program runs
    create_file_adj() # for adj matrix

    start = time.time()
    
    # generate graph one time and save the graph on dictionary 
    for i in range(min_vertices,max_vertices+1):
        graph[i] = generate_vertices(i)
        stop = time.time() - start
        print("Graph " + str(i) + " generated in " + str(round(stop,5)) + " seconds")

    # generate edges and adj_matrix
    for percentage in percentage_egdes:
        write_percentage(text_file, percentage)
        write_percentage(adj_file, percentage)
        for i in graph:
            points = graph[i]
            write_file(i, points) # write to a file "output_graph.txt" the graph
            
            # initializate the adj matrix 
            #adj_matrix = [[0 for i in points] for j in points]
            adj_matrix = generate_edges(i, points, percentage)


            write_adj_matrix(i, adj_matrix)

        

if __name__ == '__main__':
    main()
