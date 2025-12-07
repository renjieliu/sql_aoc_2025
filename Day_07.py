with open('Day_07_input.txt') as f:
    lines = f.readlines() 

arr = []
for line in lines:
    line = line.replace("\n", "")
    arr.append('.' + line + '.')

dp = [list(arr[0])] 
cnt = 0 
for r in range(1, len(arr)):
    curr = [_ for _ in arr[r]]
    for c in range(1, len(arr[0]) -1):
        if arr[r][c] == "^":
            if dp[-1][c] in ["S", "|"]:
                curr[c-1] = "|"
                curr[c+1] = "|"
                cnt += 1
        else:
            if dp[-1][c] in ["S", "|"]:
                curr[c] = "|"
    
    dp.append(curr) 

print(dp)            
print('ans1:', cnt)        




