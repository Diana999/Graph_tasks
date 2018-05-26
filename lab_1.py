#Граф считывается в fo формате.
#Программа отыскивает кратчайшие пути между вершинами 
# В выходном файле генерируется путь с объяснениями. Чтобы запустить проект нужно инициализировать класс и запустить функцию выполнения алгоритма Дейкстры. 
def Dijkstra(N, S,  current,matrix, nodes_weigth):
    valid = [True]*N   
    weight = [1000000]*N
    weight[S] = 0
    came_from = {}
    came_from[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] + nodes_weigth[ID_min_weight]< weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i] + nodes_weigth[ID_min_weight]
                came_from[i] = ID_min_weight
        valid[ID_min_weight] = False
    path = []
    ds = 0
    with open('output.txt', 'w') as f:
        f.write('Чтобы достигнуть вершину ' + str(current) +  ' из вершины ' + str(S) +  '\n')
        while came_from[current] != 0:
                    path.append(came_from[current])
                    current = came_from[current]
                    ds += 1 
        if len(path):
            for i in sorted(path):
                f.write("Посетите вершину "+ str(i) +  '\n')
        else:
            f.write('Перейдите в вершину ' + str(current) + '\n')
        f.write("Это займет у вас " + str(ds+1) + ' шагов' +  '\n')
    #return weight, path, ds

class ReadInput():
    def __init__(self):
        self.open_file('input.txt')
        self.parse_lines()
    
    def open_file(self, file):
        with open('input.txt', 'r') as f:
            self.lines = f.readlines()
    
    def parse_lines(self):
        self.lines = [i.strip() for i in self.lines]
        self.name = self.lines[0] #extract name
        self.lines.remove(self.lines[0]) #remove name from list
        self.nodes_num = int(self.lines[0][0]) #extract number of nodes in graph
        self.lines[0] = self.lines[0][2:len(self.lines[0])] #remove number of nodes from list
        self.create_map([[int(i) for i in j if i!=''] for j in [i.split(' ') for i in self.lines[0].split('0')]])
        self.lines.remove(self.lines[0]) #remove nodes dependencies from list
        self.weigth_nodes = [0 for i in range(self.nodes_num)]
        self.node_ver_attrs()
        
    def create_map(self, line): 
        nums = [i for i in range(1,int(self.nodes_num)+1)]
        self.matrix = []
        for j in line:
            self.matrix.append([1 if i in j else 0 for i in nums])
            
    def node_ver_attrs(self):
        for i in self.lines:
            if i[0] == 'V':
                self.add_node_attrs(i)
            elif i[0] == 'E':
                self.add_vert_attrs(i)
            elif '*' in i:
                print("We've done parsing file")
    
    def add_node_attrs(self, line):
        line = list(map(int, line[2:len(line)].split(' ')))
        self.weigth_nodes[line[0]-1] = line[1]
        print('Added weigths to nodes')
    
    def add_vert_attrs(self, line):
        line = list(map(int, line[2:len(line)].split(' ')))
        self.matrix[line[0]-1][line[1]-1] = line[2]
        print("Added weigths to vertices")
file = ReadInput()
file_matrix = [[1000000 if i == 0 else i for i in j ]for j in file.matrix]
Dijkstra(file.nodes_num, 0, 3, file_matrix , file.weigth_nodes)