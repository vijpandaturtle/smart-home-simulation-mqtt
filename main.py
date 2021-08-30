import time
from EdgeServer import Edge_Server
from LightDevice import Light_Device
from ACDevice import AC_Device

WAIT_TIME = 0.25  

print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = Edge_Server('edge_server_1')
time.sleep(WAIT_TIME)  
print("*******************************************************")

# Creating the light_device
print("Intitate the device creation and registration process." )
print("\nCreating the Light devices for their respective rooms.")
light_device_1 = Light_Device("light_1", "kitchen")
light_device_2 = Light_Device("light_2", "living")
light_device_3 = Light_Device("light_3", "br1")
time.sleep(WAIT_TIME)  
print("*******************************************************")

# Creating the ac_device  
print("\nCreating the AC devices for their respective rooms. ")
ac_device_1 = AC_Device("ac_1", "br2")
ac_device_2 = AC_Device("ac_2", "br2")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Getting switch status of different devices")
edge_server_1.get_status("light", "kitchen", "light_1", "SWITCH")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Getting light intensity of devices")
edge_server_1.get_status("light", "kitchen", "light_1", "COMMAND")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Getting temp status of ac devices")
edge_server_1.get_status("ac", "br2", "ac_1", "COMMAND")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Setting switch status")
edge_server_1.set_status("light", "kitchen", "light_1", "ON", "SWITCH")
edge_server_1.set_status("ac", "br2","ac_1", "ON", "SWITCH")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Setting Light Intensity")
edge_server_1.set_status("light", "kitchen", "light_1", "HIGH", "COMMAND")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Setting AC Temperature")
edge_server_1.set_status("ac", "br2","ac_1", "25", "COMMAND")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
edge_server_1.terminate()
