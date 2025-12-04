with open('Day_04_input.txt') as f:
    lines = f.readlines()

arr = [] 

for line in lines:  
    arr.append([" "] + list(line) + [" "])

arr = [[" "] * len(arr[1])] + arr + [ [" "] * len(arr[1])]

cnt = 0
total_removed = 0 

while True:
    remove = []
    for r in range(1, len(arr)-1):
        for c in range(1, len(arr[0])-1):
            if arr[r][c] == "@":
                lookaround = 0
                for a, b in [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]:
                    lookaround+= 1 if arr[r+a][c+b] == "@" else 0 
                
                if lookaround<4:
                    remove.append([r,c])

    if remove == []:
        break
    for r, c in remove:
        arr[r][c] = '.'  

    total_removed += len(remove)
    cnt+=1
    
print('total removed:' ,total_removed)
print('total iteration:' , cnt)



