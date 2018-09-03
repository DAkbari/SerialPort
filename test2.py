#!/usr/bin/python

import serial, time, threading
#initialization and open the port

#possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

ser = serial.Serial()
ser.port = "COM2"
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser.timeout = 2            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write


try:
    ser.open()
except Exception as e:
    print("error open serial port: " + str(e))
    exit()


def listen():
    while True:
        response = ser.readline()
        if response != b'':
            print("read data: " + str(response))
            print(">>", end='')


if ser.isOpen():
    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output and discard all that is in buffer

        #write data
        t = threading.Thread(target=listen)
        t.daemon = True
        t.start()
        while True:
            writeinput = input(">>")
            if(writeinput == 'exit'):
                t
                exit()
            writeinput += "\n"
            ser.write(writeinput.encode())
            print('writing data: ' + writeinput)

        # ser.write(b"System 2 saying hi\n")
        # print("write data: AT+CSQ")
        # time.sleep(0.5)  #give the serial port sometime to receive the data
        # numOfLines = 0
        # while True:
        #     response = ser.readline()
        #     print("read data: " + str(response))
        #     numOfLines = numOfLines + 1
        #     if(numOfLines >= 200):
        #         break

        ser.close()
    except Exception as e:
        print("error communicating...: " + str(e))

else:
    print("cannot open serial port ")