# Data processing
with open('input') as f:
    in_data = [line.rstrip() for line in f]

accumulator = 0
previous_instructions = []
active_instruction = 0

while not active_instruction in previous_instructions:
    previous_instructions.append(active_instruction)
    instr = in_data[active_instruction][:3]
    diff = int(in_data[active_instruction][4:])
    if instr=="acc":
        accumulator+=diff
        active_instruction+=1
    if instr=="jmp":
        active_instruction+=diff
    if instr=="nop":
        active_instruction+=1

print(accumulator)
