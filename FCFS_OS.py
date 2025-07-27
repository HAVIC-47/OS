x = int(input("Enter how many PID: "))
info = {}

for z in range(x):
    p = "P" + str(z+1)
    aa = int(input("Arrival for " + p + ": "))
    bb = int(input("Burst for " + p + ": "))
    info[p] = [aa, bb]

info = sorted(info.items(), key=lambda k: k[1][0])

comp = []
for y in range(len(info)):
    if y == 0:
        comp.append(info[y][1][0] + info[y][1][1])
    else:
        if info[y][1][0] > comp[y-1]:
            comp.append(info[y][1][0] + info[y][1][1])
        else:
            comp.append(comp[y-1] + info[y][1][1])

turn = []
for t in range(len(info)):
    turn.append(comp[t] - info[t][1][0])

wait = []
for w in range(len(info)):
    wait.append(turn[w] - info[w][1][1])

s = 0
for w in wait:
    s += w
avg = s / x

print()
print(f"{'PID':<5}{'Arv':<6}{'Bur':<6}{'Comp':<8}{'Turn':<7}{'Wait':<5}")
for i in range(x):
    print(f"{info[i][0]:<5}{info[i][1][0]:<6}{info[i][1][1]:<6}{comp[i]:<8}{turn[i]:<7}{wait[i]:<5}")

print()
print("Average Wait:", round(avg, 2))
