from BlueToothClient import setupBluetoothSocket
from gps import get_gps, setup_gps

socket = setupBluetoothSocket()
gps = setup_gps()

while True:
    lat, lon = get_gps(gps)
    gps_str = 'lat:%f,lon:%f' % (lat, lon)
    print(gps_str)
    socket.send(gps_str)