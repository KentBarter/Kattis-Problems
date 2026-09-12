n, k = list(map(int, input().split()))
trips = list(map(int, input().split()))

output = []
for x in range(len(trips)):
    midpoint = (n + 1) / 2
    if (trips[x] > midpoint):
        output.append(n)
    else:
        output.append(1)

outputstr = ""
for x in range(len(output)):
    outputstr += str(output[x]) + " "
print(outputstr)