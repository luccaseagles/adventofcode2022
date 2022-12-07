
f = open("example", "r")

#part 1
score = 0
win = [('A','Y'), ('B','Z'), ('C','X')]
draw = [('A','X'), ('B','Y'), ('C','Z')]
#loss = [('A','Z'), ('B','X'), ('C','Y')]
hand_value = {'X':1, 'Y':2 ,'Z':3 }
for l in f:
    hand = (l[0], l[2])
    if hand in win:
        score += 6
    elif hand in draw:
        score += 3
    score += hand_value[hand[1]]
print(score)

#part 2
result_value = {'X':0, 'Y':3, 'Z':6}

hand_value = {
    ('A','X'):3,
    ('A','Y'):1,
    ('A','Z'):2,
    ('B','X'):1,
    ('B','Y'):2,
    ('B','Z'):3,
    ('C','X'):2,
    ('C','Y'):3,
    ('C','Z'):1,    
}

f = open("input", "r")
score = 0

for l in f:
    hand = (l[0], l[2])
    score += result_value[hand[1]]
    score += hand_value[hand]
print(score)