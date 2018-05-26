import numpy as np

def parse_graph(fin):
    fin.readline()
    n = int(fin.readline().strip()) + 1
    g = []
    q = 0
    g.append(list(map(int, list('0'*(n)))))
    for i in range(n):
        line = list(map(int, list('0' + fin.readline().strip())))
        g.append(line)
    return n, q, g

class Complexity:
    def __init__(self):
        with open('input.txt', 'r') as infile:
            self.n, self.q, self.matrix = parse_graph(infile)

    def calculate(self, p0, p1, max_len):
        result = [p0, p1]
        k = 0
        for i in range(2, max_len+1):
            result.append(0)
            k = i+1
            for j in range(0, i):
                result[i] += k * result[j]
                k -= 1
        return result

    def get_indx(self, max_len, p0=1, p1=3):
        if self.n == 1:
            return 0
        if self.n == 2:
            return 1
        result = 0
        self.seen = np.zeros(self.n)
        chain_basis = self.calculate(p0, p1, max_len)
        for cur_len in range(max_len+1):
            if cur_len >= self.n-1:
                break
            self.chains_number = 0
            for v in range(1, self.n):
                self.get_paths(v, 0, v, cur_len)
            result += self.chains_number * chain_basis[cur_len]
        del self.chains_number
        del self.seen
        return result

    def get_paths(self, v, cur_len, start, max_len):
        if cur_len == max_len:
            if v >= start:
                self.chains_number += 1
            return
        self.seen[v] = 1
        for i in range(1, self.n):
            if self.seen[i] == 0 and self.matrix[v][i] != 0:
                self.get_paths(i, cur_len + 1, start, max_len)
        self.seen[v] = 0

res = Complexity().get_indx(max_len=5)
with open('output.txt', 'w') as f:
    f.write(str(res) + '\n')
g = Complexity().matrix[0:len(Complexity().matrix)-1]
index = 0
pars = []
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == 1:
            a = sum(1 for t in g[i] if t)
            b = 0
            for k in range(len(g)):
                b += g[k][j]
            index += 1/pow(a*b, 0.5)
            
print(index)
