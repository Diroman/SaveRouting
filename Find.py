
graph = [[ 1 for j in range(836)] for i in range(945)]

for i in range(1, 945):
    for j in range(1, 836):

        graph[i][j] = graph[i-1][j] + graph[i][j-1] + graph[i-1][j-1]

print(graph[944][835])