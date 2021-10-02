def is_unique(s):
    return len(set(s)) == len(s)

def is_unique_with_list(s):
    x = []
    for i in s:
        if i in x:
            return False
        x.append(i)
    return True