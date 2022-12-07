with open('input.txt', 'r') as file:
    priority_sum = 0
    all_groups = file.readlines()

    for i in range(0,len(all_groups),3):
        badge = set.intersection(*map(set,all_groups[i:i+3]))
        try:
            badge.remove('\n')
        except KeyError:
            pass
        badge = list(badge)[0]
        # print(badge)


        if badge.islower():
            priority = ord(badge) - ord('a') + 1
        else:
            priority = ord(badge) - ord('A') + 27

        if (priority < 1):
            print(
                "Problem Here",
                all_groups[i:i+3]
            )
            break
        
        priority_sum += priority
        # print("\nBadge: ", badge, " ", priority)
        # print("Priority: ", priority)
        # print("Priority Sum: ", priority_sum)
    
    print(priority_sum)