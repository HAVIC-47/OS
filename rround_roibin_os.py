processes = []
arrival_time = []
burst_time = []
waiting_time = []
turnaround_time = []
completion_time = []

n = int(input("Enter number of processes: "))
for i in range(n):
    print("Process", i+1)
    arrival = int(input("Arrival time: "))
    burst = int(input("Burst time: "))
    processes.append(i+1)
    arrival_time.append(arrival)
    burst_time.append(burst)
    waiting_time.append(0)
    turnaround_time.append(0)
    completion_time.append(0)

quantum = int(input("Enter Time Quantum: "))

remaining_time = burst_time[:]
time = 0
done = 0
visited = [False]*n
queue = []

order = []

while done < n:
    for i in range(n):
        if arrival_time[i] <= time and visited[i] == False:
            queue.append(i)
            visited[i] = True

    if len(queue) == 0:
        time += 1
        continue

    current = queue.pop(0)
    order.append("P" + str(processes[current]))

    if remaining_time[current] > quantum:
        time += quantum
        remaining_time[current] -= quantum
    else:
        time += remaining_time[current]
        completion_time[current] = time
        waiting_time[current] = time - arrival_time[current] - burst_time[current]
        remaining_time[current] = 0
        done += 1

    for i in range(n):
        if arrival_time[i] <= time and visited[i] == False:
            queue.append(i)
            visited[i] = True

    if remaining_time[current] > 0:
        queue.append(current)


for i in range(n):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

print("\nProcess\tAT\tBT\tCT\tWT\tTAT")
total_wt = 0
total_tat = 0
for i in range(n):
    print("P"+str(processes[i]), "\t", arrival_time[i], "\t", burst_time[i], "\t", completion_time[i], "\t", waiting_time[i], "\t", turnaround_time[i])
    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]

print("\nAverage Waiting Time:", total_wt / n)
print("Average Turnaround Time:", total_tat / n)

print("\nExecution Order:")
for p in order:
    print(p, end=" -> ")
print("END")
