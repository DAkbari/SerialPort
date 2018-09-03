import sys
import serial
import io


def listen(ser):
    print("listening...")
    while True:
        msg = ser.readline()
        print(msg)


def write(ser, text):
    ser.write(b'hello')
    ser.flush()


def main():
    #COM1 listen
    #COM1 Write <message>
    # print("python main function")
    # print("This is the name of the script: ", sys.argv[0])
    # print("Number of arguments: ", len(sys.argv))
    # print("The arguments are: ", str(sys.argv))

    portName = sys.argv[1]
    ser = serial.Serial(portName, 9600, timeout=0)
    try:
        ser.open()
    except Exception:
        print(Exception)

    if sys.argv[2] == 'listen':
        listen(ser)
    elif sys.argv[2] == 'write':
        write(ser, sys.argv[3])


if __name__ == '__main__':
    main()


