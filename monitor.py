import os
import time
import psutil

def get_cpu_temperature():
    # Read the CPU temperature from the system file
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp_str = f.read().strip()
    # Convert the temperature to Celsius
    return int(temp_str) / 1000.0

def print_system_info():
    while True:
        # Get the CPU temperature
        cpu_temp = get_cpu_temperature()
        # Get the CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        print(f"CPU Temperature: {cpu_temp:.2f}°C")
        print(f"CPU Usage: {cpu_usage:.2f}%")
        print("-" * 30)
        
        # Wait for 10 seconds before printing the information again
        time.sleep(10)

if __name__ == "__main__":
    print_system_info()
