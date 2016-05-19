import collections as c

# Dicts mapping rolls to probabilities.
def combine_rolls(roll1, roll2):
    result = c.defaultdict(lambda: 0)
    for value1, prob1 in roll1.items():
        for value2, prob2 in roll2.items():
            result[value1 + value2] += prob1 * prob2
    return result

def generic_roll(dice_type, dice_count):
    base_prob = 1 / dice_type
    base_roll = {i:base_prob for i in range(1, dice_type + 1)}
    result = base_roll
    for i in range(dice_count - 1):
        result = combine_rolls(result, base_roll)
    return result

def advantage_roll(dice_type):
    result = dict()
    search_space = pow(dice_type, 2)
    for i in range(1, dice_type + 1):
        nums_lower = i - 1
        result[i] = (1 + nums_lower) / search_space
    return result

def stats_roll():
    def get_possib(dice_count):
        if dice_count == 1:
            return [(i,) for i in range(1, 7)]
        result = []
        previous = get_possib(dice_count - 1)
        for prev in previous:
            for i in range(1, 7):
                result.append((i,) + prev)
        return result
    rolls = get_possib(4)
    rolls = [sum(roll) - min(roll) for roll in rolls]
    counts = c.Counter(rolls)
    result = dict()
    for val_sum, count in counts.items():
        result[val_sum] = count / len(rolls)
    return result

def make_culumlative(distribution, max_val, min_val):
    cumulative = 0
    result = dict()
    for i in range(max_val, min_val, -1):
        cumulative += distribution[i]
        result[i] = cumulative
    return result

stats_cumulative = make_culumlative(stats_roll(), 18, 3)
print(pow(stats_cumulative[15], 3))
print(generic_roll(8, 20))
