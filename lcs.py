def lcs(string1,string2):
    directions = {}
    table = {}
    get_directions(string1,string2,directions,table)
    operations = []
    derive_lcs(string1,string2,operations,directions)
    operations.reverse()
    return operations



def derive_lcs(string1,string2,operations,directions):
    i = len(string1)
    j = len(string2)
    while True :
        if i <= 0 and j <= 0 :
            break
        if directions[i, j] == 'D':

            operations.append('LCS ' + string1[i - 1])
            i -= 1
            j -= 1
        elif directions[i, j] == 'U':

            operations.append('ADD ' + string2[j - 1])
            j -= 1
        elif directions[i, j] == 'L':

            operations.append('REM ' + string1[i - 1])
            i -= 1
        elif directions[i, j] == 'E':
            if i == 0:

                operations.append('ADD ' + string2[j - 1])
                j -= 1
            elif j == 0:

                operations.append('REM ' + string1[j - 1])
                i -= 1


def get_directions(string1,string2,directions,table):
            for i in range(len(string1) + 1):
                for j in range(len(string2) + 1):
                    if i == 0 or j == 0:
                        table[i, j] = 0
                        directions[i, j] = "E"  # empty
                    elif string1[i - 1] == string2[j - 1]:
                        table[i, j] = table[i - 1, j - 1] + 1
                        directions[i, j] = "D"  # diagonal
                    else:
                        if table[i - 1, j] >= table[i, j - 1]:
                            table[i, j] = table[i - 1, j]
                            directions[i, j] = "L"  # left
                        else:
                            table[i, j] = table[i, j - 1]
                            directions[i, j] = "U"  # up

if __name__  ==  "__main__" :
    print lcs( ('satya'),('xsbtnyza'))