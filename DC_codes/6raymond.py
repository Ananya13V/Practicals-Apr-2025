n = 5
token = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0}
holder = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1}
req_queue = {0: [], 1: [], 2: [], 3: [], 4: []}
adj_matrix = [
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

def find_parent(req_process):
    for i in range(n):
        if adj_matrix[req_process][i] == 1:
            parent = i
            print(
                f"\nProcess {req_process} sending request to Parent Process {parent}."
            )
            req_queue[parent].append(req_process)
            break
    print(f"Request queue: {req_queue}")

    if token[parent] == 1:
        return parent
    else:
        parent = find_parent(parent)
    return parent

print("\nRaymond Tree Based Mutual Exclusion")
print("\nAdjacency Matrix for Spanning Tree:")
for i in adj_matrix:
    print(*i)

req_process = int(input("\nEnter the process which wants to enter the CS: "))
req_queue[req_process].append(req_process)
parent = find_parent(req_process)

while token[req_process] != 1:
    child = req_queue[parent][0]
    req_queue[parent].pop(0)

    holder[parent] = child
    holder[child] = 0
    token[parent] = 0
    token[child] = 1

    print(
        f"\nThe parent process {parent} has the token and sends it to child process {child}."
    )
    print(f"Request queue: {req_queue}")
    parent = child

if token[parent] == 1 and req_queue[parent][0] == parent:
    req_queue[parent].pop(0)
    holder[parent] = parent
    print(f"\nProcess {parent} enter the Critical Section")
    print(f"Request Queue: {req_queue}")

if len(req_queue[parent]) == 0:
    print(
        f"Request Queue of process {parent} is empty. Hence, release Critical Section"
    )
