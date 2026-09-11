line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
line4 = list(map(int, input().split()))
line5 = list(map(int, input().split()))

contestans = [line1, line2, line3, line4, line5]

bestId = 0
best = 0

for x in range(0, len(contestans)):
    if (sum(contestans[x]) > best):
        bestId = x + 1
        best = sum(contestans[x])

print(bestId)
print(best)