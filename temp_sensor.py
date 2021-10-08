#File: temp_sensor.py
#Author: Ville Rytinki
#Description: Contains the interface for DS18B20 temperature sensor.


import os
import glob
import time


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'
device_file = '/sys/bus/w1/devices/28-00000c8d588e/w1_slave'

class TempSensor:
    
    @classmethod
    def read_temp_raw(self):
        try:
            f = open(device_file, 'r')
            lines = f.readlines()
            f.close()
        except:
            print('Device folder could not be found')
        return lines
        
    @classmethod
    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            print('last three letters not a YES')
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
        return temp_c

