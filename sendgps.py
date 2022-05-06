from BlueToothClient import setupBluetoothSocket
import keyboard

socket = setupBluetoothSocket()

def eval_key():
    if keyboard.is_pressed("up"):
        return 1
    elif keyboard.is_pressed("left"):
        return 3
    elif keyboard.is_pressed("right"):
        return 2
    else:
        return 0
    


while True:
    mode_str = b"%d" % eval_key()
    socket.send(mode_str)
