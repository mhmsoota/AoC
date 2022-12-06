file = open('input.txt', 'r')
lines = file.readlines()

max_sum = 0
max_elf = 0

current_sum = 0
current_elf = 1


for line in lines:
    # print(line)
    if line == '\n':
        current_elf += 1
        current_sum = 0
        print("On elf no:", current_elf)
    else:
        current_sum += int(line)

    if current_sum > max_sum:
        max_sum = current_sum
        max_elf = current_elf

print("Maximum Sum: ", max_sum, "Max Elf: ", max_elf)
