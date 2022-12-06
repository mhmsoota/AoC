with open('input.txt', 'r') as file:
    score = 0
    # print(file.readlines())
    for round in file.readlines():
        opp = round[0]
        win = round[2]

        if (opp == 'A'):        # Opponent chose Rock
            if (win == 'X'):     # Lose: so choose scissor
                score += 3 + 0      # Choice score + Win Score
            elif (win == 'Y'):   # Draw: so choose Rock
                score += 1 + 3
            elif (win == 'Z'):   # Win: so choose paper
                score += 2 + 6
        elif (opp == 'B'):        # Opponent chose Paper
            if (win == 'X'):     # Lose: so choose Rock
                score += 1 + 0      # Choice score + Win Score
            elif (win == 'Y'):   # Draw: so choose Paper
                score += 2 + 3
            elif (win == 'Z'):   # Win: so choose Scissor
                score += 3 + 6
        elif (opp == 'C'):        # Opponent chose Scissor
            if (win == 'X'):     # Lose: so choose Paper
                score += 2 + 0      # Choice score + Win Score
            elif (win == 'Y'):   # Draw: so choose Scissor
                score += 3 + 3
            elif (win == 'Z'):   # Win: so choose Rock
                score += 1 + 6
        # print("Opp: ", opp, "Win: ", win, "Score Now: ", score)
    print(score)

        