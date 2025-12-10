def generate_combo(arr, curr, n, output):
    if n == 0:
        output.append(curr)
    else:
        for i in range(len(arr)):
            generate_combo(arr[i+1:], curr + [arr[i]], n-1, output)


def current_total_combo(total):
    output = []

    hmp = {}
    for n in range(total): 
        arr = list(range(total)) 
        output = [] 
        generate_combo(arr, [], n+1, output)
        hmp[n+1] = output
    
    return hmp

# print(current_total_combo(total))

def current_combo_press(curr, combo, avail):
    for c in combo:
        for i in avail[c]:
            if curr[i] == ".":
                curr[i] = "#"
            else:
                curr[i] = "."
    return curr


with open('Day_10_input.txt') as f:
    input = f.readlines()

all_list = [_.strip() for _ in input]


# go through all the possible combination, until the target is matched

######### part 1


output = []
for todo in all_list:
    target = list(todo.split(']')[0][1:].strip())
    avail_tmp =  [_.split(",") for _ in todo[todo.find(']') + 2 : todo.find('{') -1 ].replace("(", "").replace(")", "").split(" ")]
    lights = todo.split('{')[1].replace("}", "")
    avail = []
    for _ in avail_tmp:
        avail.append([])
        for x in _:
            avail[-1].append(int(x))
    total = len(avail)

    all_combo = current_total_combo(total)
    # print(total)

    for k, v in all_combo.items():
        find = 0 
        for combo in v:
            curr = ['.'  for _ in (target)]
            curr = current_combo_press(curr, combo, avail)
            if curr == target:
                find = 1 
                output.append(k)
                break
        if find == 1 :
            break 



print('ans1 : ', sum(output))




# print(current_total_combo(5))
############################# part 2 

### https://topaz.github.io/paste/#XQAAAQA4BQAAAAAAAAARiEJHiiMzw3cPM/1Vl+2nx/DqKkM2yi+HVdpp+qLh9J+V7GtPfC3aY7mQDmDbbqhKs4YpItyMXr6B64BcFlLmgUh47w6uYeXjf+4BYzbwhWanBFyIxBrbPGrdvUeKG68DLgrU7gNhkGzRqBl7eBQMR6VqCKvJ7965ScEJREQiymcFrhE92bMHoobrV26w5J7NKMOuHW1wKdlxjMIhamllyqYEHq5lWGGvFgk/cqOJAtHR0hcoaiOxrQjGpavcAISBf8Z9+1Xwjeuaz+PXKNqbY/LZmnpiTt8wISg9rRzdYLxXCnPc8iqn8C52aikMI1SuDuVYvCG5sc7Jo8oeoMSByJS/t60qBVqh916zFS7CrdOR/jeqQo+KXaeN41PQWl87VGluSpxfXfvR9n3ky74tfPAx1uPkBC3L8Dz6tcihAsAX4eazPuMsgbTmbnpbP1bQe3eatmGIOREEtOHWrNgRKGZ2q7OhrF8ahaq/zI3uY2VfQjxBxAjUWNyAerfp0jQ64yT4FlQaxSVeBOh+R40CDZSxMYuX9GvyHBKpdOFHS4wuDY+1qhWbv8A/A8qX1WZbg4AFxdCzBv1M5jNsBqnkzOUKOdlm6zpn+kpq0LQWoGkwyhmTSpiiiTv1za6p3e7pczgdBbBpAo3lXlovNGUB1Sjic9bHTRnX2c5T2rd5Z+wAN95anlllzcbqlvGgLneIQymzjHb2bh/PBI//wNdA3tobbNbUgB296kSkxC3wU4bLSZL2clWjMfiq3oUlcB77EbDSPfk7PT/aPGhQiyCopzoPQLvGbfj59DvEeY8N/CXzYTiY+v46Ea2qpv2oT6ciRL6Op683Byxz80d3LaYLGHco2DyTeAci3P0dNtE=
### https://www.reddit.com/r/adventofcode/comments/1pity70/comment/ntamo5c/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button




# import sys
import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from time import time

ts = time()

machines = []

with open("Day_10_input.txt") as f:
    input = f.readlines()

lines = [i.strip() for i in input]


for line in lines:
    button_strs = re.findall(r"\(([^)]*)\)", line)
    buttons = []
    for button in button_strs:
        inds = [int(x) for x in button.split(',')]
        buttons.append(inds)
    m = re.search(r"\{([^}]*)\}", line)
    jolts = [int(x) for x in m.group(1).split(',')]
    machines.append((buttons, jolts))

def ilp(buttons, jolts): # Mixed Integer Linear Programming
    n = len(jolts)
    m = len(buttons)

    A = np.zeros((n, m), dtype=int)
    for j, inds in enumerate(buttons):
        for i in inds:
            A[i, j] = 1

    c = np.ones(m, dtype=float)

    jolts = np.array(jolts, dtype=float)
    lc = LinearConstraint(A, lb=jolts, ub=jolts)

    bounds = Bounds(lb=np.zeros(m), ub=np.full(m, np.inf))

    integrality = np.ones(m, dtype=int)

    res = milp(c=c,
               constraints=[lc],
               integrality=integrality,
               bounds=bounds)
    if res.status != 0:
        raise RuntimeError(f"ILP failed with status {res.status}: {res.message}")

    return int(round(res.fun))

total = 0
for buttons, jolts in machines:
    total += ilp(buttons, jolts)

print(total)

# print(f"runtime: {time() - ts:.4f}s")

