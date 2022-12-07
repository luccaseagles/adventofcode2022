

CHARS="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_priority(item):
    return CHARS.index(item) + 1

score = 0
with open("example", "r") as f:
    lines = f.readlines()
    for l in lines:

        backpack = l.strip()
        first_comp = set(backpack[:len(backpack)//2])
        second_comp = set(backpack[len(backpack)//2:])
        bad_item = next(iter(first_comp & second_comp))
        score += get_priority(bad_item)

print(score)

score = 0
with open("input", "r") as f:
    lines = f.readlines()
    groups = [lines[i*3:(i+1)*3] for i in range(len(lines)//3)]
    for group in groups:
        (elfA, elfB, elfC) = (set(e.strip()) for e in group) 
        badge = next(iter(elfA & elfB & elfC))
        score += get_priority(badge)
print(score)