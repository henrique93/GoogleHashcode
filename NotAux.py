def fileReader(f):
    matrix = []
    with open(f, 'r') as file:
        line = file.readline()
        print(line)
        rows = line[0]
        columns = line[2]
        minIngredient = line[4]
        maxCell = line[6]
        for line in file:
            matrix += [line.rstrip()]
    #DEBUG PRINTS-------------------------------------------------------
    #print("Number of rows: " + rows)
    #print("Number of columns: " + columns)
    #print("Minimum of each ingredient in each slice: " + minIngredient)
    #print("Maximum cells of each slice: " + maxCell)
    #print("Matrix:")
    #for l in matrix:
        #print(l)
    #-------------------------------------------------------------------
    return (rows, columns, minIngredient, maxCell, matrix)


def checkSlice(minIngredient, maxCell, sliceMatrix):
    t = 0
    m = 0
    c = 0
    for i in sliceMatrix:
        if (i == "t"):
            t += 1
        elif (i == "m"):
            m += 1
        c += 1
        if (c > maxCell):
            return False
    if (minIngredient < t and minIngredient < m):
        return True
    return False
