with open('input.txt', 'r') as file:
    score = 0
    # print(file.readlines())
    for round in file.readlines():
        opp = round[0]
        me = round[2]
        # print("Opponent: ", opponent, "Me: ", me)
        if (opp == 'A'):        # Opponent chose Rock
            if (me == 'X'):     # I chose Rock - so draw
                score += 1 + 3      # Choice score + Win Score
            elif (me == 'Y'):   # I chose Paper - so win
                score += 2 + 6
            elif (me == 'Z'):   # I chose Scissor - so lose
                score += 3 + 0
        elif (opp == 'B'):        # Opponent chose Paper
            if (me == 'X'):     # I chose Rock - so lose
                score += 1 + 0      # Choice score + Win Score
            elif (me == 'Y'):   # I chose Paper - so draw
                score += 2 + 3
            elif (me == 'Z'):   # I chose Scissor - so win
                score += 3 + 6
        elif (opp == 'C'):        # Opponent chose Scissor
            if (me == 'X'):     # I chose Rock - so win
                score += 1 + 6      # Choice score + Win Score
            elif (me == 'Y'):   # I chose Paper - so lose
                score += 2 + 0
            elif (me == 'Z'):   # I chose Scissor - so draw
                score += 3 + 3
    print(score)

        