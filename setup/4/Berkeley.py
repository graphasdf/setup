
import time
import random

def calculate_offset(remotes):
    local_time = time.time()
    offsets = [remote - local_time for remote in remotes]
    return sum(offsets) / len(offsets)

def synchronize_clocks():
    num_peers = int(input("Enter the number of peers: "))
    local_time = time.time()
    

    remote_times = [local_time + random.uniform(-1, 1) for _ in range(num_peers)]
    print("Local time:", local_time)
    print("Remote times:", remote_times)
    

    offset = calculate_offset(remote_times)
    

    adjusted_time = local_time + offset
    print("Adjusted local time:", adjusted_time)

synchronize_clocks()
