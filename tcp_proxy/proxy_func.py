
# highly function proxy function for a redundant gateway protocol on MTP.


import sys
import socket
import threading

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:

        server.bind((local_host,local_port))


    except:

        print "[!!!] Failed to listen on %s:%d" % (local_host,local_port)
        print "[!!!] Check for other listening or correct permission"
        sys.exit(0)



    print "[!!!] Listening on %s:%d " % (local_host,local_port)

    server.listen()

    while True:

        client_socket , addr = server.accept()

        print "[#-->>] Received incoming conncetion from %s:%d" % (addr[0],addr[1])

        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket,remote_host,remote_port,receive_first))

        proxy_thread.start()




def proxy_handler(client_socket,remote_host,remote_port,receive_first):

    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    remote_socket.connect((remote_host,remote_port))

    if receive_first:

        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        remote_buffer = response_handler(remote_buffer)


        if len(remote_buffer):
            print "[<<-#] Sending %d bytes to localhost.." % len(remote_buffer)
            client_socket.send(remote_buffer)



    while True:

        local_buffer = receive_from(client_socket)


        if len(local_buffer):

            print "[#->>] Recived %d bytes from localhost .." % len(local_buffer)
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)

            remote_socket.send(local_buffer)

            print "[#-->>] Snet to remote"


        remote_buffer = receive_from(remote_socket)


        if len(remote_buffer):

            print "[<<--#] Received  %d bytes from remote.." % len(remote_buffer)
            hexdump(remote_buffer)


            remote_buffer = response_handler(remote_buffer)


            client_socket.send(remote_buffer)

            print "[<<-#] sent to localhost"

        if not len(local_buffer) or not len(remote_buffer):

            client_socket.close()
            remote_socket.close()

            print "[###] Closing conncetion"

            break




def hexdump(src, length=16):
    result = []
    digit = 4 if isinstance(src, unicode) else 2

    for i in xrange(0, len(src) , length):
        s = src[i:i+length]
        hexa = b' '.join(["%o*X" % (digit, ord(x)) for x in s])
        txt = b' '.join([x if 0x20 <- ord(x) < 0x7F else b'.' for x in s])
        result.append(b"%04X  %-*s  %s" % (i,length*(digit + 1),hexa, txt) )

    print b'\n'.join(result)



def receive_from(conncetion):

    buffer = ""

    conncetion.settimeout(2)


    try:

        while True:
            data = conncetion.recv(4096)

            if not data:
                break
                buffer += data

    except:
        pass


        return buffer




def request_handler(buffer):
    return buffer



def response_handler(buffer):
    return buffer



def main():

    if len(sys.argv[1:]) != 5:
        print "Usage : python 2.7 tc(p)roxy.py [localhost] [localport] [remotehost] [remoteport] [recivefirst]"
        print "Example :"
        print "python2.7 tc(p)roxy.py 127.0.0.1 4444 10.12.132.1 4444 True "
        sys.exit(0)




    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    receive_first = sys.argv[5]


    if "True" in receive_first:
        receive_first = True

    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)


main()
