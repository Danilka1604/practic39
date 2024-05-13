N, M = map(int, input().split())

Anya = {int(input()) for _ in range(N)}
Borya = {int(input()) for _ in range(M)}

both = sorted(Anya & Borya)
only_Anya = sorted(Anya - Borya)
only_Borya = sorted(Borya - Anya)

print(len(both))
print(*both)
print(len(only_Anya))
print(*only_Anya)
print(len(only_Borya))
print(*only_Borya)
