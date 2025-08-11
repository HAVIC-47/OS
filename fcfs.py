requests = [0,16,24,43,50,82,100,140,150,170,190,199]

head_pos = int(input("Enter starting head position: "))

total_movement = 0
current_pos = head_pos

for i in range(len(requests)):
    distance = requests[i] - current_pos
    if distance < 0:
        distance = -distance 
    total_movement = total_movement + distance
    current_pos = requests[i]

print("Total seek operations =", total_movement)
