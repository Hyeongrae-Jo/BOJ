t = int(input())
list = []
for i in range(t):
    x, y = map(int,input().split())
    list.append((x,y))

list = sorted(list, key = lambda x: (x[0], x[1]))

for i in list:
    for j in i:
        print(j, end = ' ')
    print()
