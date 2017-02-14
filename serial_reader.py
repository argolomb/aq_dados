import serial


class SerialReader(object):
    ser = serial.Serial()

    def serial_read(self):
        self.ser.open()
        print(self.ser)
        print(self.ser.read())

    def connect(self, baud_rate, port_number):
        self.ser.port = port_number
        self.ser.baudrate = baud_rate
        self.ser.timeout = 1

    def disconnect(self):
        self.ser.close()
        print(self.ser)
