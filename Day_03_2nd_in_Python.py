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



# def find_max(s, n):
#     stk = [] 
#     remove = len(s) - n

#     for c in s:
#         while remove > 0 and stk and stk[-1] < c:
#             remove -=1
#             stk.pop()
        
#         stk.append(c)

#     return int(''.join(stk[:n]))  #only return the first n characters

# # print(find_max(s, 12))

# output = 0
# for line in s:
#     line = line.replace('\n', '')
#     output += find_max(line, 12)

# print(output)


    

def find_max_dp(s, need):
    total_length = len(s) 

    dp = [["" for _ in range(need+1)] for _ in range(total_length+1)] 

    for pos in range(total_length-1, -1, -1):
        for to_take in range(1, need+1):
            if pos + to_take == total_length:  # this is the base case in the recursive.
                continue
            A = dp[pos+1][to_take]
            B = s[pos] + dp[pos+1][to_take-1]
            
            dp[pos][to_take] = max(A, B)

    return int(dp[0][need])




    # s_length = len(s)

    # dp = [[""] * (need + 1) for _ in range(s_length + 1)]
    
    # for pos in range(s_length-1, -1, -1):
    #     for to_take in range(1, need + 1):
    #         if s_length - pos >= to_take: 
    #             option_skip = dp[pos + 1][to_take]
    #             option_take = s[pos] + dp[pos + 1][to_take - 1]
    #             dp[pos][to_take] = max(option_take, option_skip)

    # return int(dp[0][need])

output = 0
for line in s:
    line = line.replace('\n', '')
    output += find_max_dp(line, 12)

print(output)

