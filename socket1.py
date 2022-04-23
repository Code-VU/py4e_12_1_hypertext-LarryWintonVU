import socket

def getWebData():
    # create and open a socket, send a request
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    response = ''

    # receive request response data then close the socket
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        response += data.decode()

    mysock.close()

    # process response header data into a dictionary, print it
    # process response body data into a list, print it
    lines = response.splitlines()
    httpHeaderData = dict()
    httpResponseBody = list()
    httpHeaderLength = 0
    responseLength = len(lines)

    for line in lines :
        if (line == '') :
            break
        else : 
            httpHeaderLength += 1
            if (line.startswith('HTTP')) :
                pieces = line.split(' ')
            else :
                pieces = line.split(': ')
            
            httpHeaderData[pieces[0]] = pieces[1]

    for keys, values in httpHeaderData.items() :
        print(keys, ':', values)

    print('\n')
    
    for x in range(httpHeaderLength+1, responseLength) :
        print(lines[x])


getWebData()