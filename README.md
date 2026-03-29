# Port_Scanner
# 🔍 Multi-threaded Port Scanner (Python)

This is a fast, multi-threaded **TCP port scanner** written in Python. It scans a target IP address across a specified port range and identifies open ports using socket connections.

---

## 🚀 Features

- Multi-threaded scanning for high speed ⚡  
- Scans full port range (0–65535)  
- Uses queue-based task distribution  
- Displays real-time progress using `tqdm`  
- Thread-safe result collection  
- Measures total scan time  

---

## 🛠️ Requirements

Make sure you have Python 3 installed along with the required library:

```bash
pip install tqdm