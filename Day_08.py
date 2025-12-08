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
print(cost[:10])

