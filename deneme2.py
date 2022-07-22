import can 

id= input("Enter ID: ")
id=hex(id,16 )

hex_arr = [0]*4
for i in range(0, 4):
    hexValue1 = input("Input first hex value: ")
    hexValue1 = int(hexValue1,16)
    hex_arr[i] = hexValue1
    print(hex_arr)
    
bus = can.interface.Bus(bustype = 'socketcan', channel='vcan0', bitrate = 250000) 
msg = can.Message(arbitration_id=id, data=hex_arr, is_extended_id=False)
try:
    bus.send(msg)
    print("Message sent on {bus.channel_info}")
    
    while True:
        message = bus.recv()
        print(message)
        
except can.CanError:
    print("Message NOT sent")
