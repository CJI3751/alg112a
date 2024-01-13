def perm(n):
    def permNext(n, p, used):
        if len(p) == n:
            result.append(p.copy())
            return
        for x in range(n):
            if not used[x]:
                p.append(x)
                used[x] = True
                permNext(n, p, used)
                used[x] = False
                p.pop()

    result = []
    permNext(n, [], [False] * n)
    return result
  
print(perm(2))
print(perm(3)) 
