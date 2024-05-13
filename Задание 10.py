
sequence = input().split()
encountered = set()
for num in sequence:
    if num in encountered:
        print("YES")
    else:
        print("NO")
        encountered.add(num)
