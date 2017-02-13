#Lista as portas seriais disponiveis

import  queue, serial, glob, os, sys


class Listar_Serial():
    def __init__(self):
        self.cur_data = None
        self.has_new_data = False

    def add_data(self, data):
        self.cur_data = data
        self.has_new_data = True

    def read_data(self):
        self.has_new_data = False
        return self.cur_data


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    print ("Serial Port ok")
    return result


