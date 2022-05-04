import bluetooth



def setupBluetoothSocket():
    bd_addr = "E4:5F:01:48:64:81"

    port = 1

    socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    socket.connect((bd_addr, port))

    socket.send("hello!!")
    return socket

