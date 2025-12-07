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

# print(dp)            
print('ans1:', cnt)        



dp = [ [ 1 if _ == "S" else 0 for _ in list(arr[0]) ] ]

for r in range(1, len(arr)):
    curr = [ x for x in dp[-1]] # copy the previous row
    
    for c in range(1, len(arr[0])-1):
        if arr[r][c+1] == "^":
            curr[c] += dp[-1][c+1] 
    
        if arr[r][c-1] == "^":
            curr[c] += dp[-1][c-1]
        
        if arr[r][c] == "^":
            curr[c] = 0 

    
    dp.append(curr)
 

# for i in range(len(dp)): 
#     print(i, dp[i])

print("ans2:", sum(dp[-1]))






