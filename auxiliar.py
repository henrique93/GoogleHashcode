def fileReader(f):
    rides = []
    j = 0
    with open(f, 'r') as file:
        line = file.readline()
        rows, columns, vehicleNum, rideNum, bonus, steps = [int(val) for val in line.split()]
        for line in file:
            line = line.split()
            #ride [ride number, start coordinates, finish coordinates, earliest start, latest finish]
            ride = [j, (int(line[0]), int(line[1])), (int(line[2]), int(line[3])), int(line[4]), int(line[5])]
            rides.append(ride)
            j += 1
    #DEBUG PRINTS-------------------------------------------------------
    #print("Number of rows: " + str(rows))
    #print("Number of columns: " + str(columns))
    #print("Number of vehicles: " + str(vehicles))
    #print("Number of rides: " + str(rideNum))
    #print("Bonus: " + str(bonus))
    #print("Steps: " + str(steps))
    #print("Rides:")
    #for l in rides:
        #print(l)
    #-------------------------------------------------------------------
    return (rows, columns, vehicleNum, rideNum, bonus, steps, rides)

def assignRide(vehiclePos, steps, rides):
    for ride in rides:
        rideStart = ride[1]
        rideFinish = ride[2]
        dist = abs((rideStart[0] - vehiclePos[0]) + (rideStart[1] - vehiclePos[1]))
        if ((dist + steps) <= ride[3]): #FIXME <= ou = ???
            distFinish = abs((rideFinish[0] - rideStart[0]) + (rideFinish[1] - rideStart[1]))
            rides.remove(ride)
            return ride, rides, distFinish
    rideToPick = (float("inf"), None, float("inf"))
    for ride in rides:
        rideStart = ride[1]
        rideFinish = ride[2]
        dist = abs((rideStart[0] - vehiclePos[0]) + (rideStart[1] - vehiclePos[1]))
        distFinish = abs((rideFinish[0] - rideStart[0]) + (rideFinish[1] - rideStart[1]))
        canComplete = distFinish + dist + steps <= ride[4]
        if (canComplete):
            if (dist == 0):
                rides.remove(ride)
                return ride, rides, distFinish
            elif (dist < rideToPick[0]):
                rideToPick = (dist, ride, distFinish)
    if (rideToPick[1] is not None):
        rides.remove(rideToPick[1])
    return rideToPick[1], rides, rideToPick[2]

def main(inputFile):
    step = 0
    result = []
    vehicles = []
    rows, columns, vehicleNum, rideNum, bonus, maxSteps, rides = fileReader(inputFile)
    rides.sort(key=lambda x: x[3])
    for i in range(0, vehicleNum):
        vehicles.append([(0,0), 0])
    for i in range(vehicleNum):
        result.append([0])
    moved = True
    while ((len(rides) > 0) and (step < maxSteps) and (moved)): #FIXME
        moved = False
        nextStep = maxSteps
        for vehicle in vehicles:
            if (vehicle[1] < nextStep):
                nextStep = vehicle[1]
        step = nextStep
        for v in range(vehicleNum):
            if (vehicles[v][1] == step):
                ride, rides, distFinish = assignRide(vehicles[v][0], step, rides)
                if (ride is not None):
                    moved = True
                    vehicles[v] = [ride[2], distFinish]
                    result[v][0] += 1
                    result[v].append(ride[0])
    output = inputFile.split(".")[0]
    output += ".out"
    with open(output, "w") as resFile:
        for line in result:
            for word in line:
                resFile.write(str(word) + " ")
            resFile.write("\n")
    return result


def check(f):
    res = 0
    with open(f, "r") as File:
        lines = File.readlines()
        for line in lines:
            line = line.split()
            res += int(line[0])
    return res