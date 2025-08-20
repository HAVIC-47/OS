def scan(requests, head, disk_size, direction="left"):
    requests = sorted(requests)
    total_seek = 0
    seek_sequence = []
    ops = 0

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    if direction == "left":
        for r in left:
            total_seek += abs(head - r)
            head = r
            seek_sequence.append(r)
            ops += 1
        total_seek += abs(head - 0)
        head = 0
        seek_sequence.append(0)

        for r in right:
            total_seek += abs(head - r)
            head = r
            seek_sequence.append(r)
            ops += 1

    elif direction == "right":
        for r in right:
            total_seek += abs(head - r)
            head = r
            seek_sequence.append(r)
            ops += 1
        total_seek += abs(disk_size - head - 1)
        head = disk_size - 1
        seek_sequence.append(disk_size - 1)

        for r in left:
            total_seek += abs(head - r)
            head = r
            seek_sequence.append(r)
            ops += 1

    return total_seek, seek_sequence, ops

requests = [11, 34, 41, 50, 52, 69, 70, 114]
head = 50
disk_size = 200

total_seek, sequence, ops = scan(requests, head, disk_size, direction="left")

print("Seek Sequence:", sequence)
print("Total Seek Operations (distance):", total_seek)
print("Total Number of Operations (steps):", ops)
print("Average Seek per Request:", total_seek / (len(sequence)))
