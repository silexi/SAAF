from importlib.resources import path
from logging.config import fileConfig
from pprint import pprint
import psutil
import platform
from datetime import datetime
import cpuinfo #py-cpuinfo
import socket
import uuid
import re
import os
from functions import *


def get_size(bytes, suffix="B"):

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def getSystemInformations():
    print("\n")
    print("> Collecting system informations...")
    fileContent = ""

    fileContent = fileContent + str("="*40 + " System Information " + "="*40)
    fileContent = fileContent + f"\n"
    uname = platform.uname()
    fileContent = fileContent + f"System: {uname.system}\n"
    fileContent = fileContent + f"Node Name: {uname.node}\n"
    fileContent = fileContent + f"Release: {uname.release}\n"
    fileContent = fileContent + f"Version: {uname.version}\n"
    fileContent = fileContent + f"Machine: {uname.machine}\n"
    fileContent = fileContent + f"Processor: {uname.processor}\n"
    fileContent = fileContent + f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}\n"
    fileContent = fileContent + f"Ip-Address: {socket.gethostbyname(socket.gethostname())}\n"
    fileContent = fileContent + f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}\n"

    
    print("> Collecting boot informations...")
    # Boot Time
    fileContent = fileContent + str("="*40 + " Boot Time " + "="*40)
    fileContent = fileContent + f"\n"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    fileContent = fileContent + f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n"

    
    print("> Collecting CPU informations...")
    # print CPU information
    fileContent = fileContent + str("="*40 + " CPU Info " + "="*40)
    fileContent = fileContent + f"\n"
    # number of cores
    fileContent = fileContent + str("Physical cores: " + str(psutil.cpu_count(logical=False)))
    fileContent = fileContent + f"\n"
    fileContent = fileContent + str("Total cores: " + str(psutil.cpu_count(logical=True)))
    fileContent = fileContent + f"\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    fileContent = fileContent + f"Max Frequency: {cpufreq.max:.2f}Mhz\n"
    fileContent = fileContent + f"Min Frequency: {cpufreq.min:.2f}Mhz\n"
    fileContent = fileContent + f"Current Frequency: {cpufreq.current:.2f}Mhz\n"
    # CPU usage
    fileContent = fileContent + f"CPU Usage Per Core:\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        fileContent = fileContent + f"Core {i}: {percentage}%\n"
    fileContent = fileContent + f"Total CPU Usage: {psutil.cpu_percent()}%\n"

    
    print("> Collecting memory informations...")
    # Memory Information
    fileContent = fileContent + str("="*40 + " Memory Information " + "="*40)
    fileContent = fileContent + f"\n"
    # get the memory details
    svmem = psutil.virtual_memory()
    fileContent = fileContent + f"Total: {get_size(svmem.total)}\n"
    fileContent = fileContent + f"Available: {get_size(svmem.available)}\n"
    fileContent = fileContent + f"Used: {get_size(svmem.used)}\n"
    fileContent = fileContent + f"Percentage: {svmem.percent}%\n"



    print(">> Collecting swap_memory informations...")
    fileContent = fileContent + str("="*20 + " SWAP " + "="*20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    fileContent = fileContent + f"Total: {get_size(swap.total)}\n"
    fileContent = fileContent + f"Free: {get_size(swap.free)}\n"
    fileContent = fileContent + f"Used: {get_size(swap.used)}\n"
    fileContent = fileContent + f"Percentage: {swap.percent}%\n"



    print("> Collecting disk informations...")
    # Disk Information
    fileContent = fileContent + str("="*40 + " Disk Information " + "="*40)
    fileContent = fileContent + f"\n"
    fileContent = fileContent + f"Partitions and Usage:\n"
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        fileContent = fileContent + f"=== Device: {partition.device} ===\n"
        fileContent = fileContent + f"    Mountpoint: {partition.mountpoint}\n"
        fileContent = fileContent + f"    File system type: {partition.fstype}\n"
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        fileContent = fileContent + f"    Total Size: {get_size(partition_usage.total)}\n"
        fileContent = fileContent + f"    Used: {get_size(partition_usage.used)}\n"
        fileContent = fileContent + f"    Free: {get_size(partition_usage.free)}\n"
        fileContent = fileContent + f"    Percentage: {partition_usage.percent}%\n"
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    fileContent = fileContent + f"Total read: {get_size(disk_io.read_bytes)}\n"
    fileContent = fileContent + f"Total write: {get_size(disk_io.write_bytes)}\n"

    
    print("> Collecting network informations...")
    ## Network information
    fileContent = fileContent + str("="*40 + " Network Information " + "="*40)
    fileContent = fileContent + f"\n"
    ## get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        fileContent = fileContent + f"=== Interface: {interface_name} ===\n"
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                fileContent = fileContent + f"    IP Address: {address.address}\n"
                fileContent = fileContent + f"    Netmask: {address.netmask}\n"
                fileContent = fileContent + f"    Broadcast IP: {address.broadcast}\n"
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                fileContent = fileContent + f"    MAC Address: {address.address}\n"
                fileContent = fileContent + f"    Netmask: {address.netmask}\n"
                fileContent = fileContent + f"    Broadcast MAC: {address.broadcast}\n"
    ##get IO statistics since boot
    net_io = psutil.net_io_counters()
    fileContent = fileContent + f"Total Bytes Sent Statistics Since Boot: {get_size(net_io.bytes_sent)}\n"
    fileContent = fileContent + f"Total Bytes Received Statistics Since Boot: {get_size(net_io.bytes_recv)}\n"

    ## write contents to file on working directory
    filePath = str(os.getcwd()) + "/systemInformations.txt"
    writeToFile(filePath,fileContent)
    
    ## and finish
    print("\nEveryting is done.")