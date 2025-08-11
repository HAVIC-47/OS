n = int(input("Enter number of processes: "))

pid = []
at = []
bt = []
pr = []
ct = [0] * n
tat = [0] * n
wt = [0] * n
done = [False] * n

for i in range(n):
    print(f"\nProcess P{i+1}:")
    pid.append(f"P{i+1}")
    at.append(int(input("  Arrival Time: ")))
    bt.append(int(input("  Burst Time: ")))
    pr.append(int(input("  Priority: ")))

rule = input("\nIs smaller number = higher priority? (Y/n): ").strip().lower()
lower_is_higher = (rule != 'n')

time = 0
completed_count = 0

while completed_count < n:
    idx = -1
    best_priority = 999999 if lower_is_higher else -999999

    for i in range(n):
        if not done[i] and at[i] <= time:
            if lower_is_higher:
                if pr[i] < best_priority:
                    best_priority = pr[i]
                    idx = i
                elif pr[i] == best_priority and at[i] < at[idx]:
                    idx = i
            else:
                if pr[i] > best_priority:
                    best_priority = pr[i]
                    idx = i
                elif pr[i] == best_priority and at[i] < at[idx]:
                    idx = i

    if idx == -1:
        time += 1
    else:
        time += bt[idx]
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]
        done[idx] = True
        completed_count += 1

print("\nProcess\tAT\tBT\tPR\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{pr[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_tat = sum(tat) / n
avg_wt = sum(wt) / n
print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
