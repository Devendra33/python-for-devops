"""
 You will create a Python script that:
- Takes threshold values (CPU, disk, memory) from **user input**
- Also fetches system metrics using a Python library (example: `psutil`)
- Compares metrics against thresholds
- Prints the result to the **terminal**

Code Created by Devendra Gohare.
for Windows OS

"""
import psutil

# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

# Memory Usage
memory = psutil.virtual_memory()
memory_usage = memory.percent
print(f"Memory Usage: {memory.percent}%")

# More detailed memory info
print(f"Total Memory: {round(memory.total / (1024**3), 2)} GB")
print(f"Available Memory: {round(memory.available / (1024**3), 2)} GB")

# Disk Usage (C: drive)
disk = psutil.disk_usage('C:\\')

disk_usage = disk.percent
print(f"Disk Usage: {disk.percent}%")

# More detailed disk info
print(f"Total Disk: {round(disk.total / (1024**3), 2)} GB")
print(f"Free Disk: {round(disk.free / (1024**3), 2)} GB")

cpu = float(input("Enter CPU threshold (%): "))
disk = float(input("Enter Disk threshold (%): "))
memory = float(input("Enter Memory threshold (%): "))

if cpu_usage > cpu:
    print("CPU usage is above threshold!")
if disk_usage > disk:
    print("Disk usage is above threshold!")
if memory_usage > memory:
    print("Memory usage is above threshold!")
