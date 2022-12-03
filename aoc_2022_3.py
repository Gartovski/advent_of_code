# Author: Fabio Gervasi
import string

import numpy as np
import pandas as pd

with open("day_3/input.txt", "r") as file:
    lines = file.readlines()

    common_characters = []

    for line in lines:
        half = int(len(line) / 2 // 1)
        first_half, second_half = line[:half], line[half:]
        common = list(set(first_half) & set(second_half))[0]
        common_characters.append(common)

lowercase_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
uppercase_dict = dict(zip(string.ascii_uppercase, range(27, 53)))
letter_dict = lowercase_dict | uppercase_dict

sum = 0
for letter in common_characters:
    sum += letter_dict[letter]

print(sum)

# %% Part2
with open("day_3/input.txt", "r") as file:
    lines = file.readlines()
    groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]

    badges = []

    for group in groups:
        common = list(
            set(group[0].strip()) & set(group[1].strip()) & set(group[2].strip())
        )[0]
        badges.append(common)

sum_badges = 0
for letter in badges:
    sum_badges += letter_dict[letter]

print(sum_badges)
