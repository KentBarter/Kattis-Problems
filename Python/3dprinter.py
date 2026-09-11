n = int(input())

printers = 1
days = 0

while printers < n:
    printers *= 2
    days += 1

days += (n + printers - 1)

print(days)
