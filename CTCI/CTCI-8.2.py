# CTCI Question 8.2
# O(2^rc) Space()
def getPath(maze) :
    if (maze == None or len(maze) == 0): return None
    path = []
    failedPoints = []
    if (grid(len(maze)-1, len(maze[0])-1, maze, path, failedPoints)):
        print(failedPoints)
        return path
        
    return None

def grid(r,c, maze, path, failedPoints) :
    if (r < 0 or c < 0):
         return False
    if(maze[r][c] == False): return False
    if( (r,c) in failedPoints): return False

    isatOrigin = ((r==0) and (c==0))
    if (isatOrigin or grid(r,c-1, maze,path, failedPoints) or grid(r-1,c,maze,path,failedPoints)):
        path.append((r,c))
        return True
    
    failedPoints.append((r,c))
    return False




    # if(r == 0 and c == 0):
    #     return True
    # print("Hello")
    # up = left = False
    # if( (r-1,c) in cellOffLimits and r-1 >= 0):
    #     up = grid(r-1,c, cellOffLimits)

    # if((r,c-1) not in cellOffLimits and c-1 >= 0):
    #     left = grid(r, c-1, cellOffLimits)
    
    # if(up == True or left == True): return True
    # else: return False


testR = 3
testC = 3
OffLimits = {(1,0), (0,1)}
# print(grid(testR,testC, OffLimits))


maze = [[True, True,True], 
        [False, True,True],
        [True, True,True]]
print(getPath(maze))


