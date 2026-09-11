firstLine = [int(x) if x != "-" else x for x in input()]
secondLine = [int(x) if x != "-" else x for x in input()]

puzzelBox = [firstLine, secondLine]
moves = 0
goalLocation = {
    1: (0, 0),
    2: (0, 1),
    3: (1, 0)
}

def boardscore(board):
    score = 0
    for x in range(2):
        for y in range(2):
            value = board[x][y]
            if value != "-":
                goalX, goalY = goalLocation[value]
                score += abs(x - goalX)
                score += abs(y - goalY)

    return score


while True:

    # Check if solved
    if puzzelBox == [[1, 2], [3, "-"]]:
        break

    # Find the blank
    for x in range(2):
        for y in range(2):
            if puzzelBox[x][y] == "-":
                blankX = x
                blankY = y

    # directions the blank can move
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    possibleMoves = []

    # Find all legal moves
    for dx, dy in directions:
        newX = blankX + dx
        newY = blankY + dy
        if 0 <= newX < 2 and 0 <= newY < 2:

            # Swap blank with the number
            newBoard = [row[:] for row in puzzelBox]
            newBoard[blankX][blankY], newBoard[newX][newY] = \
                newBoard[newX][newY], newBoard[blankX][blankY]

            possibleMoves.append(newBoard)

    # Start with the first possible move
    bestBoard = possibleMoves[0]
    bestScore = boardscore(bestBoard)

    # Find the move with the lowest score
    for board in possibleMoves[1:]:
        score = boardscore(board)
        if score < bestScore:
            bestBoard = board
            bestScore = score

    # Make the best move
    puzzelBox = bestBoard
    moves += 1


# Print result
print(moves)
