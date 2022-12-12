# stacks = [
#     ['Z','N'],
#     ['M','C','D'],
#     ['P']
# ]

stacks = [
    ['Q','F','M','R','L','W','C','V'],
    ['D','Q','L'],
    ['P','S','R','G','W','C','N','B'],
    ['L','C','D','H','B','Q','G'],
    ['V','G','L','F','Z','S'],
    ['D','G','N','P'],
    ['D','Z','P','V','F','C','W'],
    ['C','P','D','M','S'],
    ['Z','N','W','T','V','M','P','C']
]

with open("input.txt", 'r') as file:
    for move in file.readlines():
        move = move.split()
        # print(move)
        amount = int(move[1])
        from_stack = int(move[3])-1
        to_stack = int(move[5])-1

        for i in range(0,amount):
            stacks[to_stack].append(stacks[from_stack][-1])
            stacks[from_stack].pop()

        print(stacks)
string = ''
for stack in stacks:
    string += stack[-1]
print(string)    