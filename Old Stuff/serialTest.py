import serial

s = serial.Serial('COM1')
res = s.read()
print(res)
