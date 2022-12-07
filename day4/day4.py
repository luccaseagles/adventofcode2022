import re

from dataclasses import dataclass

part1_score = 0
part2_score = 0

with open("input", "r") as f:
    lines = f.readlines()
    for l in lines:
        split_in = re.split("-|,", l)
        rangeA = {*range(int(split_in[0]), int(split_in[1])+1)}
        rangeB = {*range(int(split_in[2]), int(split_in[3])+1)}
        if rangeA.issubset(rangeB) or rangeB.issubset(rangeA) :
            part1_score += 1
        if not rangeA.isdisjoint(rangeB):
            part2_score += 1

print(part1_score)
print(part2_score)