import random

NUM_NODES = 5

node_values = [random.randint(1,100) for _ in range(NUM_NODES)]
print("Initial node values: ", node_values)

ROUNDS = 8
for resync_round in range(ROUNDS):
    print(f"\n--- Round {resync_round + 1} ---")
    pairs = []
    indices = list(range(NUM_NODES))
    random.shuffle(indices)

    for i in range(0, len(indices) - 1, 2):
        a = indices[i]
        b = indices[i+1]
        pairs.append((a, b))

        for a,bb in pairs:
            va, vb = node_values[a], node_values[b]
            avg = (va + vb)/2
            node_values[a] = avg
            node_values[b] = avg
            print(f"Node {a} and Node {b} exchanged values --> New Values : {avg}")

        print("Current Values: ", [round(v,2) for v in node_values])

global_avg = sum(node_values) / NUM_NODES
print(f"\nGlobal Average: {global_avg:.2f}")