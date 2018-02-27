def fileReader(f):
    matrix = []
    with open(f, 'r') as file:
        line = file.readline()
        print(line)
        rows = line[0]
        columns = line[2]
        minIngredient = line[4]
        maxIngredient = line[6]
        for line in file:
            matrix += [line.rstrip()]
    #DEBUG PRINTS-------------------------------------------------------
    #print("Number of rows: " + rows)
    #print("Number of columns: " + columns)
    #print("Minimum of each ingredient in each slice: " + minIngredient)
    #print("Maximum of each ingredient in each slice: " + maxIngredient)
    #print("Matrix:")
    #for l in matrix:
        #print(l)
    #-------------------------------------------------------------------
    return (rows, columns, minIngredient, maxIngredient, matrix)