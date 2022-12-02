import pandas as pd

with open(r"input.txt") as f:
    inv = pd.DataFrame()
    kcal = 0
    for line in f:
        if line != '\n':
            size = len(line)
            kcal += int(line[:size-1])
        elif line == '\n':
            elfInv = pd.DataFrame({'kcal':[kcal]})
            inv = pd.concat([inv,elfInv],ignore_index=True)
            kcal = 0
    print(inv['kcal'].max()) ## Solution 1
    print(inv['kcal'].nlargest(3).sum()) ## Solution 2
