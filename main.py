import psutil
from datetime import datetime
import csv
import os
import time

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    
    return [now, cpu, memory, disk]

def write_log(data):
    file_exists = os.path.isfile("log.csv")
    with open("log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "CPU", "Memory", "Disk"])
        writer.writerow(data)

if __name__ == "__main__":
    
    print("Starting scheduled logging... (5 entries, 10 seconds apart)")
    for i in range(5):
        entry = get_system_info()
        write_log(entry)
        print(f"[{i+1}/5] Logged:", entry)
        
        if i < 4:
            time.sleep(10)
    
    print("Logging complete! Check log.csv for results.")