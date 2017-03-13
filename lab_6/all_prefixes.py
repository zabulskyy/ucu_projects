def all_prefixes(word):
    new = ''
    li = set()
    for i in word:
        if i not in new:
            new += i
    for i in range(1, len(new) + 1):
        li.add(new[:i])
    return li