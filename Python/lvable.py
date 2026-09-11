n = int(input())
text = input()

# Check if "lv" already exists
for x in range(len(text) - 1):
    if text[x] == "l" and text[x + 1] == "v":
        print(0)

has_l = "l" in text
has_v = "v" in text

# Both are missing
if not has_l and not has_v:
    print(2)

# Only one is present
elif not has_l or not has_v:
    print(1)

# Both are present, but not together
else:
    print(1)