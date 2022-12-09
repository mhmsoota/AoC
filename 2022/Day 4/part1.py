with open('input.txt', 'r') as file:
    total_pairs = 0
    for elf_pair in file.readlines():
        found = False
        elf1 = range(
            int(elf_pair.split(',')[0].split('-')[0]),
            int(elf_pair.split(',')[0].split('-')[1])
        )
        elf2 = range(
            int(elf_pair.split(',')[1].split('-')[0]),
            int(elf_pair.split(',')[1].split('-')[1])
        )
        if set(elf1).issubset(set(elf2)) or set(elf2).issubset(set(elf1)):
            total_pairs += 1
            found = True
        
        print("Elf 1: ", elf1, " Elf 2: ", elf2, " Total: ", total_pairs, " ", found)
    print(total_pairs)