# Data processing
with open('input') as f:
    in_data = [line.rstrip() for line in f]

def swap_instructions(instruction):
    if(instruction[:3] == "jmp"):
        return "nop " + instruction[4:]
    elif(instruction[:3] == "nop"):
        return "jmp " + instruction[4:]

total_instructions = len(in_data)

for i in range(0, total_instructions):
    if in_data[i][:3] == "acc":
        continue
    in_data[i] = swap_instructions(in_data[i])
    
    counted_instructions = 0
    active_instruction = 0
    accumulator = 0
    while counted_instructions < total_instructions+1:
        instr = in_data[active_instruction][:3]
        diff = int(in_data[active_instruction][4:])
        if instr=="jmp":
            active_instruction+=diff
        if instr=="acc":
            accumulator += diff
            active_instruction+=1
        if instr=="nop":
            active_instruction+=1

        counted_instructions += 1

        if active_instruction == total_instructions:
            print(accumulator)
            exit()

    in_data[i] = swap_instructions(in_data[i])
