import serial
import time
# Para mostrar puertos disponibles en linux: dmesg | grep tty

ser = serial.Serial(port='/dev/ttyUSB0', baudrate = 9600, bytesize=8, parity='N',stopbits=1, timeout=1, xonxoff=False)
print(ser.name)

ser.write(b"OFF")
#a = ser.read()

#print(a)
#print("-----")
#for i in a:
#    print(i)

"""
control = True

while control:
    try:
        ser.write(b'IP')
        print("Dame info")
        time.sleep(0.1)
        a = ser.readline()
        for i in a:
            print(i)
        #print(binascii.hexlify(a))
        control = False
    except KeyboardInterrupt:
        control = False
"""
input("Presione <enter> para finalizar")
ser.close()
print("Fin de la comunicacion")
