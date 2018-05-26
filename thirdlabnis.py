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
        self.mat = ([[int(i) for i in j if i!=''] for j in [i.split(' ') for i in self.lines[0].split('0')]])    
        self.weigth_nodes = [0 for i in range(self.nodes_num)]
        self.create_map([[int(i) for i in j if i!=''] for j in [i.split(' ') for i in self.lines[0].split('0')]])
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

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]
    seen.append(v)
    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths
def calculate():
    list_of_adjacency = [[i-1 for i in j ]for j in file.mat]
    all_paths =[]
    for i in range((file.nodes_num)):
        for j in (DFS(list_of_adjacency, i)):
            all_paths.append(j)
    ones = 1
    twos = 3
    complexity = []
    complexity.append(ones)
    complexity.append(twos)
    for i in range(2, max(len(i) for i in all_paths)+1):
        n = sum(1 for j in all_paths if len(j) == i-1)
        m = sum(1 for j in all_paths if len(j) == i-2)
        if i-2 == 0:
            m = file.nodes_num
        complexity.append(n*complexity[i-1]+m*complexity[i-2])
    with open("output.txt", 'w') as f:
        f.write(str(complexity[len(complexity)-1]) +  ' структурная спектральная сложность'+ '\n')
    index = 0
    sub = 0
    for i in range(len(file.matrix)):
        for j in range(len(file.matrix[i])):
            if file.matrix[i][j] == 1:
                d1 = sum(1 for k in file.matrix[i] if k)
                for t in range(len(file.matrix)):
                       if file.matrix[t][j]:
                           file.matrix[t][j] == 0
                           sub += 1
        index += (1/pow(sub*d1, 0.5))
    with open("output.txt", 'a') as f:
        f.write(str(index) + ' Индекс Рандича')
calculate()