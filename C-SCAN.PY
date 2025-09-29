request_sequence = [21, 39, 64, 79, 90, 176]
head = int(input("Pick a head--> "))
direction = input("Enter direction (left/right): ").lower()

total_seek = 0
current = head
head_order = [current]

requests = sorted(request_sequence)
min_req = min(requests)
max_req = max(requests)

if direction == "right":
    right = [r for r in requests if r >= current]
    left = [r for r in requests if r < current]
    for track in right:
        distance = abs(current - track)
        print(f"Move from {current} to {track}, seek = {distance}")
        total_seek += distance
        current = track
        head_order.append(current)
    if left:
        distance = abs(current - max_req)
        total_seek += distance
        print(f"Jump from {current} to {max_req} (circular move)")
        current = max_req
        head_order.append(current)

        for track in reversed(left):
            distance = abs(current - track)
            print(f"Move from {current} to {track}, seek = {distance}")
            total_seek += distance
            current = track
            head_order.append(current)

else:
    left = [r for r in requests if r <= current][::-1]
    right = [r for r in requests if r > current][::-1] 

    for track in left:
        distance = abs(current - track)
        print(f"Move from {current} to {track}, seek = {distance}")
        total_seek += distance
        current = track
        head_order.append(current)

    if right:
        distance = abs(current - max_req)
        total_seek += distance
        print(f"Jump from {current} to {max_req} (circular move)")
        current = max_req
        head_order.append(current)
        for track in right:
            distance = abs(current - track)
            print(f"Move from {current} to {track}, seek = {distance}")
            total_seek += distance
            current = track
            head_order.append(current)

print("Head move order:", head_order)
print("Total seek time =", total_seek)
