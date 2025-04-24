class Process:
    def __init__(self, process_id):
        self.id = process_id
        self.active = True

def crash(processes, process_id):
    for process in processes:
        if process.id == process_id:
            process.active = False
            print(f"Process {process_id} crashed.")
            if process_id == coordinator:
                print("Coordinator crashed. Electing new coordinator...")
            return

def election(processes, initiator):
    print(f"Process {initiator} is initiating election.")
    new_coordinator = -1

    for process in processes:
        if process.id > initiator and process.active:
            print(f"Process {process.id} responds.")
            new_coordinator = process.id

        if new_coordinator == -1:
            new_coordinator = initiator

        global coordinator 
        coordinator = new_coordinator
        print(f"New coordinator elected: Process {coordinator}.")

if __name__ == "__main__":
    num = int(input("Enter the number of processes"))
    processes = [Process(i + 1) for i in range(num)]
    coordinator = processes[-1].id
    print(f"Initial coordinator: {coordinator}")

    while True:
        print("\n1. Crash a process\n2. Start election\n3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            crash_id = int(input("Enter process ID to crash: "))
            crash(processes, crash_id)
        elif choice == 2:
            initiator = int(input("ENter Process ID to start election : "))
            if any(process.id == initiator and process.active for process in processes):
                election(processes, initiator)
            else:
                print(f"Process {initiator} is either crashed or invalid.")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
