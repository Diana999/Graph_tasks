class ReadInput():
    def __init__(self):
        self.open_file('input.txt')
        self.parse_lines()
    
    def open_file(self, file):
        with open('input.txt', 'r') as f:
            self.lines = f.readlines()
    
    def parse_lines(self):
        self.lines = [i.strip() for i in self.lines]
        self.lines.remove(self.lines[0]) #remove name from list
        self.nodes_num1 = int(self.lines[0][0]) #extract number of nodes in graph
        self.lines[0] = self.lines[0][2:len(self.lines[0])] #remove number of nodes from list
        self.nodes_num2 = int(self.lines[1][0]) #extract number of nodes in graph
        self.lines[1] = self.lines[1][2:len(self.lines[1])] #remove number of nodes from list    
        self.mat1 = ([[int(i) for i in j if i!=''] for j in [i.split(' ') for i in self.lines[0].split('0')]])       
        self.mat2 = ([[int(i) for i in j if i!=''] for j in [i.split(' ') for i in self.lines[1].split('0')]])

def permute(xs, low=0):
    file = ReadInput()
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

def check_permutation(permutation):
    
    file = ReadInput()
    c = 0
    for i,j in permutation.items():
        first = file.mat1[j-1]
        second = file.mat2[i-1]
        li = []
        for k in second:
            li.append(permutation[k])
        if sorted(li) == sorted(first):
            c += 1
    if c == 8:
        return True
    return False

def start():
    with open("output.txt", 'w') as f:
        file = ReadInput()
        if file.nodes_num1 != file.nodes_num2:
            f.write("Не совпадает количество вершин, изоморфизм невозможен")
            return
        for p in (permute([i for i in range(1, file.nodes_num1+1)])):
            if check_permutation({i+1:j for i,j in enumerate(p)}):
                for k, l in {i+1:j for i,j in enumerate(p)}.items():
                    f.write(str(k) + '-' + str(l) + '\n')
                return
        else:
            f.write("Графы не изоморфны")
start()
            
