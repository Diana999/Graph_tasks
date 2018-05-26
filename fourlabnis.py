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
        if len(self.matrix) > len(nums):
            self.matrix = self.matrix[0:len(nums)]
    def node_ver_attrs(self):
        for i in self.lines:
            if i[0] == 'E':
                self.add_vert_attrs(i)
            elif '*' in i:
                print("We've done parsing file")
    
    def add_vert_attrs(self, line):
        line = list(map(int, line[2:len(line)].split(' ')))
        self.matrix[line[0]-1][line[1]-1] = line[2]
        print("Added weigths to vertices")

def dfs(matrix, F, s, t):
        stack = [s]
        paths={s:[]}
        if s == t:
                return paths[s]
        while(stack):
                u = stack.pop()
                for v in range(len(matrix)):
                        if(matrix[u][v]-F[u][v]>0) and v not in paths:
                                paths[v] = paths[u]+[(u,v)]
                                if v == t:
                                        return paths[v]
                                stack.append(v)

def max_flow(matrix, s, t):
        n = len(matrix) # C is the capacity matrix
        F = [[0] * n for i in range(n)]
        path = dfs(matrix, F, s, t)
        while path != None:
            flow = min(matrix[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            path = dfs(matrix,F,s,t)
        return sum(F[s][i] for i in range(n))


def start():
    file = ReadInput()
    source = 0  
    sink = 4
    max_flow_value = max_flow(file.matrix, source, sink)
    with open('output.txt', 'w') as f:
        f.write("Максимальный поток = "  + str(max_flow_value))
start()