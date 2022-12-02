def convert(text,dic):
    for i,j in dic.items():
        text = text.replace(i,j)
    return int(text)

with open(r"input.txt") as f:
    sol1 = 0
    sol2 = 0
    for line in f:
        line = line.split(" ")
        #### Solution 1
        dic1 = {'A':'1','B':'2','C':'3','X':'1','Y':'2','Z':'3'}
        line1 = [convert(line[0],dic1),convert(line[1],dic1)]
        ## Find draws
        if line1[0] == line1[1]:
            line1[0] = 3
        ## Find losses
        elif (line1[1]==1 and line1[0]==2) or (line1[1]==2 and line1[0]==3) or (line1[1]==3 and line1[0]==1):
            line1[0] = 0
        ## Find wins
        elif (line1[1]==1 and line1[0]==3) or (line1[1]==2 and line1[0]==1) or (line1[1]==3 and line1[0]==2):
            line1[0] = 6
        sol1 = sum(line1,sol1)
        #### Solution 2
        dic2 = {'X':'0','Y':'3','Z':'6'} ## XYZ point correction
        dic3 = {'A':'3','B':'1','C':'2'} ## Loss points
        dic4 = {'A':'2','B':'3','C':'1'} ## Win points
        line2 = [line[0],convert(line[1],dic2)]
        ## Find draws
        if line2[1] == 3:
            line2[0] = convert(line[0],dic1)
        ## Find losses
        if line2[1] == 0:
            line2[0] = convert(line[0],dic3)
        ## Find wins
        if line2[1] == 6:
            line2[0] = convert(line[0],dic4)
        sol2 = sum(line2,sol2)

    print(sol1) ## Solution 1 answer
    print(sol2) ## Solution 2 answer
