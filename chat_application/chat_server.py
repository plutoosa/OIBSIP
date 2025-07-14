import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
portNo = 8021

server_socket.bind((host, portNo))
#server listens
server_socket.listen()
print(f"Server is listening on port number {portNo}")

#accepts client connection
client_socket, client_address = server_socket.accept()
print(f"Server is connected to {client_address}")


#message receiiving function
def message_receive():
    while True:
        try: 
            msg = client_socket.recv(1024).decode()
            if msg.lower() == 'bye':
                print("Client connection has been disconnected.")
                break
            print(f'Client says: {msg}')
            print("Type your response here: ", end="", flush=True)
        except ConnectionResetError:
            print("Client forcibly closed the connection")
            break
        
#function to send message
def message_send():
    while True:
        msg = input()
        client_socket.send(msg.encode())
        if msg.lower() == 'bye':
            print("Connection has been disconnected by server.")
            break
        
receive_thread = threading.Thread(target=message_receive)
send_thread = threading.Thread(target=message_send)

receive_thread.start()

print("Type your message here: ", end="", flush=True)
send_thread.start()