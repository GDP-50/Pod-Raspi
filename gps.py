import serial.tools.list_ports
from pynmeagps import NMEAReader
import re
import sys


class COMPorts:

    def __init__(self, data: list):
        self.data = data

    @classmethod
    def get_com_ports(cls):
        data = []
        ports = list(serial.tools.list_ports.comports())

        for port_ in ports:
            obj = Object(data=dict({"device": port_.device, "description": port_.description.split("(")[0].strip()}))
            data.append(obj)

        return cls(data=data)

    @staticmethod
    def get_description_by_device(device: str):
        for port_ in COMPorts.get_com_ports().data:
            if port_.device == device:
                return port_.description

    @staticmethod
    def get_device_by_description(description: str):
        for port_ in COMPorts.get_com_ports().data:
            if port_.description == description:
                return port_.device


class Object:
    def __init__(self, data: dict):
        self.data = data
        self.device = data.get("device")
        self.description = data.get("description")




def setup_gps():
    for port in COMPorts.get_com_ports().data:
        print(port.device)
        print(port.description)

    if sys.platform == "windows":
        gps_port = COMPorts.get_device_by_description(description="USB Serial Device")
    else:
        gps_port = COMPorts.get_device_by_description(description="u-blox 7 - GPS/GNSS Receiver")


    gps = serial.Serial(gps_port, 9600, timeout=1)
    gps.flushInput()
    gps_data = gps.readline()
    print(gps_data)
    return gps


def get_gps(gps):
    while True:
        line = gps.readline().strip()
        line = line.decode()
        if re.match("^\$GPRMC", line):
            #print("matched gprmc")
            msg = NMEAReader.parse(line)
            #print("Lat: %f" % msg.lat)
            #print("Lon: %f" % msg.lon)
            return msg.lat, msg.lon
        



""" try:
    while gps_data:
        line = gps.readline().strip()
        line = line.decode()
        if re.match("^\$GPRMC", line):
            msg = NMEAReader.parse(line)
            try:
                print("Lat: %f" % msg.lat)
                print("Lon: %f" % msg.lon)
            except:
                print("not connected yet")
except KeyboardInterrupt:
    print("Interrupted") """