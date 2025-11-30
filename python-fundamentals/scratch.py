# servers = ["web01", "web02", "web03"]
# mixed_list = ["config.yaml", 8080, True]

# for item in mixed_list:
#     print(type(item))

# print(servers[0])
# print(servers[-1])
# print(servers[:2])

# ports = [80, 443, 8080]
# ports.insert(1, 3000)
# ports.pop(0);
# print(ports)

# deployment_targets = ["us-east-1", "eu-west-1", "ap-southeast-2"]
# print(deployment_targets)
# deployment_targets.append("us-west-2")
# deployment_targets[1] = "eu-central-1"
# print(deployment_targets)

# Tuples

# host_port = ("127.0.0.1", 3000)
# rgb = (255, 0, 0)
# tuple_single_value = ("only value",)

# print(type(tuple_single_value))
# print(type(host_port))
# print(type(rgb))

# print(f"Host: {host_port[0]}")
# print(rgb[-1:])


# Sets

# unique_ports = set([80, 443, 22, 80, 8080, 433])
# print(22 in unique_ports)
# unique_ports.add(3000)
# print(unique_ports)

# # setList = set([[1,2][3,4]])
# # setSet = {{1,2}, {3,4}}
# setTuple = {(1,2), (3,4)}
# print((1,2) in setTuple)

# developers = set(["alice", "bob", "charlie"])
# admins = set(["alice", "david"])

# print("alice" in developers)
# print("alice" in admins)
# print("Union: ", developers.union(admins))
# print("Difference: ", developers.difference(admins))

# required_packages = set(["python3", "pip", "requests", "pip"])
# print("requsts" in required_packages)
# print("ansible" in required_packages)
# required_packages.add("paramiko")
# required_packages.discard("pip")
# installed = {"python3", "requests", "blath", "sdfsdf"}

# Dictionary

my_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}

# print(my_dictionary)

# print(f"Length: {len(my_dictionary)}")
# print(my_dictionary.keys())
# print(my_dictionary.values())
# print(my_dictionary.items())

# for item in my_dictionary.items(): 
#     print(item)

# for key, value in my_dictionary.items():
#     print(f"{key}: {value}")

# print("b" in my_dictionary)
# print(1 in set(my_dictionary.values()))

# print(my_dictionary["b"])
# print(my_dictionary.get("f", -1))

# default_tags = {
#     "Environment" : "Production",
#     "Owner" : "Finance"
# }

# custom_tags = {
#     "CostCenter" : "12345"
# }

# merged_tags = default_tags | custom_tags
# default_tags.update(custom_tags)
# new_dict = dict.fromkeys(['one', 'two', 'one'],0)
# print(new_dict)

# tags = {
#     "Environment" : "Production",
#     "Owner" : "Finance"
# }

# tags["Environment"] = "Bleh"
# tags["Project"] = "Python"

# print(tags)

# server_info = {
#     "id": "web01",
#     "ip_address": "192.168.1.1",
#     "state": "running",
#     "tags": {
#         "environment": "production",
#         "owner": "engineering"
#     }
# }

# print("Server state: ", server_info.get("state"))

# instance_type = server_info.get("instance_type", "t2.micro")
# server_info["state"] = "stopped"
# server_info["tags"]["random"] = "stuff"

# for key, values in server_info.items():
#     print(key, values)

# def process_data_guarded(data): 
#     print(data)

# process_data_guarded([])


# old_items = [1,2,3,4]
# doubled_items = []

# for item in old_items:
#     doubled_items.append(item*2)

# doubled_items_comp = [item * 2 for item in old_items]
# print(doubled_items_comp)

# servers = ["web", "db", "backend"]
# uppercase_servers = [server.upper() for server in servers]
# print(uppercase_servers)

# numbers = [1, 5, 10, 8, 2, 15]

# even_numbers = [num for num in numbers if num%2 == 0]
# print(even_numbers)

# numbers = [1, 2, 3, 2, 4, 1, 3]
# unique_squares = {x * x for x in numbers}
# print(unique_squares)

# servers = ["web", "backend"]
# server_ups = {server: f"192.168.1.{i}" for i, server in enumerate(servers)}
# print(server_ups)

# numbers = [1, 5, 10, 8, 2, 15]

# catagories = ["Pass" if num>= 8 else "Fail" for num in numbers if num%2 == 0]
# print(catagories)
