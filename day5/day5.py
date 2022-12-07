from dataclasses import dataclass
import re

@dataclass
class Instruction:
    n: int
    start_stack: int
    end_stack: int

def parse_input():
    N = 9
    inst_idx = 0
    instructions = []
    with open("input", "r") as f:
        lines = f.readlines()
        stacks = [ [] for _ in range(N)]
        for j, l in enumerate(lines):
            if lines[j+1] == "\n":
                inst_idx = j+2 
                break
            for i in range(N):
                if l[i*4+1] != ' ':
                    stacks[i].append(l[i*4+1])
        for l in lines[inst_idx:]:
            c = re.findall(r'\d+', l)
            instructions.append(Instruction(int(c[0]),int(c[1])-1,int(c[2])-1))
    return stacks, instructions
    
def print_top(stacks):
    for s in stacks:
        print(s[0], end="")
    print()

stacks, instructions = parse_input()

for inst in instructions:
    for i in range(inst.n):
        el = stacks[inst.start_stack].pop(0)
        stacks[inst.end_stack].insert(0,el)
print_top(stacks)


stacks, instructions = parse_input()

for inst in instructions:
    stacks[inst.end_stack] = stacks[inst.start_stack][:inst.n] + stacks[inst.end_stack]
    stacks[inst.start_stack] = stacks[inst.start_stack][inst.n:]
    

print_top(stacks)





        
