from os import write
from itertools import combinations, permutations
import time
import random

random.seed(101193) #define seed with my number of student
text_file = "output_graph.txt"

def generate_coordinate(min=1, max=9):
    x = random.randint(min, max)
    y = random.randint(min, max)
    if x == y:
       x, y = generate_coordinate(min, max)
    return x, y

def generate_edges(vertices):
    graph = {}
   
    
def generate_vertices(n_vertices):
    vertices = []
   
    #print(list(generate_coordinate()))
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
    file.write(str(id) + ":\n")
    #file.write(str(graph) + "\n\n")
    for row in range(len(graph)):
        file.write("\t\t" + str(graph[0][row]))

    file.write("\n")

    for i in range(len(graph)):
        file.write(str(graph[0][i]) + "\t")
        for j in range(len(graph)):
            file.write(str(graph[i][j]) + "\t")
        file.write("\n")
    file.write("\n\n")
    file.close() 

#function to write the percentage of edges on file before writing graph    
def write_percentage(percentage):
    file = open(text_file, "a")
    file.write("\nPercentage of egdes " + str(percentage) + "% \n")
    file.close()

#convert graph into adj_matrix and set edges
def make_adj_matrix(graph):
    for id in graph: # loop through id vertices 
        row = []
        for point in graph[id]: # loop to get the points generated previous 
            row.append(point)
            col = []
            for point2 in graph[id]:
                col.append(point2)
            adj_matrix = [row, col]
        print(adj_matrix)

    for row in adj_matrix:
        print(row)
        for col in row:
            print(col)


    

def main():
    count_operations = 0
    graph = {}
    percentage_egdes = [0, 25, 50, 75, 100]
    min_vertices = 2
    max_vertices = 10
    create_file()
    start = time.time()
    
    for i in range(min_vertices,max_vertices+1):
        vert = generate_vertices(i)
        graph[i] = [[point for point in vert] for point in vert]
        #print(graph)
        stop = time.time() - start
        print("Time generated " + str(stop))

    for percentage in percentage_egdes:
        write_percentage(percentage)
        for i in graph:
            write_file(i, graph[i])
            print(graph[i])
    

    #make_adj_matrix(graph)
    
    #print(adj_matrix)
        

if __name__ == '__main__':
    main()
