import random
import socket

# def greet_user(name):
#     print(f"Hello, {name}")

# greet_user("Alice")

# def random_number(min_val, max_val):
#     return random.randint(min_val, max_val)

# generated_number = random_number(-1, 100)

# def check_service_status(service_name, expected_status):
#     print(f"Checking {service_name} for {expected_status}...")
#     return True 

# check_service_status(service_name= "nginx", expected_status= "running")

# def connect(host, port=22, timeout=30):
#     print(f"Connect to host {host} on port {port} (timeout {timeout})")

# connect("web01")

# def check_port(host, port, timeout=5):
#     try:
#         with socket.create_connection((host, port), timeout):
#             return True
#     except Exception:
#         return False

# print(check_port("www.google.com", 443))
# print(check_port("www.googdfdfdfs789798bfle.com", 22))

# def greet_users(names):
#     for name in names:
#         print(f"Hello, {name}")

# def sum_even(numbers):
#     return sum(x for x in numbers if x % 2 == 0)

# print(sum_even([1,2,3,4,5,6]))

# def fibonacci(n):
#     seq = [0, 1]

#     for _ in range(2, n):
#         seq.append(seq[-1] + seq[-2])
    
#     return seq[:n]

# print(fibonacci(5))

# servers = ["web01", "web02", "web03"]

# for idx, server in enumerate(servers, 1):
#     print(f"{idx} processing server {server}")

# hosts = ["host1", "hostb", "hostc"]

# ips = ["10.0.0.1", "10.0.0.2"]
# azs = ["us-east-1a", "us-east-1b"]

# for host, ip, az in zip(hosts,ips, azs):
#     print(f"Host: {host}, IP: {ip}, AZ: {az}")

def validate_server(server):
    if not isinstance(server, dict):
        return False
    
    required_keys = {"name", "region", "status"}
    if not required_keys.issubset(server.keys()):
        return False 
    
    if not isinstance(server["name"], str) or not server["name"]:
        return False
    
    if not isinstance(server["region"], str) or not server["region"]:
        return False 
    
    if server["status"] not in ["active", "inactive"]:
        return False
    return True

def generate_inventory_report(servers):
    if not isinstance(servers, list):
        return {}

    report = {}

    for server in servers:
        if not validate_server(server):
            continue
        region = server["region"]
        status = server["status"]
        name = server["name"]

        if region not in report:
            report[region] = {
                "active" : [],
                "inactive" : []
            }
        report[region][status].append(name)
    return report