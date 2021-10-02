import collections
def check_permutations(s, t):
    s_map = collections.Counter(s)
    t_map = collections.Counter(t)
    return t_map == s_map