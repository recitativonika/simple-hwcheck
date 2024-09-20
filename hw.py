import platform, uuid, psutil, socket, GPUtil
from screeninfo import get_monitors

def get_system_info():
    # Get system information
    system_info = {
        "System": platform.system(),
        "Device Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "hardware ID" : str(uuid.getnode()),
        "Local IP" : socket.gethostbyname(socket.gethostname()),
        "MAC address" : ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    }
    return system_info

def display_info(info):
    print(" ")
    print("\033[96m")
    print("-" * 30)
    print("\033[95m Hardware Specifications :\n")
    print("\033[96m")
    for key, value in info.items():
        print(f"{key}: {value}")
    print("\n")
if __name__ == "__main__":
    system_info = get_system_info()
    display_info(system_info)
    
def get_disk_info():
    partitions = psutil.disk_partitions()

    for partition in partitions:
        print(f"=== Disk Partition: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File System Type: {partition.fstype}")
        
        # Get disk usage statistics
        usage = psutil.disk_usage(partition.mountpoint)
        
        print(f"  Total Size: {usage.total / (1024 ** 3):.2f} GB")
        print(f"  Used: {usage.used / (1024 ** 3):.2f} GB")
        print(f"  Free: {usage.free / (1024 ** 3):.2f} GB")
        print(f"  Percentage Used: {usage.percent}%")
        print("-" * 30)

if __name__ == "__main__":
    get_disk_info()
    
def get_gpu_info():
    # Get the list of active GPUs
    gpus = GPUtil.getGPUs()
    
    if not gpus:
        print("No GPU found.")
        return
    
    for gpu in gpus:
        print("\033[92m")
        print("-" * 30)
        print("\033[95m Grapics info :\n")
        print(" ")
        print("\033[92m")
        print(f"GPU ID: {gpu.id}")
        print(f"GPU Name: {gpu.name}")
        print(f"Memory Total: {gpu.memoryTotal} MB")
        print(f"Memory Free: {gpu.memoryFree} MB")
        print(f"Memory Used: {gpu.memoryUsed} MB")
        print(f"GPU Load: {gpu.load * 100:.1f}%")
        print(f"Temperature: {gpu.temperature} °C")
        print("-" * 30)
        print("\n")

if __name__ == "__main__":
    get_gpu_info()

def get_display_info():
    monitors = get_monitors()

    if not monitors:
        print("No displays found.")
        return
    
    for i, monitor in enumerate(monitors):
        print("\033[94m")
        print("-" * 30)
        print("\033[95m Display info :\n")
        print("\033[94m")
        print(f"Display {i + 1}:")
        print(f"  Width: {monitor.width} pixels")
        print(f"  Height: {monitor.height} pixels")
        print(f"  Is Primary: {'Yes' if monitor.is_primary else 'No'}")
        print(f"  Position: ({monitor.x}, {monitor.y})")
        print("-" * 30)
        print("\n")
        
if __name__ == "__main__":
    get_display_info()
