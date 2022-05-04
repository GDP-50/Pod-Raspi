import bluetooth

bd_addr = "E4:5F:01:48:64:7F"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

