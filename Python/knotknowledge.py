n = int(input())
l = list(map(int, input().split()))
y = list(map(int, input().split()))

print(list(set(l) - set(y))[0])