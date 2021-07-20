import math


def steps_based(steps):
    initial_competence = 0.01
    total_steps = 10000
    p = 2
    return min(1, math.pow(steps * (1 - math.pow(initial_competence, p)) / total_steps + math.pow(initial_competence, p), 1 / p))
