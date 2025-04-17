class Process:
    def __init__(self, initial_clock):
        self.clock = initial_clock

    def get_clock(self):
        return self.clock
    
    def send_message(self):
        self.clock += 1
        print(f"Sent message at logical time: {self.clock}")

    def recieve_message(self, sender_clock):
        self.clock = max(self.clock, sender_clock) + 1
        print(f"Recd message. Updated local time: {self.clock}")

def main():
    pr1 = Process(0)
    pr2 = Process(5)

    print(f"Process 1 initial time: {pr1.get_clock()}")
    print(f"Process 2 initial time: {pr2.get_clock()}")

    while True:
        print("\n Choose an action: ")
        print("1. Process 1 sends message")
        print("2. Process 2 sends message")
        print("3. Exit")
        choice = int(input("Enter Choice : "))

        if choice == 1:
            pr1.send_message()
            pr2.recieve_message(pr1.get_clock())

        elif choice == 2:
            pr2.send_message()
            pr1.recieve_message(pr2.get_clock())

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()

