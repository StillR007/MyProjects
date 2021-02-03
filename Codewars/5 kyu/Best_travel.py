"""
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper
a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of
driving and he says to Mary that he doesn't want to drive more than t = 174 miles and
he will visit only 3 towns.
Which distances, hence which towns, they will choose so that the sum of the distances
is the biggest possible to please Mary and John?
"""

from itertools import combinations


def choose_best_sum(t, k, ls):
    a = [i for i in combinations(ls, k) if sum(list(i)) <= t]
    while True:
        for combi in a:
            if sum(combi) == t:
                return sum(combi)
            else:
                pass
        t -= 1
        if t < 0:
            return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
choose_best_sum(230, 4, xs)  # 230
choose_best_sum(430, 5, xs)  # 430
choose_best_sum(430, 8, xs)  # None
