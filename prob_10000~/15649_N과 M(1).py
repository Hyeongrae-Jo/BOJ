from itertools import permutations
n, m = map(int, input().split())
arr = []
for i in range(1, n+1):
    arr.append(i)

result = list(permutations(arr, m))
for i in result:
    for j in i:
        print(j, end = ' ')
    print()
