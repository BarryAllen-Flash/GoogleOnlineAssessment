def compare_strings(A, B):
    A, B = A.split(','), B.split(',')
    C = []
    for b in B:
        count = 0
        for a in A:
            if a.count(min(a)) < b.count(min(b)):
                count += 1
        C.append(count)
    return C
