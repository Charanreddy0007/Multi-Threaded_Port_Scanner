import socket
import time 
import threading
from queue import Queue
from tqdm import tqdm

ip = "192.168.205.6"
start_range = 0
end_range = 65535
num_threading = 750

open_ports = []
port_queue = Queue()
start_time = time.time()
print_lock = threading.Lock()
process = tqdm(total=end_range, desc="Scanning", ncols=70)


for port in range(start_range, end_range):
    port_queue.put(port)


def scanner():
    while not port_queue.empty():

        port = port_queue.get()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)

        result = s.connect_ex((ip, port))

        if result == 0:
            with print_lock:
                open_ports.append(f"{port} is Open")
    
        s.close()
        port_queue.task_done()
        process.update(1)


for _ in range(num_threading):
    t = threading.Thread(target=scanner)
    t.start()

port_queue.join()
process.close()

end_time = time.time()
time_taken = end_time - start_time

print("-"*50)

for i in open_ports:
    print(i)

print("-"*50)

print(f"Total Time Taken: {time_taken:.3f} in seconds\n")