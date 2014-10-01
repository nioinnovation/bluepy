from bluepy.sensortag import SensorTag, IRTemperatureSensor
from time import sleep

s = SensorTag("B4:99:4C:64:30:9F")

ir_temp = s.IRtemperature

# # ir_temp.enable_notifications()
# ir_temp.enable(True)
# print(ir_temp.read())

# k = s.keypress
# k.enable()

print(ir_temp.process_tmp((49406, 64523)))
