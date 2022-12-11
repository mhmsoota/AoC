with open('input.txt', 'r') as f:
    lines = f.readlines()
    assignment_pairs = [entry.strip() for entry in lines]

def is_range_a_in_range_b(range_a, range_b):
    start_a, end_a = map(int, range_a.split('-'))
    start_b, end_b = map(int, range_b.split('-'))
    return start_b <= start_a and end_a <= end_b

number_of_contains = 0
for assignment_pair in assignment_pairs:
    first_range, second_range = assignment_pair.split(',')
    if is_range_a_in_range_b(first_range, second_range) or is_range_a_in_range_b(second_range, first_range):
        number_of_contains += 1
print(number_of_contains)    


# with open('input.txt', 'r') as file:
#     total_pairs = 0
#     for elf_pair in file.readlines():
#         found = False
#         elf1 = range(
#             int(elf_pair.split(',')[0].split('-')[0]),
#             int(elf_pair.split(',')[0].split('-')[1])
#         )
#         elf2 = range(
#             int(elf_pair.split(',')[1].split('-')[0]),
#             int(elf_pair.split(',')[1].split('-')[1])
#         )
#         if set(elf1).issubset(set(elf2)) or set(elf2).issubset(set(elf1)):
#             total_pairs += 1
#             found = True
        
#         print("Elf 1: ", elf1, " Elf 2: ", elf2, " Total: ", total_pairs, " ", found)
#     print(total_pairs)