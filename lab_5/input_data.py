import math
from random import uniform


def sub_sequence():
    return math.sqrt(12 / 5) * (sum([uniform(0, 1) for _ in range(5)]) - (5 / 2))


def sequence_with_math_hope_and_dispersion(sub_seq, math_hope=8, dispersion=1.2):
    return math_hope + dispersion * (0.01 * sub_seq * (97 + sub_seq ** 2))


def create_input(n=30000):
    return [sequence_with_math_hope_and_dispersion(sub_sequence()) for _ in range(n)]
