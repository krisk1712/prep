import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 4447  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    a = 0
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        print(data)
        command = data.split()
        tcdb = open("/Users/kris/Downloads/main_sim-master/tele_met/tmdb.txt",'a')
        tcdb.write(str(a) + "\n")
        tcdb.write(data + "\n")
        print("the packet received")
        send = "The command has been received"
        conn.send(send.encode())
        a = a + 1
    tcdb.write("EOF" + "\n")    
    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()
