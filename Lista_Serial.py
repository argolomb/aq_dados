#Lista as portas seriais disponiveis

import  queue, serial, glob, os


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


def get_portas(self):
    portas_disponiveis=[]
    for i in range(256):
        try:
            s = serial.Serial(i)
            portas_disponiveis.append(s.portstr)
            s.close()
        except serial.SerialException:
            pass
    return portas_disponiveis



