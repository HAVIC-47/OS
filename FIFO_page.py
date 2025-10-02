def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    page_order = []  # to keep track of replacement order

    print(f"Reference String: {pages}")
    print(f"Frame Capacity: {capacity}\n")

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                # FIFO: remove oldest page
                removed = memory.pop(0)
                memory.append(page)
                print(f"Page {removed} replaced with {page}")
            page_faults += 1
        else:
            print(f"Page {page} already in memory (HIT)")
        
        page_order.append(memory.copy())
        print(f"Frames: {memory}")

    return page_faults, page_order


# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3

faults, order = fifo_page_replacement(pages, capacity)
print("\nTotal Page Faults:", faults)
