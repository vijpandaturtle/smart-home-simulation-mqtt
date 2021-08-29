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
light_device_1 = Light_Device("light_1", "Kitchen")
light_device_2 = Light_Device("light_2", "Living")
light_device_3 = Light_Device("light_3", "BR1")
time.sleep(WAIT_TIME)  
print("*******************************************************")

# Creating the ac_device  
print("\nCreating the AC devices for their respective rooms. ")
ac_device_1 = AC_Device("ac_1", "BR1")
ac_device_2 = AC_Device("ac_2", "BR2")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Getting switch status of different devices")
edge_server_1.get_status(["light_1", "light_2", "light_3", "ac_1", "ac_2"])
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Setting switch status")
edge_server_1.set_status("light_1", "ON", "SWITCH")
edge_server_1.set_status("ac_1", "ON", "SWITCH")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Setting Light Intensity")
edge_server_1.set_status("light_1", "HIGH", "COMMAND")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("Setting AC Temperature")
edge_server_1.set_status("ac_1", "25", "COMMAND")
time.sleep(WAIT_TIME)  
print("*******************************************************")

print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
edge_server_1.terminate()
