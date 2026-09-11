numberOfBoardSquares, indexStartingSquare, magicNumber = map(int, input().split())
board = [0] + list(map(int, input().split()))

frogLocation = indexStartingSquare
frogPreviousLocations = []

end     = False
hops    = 0
endType = ""
    
while not end:
    # contains magic number
    if (board[frogLocation] == magicNumber):
        endType = "magic"
        break
    
    # cycle
    if (frogLocation in frogPreviousLocations):
        endType = "cycle"
        break
    
    # Move the frog
    frogPreviousLocations.append(frogLocation)
    frogLocation += board[frogLocation]
    hops += 1
    
    # left of the board
    if (frogLocation < 1):
        endType = "left"
        break
    
    # right of the board
    if (frogLocation > numberOfBoardSquares):
        endType = "right"
        break

print(endType)
print(hops)
