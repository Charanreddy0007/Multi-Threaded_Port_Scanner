import socket
import time 
import threading
from queue import Queue
from tqdm import tqdm

# Target IP
ip = "192.168.205.6"  

# Port range
start_range = 0
end_range = 65535

# Number  of threads
num_threading = 750

open_ports = []              # Store open ports
port_queue = Queue()         # Queue of ports
start_time = time.time()     # Start timmer
print_lock = threading.Lock()

# Progress bar
process = tqdm(total=end_range, desc="Scanning", ncols=70)


# Add ports to queue
for port in range(start_range, end_range):
    port_queue.put(port)


def scanner():
    while not port_queue.empty():

        port = port_queue.get() # Get port

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)       # Timeout

        result = s.connect_ex((ip, port))   # Try connect

        if result == 0:         # Port is open
            with print_lock:
                open_ports.append(f"{port} is Open")
    
        s.close()
        port_queue.task_done()  # Mark done
        process.update(1)       # Update progress


# Start threads
for _ in range(num_threading):
    t = threading.Thread(target=scanner)
    t.start()

port_queue.join()    # Wait for all tasks
process.close()

end_time = time.time()
time_taken = end_time - start_time

print("-"*50)

# Print open ports
for i in open_ports:
    print(i)

print("-"*50)

print(f"Total Time Taken: {time_taken:.3f} in seconds\n")