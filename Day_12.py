# no need to figure out the big algo for exact-cover problem. Just need to check if the area is big enough to host all the gifts without rotating/flipping.

import re

with open('Day_12_input.txt') as f: 
    input = f.read()

*shape, regions = input.strip().split('\n\n')

gift_size = []

for s in shape:
    gift_size.append(s.count('#'))


cleaned_region = []

for region in regions.split('\n'): #unpack the numbers into [x, x, x, x, x, x, x], first two is the size of the region
    curr = list (map(int, re.findall(r'\d+', region)))
    cleaned_region.append(curr)

cnt = 0  


for w, h, *nums in cleaned_region:  
    avail_space_gift_cnt = w*h # (w*h//9)
    total_size = 0
    for i, n in enumerate(nums):
        total_size += n * gift_size[i]
    if avail_space_gift_cnt >= total_size:
        print(w, h, nums)
        cnt += 1
print(cnt)
    
    










