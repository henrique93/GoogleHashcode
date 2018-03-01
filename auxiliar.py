def fileReader(f):
    rides = []
    vehicles = []
    with open(f, 'r') as file:
        line = file.readline()
        rows, columns, vehicleNum, rideNum, bonus, steps = [int(val) for val in line.split()]
        for i in range(0, vehicleNum):
            vehicles.append((0,0))
        for line in file:
            line = line.split()
            ride = [(line[0], line[1]), (line[2], line[3]), line[4], line[5]]
            rides.append(ride)
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
    return (rows, columns, vehicles, rideNum, bonus, steps, rides)

def assignRide(vehiclePos, steps, rides):
    
