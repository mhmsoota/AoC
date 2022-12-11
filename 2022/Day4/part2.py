with open('input.txt', 'r') as f:
    lines = f.readlines()
    assignment_pairs = [entry.strip() for entry in lines]
    number_of_overlap = 0
    for assignment_pair in assignment_pairs:
        first_range, second_range = assignment_pair.split(',')
        start_a, end_a = map(int, first_range.split('-'))
        start_b, end_b = map(int, second_range.split('-'))
        if start_a in range(start_b, end_b+1) or end_a in range(start_b, end_b+1) or  start_b in range(start_a, end_a+1) or end_b in range(start_a, end_a+1):
            number_of_overlap += 1
    print(number_of_overlap)