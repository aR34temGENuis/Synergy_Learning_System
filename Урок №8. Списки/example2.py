n = int(input())
tmp = list(map(int, input().split()))

result = [tmp[-1]] + tmp[:-1]

print(*result)