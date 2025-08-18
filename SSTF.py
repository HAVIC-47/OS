def sstf(requests, head):
    requests = requests.copy()
    total_seek = 0
    seek_sequence = []
    operations = 0  

    while requests:
        distances = {req: abs(head - req) for req in requests}
        nearest = min(distances, key=distances.get)

        total_seek += abs(head - nearest)
        head = nearest
        seek_sequence.append(nearest)
        requests.remove(nearest)

        operations += 1 

    return total_seek, seek_sequence, operations


requests = [11,34,41,50,52,69,70,114]
head = 50
total_seek, sequence, ops = sstf(requests, head)

print("Seek Sequence:", sequence)
print("Total Seek Operations (distance):", total_seek)
print("Total Number of Operations (steps):", ops)
