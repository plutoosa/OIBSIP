import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
portNo = 8021

client_socket.connect((host, portNo))
print("Connection to server established.")

def message_receive():
    while True:
        msg = client_socket.recv(1024).decode()
        if msg.lower () == "bye":
            print("Connection to server disconnected. ")
            break
        print(f"Server says: {msg}")
        print ("Type your response here: ", end="", flush=True)
        
def message_send():
    while True:
        msg = input()
        client_socket.send(msg.encode())
        if msg.lower() == "bye":
            print("Client disconnected te server connection.")
            break
        
receive_thread = threading.Thread(target=message_receive)
send_thread = threading.Thread(target=message_send)

receive_thread.start()


send_thread.start()