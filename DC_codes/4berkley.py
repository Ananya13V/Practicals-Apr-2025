from datetime import timedelta

def calc(time):
    hours, minutes = map(int, time.split(':'))
    return hours * 3600 + minutes * 60

# Input
total_clients = int(input("Enter number of clients : "))
client_timing = input("Enter client times(space separated) HH:MM : ").split()
# if len(client_times)!=total_clients:
#     print(f"Error: Expected {total_clients} times for clients, but received {len(client_times)}. Exiting.")
#     exit(1)
# Error handling above
ts = input("Enter server time HH:MM : ")

# Calc total time and average
client_times = [calc(t) for t in client_timing]
server_time = calc(ts)
avg_time = (sum(client_times) + server_time)//(total_clients + 1)

#For server sync
if server_time == avg_time:
    print("Server is syncronized")
else:
    time_diff = timedelta(seconds=abs(server_time - avg_time))
    action = "increase" if server_time < avg_time else "decrease"
    print(f"Server is {action}d by {time_diff}, new server time is {timedelta(seconds = avg_time)}")

#For client sync
for i, client_time in enumerate(client_times):
    time_diff = timedelta(seconds=abs(client_time - avg_time))
    action = "increase" if client_time < avg_time else "decrease" if client_time > avg_time else "syncronized"
    print(f"Client {i} is {action}d by {time_diff}, new client time is {timedelta(seconds = avg_time)}")
