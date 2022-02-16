from itertools import zip_longest


def closest_enemy(positions):
    if len(positions) == 1:
        return 0
    me = positions.index(1)
    if me == 0:
        left = []
    elif me == len(positions):
        right = []
    right = positions[me+1:]
    left = list(reversed(positions[0: me]))
    enemies = zip_longest(right, left)
    for pos, enemy in enumerate(enemies):
        if (enemy[0] or 0) + (enemy[1] or 0) >= 2:
            return pos + 1

    return 0