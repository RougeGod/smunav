import roomConnections as rc
from collections import deque

print("Please enter your current room number:")
startingFloor = (rc.roomToFloor(input()))
if (startingFloor == None):
    exit()
print("Please enter your destination room number:")
endingFloor = (rc.roomToFloor(input()))
searchSpace = deque([startingFloor]) #creates a deque with one element, the starting floor
visited = {} #key is where we are, value is where we came from

def traverseAndPrintPath():
    fullPath = deque()
    currentLocation = endingFloor
    #work backwards, adding to the left of the deque so that the final path is forwards
    while not (currentLocation == startingFloor):
        fullPath.appendleft(visited[currentLocation])
        currentLocation = visited[currentLocation]
    if (len(fullPath) == 0):
        print("You're already on the right floor!")
        exit()
    #print the final path
    for floor in fullPath:
        print(floor + "-->", end="")
    print(endingFloor)
    exit()


##MAIN FUNC##
#uses BFS but could be modified to use Djikstra if distances are known between floors
while not len(searchSpace) == 0:
    currentFloor = searchSpace.popleft() #take the first element from the deque
    neighbours = rc.floorConnectionMap[currentFloor]
    for floor in neighbours: #and add all of its connections to the deque as long as we haven't already gone there
        if not (floor in visited):
            visited[floor] = currentFloor 
            searchSpace.append(floor)
        if (floor == endingFloor):
            traverseAndPrintPath()
print("No indoor-only route found.")

        
