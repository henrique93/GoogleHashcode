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

def exampleSubmition(f):
    values = filereader(f)
    rows = values[0]
    columns = values[1]
    minIngredient = values[2]
    maxIngredient = values[3]
    matrix = values[4]
    for l in range(0, rows):
        for c in range(0 , collumns):
            print(lul)
            
            
def slice(currentRow,currentColumn,maxRow,maxColumn,minIngredient,maxIngredient,matrix):
    if(( currentRow + maxIngredient) > maxRow):
        maxRowSlice = maxRow
    else: 
        maxRowSlice = currentRow + maxIngredient
    if(( currentColumn + maxIngredient) > maxColumn):
        maxColumnSlice = maxColumn
    else: 
        maxColumnSlice = currentColumn + maxIngredient    
    for l in range(0, maxRowSlice - currentRow) :
        for c in range(0, maxColumnSlice - currentColumn):
            