# Bankers Algorithm
class Bankers:
    def __init__(self, processes, resources):
        self.processes = processes
        self.resources = resources
        self.max_resources = []
        self.allocations = []
        self.need = []

    def set_max_resources(self, max_resources):
        self.max_resources = max_resources
        self.need = [[max_resources[i][j] - self.allocations[i][j] for j in range(len(self.resources))] for i in range(len(self.processes))]

    def set_allocations(self, allocations):
        self.allocations = allocations

    def is_safe(self):
        work = self.resources.copy()
        finish = [False] * len(self.processes)
        safe_sequence = []

        while len(safe_sequence) < len(self.processes):
            progress = False
            for i in range(len(self.processes)):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(len(self.resources))):
                    work = [work[j] + self.allocations[i][j] for j in range(len(self.resources))]
                    finish[i] = True
                    safe_sequence.append(self.processes[i])
                    progress = True
                    break
                if not progress:
                    return None
                
        return safe_sequence
    
if __name__ == "__main__":
    processes = ['P0', 'P1', 'P2', 'P3', 'P4']
    resources = [3, 3, 2]

    max_resources = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ]

    allocations = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ]

    bankers_algorithm = Bankers(processes, resources)
    bankers_algorithm.set_allocations(allocations)
    bankers_algorithm.set_max_resources(max_resources)

    safe_sequence = bankers_algorithm.is_safe()

    if safe_sequence:
        print("Safe sequence : ", safe_sequence)
    else:
        print("No safe sequence found, Deadlock detected")