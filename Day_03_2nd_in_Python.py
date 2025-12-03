s='98767615212221333223223642257233232272642637612321222242222326772231222771342132342272214328275121812237221111'

with open("Day_03_input.txt") as f:
    s = f.readlines()


# @lru_cache
# def find_max(s, n):
    
#     if len(s) == n:
#         return s
#     elif n == 1:
#         return str(max(list(s)))
#     else: 
#         A = s[0] + find_max(s[1:], n-1)
#         B = find_max(s[1:], n)
#         return str(max(int(A), int(B)))

# total = 0
# for curr in s:
#     total += int(find_max(curr, 12))

# print(total)



def find_max(s, n):
    stk = [] 
    remove = len(s) - n

    for c in s:
        while remove > 0 and stk and stk[-1] < c:
            remove -=1
            stk.pop()
        
        stk.append(c)

    return int(''.join(stk[:n]))  #only return the first n characters

# print(find_max(s, 12))

output = 0
for line in s:
    line = line.replace('\n', '')
    output += find_max(line, 12)

print(output)


    

        