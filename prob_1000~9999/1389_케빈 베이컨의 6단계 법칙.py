import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().rstrip().split())
graph = [[INF] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []
for i in range(n):
    result.append(sum(graph[i]))

print(result.index(min(result))+1)
