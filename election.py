#Bully Algorithm (Election)
class Process:
    def __init__(self, process_id):
        self.id = process_id
        self.active = True

def crash_process(processes, process_id):
        for process in processes:
            if process.id == process_id:
                process.active = False
                print(f"Process {process_id} crashed")
                if process_id == coordinator:
                    print("Coordinator crashed. Election begins")
                return
            
def election(processes, initiator):
        print(f"Election started by {initiator}")
        new_coordinator = -1

        for process in processes:
            if process.id > initiator and process.active:
                print(f"Process {process.id} responds")
                new_coordinator = process.id

        if new_coordinator == -1:
            new_coordinator = initiator

        global coordinator
        coordinator = new_coordinator
        print(f"New coordinator appointed as {coordinator}")

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes : "))
    processes = [Process(i+1) for i in range(num_processes)]

    coordinator = processes[-1].id
    print(f"Initial Coordinator : {coordinator}")

    while True:
        print("\n1. Crash a Process \n2. Start Election\n3. Exit")
        choice = int(input("Enter a choice"))

        if choice == 1:
            crash_id = int(input("Enter process to crash"))
            crash_process(processes, crash_id)

        elif choice == 2:
            initiator = int(input("Enter process ID to start election: "))
            if any(process.id == initiator and process.active for process in processes):
                election(processes, initiator)

            else:
                print(f"Process {initiator} either crashed or is inactive")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid input")
