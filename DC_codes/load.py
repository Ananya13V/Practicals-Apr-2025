#Load Balancing algorithm 

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_next_server(self):
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server
    
if __name__ == "__main__":
    server_list = ["Server1", "Server2", "Server3", "Server4"]
    lb = LoadBalancer(server_list)

    tasks = 10

    for i in range(1, tasks + 1):
        assigned_server = lb.get_next_server()
        print(f"Task {i} assigned to {assigned_server}")