from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)  #queue upto 5 more requests if busy serving one
        while(1):
            (clientsocket, address)=serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split('\n')
            if len(pieces) > 0:
                print("A"+ pieces[0])
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World </body></html>\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    
    except Exception as exc:
        print("Error: \n")
        print(exc)

    serversocket.close()


print('Access http://localhost:9000')
createServer()








mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/page2.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
