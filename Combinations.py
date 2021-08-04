from itertools import combinations
s, n = input().split()
print(*[''.join(i) for i in sorted(s)],sep='\n')
print(*[''.join(i) for i in combinations(sorted(s),int(n))] , sep='\n')
