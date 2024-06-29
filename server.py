import socket

# Animal Dictionary
our_animals = {
    "lion": ("Bruce, 25yrs old", "Tony, 10yrs old", "Michael, 12 yrs old"),
    "elephant": ("Ellie 108yrs old", "Ella, 30yrs old", "Dumbo 68yrs old"),
    "giraffe": ("Gerry, 7yrs old", "Grace, 9yrs old", "Geoffrey, 14yrs old"),
    "zebra": ("Stripey, 5yrs old", "Loki, 8yrs old", "Stella, 6yrs old"),
    "monkey": ("Squiggles, 3yrs old", "Winston, 5yrs old", "Jiggles, 4yrs old"),
    "emu": ("Karen, 15yrs old", "Judy, 12yrs old", "Ken, 18yrs old"),
    "kangaroo": ("Kenny, 6yrs old", "Kylie, 4yrs old", "Kevin, 8yrs old"),
    "penguin": ("Penny, 2yrs old", "Pablo, 3yrs old", "Pippin, 1yr old"),
    "tiger": ("Tanya, 9yrs old", "Tyler, 6yrs old", "Tara, 7yrs old")
}


# Server IP and Port Number
server_ip = "127.0.0.1"
server_port = 5365

# Socket set up for communications
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

# Server running message
print("Our animal database is running...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    animal = data.decode().strip().lower()

    # If loop for communicating animals to server
    if animal in our_animals:
        response = " , ".join(our_animals[animal])
        print("Client sent request for:", animal)
        print("Server sent animal names:", response)
        server_socket.sendto(response.encode(), client_address)
    else:
        server_socket.sendto("Animal not found in our database".encode(),client_address)