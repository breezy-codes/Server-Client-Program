# Server-Client Animal Database Tutorial
<div align="center">
  <a href="https://www.linkedin.com/in/brianna-laird/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="linkedin logo"  />
  </a>
</div>

In this tutorial, we will be building a simple server-client Python program that allows the client to send a request for an animal's name, and the server responds with the names of animals of that type from a predefined dictionary.

## Prerequisites

- Basic knowledge of Python programming.
- Understanding of sockets and basic networking concepts.

## Getting Started

### Server Side

1. Open the provided `server.py` file.

2. You will notice that we import the `socket` module. This module provides us with the necessary functions for creating and managing sockets.

3. Define the IP address and port number on which the server will listen for incoming requests. Update the `server_ip` and `server_port` variables with the appropriate values.

4. Create a socket for communication using `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`. Here, `AF_INET` indicates the use of IPv4 and `SOCK_DGRAM` indicates that we are using a UDP socket for communication.

5. Bind the socket to the server IP and port using `server_socket.bind((server_ip, server_port))`.

6. A while loop has been implemented to keep the server running indefinitely. Inside the loop:
   - Receive data and client address using `data, client_address = server_socket.recvfrom(1024)`.
   - Convert the received data (animal name) to lowercase and strip any whitespace.
   - Check if the received animal name exists in the `our_animals` dictionary. If it exists, prepare the response by joining the animal names and send it back to the client using `server_socket.sendto(response.encode(), client_address)`. If the animal name is not found, send an appropriate error message.

7. Close the server socket using `server_socket.close()`.

### Client Side

1. Open the provided `client.py` file.

2. Similar to the server side, import the `socket` module.

3. Define the server IP and port number in the `server_ip` and `server_port` variables.

4. Create a socket for communication using `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`.

5. Enter a `while True` loop to keep the client running until the user decides to exit.

6. Inside the loop, prompt the user to enter an animal name using `input()`. Send the entered animal name to the server using `client_socket.sendto(animal.encode(), (server_ip, server_port))`.

7. Receive the response from the server using `response, _ = client_socket.recvfrom(1024)` and print the names of animals associated with the provided animal type.

8. Ask the user if they want to continue. If the input is not 'y', break out of the loop.

9. Close the client socket using `client_socket.close()`.

## Usage

1. Run the `server.py` file to start the animal database server.

2. Run the `client.py` file to start the client.

3. The client will prompt you to enter an animal type. For example, you can enter "lion".

4. The server will respond with the names and ages of lions from the predefined `our_animals` dictionary.

5. The client will then ask if you want to continue. If you enter 'y', you can request information for another animal. If you enter anything else, the client will exit.

## Conclusion

In this tutorial, we've created a basic server-client program to fetch animal names from a server's predefined dictionary. This example serves as a simple introduction to socket programming in Python and can be expanded upon for more complex applications. Remember to consider error handling, security, and scalability when working with real-world networking scenarios.
