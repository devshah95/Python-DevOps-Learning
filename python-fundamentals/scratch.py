servers = ["web01", "web02", "web03"]
mixed_list = ["config.yaml", 8080, True]

# for item in mixed_list:
#     print(type(item))

# print(servers[0])
# print(servers[-1])
# print(servers[:2])

ports = [80, 443, 8080]
ports.append(5000)
ports.insert(1, 3000)
print(ports)



