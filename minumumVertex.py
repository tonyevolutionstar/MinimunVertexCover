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

    
def generate_vertices(n_vertices):
    vertices = []
    sum_edge = 0
    for i in range(n_vertices):
        vertices.append(generate_coordinate())
    graph = {} 
    for j in vertices:
        num_edge = random.randint(0, n_vertices)
        sum_edge += num_edge
        if sum_edge <= n_vertices:
            graph[j] = num_edge
        else: 
            graph[j] = 0
    return graph

def create_file():
    file = open(text_file, "w")  
    file.write("id: {(x, y): n_edges}\n")
    file.close()

def write_file(id, graph):
    file = open(text_file, "a")  
    file.write(str(id) + ": " + str(graph) + "\n")
    file.close() 
    

def main():
    count_operations = 0
    create_file()
    start = time.time()

    for i in range(2,26):
        graph = generate_vertices(i)
        print(graph)
        write_file(i, graph)
        stop = time.time() - start
        print("Time generated " + str(stop))


if __name__ == '__main__':
    main()
