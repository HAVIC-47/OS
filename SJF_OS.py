n = int(input("Enter the number of the PIDs: "))
processes = []

for i in range(n):
    pid = "P" + str(i + 1)
    arrival = int(input(f"Enter arrival time of PID {pid}: "))
    burst = int(input(f"Enter burst time of PID {pid}: "))
    processes.append([pid, arrival, burst])

processes.sort(key=lambda x: x[1])

completed = 0
current_time = 0
visited = [False] * n

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

while completed < n:
    ready_queue = [
        (i, p) for i, p in enumerate(processes)
        if p[1] <= current_time and not visited[i]
    ]

    if ready_queue:
        idx, proc = min(ready_queue, key=lambda x: x[1][2])
        start_time = current_time
        current_time += proc[2]  # burst time
        completion_time[idx] = current_time
        turnaround_time[idx] = completion_time[idx] - proc[1]
        waiting_time[idx] = turnaround_time[idx] - proc[2]
        visited[idx] = True
        completed += 1
    else:
        current_time = min(p[1] for i, p in enumerate(processes) if not visited[i])


avg_WT = sum(waiting_time) / n


print("\nPID | Arrival | Burst | Completion | Turn Around | Waiting")
for i in range(n):
    pid, arrival, burst = processes[i]
    print(f"{pid:>3} |   {arrival:>5}  |  {burst:>5} |    {completion_time[i]:>5}    |     {turnaround_time[i]:>5}    |   {waiting_time[i]:>5}")

print(f"\nAverage Waiting Time: {avg_WT:.2f}")