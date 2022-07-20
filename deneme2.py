import can

ıd= input("Enter ID: ")
ıd=int(ıd)

hex_arr = [0]*4
for i in range(0, 4):
    hexValue1 = input("Input first hex value: ")
    hexValue1 = int(hexValue1,16)
    hex_arr[i] = hexValue1
    print(hex_arr)



bus = can.Bus(interface='socketcan',channel='vcan0', receive_own_messages=True)


message = can.Message(arbitration_id=ıd, is_extended_id=True,data=hex_arr)



bus.send(message, timeout=0.2)



for msg in bus:
    print(f"{msg.arbitration_id:X}: {msg.data}")


notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])

bus = can.Bus(interface='socketcan',channel='vcan0')
read_msg = bus.recv()
binValue1 = bin(read_msg)
print("bin ",binValue1[2:8])
