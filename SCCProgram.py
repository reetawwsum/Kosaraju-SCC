from collections import defaultdict

g = defaultdict(list)
grev = defaultdict(list)
newGraph = defaultdict(list)
explored = {}
finish = {}
leader = {}

def dfs(g, v):
	global t
	explored[v] = 1
	leader[v] = s
	for j in g[v]:
		if not explored[j]:
			dfs(g, j)
	t = t+1
	finish[v] = t

def dfsLoop(g):
	global t #No. of nodes process so far
	global s #Current source vertex
	t = 0
	s = 0
	i = len(g)
	while i > 0:
		if not explored[i]:
			s = i
			dfs(g, i)
		i = i-1		

with open('SCC.txt', 'r') as inputFile:
	for line in inputFile:
		u = int(line.split()[0])
		v = int(line.split()[1])
		g[u].append(v)
		grev[v].append(u)
		explored[u] = 0
		finish[u] = 0

dfsLoop(grev)
#Creating a new graph using finish timings of nodes.
for i in range(1, len(g)+1):
	for x in g[i]:
		newGraph[finish[i]].append(finish[x])
#Initialising the variables
for i in range(1, len(g)+1):
	explored[i] = 0
	finish[i] = 0
	leader[i] = 0
dfsLoop(newGraph)
#Result
lst = sorted(leader.values())
stat=[]
pre=0
for i in range(0,len(g)-1):
    if lst[i]!=lst[i+1]:
        stat.append(i+1-pre)
        pre=i+1
stat.append(len(g)-pre)
L= sorted(stat)
L.reverse()
print(L[0:5])