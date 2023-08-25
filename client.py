import socket

# Server IP and Port Number
server_ip = "127.0.0.1"
server_port = 53

# Socket set up for communications
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    animal = input("Enter an animal to find their names:")
    client_socket.sendto(animal.encode(), (server_ip, server_port))

    response, _ = client_socket.recvfrom(1024)
    print("The names for those animals in our database are:", response.decode())

    choice = input("Do you want to continue? (y/n")
    if choice.lower() != "y":
        break

client_socket.close()