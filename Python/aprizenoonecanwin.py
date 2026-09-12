N, X = list(map(int, input().split()))
items = list(map(int, input().split()))
items.sort()

if N == 1:
    print("1")
elif items[-1] + items[-2] <= X:
    print(N)
else:
    for i in range(N):
        if items[i] + items[i+1] > X:
            print(i+1)
            break