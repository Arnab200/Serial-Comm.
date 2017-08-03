"""Refer the binary codes for speed and
    0000 is universal acknowledgement signal
    handshake signal binary(int) 0000 sent from the arduino
    handshake signal binary(int) 1111 sent from the computer

    0101 full thrust forward
    0111 right turn
    1101 left turn
    0001 stop

"""

import serial
import time

ser = serial.Serial(port='COM3', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=1)
print("Connected to serial port "+ser.portstr)
file = open("D:\\Pond_test_logs\\Pond_text.txt" , "a")


def handshake():
    time.sleep(5)
    rec = ser.readline()
    rec = rec.decode()
    if rec == '0000':
        print("Acknowledgement recieved")
        sen = '1111'
        ser.write(sen.encode())
        print("Acknowledgement sent")
        time.sleep(5)
        print("Handshake done")
        return True


def run_forward():
    sen1 = '0101'
    ser.write(sen1.encode())
    rec1 = ser.readline()
    rec1 = rec1.decode()
    if rec1 == '0000':
        print("Running forward")


def turn_left():
    sen2 = '1101'
    ser.write(sen2.encode())
    rec2 = ser.readline()
    rec2 = rec2.decode()
    if rec2 == '0000':
        print("Turning left")


def turn_right():
    sen3 = '1101'
    ser.write(sen3.encode())
    rec3 = ser.readline()
    rec3 = rec3.decode()
    if rec3 == '0000':
        print("Turning right")


def main():
    while False:
        handshake()
        # start running from this line


if __name__ == "__main__":
    main()




