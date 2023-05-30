import os
import subprocess
import socket
import requests


def ping(host):
    """
    Ping a host and check if it is reachable.
    """
    try:
        output = subprocess.check_output(['ping', '-n', '1', host])
        return True
    except subprocess.CalledProcessError:
        return False


def traceroute(host):
    """
    Perform a traceroute to a host and return the list of hops.
    """
    hops = []
    try:
        output = subprocess.check_output(['tracert', host])
        lines = output.decode().splitlines()
        for line in lines[2:]:
            if line.startswith(" "):
                hop_info = line.split()
                if len(hop_info) >= 3:
                    hops.append(hop_info[2])
        return hops
    except subprocess.CalledProcessError:
        return []


def get_host_ip():
    """
    Get the IP address of the current host.
    """
    return socket.gethostbyname(socket.gethostname())


def check_internet_connection():
    """
    Check if there is an active internet connection.
    """
    try:
        response = requests.get('https://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False


# Example usage
if __name__ == '__main__':
    host = 'google.com'
    print(f"Ping {host}: {ping(host)}")
    print(f"Traceroute to {host}: {traceroute(host)}")
    print(f"Host IP address: {get_host_ip()}")
    print(f"Internet connection available: {check_internet_connection()}")