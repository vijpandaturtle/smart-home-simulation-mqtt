## IOT Smart Home Project 

The aim of this project is to simulate a basic IOT smart home environment using a number of Light and ACDevices an Edge Server and an MQTT broker using software packages and scripts. 

**Requirements Discussion**
1. Rooms : Kitchen, BR1, BR2, Living 
2. Device type : LightDevice, ACDevice 
3. Light Device State : on/off and low/medium/high 
4. AC Device State : on/off and temperature control (18C - 32C)
5. Edge Server Capabilities : Device Registration, Send command to device, GET Device Status 
6. Main Class in Edge Server to show capabilities 

**Demonstration**
1. 3 Light Devices & 2 AC Device 
2. Various Operations 

**Design Decisions** 
1. Single Topic vs Multilevel Topic

**Some Best Practices for MQTT Topics**

([Rest of them can be found in the AWS White paper here.](https://d1.awsstatic.com/whitepapers/Designing_MQTT_Topics_for_AWS_IoT_Core.pdf))
1. Ensure MQTT topic levels only use lowercase letters, numbers, and dashes.
2. Ensure MQTT topic levels structure follows a general to specific pattern.
3. Include any relevant routing information in the MQTT topic. 
4. Prefix your MQTT topics to distinguish data topics from command topics.
5. Document proposed MQTT topic structures as part of your operations practice. 
6. Use the Device name as the MQTT client ID for connecting as a device 
over MQTT
7. Include the Device Name of the device in any MQTT topic the device uses for 
publishing or subscribing to its data.
8. Include additional contextual information about a specific message in the payload 
of the MQTT message. 
9. Avoid MQTT communication patterns that result in a sizeable fan-in scenario to a 
single device. 

**Topic Design**
1. Main Topic : devices/
2. Sub-topics : devices/room_type/device_type/device_id/
2. Issuing Registration Request : devices/room_type/device_type/device_id//REG
3. Registration Confirmation : devices/room_type/device_type/device_id/CONFREG
4. Issuing request for device status : devices/room_type/device_type/device_id/GETSTAT  
5. Device posting status : devices/room_type/device_type/device_id/STAT
6. Issuing request for setting device status : devices/room_type/device_type/device_id/SETSTAT
7. Issuing request for device parameters : devices/room_type/device_type/device_id/GETCOMMAND
8. Device posting device parameters : devices/room_type/device_type/device_id/COMMAND
8. Issuing request for setting device parameters : devices/room_type/device_type/device_id/SETCOMMAND
