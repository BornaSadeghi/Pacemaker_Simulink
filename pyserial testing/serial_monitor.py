import serial
import io
import struct

with serial.Serial('COM13', 115200, timeout=5) as ser:

    ser.write(b'\x16') # SYNC
    ser.write(b'\x55') # FN_CODE

    ser.write(b'\x00') # RED_ENABLE
    ser.write(b'\x01') # GREEN_ENABLE
    ser.write(b'\x01') # BLUE_ENABLE

    ser.write(b'\x00') # OFF_TIME 0
    ser.write(b'\x00') # OFF_TIME 1
    ser.write(b'\x00') # OFF_TIME 2
    ser.write(b'\x3f') # OFF_TIME 3

    ser.write(b'\xc8') # SWITCH_TIME 0
    ser.write(b'\x00') # SWITCH_TIME 1
    



    # while True:

    #     data = ser.readline()

    #     if len(data) == 2:

    #         print(data)

            # print(data)

            # VENT_SIGNAL = struct.unpack('d',data[0:8])[0]
            # ATR_SIGNAL = struct.unpack('d',data[8:16])[0]
            # ATR_SIGNAL = 0;

            # print(f"v: {VENT_SIGNAL}\t\ta: {ATR_SIGNAL}")
        