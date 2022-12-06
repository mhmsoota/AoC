with open("input.txt", 'r') as file:
    elf_calories = []
    sum = 0
    for line in file.readlines():
        if line == '\n':
            elf_calories.append(sum)
            sum = 0
        else:
            sum += int(line)
    elf_calories.sort(reverse=True)
    print(elf_calories[0]+elf_calories[1]+elf_calories[2])