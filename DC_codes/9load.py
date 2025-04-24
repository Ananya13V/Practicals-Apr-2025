class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_next(self):
        server = self.server[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server
    
if __name__ == "__main__":
    list = ["S1", "S2", "S3", "S4"]
    lb = LoadBalancer(list)

    tasks = 10

    for i in range(1, tasks + 1):
        ass_server = lb.get_next()
        print(f"Task {i} assigned to {ass_server}")
        