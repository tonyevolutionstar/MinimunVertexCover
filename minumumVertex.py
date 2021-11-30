""" António Ramos N101193"""

from os import write
import time
import random
import itertools

random.seed(101193) #define seed with my number of student
text_file = "output_graph.txt"
adj_file = "adj_matrix.txt"
results_file = "results.csv" # the propose is analyse results from algorithm

#function to generate the coordinates for x and y 
def generate_coordinate(min=1, max=9):
    x = random.randint(min, max)
    y = random.randint(min, max)
    if x == y:
       x, y = generate_coordinate(min, max)
    return x, y

def generate_edges(vertices, percentage):
    adj_matrix = [[0 for i in range(len(vertices))] for j in range(len(vertices))]
    size_graph = len(vertices)

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
    file.write("id: {(x, y)}\n")
    file.close()

#function to write information of graph on the file
def write_file(id, graph):
    file = open(text_file, "a")  
    file.write(f"{id}: {graph} \n\n")
    file.close() 

#function to write the percentage of edges on file before writing graph    
def write_percentage(text, percentage):
    file = open(text, "a")
    file.write(f"\nPercentage of egdes, {percentage} \n")
    file.close()

def create_file_adj():
    file_adj = open(adj_file, "w")
    file_adj.write("id: adj matrix")
    file_adj.close()

def write_adj_matrix(id, graph):
    file = open(adj_file, "a")  
    file.write(f"{id} :\n")
 
    for i in range(len(graph)):
        for j in range(len(graph)):
            file.write(str(graph[i][j]) + "\t")
        file.write("\n")
    file.write("\t\n")
    file.close() 

def write_operations_minimum(points, exaustive, counts, min_vertex):
    file = open(adj_file, "a")
    file.write("Minimum Vertex Cover Set: ")
    for node in range(len(points)):
        if exaustive[node]:
            file.write(f"{node} ")
    file.write(f"\nNumber of operations: {counts}\n")
    file.write(f"The minimum vertex cover is {min_vertex}\n\n")
    file.close()


def create_file_results():
    file = open(results_file, "w")
    file.write("Number of Vertices, Percentage, Number of operations, Minimum Vertex Cover, Execution Time\n")
    file.close()

def write_results_csv(n_graph, percentage, counts, min_vertex, execution_time):
    file = open(results_file, "a")
    file.write(f"{n_graph},{percentage},{counts},{min_vertex},{execution_time}\n")
    file.close()


def exaustive_search_vertex(graph):
    count_operations = 0

    """ THIS CODE WAS ADAPTED FROM
        https://www.geeksforgeeks.org/vertex-cover-problem-set-1-introduction-approximate-algorithm-2/
    """
    # Initialize all vertices as not visited.
    visited = [False for i in range(len(graph))]

    for node in range(len(graph)):
        # An edge is only picked when both visited[u] and visited[v] are false
        if not visited[node]:
            # Go through all adjacents of u and pick the first not yet visited vertex (We are basically picking
            # an edge (u, v) from remaining edges.
            for v in range(len(graph)):
                if not visited[node]:   
                    # Add the vertices (u, v) to the result set. We make the vertex u and v visited so that all
                    # edges from/to them would be ignored
                    visited[v] = True
                    visited[node] = True
                    count_operations += 1
                    break

    return visited, count_operations

def validity_check(graph, cover):
    is_valid = True
    for i in range(len(graph)):
        for j in range(i+1, len(graph[i])):
            if graph[i][j] == 1 and cover[i] != '1' and cover[j] != '1':
                return False

    return is_valid

def vertex_cover_naive(graph, ins):
    n = len(graph)
    minimum_vertex_cover = n
    a = list(itertools.product(*["01"] * n))
    for i in a:
        if validity_check(ins, i):
            counter = 0
            for value in i:
                if value == '1':
                    counter += 1
            minimum_vertex_cover = min(counter, minimum_vertex_cover)
    return minimum_vertex_cover
    
def main():
    graph = {}
    # in this problem doesn't make sence to do a graph with 0% and 100% of edges 
    percentage_egdes = [25, 50, 75]
    min_vertices = 10
    max_vertices = 11
    create_file() # create "output_graph.txt" every time that program runs
    create_file_adj() # for adj matrix
    create_file_results()
    exec_time = 0
    start = time.time()

    if min_vertices == max_vertices:
        print("The max and the min can't be equal")
        exit(1)

    if min_vertices >= 10:
        # generate graph one time and save the graph on dictionary 
        for i in range(min_vertices,max_vertices+1):
            graph[i] = generate_vertices(i)
            stop = time.time() - start
            exec_time = round(stop,5)
            print(f"Graph, {i} generated in, {exec_time} seconds")
            write_file(i, graph[i]) # write to a file "output_graph.txt" the graph

        # generate edges and adj_matrix
        for i in graph:
            for percentage in percentage_egdes:
                write_percentage(adj_file, percentage)
            
                points = graph[i]
                # initializate the adj matrix 
                adj_matrix = generate_edges(points, percentage)
                exaustive, counts = exaustive_search_vertex(points)
                #print(f"graph, {i} percentage, {percentage}")
                #print("Minimum Vertex Cover Set")
                #print(f"Number of operations, {counts} ")
                write_adj_matrix(i, adj_matrix)
                min_vertex = vertex_cover_naive(adj_matrix, adj_matrix)
                write_operations_minimum(points, exaustive, counts, min_vertex)
                write_results_csv(i, percentage, counts, min_vertex, exec_time)
                #print(f"The minimum vertex cover is {vertex_cover_naive(adj_matrix, adj_matrix)}")
    else:
        print("The program only accepts graph with 10 or more vertices")
        exit(1)

        
if __name__ == '__main__':
    main()
