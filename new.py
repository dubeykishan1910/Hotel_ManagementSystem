

# print(s.find("://"))
def parseURL(url):
    # parse protocol
    protocol_end = url.find("://")
    protocol = url[:protocol_end]
    remaining_url = url[protocol_end+3:]
    
    # parse hostname and port
    path_start = remaining_url.find("/")
    if path_start == -1:
        path_start = len(remaining_url)
    host_port = remaining_url[:path_start]
    if ":" in host_port:
        host, port = host_port.split(":")
    else:
        host = host_port
        if protocol == "http":
            port = "80"
        else:
            port = "443"
    
    # parse resource path
    if path_start == len(remaining_url):
        resource_path = "/"
    else:
        resource_path = remaining_url[path_start:]
    
    # print parsed parts
    all="GET / "
    all2="HTTP/2"
    # print("Protocol:", protocol)
    print(all+all2)
    print("Host:", host)
    print("x-Port:", port)
    if protocol=="http":
        print("x-Secure-Protocol: N")
    else:
        print("x-Secure-Protocol: Y")
s="https://www.example.com/index.htm"
s="http://localhost:9046"
parseURL(s)