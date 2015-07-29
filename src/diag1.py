#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     30/07/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#def main():
    #pass

grid = [
[7,8,8,4,0,0],
[0,5,1,0,4,9],
[8,0,0,6,9,5],
[4,5,8,1,2,0]
]

def checkDiags(grid,diagLen,n):
    for y in range(len(grid) - (diagLen - 1)):
        for x in range(len(grid[y])):
            if grid[y][x] == n:
                if x - (diagLen - 1) >= 0:
                    if grid[y+1][x-1] == n:
                        if grid[y+2][x-2] == n:
                            return True
    return False

print ("done"),
print (checkDiags(grid,3,0))



#if __name__ == '__main__':
    #main()