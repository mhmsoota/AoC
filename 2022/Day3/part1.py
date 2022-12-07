with open('input.txt', 'r') as file:
    priority_sum = 0
    for rucksack in file.readlines():
        compartment1 = rucksack[:len(rucksack)//2]
        compartment2 = rucksack[len(rucksack)//2:]
        # print(compartment1, '\n', compartment2)
        common_element = list(set(compartment1)&set(compartment2))[0]
        # print(a)

        if common_element.islower():
            priority = ord(common_element) - ord('a') + 1
        else:
            priority = ord(common_element) - ord('A') + 27

        priority_sum += priority

        # print("\nCommon Element: ", common_element, ' ', ord(common_element))
        # print("Priority: ", priority)
        # print("Priority Sum: ", priority_sum)
    print(priority_sum)