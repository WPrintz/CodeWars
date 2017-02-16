def bouncy_ratio(percent):
    is_bouncy = lambda n: any(a < b for a, b in zip(n, n[1:])) \
                        and any(a > b for a, b in zip(n, n[1:]))
    n, bouncy = 99, 0
    while bouncy < percent * n:
        n += 1
        bouncy += is_bouncy(str(n))
    return n