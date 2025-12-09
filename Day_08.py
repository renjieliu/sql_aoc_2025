with open('Day_08_input.txt') as f:
    input = f.readlines()
    
arr = [i.replace("\n", "") for i in input]
cost = []

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        A = [int(_) for _ in arr[i].split(",") ]  
        B = [int(_) for _ in arr[j].split(",") ] 
        C = (B[0]-A[0])**2 + (B[1]-A[1])**2 +(B[2]-A[2])**2
        cost.append((i, j, C)) 

cost = sorted(cost, reverse=0, key = lambda x: x[2])

pick = 1000 

# print(len(cost))

parent = {}
size = {}


def find(a): # to find parent of a
    if parent[a]!=a:
        parent[a] = find(parent[a])
    return parent[a]

    
def union(a, b):
    if a not in parent:
        parent[a] = a 
        size[a] = 1

    if b not in parent:
        parent[b] = b 
        size[b] = 1

    root_a = find(a)
    root_b = find(b)
    
    if root_a != root_b:
        if size[root_a] >= size[root_b]:
            parent[root_b] = root_a 
            size[root_a] += size[root_b] 
        
        elif size[root_a] < size[root_b]:
            parent[root_a] = root_b 
            size[root_b] +=  size[root_a]
        
    
for a, b, c in cost[:pick]:
    union(a, b)

leaf = {}

for a, b, c in cost[:pick]:
    p_a = find(a)
    p_b = find(b) 
    
    if p_a not in leaf:
        leaf[p_a] = set() 
    leaf[p_a].add(a)
    if p_b not in leaf:
        leaf[p_b] = set() 
    leaf[p_b].add(b)

# print(leaf)
lst = sorted ( [len(v) for k, v in leaf.items() ], reverse=1)  

print('ans1: ', lst[0]*lst[1]*lst[2]) 




# part 2: to be done. need to find the point where all the 1000 boxes are connected into one tree

cnt = 0 
while True:
  
    parent = {}
    size = {}

    for a, b, c in cost[:cnt]:
        union(a, b)

    leaf = {}
    
    for a, b, c in cost[:cnt]:
        p_a = find(a)
        p_b = find(b) 
        
        if p_a not in leaf:
            leaf[p_a] = set() 
        leaf[p_a].add(a)
        if p_b not in leaf:
            leaf[p_b] = set() 
        leaf[p_b].add(b)


    lst =[ [k, len(v)] for k, v in leaf.items() ]
    
    if len(lst) == 1 and lst[0][1] == 1000 :
        print(cnt)
        break
    else:
        cnt += 1 
    print(cnt)

print(cost[cnt-1])

A = int(arr[cost[cnt-1][0]].split(",")[0])
B = int(arr[cost[cnt-1][1]].split(",")[0])

print('ans2: ', A*B)




