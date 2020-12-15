def play(game, turns):
    if turns < 1:
        return None
    if len(game) == 0:
        game = [0]
    if turns <= len(game):
        return game[turns - 1]
    lastnum = game[-1]
    seen = [0] * turns  # dumb but fast :(
    i = 1
    while i < len(game):
        seen[game[i - 1]] = i
        i += 1
    while i < turns:
        j = seen[lastnum]
        seen[lastnum] = i
        lastnum = 0 if j == 0 else i - j
        i += 1
    return lastnum

# Van Eck sequence
# https://www.rosettacode.org/wiki/Van_Eck_sequence
print('Van Eck:', [play([], i) for i in range(1, 20)])

# Test input
# https://adventofcode.com/2020/day/15
from itertools import permutations
for game in permutations([1, 2, 3]):
    print(game, 'x 2020 =', play(game, 2020))

# Part 1
game = [0,3,6]
print('1:', play(game, 2020))

# Part 2
game = [13,16,0,12,15,1]
print('2:', play(game, 30000000))
