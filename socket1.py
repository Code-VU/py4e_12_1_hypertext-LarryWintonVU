import socket

def getWebData():
    # create and open a socket, send a request
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))

    # data specified in assignment
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

    # data used to test code
    # non-ascii characters, could not solve decoding these, so only dealing with exception on decode()
    # cmd = 'GET http://data.pr4e.org/authors.txt HTTP/1.0\r\n\r\n'.encode()
    # not a .txt file
    # cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
    # longer file 
    # cmd = 'GET http://data.pr4e.org/words.txt HTTP/1.0\r\n\r\n'.encode()
    # file does not exist, non 200 response
    # cmd = 'GET http://data.pr4e.org/doesnotexist.txt HTTP/1.0\r\n\r\n'.encode()

    mysock.send(cmd)

    # receive request response data then close the socket
    response = ''

    try :
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            response += data.decode()

    except :
        print('Not able to process response data')
        quit()

    mysock.close()

    # process response header data into a dictionary 
    lines = response.splitlines()
    responseLength = len(lines)
    httpHeaderData = dict()
    httpHeaderLength = 0

    for line in lines :
        # process header lines until the first blank line that separates header from body
        if (line == '') :
            break
        else : 
            # keep track of the length of the header data, in terms of number of lines in a list
            httpHeaderLength += 1
            if (line.startswith('HTTP')) :
                # value is both status code and reason phrase, split on first instance of space character
                pieces = line.split(' ',1)
            else :
                pieces = line.split(': ')
            
            # add entry to dictionary
            httpHeaderData[pieces[0]] = pieces[1]

    # print header data, visual separator, response body
    for keys, values in httpHeaderData.items() :
        print(keys, ':', values)

    print('\n')
    
    # print response body using indices
    for x in range(httpHeaderLength+1, responseLength) :
        print(lines[x])


getWebData()