from socket import *
serv_addr = "IP address of server"
serv_port = 8000
client_sock = socket (AF_INET, SOCK_STREAM) 
client_sock.connect((serv_addr, serv_port)) 
msg = input("Enter the text message: ") 
client_sock.send(msg.encode())
mod_msg = client_sock.revc(2048) 
print("From Server:", mod_msg.decode()) 
client_sock.close()